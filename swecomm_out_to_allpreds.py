import json
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("swecomm_out", type=str, help="Path to the swecomm output file")
parser.add_argument("model_name", type=str, help="Name of the model")
args = parser.parse_args()

swecomm_out_dir = os.path.dirname(args.swecomm_out)
os.makedirs(os.path.join(swecomm_out_dir, "trajs"), exist_ok=True)

with open(args.swecomm_out) as f:
    data = json.load(f)
    
    all_preds = []
    for instance in data:
        instance_id = instance['evaluations'][instance['best_choice']]['patch']['instance_id']
        with open(os.path.join(swecomm_out_dir, "trajs", instance_id + ".json"), "w") as f:
            json.dump(instance, f, indent=4)
        all_preds.append(
            {
                "instance_id": instance_id,
                "model_patch": instance['evaluations'][instance['best_choice']]['patch']['model_patch'],
                "model_name_or_path": args.model_name,
            }
        )

with open(os.path.join(swecomm_out_dir, "all_preds.jsonl"), "w") as f:
    for l in all_preds:
        f.write(json.dumps(l) + "\n")