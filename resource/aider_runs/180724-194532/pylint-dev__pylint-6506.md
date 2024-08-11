
# aider chat started at 2024-07-18 18:51:42

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp588vwwar/.git with 2,563 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Traceback printed for unrecognized option  
#### ### Bug description  
####   
#### A traceback is printed when an unrecognized option is passed to pylint.  
####   
#### ### Configuration  
####   
#### _No response_  
####   
#### ### Command used  
####   
#### ```shell  
#### pylint -Q  
#### ```  
####   
####   
#### ### Pylint output  
####   
#### ```shell  
#### ************* Module Command line  
#### Command line:1:0: E0015: Unrecognized option found: Q (unrecognized-option)  
#### Traceback (most recent call last):  
####   File "/Users/markbyrne/venv310/bin/pylint", line 33, in <module>  
####     sys.exit(load_entry_point('pylint', 'console_scripts', 'pylint')())  
####   File "/Users/markbyrne/programming/pylint/pylint/__init__.py", line 24, in run_pylint  
####     PylintRun(argv or sys.argv[1:])  
####   File "/Users/markbyrne/programming/pylint/pylint/lint/run.py", line 135, in __init__  
####     args = _config_initialization(  
####   File "/Users/markbyrne/programming/pylint/pylint/config/config_initialization.py", line 85, in _config_initialization  
####     raise _UnrecognizedOptionError(options=unrecognized_options)  
#### pylint.config.exceptions._UnrecognizedOptionError  
#### ```  
####   
####   
#### ### Expected behavior  
####   
#### The top part of the current output is handy:  
#### `Command line:1:0: E0015: Unrecognized option found: Q (unrecognized-option)`  
####   
#### The traceback I don't think is expected & not user-friendly.  
#### A usage tip, for example:  
#### ```python  
#### mypy -Q  
#### usage: mypy [-h] [-v] [-V] [more options; see below]  
####             [-m MODULE] [-p PACKAGE] [-c PROGRAM_TEXT] [files ...]  
#### mypy: error: unrecognized arguments: -Q  
#### ```  
####   
#### ### Pylint version  
####   
#### ```shell  
#### pylint 2.14.0-dev0  
#### astroid 2.11.3  
#### Python 3.10.0b2 (v3.10.0b2:317314165a, May 31 2021, 10:02:22) [Clang 12.0.5 (clang-1205.0.22.9)]  
#### ```  
####   
####   
#### ### OS / Environment  
####   
#### _No response_  
####   
#### ### Additional dependencies  
####   
#### _No response_  
> /private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp588vwwar/tests/functional/i/implicit/implicit_str_concat_latin1.py: 'utf-8' codec can't decode byte 0xe9 in position 105: invalid continuation byte  
> Use --encoding to set the unicode encoding.  
> 33712 prompt tokens, 95 completion tokens, $0.169985 cost  

To address the issue of the traceback being printed for an unrecognized option, we need to modify the following files:

1. `pylint/config/config_initialization.py` - This file likely contains the `_config_initialization` function where the exception is raised.
2. `pylint/config/exceptions.py` - This file likely contains the `_UnrecognizedOptionError` exception class.

Please add these files to the chat so I can proceed with the necessary changes.

> pylint/config/exceptions.py  
> pylint/config/config_initialization.py  
> Add these files to the chat? yes  
> 5270 prompt tokens, 315 completion tokens, $0.031075 cost  

To address the issue of the traceback being printed for an unrecognized option, we need to:

1. Modify the `_UnrecognizedOptionError` exception class in `pylint/config/exceptions.py` to avoid printing the traceback.
2. Update the `_config_initialization` function in `pylint/config/config_initialization.py` to handle the exception gracefully and print a user-friendly message.

Here are the necessary changes:

pylint/config/exceptions.py
```python
<<<<<<< SEARCH
class _UnrecognizedOptionError(Exception):
    """Raised if an ArgumentManager instance tries to parse an option that is unknown."""

    def __init__(self, options: list[str], *args: object) -> None:
        self.options = options
        super().__init__(*args)
=======
class _UnrecognizedOptionError(SystemExit):
    """Raised if an ArgumentManager instance tries to parse an option that is unknown."""

    def __init__(self, options: list[str], *args: object) -> None:
        self.options = options
        super().__init__(f"Unrecognized options: {', '.join(options)}")
>>>>>>> REPLACE
```

pylint/config/config_initialization.py
```python
<<<<<<< SEARCH
        raise _UnrecognizedOptionError(options=unrecognized_options)
=======
        raise _UnrecognizedOptionError(options=unrecognized_options) from None
>>>>>>> REPLACE
```

These changes will ensure that the exception is raised as a `SystemExit` with a user-friendly message, and the traceback will not be printed.

> Applied edit to pylint/config/exceptions.py  
> Applied edit to pylint/config/config_initialization.py  
