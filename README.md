# Salesforce SWE Committee

## Prepare Relevant Code Spans

We use the code spans identified as relevant to an issue to rerank the candidates.

Our experiments use the code spans identified by Moatless Tools.
`resource/20240623_moatless_claude-3.5-sonnet` contains the trajectories, from which we extract the code spans identified.
Most of the trajectories are from Moatless Tools + Claude 3.5 Sonnet, but for those that are missing in that setting, we use the trajectories from Moatless Tools + GPT-4o.

Run `prepare_spans.py` to extract the code spans from the trajectories.

Note that you can always run moatless tools yourself to get the code spans. You can also use other agents of your choice to identify the relevant code spans.


## Ensembling Custom Predictions

Ensemble your own predictions by running the following command:

```bash
python swecomm.py
  --output_dir committee_out_1
  --submission_preds pred1.jsonl,pred2.jsonl,...
  --submission_results results1.json,results2.json,...
```

The `--submission_results` argument is optional. When it is provided, SWE committee only scores and reranks candidates for patches that are solved by at least one agent, so that you can save some time and money.
Note that this optional argument does not give the committee any unfair advantage.
You can still run reranking for all instances, and the results would be the same.
More importantly, this relies on the assumption that the evaluation results are correct, which is not always the case. As can be seen in the difference in resolve rates between the SWE-Bench Leaderboard and the evaluations conducted by [https://eval.moatless.ai/](https://eval.moatless.ai/).

```bash

The `--submission_results` argument should be comma-separated lists of the paths to the predictions and results files, respectively. Each `results.json` needs to have a field named `resolved` or `resolved_ids` which contains the list of resolved instance ids.



where `pred1.jsonl`, `pred2.jsonl`, etc. are the predictions you want to ensemble and `results.jsonl` is the output file.
```


`moatless-tools` is the 323582b commit of the Moatless Tools repository. We use some of the utils from this repo.


## Ensembling Leaderboard Submissions

`resource/` contains the candidate patches and the code spans you can use to reproduce the results in the paper.
They can be obtained elsewhere, but we provide them here for convenience.

`resource/experiments/` contains all the submissions on the leaderboard of SWE-Bench Lite as of August 3, 2024. We also include CosineAI's [submission](https://github.com/swe-bench/experiments/pull/45), which was not merged into the leaderboard due to the new requirement for providing trajectories.

`resource/20240623_moatless_claude-3.5-sonnet` contains the trajectories of moatless tools, from which we extract the code spans identified by moatless tools.
Most of the trajectories are from Moatless Tools + Claude 3.5 Sonnet, but for those that are missing in that setting, we use the trajectories from Moatless Tools + GPT-4o.
Note that we only use the identified code spans, not the trajectories themselves.
To create these from scratch, we refer you to moatless tools' search loop.