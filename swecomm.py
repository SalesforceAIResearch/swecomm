from moatless.workspace import Workspace
from moatless.benchmark.swebench import get_repo_dir_name, setup_swebench_repo
from tqdm import tqdm
import os
import random
from utils import get_resolved_set, get_candidate_instances, evaluate_ranking
from tqdm import tqdm
import argparse
import json
from prompts import SINGLE_SCORING_WITH_IDENTIFIED_SPANS_TEMPLATE, SYSTEM_PROMPT
from utils import (
    get_before_after_code_with_context,
    extract_gpt4_tag,
    get_identified_spans,
    get_submission_patches,
    get_submission_resolved_set,
    get_resolved_set,
    get_full_data,
)

from collections import defaultdict

with open("api_keys.json", "r") as f:
    api_keys = json.load(f)
    for k in api_keys:
        os.environ[k] = api_keys[k]
os.environ['LITELLM_LOG'] = 'DEBUG'

parser = argparse.ArgumentParser()
parser.add_argument("output_dir", type=str, default=None)
parser.add_argument("--processed_span_path", type=str, default="resource/relevant_context")
parser.add_argument("--preds_to_eval", type=str, default=None)
parser.add_argument("--subs_to_eval", type=str, default=None)
parser.add_argument("--pred_results", type=str, default=None)
parser.add_argument("--save", default=False, action="store_true")
parser.add_argument("--votes", type=int, default=10)
parser.add_argument("--model", type=str, default="gpt-4o")
args = parser.parse_args()

if not args.preds_to_eval and not args.subs_to_eval:
    raise ValueError("Please provide either preds_to_eval or subs_to_eval")
if args.preds_to_eval and args.subs_to_eval:
    raise ValueError("Please provide either preds_to_eval or subs_to_eval, not both")

evals = None
preds = {}
resolved_sets = None

if args.preds_to_eval:
    preds_paths = args.preds_to_eval.split(",")
    for preds_path in preds_paths:
        with open(preds_path, 'r') as f:
            preds[preds_path] = {}
            for line in f:
                instance = json.loads(line)
                preds[preds_path][instance["instance_id"]] = instance
    evals = preds_paths
    
    if args.pred_results:
        resolved_sets = {}
        pred_result_paths = args.pred_results.split(",")
        assert len(pred_result_paths) == len(preds), "Number of pred results should match the number of preds"
        for pred_path, pred_result_path in zip(preds_paths, pred_result_paths):
            resolved_sets[pred_path] = get_resolved_set(pred_result_path)

if args.subs_to_eval:
    subs = args.subs_to_eval.split(",")
    resolved_sets = {}
    for sub in subs:
        preds[sub] = get_submission_patches(sub)
        resolved_sets[sub] = get_submission_resolved_set(sub)
    evals = subs

SEED = 42 # the answer to everything
random.seed(SEED)

dataset = get_full_data()

if args.save:
    resolved_sets_union = set()
    for resolved_set in resolved_sets.values():
        resolved_sets_union.update(resolved_set)
    print(len(resolved_sets_union))
    dataset = [instance for instance in dataset if instance["instance_id"] in resolved_sets_union]

dataset = sorted(dataset, key=lambda x: x['created_at'])

evaluations_dir = "./swecomm_runs"
evaluation_dir = f"{evaluations_dir}/{args.output_dir}"
model = "gpt-4o"

def organize_identified_spans(identified_spans):
    concat_spans = ""
    for identified_span in identified_spans:
        file_path = identified_span["file_path"]
        for span in identified_span["content"]:
            content = span["content"]
            span_id = span["span_id"]
            start_line = span["start_line"]
            # pad the line numbers to 4 digits
            line_numbered_content = ''.join([f"({start_line + i:04d}) {line}" for i, line in enumerate(content)])
            wrapped_code_span = f"<code_span={file_path} span_id={span_id}>\n{line_numbered_content}\n</code_span>"
            if not concat_spans:
                concat_spans = wrapped_code_span
            else:
                concat_spans += f"\n\n{wrapped_code_span}"
    return concat_spans


requests = []
eval2score = {}
eval2patch = {}
eval2exp = {}

output_score = {
    "top 1 pass": 0,
    "top 3 pass": 0,
    "top 5 pass": 0,
}


#whitelist = ["scikit-learn__scikit-learn-10297"]
whitelist = []

dataset = [instance for instance in dataset if not whitelist or instance["instance_id"] in whitelist]

before_after_dict = {}
if os.path.exists("cache/before_after_dict.json"):
    before_after_dict = json.load(open("cache/before_after_dict.json", "r"))

for instance in tqdm(dataset, desc="Preparing spans before and after patch"):
    with open(os.path.join(args.processed_span_path, f"{instance['instance_id']}.json")) as f:
        identified_spans = json.load(f)["identified_spans"]
        concat_spans = organize_identified_spans(identified_spans)
        
    instance_id = instance["instance_id"]
    
    for eval_ in evals:
        messages = None
        if instance_id + ":" + eval_ in before_after_dict: # already computed
            continue
        
        if instance_id not in preds[eval_] or not preds[eval_][instance_id]["model_patch"]:
            print(f"Instance {instance_id} not found in {eval_}")
            score = -1
        else:
            # read and get the repo map and issue text
            issue_text = instance["problem_statement"]
            before, after = get_before_after_code_with_context(instance, preds[eval_][instance_id]['model_patch'], f"{os.getcwd()}/agent_repos/repos", 5)
            
            before_after_dict[(
                instance_id + ":" + eval_
            )] = {
                "before": before,
                "after": after
            }

if not os.path.exists("cache"):
    os.makedirs("cache")
with open("cache/before_after_dict.json", "w") as f:
    json.dump(before_after_dict, f)
        
from litellm import token_counter

import litellm
from litellm import batch_completion, completion_cost

for instance in tqdm(dataset, desc="Preparing requests"):
    with open(os.path.join(args.processed_span_path, f"{instance['instance_id']}.json")) as f:
        identified_spans = json.load(f)["identified_spans"]
        concat_spans = organize_identified_spans(identified_spans)
        
    instance_id = instance["instance_id"]
    if instance_id not in eval2score:
        eval2score[instance_id] = defaultdict(list)
        eval2patch[instance_id] = {}
        eval2exp[instance_id] = {}
    
    for eval_ in evals:
        messages = None
        if instance_id not in preds[eval_] or not preds[eval_][instance_id]["model_patch"]:
            print(f"Instance {instance_id} not found in {eval_}")
            score = -1
        else:
            # read and get the repo map and issue text
            issue_text = instance["problem_statement"]
            
            before = before_after_dict[instance_id + ":" + eval_]["before"]
            after = before_after_dict[instance_id + ":" + eval_]["after"]
            
            formatted_user_input = SINGLE_SCORING_WITH_IDENTIFIED_SPANS_TEMPLATE.format(
                issue_text=issue_text,
                code_spans=concat_spans,
                before_patch=before,
                after_patch=after
            )
            
            messages = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT if "claude" in args.model else [{
                        "type": "text",
                        "text": SYSTEM_PROMPT
                    }]
                },
                {
                    "role": "user",
                    "content": formatted_user_input if "claude" in args.model else [{
                        "type": "text",
                        "text": formatted_user_input,
                    }]
                }
            ]
            if messages == -1:
                score = -1
                messages = None
        if messages is None:
            eval2score[instance_id][eval_].append(score)
        else:
            requests.append((instance_id, eval_, messages))
        
        eval2patch[instance_id][eval_] = preds[eval_].get(instance_id)

tot_tokens = 0

for instance_id, eval_, messages in requests:
    cnt = token_counter(model=args.model, messages=messages)
    if cnt >= 100000:
        print(f"Context window exceeded for instance {instance_id} in evaluation {eval_}")
    else:
        tot_tokens += cnt
          
print(f"Total tokens: {tot_tokens * args.votes}")
requests = requests * args.votes
print(f"Attemp Total requests: {len(requests)} to be sent to {args.model}")
requests = requests

responses = batch_completion(
    model=args.model,
    messages=[req[2] for req in requests],
    temperature=1.2,
    max_tokens=4096,
    top_p=1,
)

tot_cost = 0
for response, (instance_id, eval_, _) in zip(responses, requests):
    if hasattr(response, "choices") and response.choices:
        msg = response.choices[0].message.content
        tot_cost += completion_cost(response)
    else:
        print(f"Error in response for instance {instance_id} in evaluation {eval_}")
        print(response)
    if eval_ not in eval2exp[instance_id]:        
        eval2exp[instance_id][eval_] = [{}]
    else:
        eval2exp[instance_id][eval_].append({})
    
    exp_keys = [
        "issue_exp",
        "code_span_exp",
        "patch_exp",
        "code_span_exp",
        "new_issues_exp",
        "fixes_issue_exp",
    ]
    for exp_key in exp_keys:
        eval2exp[instance_id][eval_][-1][exp_key] = extract_gpt4_tag(msg, exp_key) or ""
    eval2exp[instance_id][eval_][-1]["msg"] = msg
    try:
        score = extract_gpt4_tag(msg, "score")
        score = score.replace('#', '').strip()
        eval2score[instance_id][eval_].append(int(score) if score else -1)
    except Exception as e:
        print(f"Error in extracting score for instance {instance_id} in evaluation {eval_}")

processed_meta_info = []

for instance in dataset:
    instance_id = instance['instance_id']
    # rank different evaluation candidates by the score
    avg = lambda l: sum(l) / len(l) if l else -1
    
    sorted_evals = sorted(evals, key=lambda x: avg(eval2score[instance_id][x]), reverse=True)
    best_eval = sorted_evals[0]
    
    # get whether this candidate is resolved
    resolved = None
    if resolved_sets:
        resolved = instance_id in resolved_sets[best_eval]
        # only do evaluation during inference when we know the correctness of each candidate
        topk_eval = evaluate_ranking(instance_id, sorted_evals, resolved_sets)

    save_item = {}
    for eval_ in evals:
        save_item[eval_] = {
            "score": eval2score[instance_id][eval_],
            "avg_score": avg(eval2score[instance_id][eval_]),
            "resolved": eval_ in resolved_sets[eval_] if resolved_sets else False,
            "patch": eval2patch[instance_id][eval_],
            "explanation": "" if eval_ not in eval2exp[instance_id] else eval2exp[instance_id][eval_],
        }
    meta_info = {
        "best_choice": best_eval,
        "best_choice_resolved": resolved,
        "evaluations": save_item
    }
    if resolved_sets:
        meta_info.update(topk_eval)
    
    processed_meta_info.append(meta_info)

if resolved_sets:
    for meta_info in processed_meta_info:
        for k in output_score.keys():
            output_score[k] += meta_info[k]
    for k in output_score.keys():
        output_score[k] /= len(dataset) if len(dataset) == 20 else 300
    print("==> Topk pass: ", output_score)

os.makedirs(evaluation_dir, exist_ok=True)

import datetime

date = datetime.datetime.now().strftime("%Y%m%d_%H%M")

with open(os.path.join(evaluation_dir, f"output_{date}.json"), 'w') as f:
    json.dump(processed_meta_info, f, indent=4)