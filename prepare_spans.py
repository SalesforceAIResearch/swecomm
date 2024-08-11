from tqdm import tqdm
import os
from moatless.workspace import Workspace
from moatless.benchmark.swebench import get_repo_dir_name, setup_swebench_repo
import json

import argparse
from utils import get_full_data, get_identified_spans

parser = argparse.ArgumentParser()
parser.add_argument("--processed_span_path",
    help="Path to the identified spans file",
    default="resource/relevant_context",
    required=False
)
parser.add_argument("--trajectory_path",
    help="Path to the trajectory file",
    default="resource/20240623_moatless_claude-3.5-sonnet/trajs",
    required=False
)
args = parser.parse_args()
processed_span_path = args.processed_span_path
trajectory_path = args.trajectory_path

dataset = get_full_data()

if not os.path.exists(processed_span_path):
    os.makedirs(processed_span_path)

for instance in tqdm(dataset, desc="Preparing identified spans"):
    if os.path.exists(os.path.join(processed_span_path, f"{instance['instance_id']}.json")):
        print(f"Skipping {instance['instance_id']}, generated already")
        continue
    
    identified_spans = get_identified_spans(instance, trajectory_path)
    
    repo_dir = setup_swebench_repo(instance, f"{os.getcwd()}/agent_repos/repos")
    workspace = Workspace.from_dirs(repo_dir=repo_dir, index_dir=None)
    
    for identified_span in identified_spans:
        file_path = identified_span["file_path"]
        file = workspace.file_repo.get_file(file_path)
        
        with open(os.path.join(repo_dir, file_path)) as f:
            content_lines = f.readlines()
        
        identified_span["content"] = []
        
        for span_id in identified_span["span_ids"]:
            span = file.module.find_span_by_id(span_id)
            if not span:
                print(f"Span not found: {span_id} in {file_path}, Instance {instance['instance_id']}")
                continue
            
            start_line = span.start_line # max(span.start_line - 10, 0)
            end_line = span.end_line # min(span.end_line + 10, len(content_lines) - 1)
            
            content = content_lines[start_line - 1: end_line]
            identified_span["content"].append({
                "span_id": span_id,
                "start_line": start_line,
                "end_line": end_line,
                "content": content
            })
    
    output = {
        "instance_id": instance["instance_id"],
        "identified_spans": identified_spans   
    }
        
    with open(os.path.join(processed_span_path, f"{instance['instance_id']}.json"), 'w') as f:
        json.dump(output, f)