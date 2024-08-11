
# aider chat started at 2024-07-20 13:09:18

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpq8k14xul/.git with 167 files  
> Repo-map: using 2048 tokens  

#### Allow lists in the dict values of the hooks argument  
#### Currently the Request class has a .register_hook() method but it parses the dictionary it expects from it's hooks argument weirdly: the argument can only specify one hook function per hook.  If you pass in a list of hook functions per hook the code in Request.**init**() will wrap the list in a list which then fails when the hooks are consumed (since a list is not callable).  This is especially annoying since you can not use multiple hooks from a session.  The only way to get multiple hooks now is to create the request object without sending it, then call .register_hook() multiple times and then finally call .send().  
####   
#### This would all be much easier if Request.**init**() parsed the hooks parameter in a way that it accepts lists as it's values.  
####  
> 15904 prompt tokens, 66 completion tokens, $0.080510 cost  

To implement the requested change, we will need to modify the `requests/models.py` file. Specifically, we will need to update the `Request.__init__` method to handle lists in the `hooks` argument properly.

Please add the `requests/models.py` file to the chat so I can proceed with the necessary changes.

> requests/models.py  
> Add these files to the chat? yes  
> 9652 prompt tokens, 162 completion tokens, $0.050690 cost  

Here are the changes needed to allow lists in the dictionary values of the `hooks` argument in the `Request` class:

1. Update the `Request.__init__` method to handle lists in the `hooks` argument properly.

requests/models.py
```python
<<<<<<< SEARCH
        for (k, v) in list(hooks.items()):
            self.register_hook(event=k, hook=v)
=======
        for (k, v) in hooks.items():
            if isinstance(v, list):
                for hook in v:
                    self.register_hook(event=k, hook=hook)
            else:
                self.register_hook(event=k, hook=v)
>>>>>>> REPLACE
```

This change will ensure that if a list of hooks is provided for a particular event, each hook in the list will be registered individually.

> Applied edit to requests/models.py  
