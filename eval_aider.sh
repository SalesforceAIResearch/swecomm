run_ids=(
    180724-194532
    190724-035805
    190724-120220
    190724-191444
    200724-030837
    200724-074412
    200724-121458
    200724-164334
    200724-221013
    210724-045403
)

# format pred_paths like this: "resource/aider_runs/180724-194532/all_preds.json"

pred_paths=()
for run_id in ${run_ids[@]}; do
    pred_paths+=("resource/aider_runs/$run_id/all_preds.jsonl")
done

res_paths=()
for run_id in ${run_ids[@]}; do
    res_paths+=("resource/aider_runs/$run_id.aider_$run_id.json")
done

pred_paths=$(IFS=,; echo "${pred_paths[*]}")
res_paths=$(IFS=,; echo "${res_paths[*]}")


python swecomm.py swecomm_aider \
 --preds_to_eval "$pred_paths" \
 --pred_results "$res_paths"