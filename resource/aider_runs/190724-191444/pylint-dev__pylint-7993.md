
# aider chat started at 2024-07-19 14:44:27

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpwbx53nej/.git with 3,393 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Using custom braces in message template does not work  
#### ### Bug description  
####   
#### Have any list of errors:  
####   
#### On pylint 1.7 w/ python3.6 - I am able to use this as my message template  
#### ```  
#### $ pylint test.py --msg-template='{{ "Category": "{category}" }}'  
#### No config file found, using default configuration  
#### ************* Module [redacted].test  
#### { "Category": "convention" }  
#### { "Category": "error" }  
#### { "Category": "error" }  
#### { "Category": "convention" }  
#### { "Category": "convention" }  
#### { "Category": "convention" }  
#### { "Category": "error" }  
#### ```  
####   
#### However, on Python3.9 with Pylint 2.12.2, I get the following:  
#### ```  
#### $ pylint test.py --msg-template='{{ "Category": "{category}" }}'  
#### [redacted]/site-packages/pylint/reporters/text.py:206: UserWarning: Don't recognize the argument '{ "Category"' in the --msg-template. Are you sure it is supported on the current version of pylint?  
####   warnings.warn(  
#### ************* Module [redacted].test  
#### " }  
#### " }  
#### " }  
#### " }  
#### " }  
#### " }  
#### ```  
####   
#### Is this intentional or a bug?  
####   
#### ### Configuration  
####   
#### _No response_  
####   
#### ### Command used  
####   
#### ```shell  
#### pylint test.py --msg-template='{{ "Category": "{category}" }}'  
#### ```  
####   
####   
#### ### Pylint output  
####   
#### ```shell  
#### [redacted]/site-packages/pylint/reporters/text.py:206: UserWarning: Don't recognize the argument '{ "Category"' in the --msg-template. Are you sure it is supported on the current version of pylint?  
####   warnings.warn(  
#### ************* Module [redacted].test  
#### " }  
#### " }  
#### " }  
#### " }  
#### " }  
#### " }  
#### ```  
####   
####   
#### ### Expected behavior  
####   
#### Expect the dictionary to print out with `"Category"` as the key.  
####   
#### ### Pylint version  
####   
#### ```shell  
#### Affected Version:  
#### pylint 2.12.2  
#### astroid 2.9.2  
#### Python 3.9.9+ (heads/3.9-dirty:a2295a4, Dec 21 2021, 22:32:52)   
#### [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]  
####   
####   
#### Previously working version:  
#### No config file found, using default configuration  
#### pylint 1.7.4,   
#### astroid 1.6.6  
#### Python 3.6.8 (default, Nov 16 2020, 16:55:22)   
#### [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]  
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
> /private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpwbx53nej/tests/functional/i/implicit/implicit_str_concat_latin1.py: 'utf-8' codec can't decode byte 0xe9 in position 105: invalid continuation byte  
> Use --encoding to set the unicode encoding.  
> 33694 prompt tokens, 48 completion tokens, $0.169190 cost  

To address the issue with custom braces in the message template, we will likely need to modify the following file:

- `pylint/reporters/text.py`

Please add this file to the chat so I can proceed with the necessary changes.

> pylint/reporters/text.py  
> Add these files to the chat? yes  
> 6721 prompt tokens, 120 completion tokens, $0.035405 cost  

To fix the issue with custom braces in the message template, we need to adjust the regular expression used to find arguments in the template. Specifically, we need to account for the possibility of nested braces.

Here are the changes:

pylint/reporters/text.py
```python
<<<<<<< SEARCH
        arguments = re.findall(r"\{(.+?)(:.*)?\}", template)
=======
        arguments = re.findall(r"\{([^{}]+?)(:.*)?\}", template)
>>>>>>> REPLACE
```

This change will allow the regular expression to correctly identify arguments within nested braces.

> Applied edit to pylint/reporters/text.py  
