
# aider chat started at 2024-07-19 08:01:48

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpubo8ieek/.git with 1,202 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Comparing string to array in _estimate_mi  
#### In ``_estimate_mi`` there is ``discrete_features == 'auto'`` but discrete features can be an array of indices or a boolean mask.  
#### This will error in future versions of numpy.  
#### Also this means we never test this function with discrete features != 'auto', it seems?  
> 33420 prompt tokens, 61 completion tokens, $0.168015 cost  

To address the issue with comparing `discrete_features` to `'auto'` in `_estimate_mi`, we will likely need to edit the following file:

- `sklearn/feature_selection/_mutual_info.py`

Please add this file to the chat so I can proceed with the necessary changes.

