
# aider chat started at 2024-07-20 06:50:32

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpiy5mw0_q/.git with 167 files  
> Repo-map: using 2048 tokens  

#### Allow lists in the dict values of the hooks argument  
#### Currently the Request class has a .register_hook() method but it parses the dictionary it expects from it's hooks argument weirdly: the argument can only specify one hook function per hook.  If you pass in a list of hook functions per hook the code in Request.**init**() will wrap the list in a list which then fails when the hooks are consumed (since a list is not callable).  This is especially annoying since you can not use multiple hooks from a session.  The only way to get multiple hooks now is to create the request object without sending it, then call .register_hook() multiple times and then finally call .send().  
####   
#### This would all be much easier if Request.**init**() parsed the hooks parameter in a way that it accepts lists as it's values.  
####  
> 15904 prompt tokens, 62 completion tokens, $0.080450 cost  

To implement the requested change, we will need to modify the `requests/models.py` file. This file contains the `Request` class and its `__init__` and `register_hook` methods.

Please add the `requests/models.py` file to the chat so I can proceed with the necessary changes.

> requests/models.py  
> Add these files to the chat? yes  
> 9711 prompt tokens, 199 completion tokens, $0.051540 cost  

To allow lists in the dictionary values of the `hooks` argument, we need to modify the `__init__` method of the `Request` class to handle lists correctly. Specifically, we will check if the hook value is a list and extend the existing list of hooks instead of wrapping it in another list.

Here are the necessary changes:

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

This change ensures that if the value of a hook is a list, each item in the list is registered as a separate hook. If the value is not a list, it is registered as a single hook.

> Applied edit to requests/models.py  
