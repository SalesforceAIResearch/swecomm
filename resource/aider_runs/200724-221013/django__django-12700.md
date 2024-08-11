
# aider chat started at 2024-07-20 19:36:25

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp0942voor/.git with 6,208 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Settings are cleaned insufficiently.  
#### Description  
#### 	  
#### Posting publicly after checking with the rest of the security team.  
#### I just ran into a case where django.views.debug.SafeExceptionReporterFilter.get_safe_settings() would return several un-cleansed values. Looking at cleanse_setting() I realized that we ​only take care of `dict`s but don't take other types of iterables into account but ​return them as-is.  
#### Example:  
#### In my settings.py I have this:  
#### MY_SETTING = {  
#### 	"foo": "value",  
#### 	"secret": "value",  
#### 	"token": "value",  
#### 	"something": [  
#### 		{"foo": "value"},  
#### 		{"secret": "value"},  
#### 		{"token": "value"},  
#### 	],  
#### 	"else": [  
#### 		[  
#### 			{"foo": "value"},  
#### 			{"secret": "value"},  
#### 			{"token": "value"},  
#### 		],  
#### 		[  
#### 			{"foo": "value"},  
#### 			{"secret": "value"},  
#### 			{"token": "value"},  
#### 		],  
#### 	]  
#### }  
#### On Django 3.0 and below:  
#### >>> import pprint  
#### >>> from django.views.debug import get_safe_settings  
#### >>> pprint.pprint(get_safe_settings()["MY_SETTING"])  
#### {'else': [[{'foo': 'value'}, {'secret': 'value'}, {'token': 'value'}],  
#### 		 [{'foo': 'value'}, {'secret': 'value'}, {'token': 'value'}]],  
####  'foo': 'value',  
####  'secret': '********************',  
####  'something': [{'foo': 'value'}, {'secret': 'value'}, {'token': 'value'}],  
####  'token': '********************'}  
#### On Django 3.1 and up:  
#### >>> from django.views.debug import SafeExceptionReporterFilter  
#### >>> import pprint  
#### >>> pprint.pprint(SafeExceptionReporterFilter().get_safe_settings()["MY_SETTING"])  
#### {'else': [[{'foo': 'value'}, {'secret': 'value'}, {'token': 'value'}],  
#### 		 [{'foo': 'value'}, {'secret': 'value'}, {'token': 'value'}]],  
####  'foo': 'value',  
####  'secret': '********************',  
####  'something': [{'foo': 'value'}, {'secret': 'value'}, {'token': 'value'}],  
####  'token': '********************'}  
> 34071 prompt tokens, 71 completion tokens, $0.171420 cost  

To address the issue with insufficiently cleaned settings, we need to modify the `cleanse_setting` function in the `django/views/debug.py` file. This function should be updated to handle other types of iterables, not just dictionaries.

Please add the following file to the chat so I can provide the necessary changes:
- `django/views/debug.py`

> django/views/debug.py  
> Add these files to the chat? yes  
> 8556 prompt tokens, 125 completion tokens, $0.044655 cost  

Here are the necessary changes to handle other types of iterables in the `cleanse_setting` function:

django/views/debug.py
```python
<<<<<<< SEARCH
            else:
=======
            elif isinstance(value, (list, tuple, set)):
                cleansed = type(value)(self.cleanse_setting(k, v) for k, v in enumerate(value))
>>>>>>> REPLACE
```

django/views/debug.py
```python
<<<<<<< SEARCH
        except TypeError:
=======
        except (TypeError, IndexError):
>>>>>>> REPLACE
```

This will ensure that lists, tuples, and sets are also cleansed properly.

> Applied edit to django/views/debug.py  
>   
> Test Script:  ./tests/runtests.py --verbosity 2 view_tests.tests.test_debug;  
> [django__django__3.1] [django__django-12700] Command: ./tests/runtests.py --verbosity 2 view_tests.tests.test_debug   
> [django__django__3.1] [django__django-12700] Subprocess args: {"cwd": "/opt/django__django", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [django__django__3.1] [django__django-12700] Std. Output:  
> Testing against Django installed in '/opt/django__django/django' with up to 16 processes  
> Importing application view_tests  
> Skipping setup of unused database(s): other.  
> Operations to perform:  
>   Synchronize unmigrated apps: auth, contenttypes, messages, sessions, staticfiles, view_tests  
>   Apply all migrations: admin, sites  
> Synchronizing apps without migrations:  
>   Creating tables...  
>     Creating table django_content_type  
>     Creating table auth_permission  
>     Creating table auth_group  
>     Creating table auth_user  
>     Creating table django_session  
>     Creating table view_tests_author  
>     Creating table view_tests_article  
>     Creating table view_tests_urlarticle  
>     Creating table view_tests_datearticle  
>     Running deferred SQL...  
> Running migrations:  
>   Applying admin.0001_initial... OK  
>   Applying admin.0002_logentry_remove_auto_add... OK  
>   Applying admin.0003_logentry_add_action_flag_choices... OK  
>   Applying sites.0001_initial... OK  
>   Applying sites.0002_alter_domain_unique... OK  
> System check identified no issues (0 silenced).  
> Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> test_sensitive_post_parameters_not_called (view_tests.tests.test_debug.DecoratorsTests) ... ok  
> test_sensitive_variables_not_called (view_tests.tests.test_debug.DecoratorsTests) ... ok  
> test_repr (view_tests.tests.test_debug.CallableSettingWrapperTests) ... ok  
> test_cleansed_substitute_override (view_tests.tests.test_debug.CustomExceptionReporterFilterTests) ... ok  
> test_hidden_settings_override (view_tests.tests.test_debug.CustomExceptionReporterFilterTests) ... ok  
> test_setting_allows_custom_subclass (view_tests.tests.test_debug.CustomExceptionReporterFilterTests) ... ok  
> test_handle_db_exception (view_tests.tests.test_debug.DebugViewQueriesAllowedTests) ... ERROR  
> test_disallowed_host (view_tests.tests.test_debug.PlainTextReportTests)  
> An exception report can be generated even for a disallowed host. ... ERROR  
> test_message_only (view_tests.tests.test_debug.PlainTextReportTests) ... ERROR  
> test_no_exception (view_tests.tests.test_debug.PlainTextReportTests)  
> An exception report can be generated for just a request ... ERROR  
> test_no_request (view_tests.tests.test_debug.PlainTextReportTests)  
> An exception report can be generated without request ... ERROR  
> test_request_and_exception (view_tests.tests.test_debug.PlainTextReportTests)  
> A simple exception report can be generated ... ERROR  
> test_request_and_message (view_tests.tests.test_debug.PlainTextReportTests)  
> A message can be provided in addition to a request ... ERROR  
> test_request_with_items_key (view_tests.tests.test_debug.PlainTextReportTests) ... ERROR  
> test_template_exception (view_tests.tests.test_debug.PlainTextReportTests) ... ERROR  
> test_disallowed_host (view_tests.tests.test_debug.ExceptionReporterTests)  
> An exception report can be generated even for a disallowed host. ... ERROR  
> test_encoding_error (view_tests.tests.test_debug.ExceptionReporterTests) ... ERROR  
> test_eol_support (view_tests.tests.test_debug.ExceptionReporterTests)  
> The ExceptionReporter supports Unix, Windows and Macintosh EOL markers ... ok  
> test_exception_fetching_user (view_tests.tests.test_debug.ExceptionReporterTests) ... ERROR  
> test_ignore_traceback_evaluation_exceptions (view_tests.tests.test_debug.ExceptionReporterTests) ... ERROR  
> test_local_variable_escaping (view_tests.tests.test_debug.ExceptionReporterTests)  
> Safe strings in local variables are escaped. ... ERROR  
> test_message_only (view_tests.tests.test_debug.ExceptionReporterTests) ... ERROR  
> test_no_exception (view_tests.tests.test_debug.ExceptionReporterTests)  
> An exception report can be generated for just a request ... ERROR  
> test_no_request (view_tests.tests.test_debug.ExceptionReporterTests)  
> An exception report can be generated without request ... ERROR  
> test_non_utf8_values_handling (view_tests.tests.test_debug.ExceptionReporterTests)  
> Non-UTF-8 exceptions/values should not make the output generation choke. ... ERROR  
> test_reporting_frames_for_cyclic_reference (view_tests.tests.test_debug.ExceptionReporterTests) ... ok  
> test_reporting_frames_source_not_match (view_tests.tests.test_debug.ExceptionReporterTests) ... ERROR  
> test_reporting_frames_without_source (view_tests.tests.test_debug.ExceptionReporterTests) ... ERROR  
> test_reporting_of_nested_exceptions (view_tests.tests.test_debug.ExceptionReporterTests) ... ERROR  
> test_request_and_exception (view_tests.tests.test_debug.ExceptionReporterTests)  
> A simple exception report can be generated ... ERROR  
> test_request_and_message (view_tests.tests.test_debug.ExceptionReporterTests)  
> A message can be provided in addition to a request ... ERROR  
> test_request_with_items_key (view_tests.tests.test_debug.ExceptionReporterTests) ... ERROR  
> test_template_encoding (view_tests.tests.test_debug.ExceptionReporterTests) ... ERROR  
> test_too_large_values_handling (view_tests.tests.test_debug.ExceptionReporterTests)  
> Large values should not create a large HTML. ... ERROR  
> test_unfrozen_importlib (view_tests.tests.test_debug.ExceptionReporterTests) ... ERROR  
> test_unprintable_values_handling (view_tests.tests.test_debug.ExceptionReporterTests)  
> Unprintable values should not make the output generation choke. ... ERROR  
> test_custom_exception_reporter_filter (view_tests.tests.test_debug.NonHTMLResponseExceptionReporterFilter) ... ERROR  
> test_non_html_response_encoding (view_tests.tests.test_debug.NonHTMLResponseExceptionReporterFilter) ... ERROR  
> test_non_sensitive_request (view_tests.tests.test_debug.NonHTMLResponseExceptionReporterFilter) ... ERROR  
> test_paranoid_request (view_tests.tests.test_debug.NonHTMLResponseExceptionReporterFilter) ... ERROR  
> test_sensitive_request (view_tests.tests.test_debug.NonHTMLResponseExceptionReporterFilter) ... ERROR  
> test_400 (view_tests.tests.test_debug.NonDjangoTemplatesDebugViewTests) ... ERROR  
> test_403 (view_tests.tests.test_debug.NonDjangoTemplatesDebugViewTests) ... ok  
> test_404 (view_tests.tests.test_debug.NonDjangoTemplatesDebugViewTests) ... ERROR  
> test_template_not_found_error (view_tests.tests.test_debug.NonDjangoTemplatesDebugViewTests) ... ERROR  
> test_callable_settings (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_callable_settings_forbidding_to_set_attributes (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_cleanse_setting_basic (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_cleanse_setting_ignore_case (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ok  
> test_cleanse_setting_recurses_in_dictionary (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_custom_exception_reporter_filter (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_dict_setting_with_non_str_key (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_exception_report_uses_meta_filtering (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_multivalue_dict_key_error (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_non_sensitive_request (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_paranoid_request (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_request_meta_filtering (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_sensitive_function_arguments (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_sensitive_function_keyword_arguments (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_sensitive_method (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_sensitive_request (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_sensitive_settings (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_settings_with_sensitive_keys (view_tests.tests.test_debug.ExceptionReporterFilterTests) ... ERROR  
> test_400 (view_tests.tests.test_debug.DebugViewTests) ... ERROR  
> test_403 (view_tests.tests.test_debug.DebugViewTests) ... ok  
> test_403_template (view_tests.tests.test_debug.DebugViewTests) ... ok  
> test_404 (view_tests.tests.test_debug.DebugViewTests) ... ERROR  
> test_404_empty_path_not_in_urls (view_tests.tests.test_debug.DebugViewTests) ... ERROR  
> test_404_not_in_urls (view_tests.tests.test_debug.DebugViewTests) ... ERROR  
> test_classbased_technical_404 (view_tests.tests.test_debug.DebugViewTests) ... ERROR  
> test_default_urlconf_template (view_tests.tests.test_debug.DebugViewTests) ... ok  
> test_exception_reporter_from_request (view_tests.tests.test_debug.DebugViewTests) ... ok  
> test_exception_reporter_from_settings (view_tests.tests.test_debug.DebugViewTests) ... ok  
> test_files (view_tests.tests.test_debug.DebugViewTests) ... ERROR  
> test_no_template_source_loaders (view_tests.tests.test_debug.DebugViewTests) ... ERROR  
> test_non_l10ned_numeric_ids (view_tests.tests.test_debug.DebugViewTests) ... ERROR  
> test_regression_21530 (view_tests.tests.test_debug.DebugViewTests) ... ERROR  
> test_technical_404 (view_tests.tests.test_debug.DebugViewTests) ... ERROR  
> test_technical_404_converter_raise_404 (view_tests.tests.test_debug.DebugViewTests) ... ERROR  
> test_template_encoding (view_tests.tests.test_debug.DebugViewTests) ... ERROR  
> test_template_exceptions (view_tests.tests.test_debug.DebugViewTests) ... FAIL  
> test_template_loader_postmortem (view_tests.tests.test_debug.DebugViewTests)  
> Tests for not existing file ... ERROR  
>   
> ======================================================================  
> ERROR: test_handle_db_exception (view_tests.tests.test_debug.DebugViewQueriesAllowedTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 280, in test_handle_db_exception  
>     response = technical_500_response(rf.get('/'), *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_disallowed_host (view_tests.tests.test_debug.PlainTextReportTests)  
> An exception report can be generated even for a disallowed host.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/django/test/utils.py", line 381, in inner  
>     return func(*args, **kwargs)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 873, in test_disallowed_host  
>     text = reporter.get_traceback_text()  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_message_only (view_tests.tests.test_debug.PlainTextReportTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 866, in test_message_only  
>     reporter.get_traceback_text()  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 300, in get_traceback_data  
>     'settings': self.filter.get_safe_settings(),  
>   File "/opt/django__django/django/views/debug.py", line 113, in get_safe_settings  
>     settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_no_exception (view_tests.tests.test_debug.PlainTextReportTests)  
> An exception report can be generated for just a request  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 807, in test_no_exception  
>     reporter.get_traceback_text()  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_no_request (view_tests.tests.test_debug.PlainTextReportTests)  
> An exception report can be generated without request  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 792, in test_no_request  
>     text = reporter.get_traceback_text()  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 300, in get_traceback_data  
>     'settings': self.filter.get_safe_settings(),  
>   File "/opt/django__django/django/views/debug.py", line 113, in get_safe_settings  
>     settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_request_and_exception (view_tests.tests.test_debug.PlainTextReportTests)  
> A simple exception report can be generated  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 773, in test_request_and_exception  
>     text = reporter.get_traceback_text()  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_request_and_message (view_tests.tests.test_debug.PlainTextReportTests)  
> A message can be provided in addition to a request  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 813, in test_request_and_message  
>     reporter.get_traceback_text()  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_request_with_items_key (view_tests.tests.test_debug.PlainTextReportTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 843, in test_request_with_items_key  
>     text = reporter.get_traceback_text()  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_template_exception (view_tests.tests.test_debug.PlainTextReportTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/django/test/utils.py", line 381, in inner  
>     return func(*args, **kwargs)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 823, in test_template_exception  
>     text = reporter.get_traceback_text()  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_disallowed_host (view_tests.tests.test_debug.ExceptionReporterTests)  
> An exception report can be generated even for a disallowed host.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/django/test/utils.py", line 381, in inner  
>     return func(*args, **kwargs)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 682, in test_disallowed_host  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_encoding_error (view_tests.tests.test_debug.ExceptionReporterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 634, in test_encoding_error  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 300, in get_traceback_data  
>     'settings': self.filter.get_safe_settings(),  
>   File "/opt/django__django/django/views/debug.py", line 113, in get_safe_settings  
>     settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_exception_fetching_user (view_tests.tests.test_debug.ExceptionReporterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 737, in test_exception_fetching_user  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_ignore_traceback_evaluation_exceptions (view_tests.tests.test_debug.ExceptionReporterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 673, in test_ignore_traceback_evaluation_exceptions  
>     ExceptionReporter(request, exc_type, exc_value, tb).get_traceback_html(),  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_local_variable_escaping (view_tests.tests.test_debug.ExceptionReporterTests)  
> Safe strings in local variables are escaped.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 590, in test_local_variable_escaping  
>     html = ExceptionReporter(None, exc_type, exc_value, tb).get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 300, in get_traceback_data  
>     'settings': self.filter.get_safe_settings(),  
>   File "/opt/django__django/django/views/debug.py", line 113, in get_safe_settings  
>     settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_message_only (view_tests.tests.test_debug.ExceptionReporterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 557, in test_message_only  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 300, in get_traceback_data  
>     'settings': self.filter.get_safe_settings(),  
>   File "/opt/django__django/django/views/debug.py", line 113, in get_safe_settings  
>     settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_no_exception (view_tests.tests.test_debug.ExceptionReporterTests)  
> An exception report can be generated for just a request  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 383, in test_no_exception  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_no_request (view_tests.tests.test_debug.ExceptionReporterTests)  
> An exception report can be generated without request  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 349, in test_no_request  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 300, in get_traceback_data  
>     'settings': self.filter.get_safe_settings(),  
>   File "/opt/django__django/django/views/debug.py", line 113, in get_safe_settings  
>     settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_non_utf8_values_handling (view_tests.tests.test_debug.ExceptionReporterTests)  
> Non-UTF-8 exceptions/values should not make the output generation choke.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 579, in test_non_utf8_values_handling  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 300, in get_traceback_data  
>     'settings': self.filter.get_safe_settings(),  
>   File "/opt/django__django/django/views/debug.py", line 113, in get_safe_settings  
>     settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_reporting_frames_source_not_match (view_tests.tests.test_debug.ExceptionReporterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 481, in test_reporting_frames_source_not_match  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_reporting_frames_without_source (view_tests.tests.test_debug.ExceptionReporterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 440, in test_reporting_frames_without_source  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_reporting_of_nested_exceptions (view_tests.tests.test_debug.ExceptionReporterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 412, in test_reporting_of_nested_exceptions  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_request_and_exception (view_tests.tests.test_debug.ExceptionReporterTests)  
> A simple exception report can be generated  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 328, in test_request_and_exception  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_request_and_message (view_tests.tests.test_debug.ExceptionReporterTests)  
> A message can be provided in addition to a request  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 544, in test_request_and_message  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_request_with_items_key (view_tests.tests.test_debug.ExceptionReporterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 694, in test_request_with_items_key  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_template_encoding (view_tests.tests.test_debug.ExceptionReporterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 754, in test_template_encoding  
>     reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 300, in get_traceback_data  
>     'settings': self.filter.get_safe_settings(),  
>   File "/opt/django__django/django/views/debug.py", line 113, in get_safe_settings  
>     settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_too_large_values_handling (view_tests.tests.test_debug.ExceptionReporterTests)  
> Large values should not create a large HTML.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 620, in test_too_large_values_handling  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 300, in get_traceback_data  
>     'settings': self.filter.get_safe_settings(),  
>   File "/opt/django__django/django/views/debug.py", line 113, in get_safe_settings  
>     settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_unfrozen_importlib (view_tests.tests.test_debug.ExceptionReporterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 650, in test_unfrozen_importlib  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_unprintable_values_handling (view_tests.tests.test_debug.ExceptionReporterTests)  
> Unprintable values should not make the output generation choke.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 604, in test_unprintable_values_handling  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 300, in get_traceback_data  
>     'settings': self.filter.get_safe_settings(),  
>   File "/opt/django__django/django/views/debug.py", line 113, in get_safe_settings  
>     settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_custom_exception_reporter_filter (view_tests.tests.test_debug.NonHTMLResponseExceptionReporterFilter)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1359, in test_custom_exception_reporter_filter  
>     self.verify_unsafe_response(custom_exception_reporter_filter_view, check_for_vars=False)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 893, in verify_unsafe_response  
>     response = view(request)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 42, in sensitive_variables_wrapper  
>     return func(*func_args, **func_kwargs)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 89, in sensitive_post_parameters_wrapper  
>     return view(request, *args, **kwargs)  
>   File "/opt/django__django/tests/view_tests/views.py", line 226, in custom_exception_reporter_filter_view  
>     send_log(request, exc_info)  
>   File "/opt/django__django/tests/view_tests/views.py", line 114, in send_log  
>     extra={'status_code': 500, 'request': request},  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1337, in error  
>     self._log(ERROR, msg, args, **kwargs)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1444, in _log  
>     self.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1454, in handle  
>     self.callHandlers(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1516, in callHandlers  
>     hdlr.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 865, in handle  
>     self.emit(record)  
>   File "/opt/django__django/django/utils/log.py", line 120, in emit  
>     message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_non_html_response_encoding (view_tests.tests.test_debug.NonHTMLResponseExceptionReporterFilter)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/django/test/utils.py", line 381, in inner  
>     return func(*args, **kwargs)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1366, in test_non_html_response_encoding  
>     response = self.client.get('/raises500/', HTTP_ACCEPT='application/json')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 55, in technical_500_response  
>     text = reporter.get_traceback_text()  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_non_sensitive_request (view_tests.tests.test_debug.NonHTMLResponseExceptionReporterFilter)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1326, in test_non_sensitive_request  
>     self.verify_unsafe_response(non_sensitive_view, check_for_vars=False)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 893, in verify_unsafe_response  
>     response = view(request)  
>   File "/opt/django__django/tests/view_tests/views.py", line 129, in non_sensitive_view  
>     send_log(request, exc_info)  
>   File "/opt/django__django/tests/view_tests/views.py", line 114, in send_log  
>     extra={'status_code': 500, 'request': request},  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1337, in error  
>     self._log(ERROR, msg, args, **kwargs)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1444, in _log  
>     self.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1454, in handle  
>     self.callHandlers(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1516, in callHandlers  
>     hdlr.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 865, in handle  
>     self.emit(record)  
>   File "/opt/django__django/django/utils/log.py", line 120, in emit  
>     message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_paranoid_request (view_tests.tests.test_debug.NonHTMLResponseExceptionReporterFilter)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1348, in test_paranoid_request  
>     self.verify_unsafe_response(paranoid_view, check_for_vars=False)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 893, in verify_unsafe_response  
>     response = view(request)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 42, in sensitive_variables_wrapper  
>     return func(*func_args, **func_kwargs)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 89, in sensitive_post_parameters_wrapper  
>     return view(request, *args, **kwargs)  
>   File "/opt/django__django/tests/view_tests/views.py", line 161, in paranoid_view  
>     send_log(request, exc_info)  
>   File "/opt/django__django/tests/view_tests/views.py", line 114, in send_log  
>     extra={'status_code': 500, 'request': request},  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1337, in error  
>     self._log(ERROR, msg, args, **kwargs)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1444, in _log  
>     self.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1454, in handle  
>     self.callHandlers(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1516, in callHandlers  
>     hdlr.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 865, in handle  
>     self.emit(record)  
>   File "/opt/django__django/django/utils/log.py", line 120, in emit  
>     message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_sensitive_request (view_tests.tests.test_debug.NonHTMLResponseExceptionReporterFilter)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1337, in test_sensitive_request  
>     self.verify_unsafe_response(sensitive_view, check_for_vars=False)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 893, in verify_unsafe_response  
>     response = view(request)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 42, in sensitive_variables_wrapper  
>     return func(*func_args, **func_kwargs)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 89, in sensitive_post_parameters_wrapper  
>     return view(request, *args, **kwargs)  
>   File "/opt/django__django/tests/view_tests/views.py", line 145, in sensitive_view  
>     send_log(request, exc_info)  
>   File "/opt/django__django/tests/view_tests/views.py", line 114, in send_log  
>     extra={'status_code': 500, 'request': request},  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1337, in error  
>     self._log(ERROR, msg, args, **kwargs)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1444, in _log  
>     self.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1454, in handle  
>     self.callHandlers(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1516, in callHandlers  
>     hdlr.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 865, in handle  
>     self.emit(record)  
>   File "/opt/django__django/django/utils/log.py", line 120, in emit  
>     message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_400 (view_tests.tests.test_debug.NonDjangoTemplatesDebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 297, in test_400  
>     response = self.client.get('/raises400/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_404 (view_tests.tests.test_debug.NonDjangoTemplatesDebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 305, in test_404  
>     response = self.client.get('/raises404/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_template_not_found_error (view_tests.tests.test_debug.NonDjangoTemplatesDebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 312, in test_template_not_found_error  
>     response = self.client.get(url)  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_callable_settings (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1166, in test_callable_settings  
>     response = self.client.get('/raises500/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_callable_settings_forbidding_to_set_attributes (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1181, in test_callable_settings_forbidding_to_set_attributes  
>     response = self.client.get('/raises500/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_cleanse_setting_basic (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1231, in test_cleanse_setting_basic  
>     self.assertEqual(reporter_filter.cleanse_setting('TEST', 'TEST'), 'TEST')  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_cleanse_setting_recurses_in_dictionary (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1248, in test_cleanse_setting_recurses_in_dictionary  
>     reporter_filter.cleanse_setting('SETTING_NAME', initial),  
>   File "/opt/django__django/django/views/debug.py", line 92, in cleanse_setting  
>     cleansed = {k: self.cleanse_setting(k, v) for k, v in value.items()}  
>   File "/opt/django__django/django/views/debug.py", line 92, in <dictcomp>  
>     cleansed = {k: self.cleanse_setting(k, v) for k, v in value.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_custom_exception_reporter_filter (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1112, in test_custom_exception_reporter_filter  
>     self.verify_unsafe_response(custom_exception_reporter_filter_view)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 893, in verify_unsafe_response  
>     response = view(request)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 42, in sensitive_variables_wrapper  
>     return func(*func_args, **func_kwargs)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 89, in sensitive_post_parameters_wrapper  
>     return view(request, *args, **kwargs)  
>   File "/opt/django__django/tests/view_tests/views.py", line 226, in custom_exception_reporter_filter_view  
>     send_log(request, exc_info)  
>   File "/opt/django__django/tests/view_tests/views.py", line 114, in send_log  
>     extra={'status_code': 500, 'request': request},  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1337, in error  
>     self._log(ERROR, msg, args, **kwargs)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1444, in _log  
>     self.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1454, in handle  
>     self.callHandlers(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1516, in callHandlers  
>     hdlr.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 865, in handle  
>     self.emit(record)  
>   File "/opt/django__django/django/utils/log.py", line 120, in emit  
>     message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_dict_setting_with_non_str_key (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1190, in test_dict_setting_with_non_str_key  
>     response = self.client.get('/raises500/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_exception_report_uses_meta_filtering (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1261, in test_exception_report_uses_meta_filtering  
>     response = self.client.get('/raises500/', HTTP_SECRET_HEADER='super_secret')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 108, in response_for_exception  
>     exc_info=sys.exc_info(),  
>   File "/opt/django__django/django/utils/log.py", line 228, in log_response  
>     exc_info=exc_info,  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1337, in error  
>     self._log(ERROR, msg, args, **kwargs)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1444, in _log  
>     self.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1454, in handle  
>     self.callHandlers(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1516, in callHandlers  
>     hdlr.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 865, in handle  
>     self.emit(record)  
>   File "/opt/django__django/django/utils/log.py", line 120, in emit  
>     message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_multivalue_dict_key_error (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1099, in test_multivalue_dict_key_error  
>     self.verify_unsafe_response(multivalue_dict_key_error)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 893, in verify_unsafe_response  
>     response = view(request)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 42, in sensitive_variables_wrapper  
>     return func(*func_args, **func_kwargs)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 89, in sensitive_post_parameters_wrapper  
>     return view(request, *args, **kwargs)  
>   File "/opt/django__django/tests/view_tests/views.py", line 276, in multivalue_dict_key_error  
>     send_log(request, exc_info)  
>   File "/opt/django__django/tests/view_tests/views.py", line 114, in send_log  
>     extra={'status_code': 500, 'request': request},  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1337, in error  
>     self._log(ERROR, msg, args, **kwargs)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1444, in _log  
>     self.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1454, in handle  
>     self.callHandlers(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1516, in callHandlers  
>     hdlr.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 865, in handle  
>     self.emit(record)  
>   File "/opt/django__django/django/utils/log.py", line 120, in emit  
>     message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_non_sensitive_request (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1060, in test_non_sensitive_request  
>     self.verify_unsafe_response(non_sensitive_view)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 893, in verify_unsafe_response  
>     response = view(request)  
>   File "/opt/django__django/tests/view_tests/views.py", line 129, in non_sensitive_view  
>     send_log(request, exc_info)  
>   File "/opt/django__django/tests/view_tests/views.py", line 114, in send_log  
>     extra={'status_code': 500, 'request': request},  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1337, in error  
>     self._log(ERROR, msg, args, **kwargs)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1444, in _log  
>     self.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1454, in handle  
>     self.callHandlers(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1516, in callHandlers  
>     hdlr.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 865, in handle  
>     self.emit(record)  
>   File "/opt/django__django/django/utils/log.py", line 120, in emit  
>     message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_paranoid_request (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1086, in test_paranoid_request  
>     self.verify_unsafe_response(paranoid_view)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 893, in verify_unsafe_response  
>     response = view(request)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 42, in sensitive_variables_wrapper  
>     return func(*func_args, **func_kwargs)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 89, in sensitive_post_parameters_wrapper  
>     return view(request, *args, **kwargs)  
>   File "/opt/django__django/tests/view_tests/views.py", line 161, in paranoid_view  
>     send_log(request, exc_info)  
>   File "/opt/django__django/tests/view_tests/views.py", line 114, in send_log  
>     extra={'status_code': 500, 'request': request},  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1337, in error  
>     self._log(ERROR, msg, args, **kwargs)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1444, in _log  
>     self.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1454, in handle  
>     self.callHandlers(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1516, in callHandlers  
>     hdlr.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 865, in handle  
>     self.emit(record)  
>   File "/opt/django__django/django/utils/log.py", line 120, in emit  
>     message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_request_meta_filtering (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1256, in test_request_meta_filtering  
>     reporter_filter.get_safe_request_meta(request)['HTTP_SECRET_HEADER'],  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_sensitive_function_arguments (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1138, in test_sensitive_function_arguments  
>     self.verify_unsafe_response(sensitive_args_function_caller)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 893, in verify_unsafe_response  
>     response = view(request)  
>   File "/opt/django__django/tests/view_tests/views.py", line 170, in sensitive_args_function_caller  
>     send_log(request, exc_info)  
>   File "/opt/django__django/tests/view_tests/views.py", line 114, in send_log  
>     extra={'status_code': 500, 'request': request},  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1337, in error  
>     self._log(ERROR, msg, args, **kwargs)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1444, in _log  
>     self.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1454, in handle  
>     self.callHandlers(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1516, in callHandlers  
>     hdlr.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 865, in handle  
>     self.emit(record)  
>   File "/opt/django__django/django/utils/log.py", line 120, in emit  
>     message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_sensitive_function_keyword_arguments (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1152, in test_sensitive_function_keyword_arguments  
>     self.verify_unsafe_response(sensitive_kwargs_function_caller)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 893, in verify_unsafe_response  
>     response = view(request)  
>   File "/opt/django__django/tests/view_tests/views.py", line 188, in sensitive_kwargs_function_caller  
>     send_log(request, exc_info)  
>   File "/opt/django__django/tests/view_tests/views.py", line 114, in send_log  
>     extra={'status_code': 500, 'request': request},  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1337, in error  
>     self._log(ERROR, msg, args, **kwargs)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1444, in _log  
>     self.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1454, in handle  
>     self.callHandlers(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1516, in callHandlers  
>     hdlr.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 865, in handle  
>     self.emit(record)  
>   File "/opt/django__django/django/utils/log.py", line 120, in emit  
>     message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_sensitive_method (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1124, in test_sensitive_method  
>     self.verify_unsafe_response(sensitive_method_view, check_for_POST_params=False)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 893, in verify_unsafe_response  
>     response = view(request)  
>   File "/opt/django__django/tests/view_tests/views.py", line 264, in sensitive_method_view  
>     return Klass().method(request)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 42, in sensitive_variables_wrapper  
>     return func(*func_args, **func_kwargs)  
>   File "/opt/django__django/tests/view_tests/views.py", line 259, in method  
>     send_log(request, exc_info)  
>   File "/opt/django__django/tests/view_tests/views.py", line 114, in send_log  
>     extra={'status_code': 500, 'request': request},  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1337, in error  
>     self._log(ERROR, msg, args, **kwargs)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1444, in _log  
>     self.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1454, in handle  
>     self.callHandlers(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1516, in callHandlers  
>     hdlr.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 865, in handle  
>     self.emit(record)  
>   File "/opt/django__django/django/utils/log.py", line 120, in emit  
>     message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_sensitive_request (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1073, in test_sensitive_request  
>     self.verify_unsafe_response(sensitive_view)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 893, in verify_unsafe_response  
>     response = view(request)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 42, in sensitive_variables_wrapper  
>     return func(*func_args, **func_kwargs)  
>   File "/opt/django__django/django/views/decorators/debug.py", line 89, in sensitive_post_parameters_wrapper  
>     return view(request, *args, **kwargs)  
>   File "/opt/django__django/tests/view_tests/views.py", line 145, in sensitive_view  
>     send_log(request, exc_info)  
>   File "/opt/django__django/tests/view_tests/views.py", line 114, in send_log  
>     extra={'status_code': 500, 'request': request},  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1337, in error  
>     self._log(ERROR, msg, args, **kwargs)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1444, in _log  
>     self.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1454, in handle  
>     self.callHandlers(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 1516, in callHandlers  
>     hdlr.handle(record)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/logging/__init__.py", line 865, in handle  
>     self.emit(record)  
>   File "/opt/django__django/django/utils/log.py", line 120, in emit  
>     message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())  
>   File "/opt/django__django/django/views/debug.py", line 334, in get_traceback_text  
>     c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_sensitive_settings (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1206, in test_sensitive_settings  
>     response = self.client.get('/raises500/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_settings_with_sensitive_keys (view_tests.tests.test_debug.ExceptionReporterFilterTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 1226, in test_settings_with_sensitive_keys  
>     response = self.client.get('/raises500/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_400 (view_tests.tests.test_debug.DebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 86, in test_400  
>     response = self.client.get('/raises400/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_404 (view_tests.tests.test_debug.DebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 114, in test_404  
>     response = self.client.get('/raises404/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_404_empty_path_not_in_urls (view_tests.tests.test_debug.DebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/django/test/utils.py", line 381, in inner  
>     return func(*args, **kwargs)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 132, in test_404_empty_path_not_in_urls  
>     response = self.client.get('/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_404_not_in_urls (view_tests.tests.test_debug.DebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 119, in test_404_not_in_urls  
>     response = self.client.get('/not-in-urls')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_classbased_technical_404 (view_tests.tests.test_debug.DebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 141, in test_classbased_technical_404  
>     response = self.client.get('/classbased404/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_files (view_tests.tests.test_debug.DebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 72, in test_files  
>     response = self.client.get('/raises/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_no_template_source_loaders (view_tests.tests.test_debug.DebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 202, in test_no_template_source_loaders  
>     self.client.get('/render_no_template/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_non_l10ned_numeric_ids (view_tests.tests.test_debug.DebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 151, in test_non_l10ned_numeric_ids  
>     response = self.client.get('/raises500/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_regression_21530 (view_tests.tests.test_debug.DebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/django/test/utils.py", line 381, in inner  
>     return func(*args, **kwargs)  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 227, in test_regression_21530  
>     response = self.client.get('/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_technical_404 (view_tests.tests.test_debug.DebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 136, in test_technical_404  
>     response = self.client.get('/technical404/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_technical_404_converter_raise_404 (view_tests.tests.test_debug.DebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 249, in test_technical_404_converter_raise_404  
>     response = self.client.get('/path-post/1/')  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_template_encoding (view_tests.tests.test_debug.DebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 244, in test_template_encoding  
>     technical_404_response(mock.MagicMock(), mock.Mock())  
>   File "/opt/django__django/django/views/debug.py", line 510, in technical_404_response  
>     'settings': reporter_filter.get_safe_settings(),  
>   File "/opt/django__django/django/views/debug.py", line 113, in get_safe_settings  
>     settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> ERROR: test_template_loader_postmortem (view_tests.tests.test_debug.DebugViewTests)  
> Tests for not existing file  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 185, in test_template_loader_postmortem  
>     response = self.client.get(reverse('raises_template_does_not_exist', kwargs={"path": template_name}))  
>   File "/opt/django__django/django/test/client.py", line 732, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 395, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 470, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 704, in request  
>     response = self.handler(environ)  
>   File "/opt/django__django/django/test/client.py", line 142, in __call__  
>     response = self.get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 128, in get_response  
>     response = self._middleware_chain(request)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 49, in inner  
>     response = response_for_exception(request, exc)  
>   File "/opt/django__django/django/core/handlers/exception.py", line 103, in response_for_exception  
>     response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())  
>   File "/opt/django__django/django/core/handlers/exception.py", line 138, in handle_uncaught_exception  
>     return debug.technical_500_response(request, *exc_info)  
>   File "/opt/django__django/django/views/debug.py", line 52, in technical_500_response  
>     html = reporter.get_traceback_html()  
>   File "/opt/django__django/django/views/debug.py", line 327, in get_traceback_html  
>     c = Context(self.get_traceback_data(), use_l10n=False)  
>   File "/opt/django__django/django/views/debug.py", line 297, in get_traceback_data  
>     'request_meta': self.filter.get_safe_request_meta(self.request),  
>   File "/opt/django__django/django/views/debug.py", line 122, in get_safe_request_meta  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 122, in <dictcomp>  
>     return {k: self.cleanse_setting(k, v) for k, v in request.META.items()}  
>   File "/opt/django__django/django/views/debug.py", line 100, in cleanse_setting  
>     if callable(cleansed):  
> UnboundLocalError: local variable 'cleansed' referenced before assignment  
>   
> ======================================================================  
> FAIL: test_template_exceptions (view_tests.tests.test_debug.DebugViewTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/view_tests/tests/test_debug.py", line 172, in test_template_exceptions  
>     "traceback, instead found: %s" % raising_loc  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 838, in assertNotEqual  
>     raise self.failureException(msg)  
> AssertionError: -1 == -1 : Failed to find 'raise Exception' in last frame of traceback, instead found: if callable(cleansed):  
>   
> ----------------------------------------------------------------------  
> Ran 82 tests in 3.287s  
>   
> FAILED (failures=1, errors=66)  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
>    
> [django__django__3.1] [django__django-12700] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [django__django__3.1] [django__django-12700] Test script run successful   
> Attempt to fix test errors? yes  
> 47340 prompt tokens, 191 completion tokens, $0.239565 cost  

To fix the issue with the `cleansed` variable being referenced before assignment, we need to ensure that the `cleansed` variable is always assigned a value before it is used. Here are the necessary changes:

django/views/debug.py
```python
<<<<<<< SEARCH
                cleansed = type(value)(self.cleanse_setting(k, v) for k, v in enumerate(value))
                cleansed = value
=======
                cleansed = type(value)(self.cleanse_setting(k, v) for k, v in enumerate(value))
            else:
                cleansed = value
>>>>>>> REPLACE
```

django/views/debug.py
```python
<<<<<<< SEARCH
        except (TypeError, IndexError):
=======
        except (TypeError, IndexError):
            cleansed = value
>>>>>>> REPLACE
```

This will ensure that the `cleansed` variable is always assigned a value, preventing the `UnboundLocalError`.

> Applied edit to django/views/debug.py  
> summarizer unexpectedly failed for gpt-3.5-turbo  
