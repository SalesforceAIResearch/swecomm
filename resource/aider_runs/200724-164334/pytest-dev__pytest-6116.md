
# aider chat started at 2024-07-20 15:58:47

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp878nq_lx/.git with 474 files  
> Repo-map: using 2048 tokens  

#### pytest --collect-only needs a one char shortcut command  
#### I find myself needing to run `--collect-only` very often and that cli argument is a very long to type one.   
####   
#### I do think that it would be great to allocate a character for it, not sure which one yet. Please use up/down thumbs to vote if you would find it useful or not and eventually proposing which char should be used.   
####   
#### Clearly this is a change very easy to implement but first I want to see if others would find it useful or not.  
#### pytest --collect-only needs a one char shortcut command  
#### I find myself needing to run `--collect-only` very often and that cli argument is a very long to type one.   
####   
#### I do think that it would be great to allocate a character for it, not sure which one yet. Please use up/down thumbs to vote if you would find it useful or not and eventually proposing which char should be used.   
####   
#### Clearly this is a change very easy to implement but first I want to see if others would find it useful or not.  
> 33355 prompt tokens, 82 completion tokens, $0.168005 cost  

To add a one-character shortcut for the `--collect-only` option, we will likely need to modify the following file:

1. `src/_pytest/config/argparsing.py` - This file is responsible for parsing command-line arguments and is where we would add the new shortcut.

Please add `src/_pytest/config/argparsing.py` to the chat so I can proceed with the changes.

> src/_pytest/config/argparsing.py  
> Add these files to the chat? yes  
> 7769 prompt tokens, 129 completion tokens, $0.040780 cost  

To add a one-character shortcut for the `--collect-only` option, we will:

1. Add the new shortcut `-c` to the `--collect-only` option in the `Parser` class.

Here is the *SEARCH/REPLACE* block:

src/_pytest/config/argparsing.py
```python
<<<<<<< SEARCH
        self._anonymous.addoption(*opts, **attrs)
=======
        # Adding a shortcut for --collect-only
        if '--collect-only' in opts:
            opts = opts + ('-c',)
        self._anonymous.addoption(*opts, **attrs)
>>>>>>> REPLACE
```

> Applied edit to src/_pytest/config/argparsing.py  
