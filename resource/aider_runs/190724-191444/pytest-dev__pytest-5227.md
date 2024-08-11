
# aider chat started at 2024-07-19 14:54:00

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpwhljwvq2/.git with 434 files  
> Repo-map: using 2048 tokens  

#### Improve default logging format  
#### Currently it is:  
####   
#### > DEFAULT_LOG_FORMAT = "%(filename)-25s %(lineno)4d %(levelname)-8s %(message)s"  
####   
#### I think `name` (module name) would be very useful here, instead of just the base filename.  
####   
#### (It might also be good to have the relative path there (maybe at the end), but it is usually still very long (but e.g. `$VIRTUAL_ENV` could be substituted therein))  
####   
#### Currently it would look like this:  
#### ```  
#### utils.py                   114 DEBUG    (0.000) SELECT "app_url"."id", "app_url"."created", "app_url"."url" FROM "app_url" WHERE "app_url"."id" = 2; args=(2,)  
#### multipart.py               604 DEBUG    Calling on_field_start with no data  
#### ```  
####   
####   
#### Using `DEFAULT_LOG_FORMAT = "%(levelname)-8s %(name)s:%(filename)s:%(lineno)d %(message)s"` instead:  
####   
#### ```  
#### DEBUG    django.db.backends:utils.py:114 (0.000) SELECT "app_url"."id", "app_url"."created", "app_url"."url" FROM "app_url" WHERE "app_url"."id" = 2; args=(2,)  
#### DEBUG    multipart.multipart:multipart.py:604 Calling on_field_start with no data  
#### ```  
> 33379 prompt tokens, 40 completion tokens, $0.167495 cost  

To improve the default logging format, the most likely file to need changes is:

- `src/_pytest/logging.py`

Please add this file to the chat so I can proceed with the changes.

> src/_pytest/logging.py  
> Add these files to the chat? yes  
> 8644 prompt tokens, 83 completion tokens, $0.044465 cost  

Here is the change to improve the default logging format:

src/_pytest/logging.py
```python
<<<<<<< SEARCH
DEFAULT_LOG_FORMAT = "%(filename)-25s %(lineno)4d %(levelname)-8s %(message)s"
=======
DEFAULT_LOG_FORMAT = "%(levelname)-8s %(name)s:%(filename)s:%(lineno)d %(message)s"
>>>>>>> REPLACE
```

> Applied edit to src/_pytest/logging.py  
>   
> Test Script: conda run -n pytest-dev__pytest__4.4  pytest -rA testing/logging/test_reporting.py;  
> [pytest-dev__pytest__4.4] [pytest-dev__pytest-5227] Command: conda run -n pytest-dev__pytest__4.4 pytest -rA testing/logging/test_reporting.py   
> [pytest-dev__pytest__4.4] [pytest-dev__pytest-5227] Subprocess args: {"cwd": "/home/swe-bench/pytest-dev__pytest", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [pytest-dev__pytest__4.4] [pytest-dev__pytest-5227] Std. Output:  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /home/swe-bench/pytest-dev__pytest, inifile: tox.ini  
> collected 34 items  
>   
> testing/logging/test_reporting.py ..........F.F...FFF...............     [100%]  
>   
> =================================== FAILURES ===================================  
> _____________________ test_log_cli_enabled_disabled[True] ______________________  
>   
> testdir = <Testdir local('/tmp/pytest-of-swe-bench/pytest-0/test_log_cli_enabled_disabled0')>  
> enabled = True  
>   
>     @pytest.mark.parametrize("enabled", [True, False])  
>     def test_log_cli_enabled_disabled(testdir, enabled):  
>         msg = "critical message logged by test"  
>         testdir.makepyfile(  
>             """  
>             import logging  
>             def test_log_cli():  
>                 logging.critical("{}")  
>         """.format(  
>                 msg  
>             )  
>         )  
>         if enabled:  
>             testdir.makeini(  
>                 """  
>                 [pytest]  
>                 log_cli=true  
>             """  
>             )  
>         result = testdir.runpytest()  
>         if enabled:  
> >           result.stdout.fnmatch_lines(  
>                 [  
>                     "test_log_cli_enabled_disabled.py::test_log_cli ",  
>                     "*-- live log call --*",  
>                     "test_log_cli_enabled_disabled.py* CRITICAL critical message logged by test",  
>                     "PASSED*",  
>                 ]  
>             )  
> E           Failed: nomatch: 'test_log_cli_enabled_disabled.py::test_log_cli '  
> E               and: '============================= test session starts =============================='  
> E               and: 'platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python'  
> E               and: 'cachedir: .pytest_cache'  
> E               and: 'rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_enabled_disabled0, inifile: tox.ini'  
> E               and: 'collecting ... collected 1 item'  
> E               and: ''  
> E           exact match: 'test_log_cli_enabled_disabled.py::test_log_cli '  
> E           fnmatch: '*-- live log call --*'  
> E              with: '-------------------------------- live log call ---------------------------------'  
> E           nomatch: 'test_log_cli_enabled_disabled.py* CRITICAL critical message logged by test'  
> E               and: 'CRITICAL root:test_log_cli_enabled_disabled.py:3 critical message logged by test'  
> E               and: 'PASSED                                                                   [100%]'  
> E               and: ''  
> E               and: '=========================== 1 passed in 0.01 seconds ==========================='  
> E               and: ''  
> E           remains unmatched: 'test_log_cli_enabled_disabled.py* CRITICAL critical message logged by test'  
>   
> /home/swe-bench/pytest-dev__pytest/testing/logging/test_reporting.py:247: Failed  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_enabled_disabled0, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> test_log_cli_enabled_disabled.py::test_log_cli   
> -------------------------------- live log call ---------------------------------  
> CRITICAL root:test_log_cli_enabled_disabled.py:3 critical message logged by test  
> PASSED                                                                   [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> CRITICAL root:test_log_cli_enabled_disabled.py:3 critical message logged by test  
> __________________________ test_log_cli_default_level __________________________  
>   
> testdir = <Testdir local('/tmp/pytest-of-swe-bench/pytest-0/test_log_cli_default_level0')>  
>   
>     def test_log_cli_default_level(testdir):  
>         # Default log file level  
>         testdir.makepyfile(  
>             """  
>             import pytest  
>             import logging  
>             def test_log_cli(request):  
>                 plugin = request.config.pluginmanager.getplugin('logging-plugin')  
>                 assert plugin.log_cli_handler.level == logging.NOTSET  
>                 logging.getLogger('catchlog').info("INFO message won't be shown")  
>                 logging.getLogger('catchlog').warning("WARNING message will be shown")  
>         """  
>         )  
>         testdir.makeini(  
>             """  
>             [pytest]  
>             log_cli=true  
>         """  
>         )  
>       
>         result = testdir.runpytest()  
>       
>         # fnmatch_lines does an assertion internally  
> >       result.stdout.fnmatch_lines(  
>             [  
>                 "test_log_cli_default_level.py::test_log_cli ",  
>                 "test_log_cli_default_level.py*WARNING message will be shown*",  
>             ]  
>         )  
> E       Failed: nomatch: 'test_log_cli_default_level.py::test_log_cli '  
> E           and: '============================= test session starts =============================='  
> E           and: 'platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python'  
> E           and: 'cachedir: .pytest_cache'  
> E           and: 'rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_default_level0, inifile: tox.ini'  
> E           and: 'collecting ... collected 1 item'  
> E           and: ''  
> E       exact match: 'test_log_cli_default_level.py::test_log_cli '  
> E       nomatch: 'test_log_cli_default_level.py*WARNING message will be shown*'  
> E           and: '-------------------------------- live log call ---------------------------------'  
> E           and: 'WARNING  catchlog:test_log_cli_default_level.py:7 WARNING message will be shown'  
> E           and: 'PASSED                                                                   [100%]'  
> E           and: ''  
> E           and: '=========================== 1 passed in 0.01 seconds ==========================='  
> E           and: ''  
> E       remains unmatched: 'test_log_cli_default_level.py*WARNING message will be shown*'  
>   
> /home/swe-bench/pytest-dev__pytest/testing/logging/test_reporting.py:282: Failed  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_default_level0, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> test_log_cli_default_level.py::test_log_cli   
> -------------------------------- live log call ---------------------------------  
> WARNING  catchlog:test_log_cli_default_level.py:7 WARNING message will be shown  
> PASSED                                                                   [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  catchlog:test_log_cli_default_level.py:7 WARNING message will be shown  
> _______________ test_sections_single_new_line_after_test_outcome _______________  
>   
> testdir = <Testdir local('/tmp/pytest-of-swe-bench/pytest-0/test_sections_single_new_line_after_test_outcome0')>  
> request = <FixtureRequest for <Function test_sections_single_new_line_after_test_outcome>>  
>   
>     def test_sections_single_new_line_after_test_outcome(testdir, request):  
>         """Check that only a single new line is written between log messages during  
>         teardown/finish."""  
>         filename = request.node.name + ".py"  
>         testdir.makeconftest(  
>             """  
>             import pytest  
>             import logging  
>       
>             def pytest_runtest_logstart():  
>                 logging.warning('>>>>> START >>>>>')  
>       
>             def pytest_runtest_logfinish():  
>                 logging.warning('<<<<< END <<<<<<<')  
>                 logging.warning('<<<<< END <<<<<<<')  
>         """  
>         )  
>       
>         testdir.makepyfile(  
>             """  
>             import pytest  
>             import logging  
>       
>             @pytest.fixture  
>             def fix(request):  
>                 logging.warning("log message from setup of {}".format(request.node.name))  
>                 yield  
>                 logging.warning("log message from teardown of {}".format(request.node.name))  
>                 logging.warning("log message from teardown of {}".format(request.node.name))  
>       
>             def test_log_1(fix):  
>                 logging.warning("log message from test_log_1")  
>         """  
>         )  
>         testdir.makeini(  
>             """  
>             [pytest]  
>             log_cli=true  
>         """  
>         )  
>       
>         result = testdir.runpytest()  
>         result.stdout.fnmatch_lines(  
>             [  
>                 "{}::test_log_1 ".format(filename),  
>                 "*-- live log start --*",  
>                 "*WARNING* >>>>> START >>>>>*",  
>                 "*-- live log setup --*",  
>                 "*WARNING*log message from setup of test_log_1*",  
>                 "*-- live log call --*",  
>                 "*WARNING*log message from test_log_1*",  
>                 "PASSED *100%*",  
>                 "*-- live log teardown --*",  
>                 "*WARNING*log message from teardown of test_log_1*",  
>                 "*-- live log finish --*",  
>                 "*WARNING* <<<<< END <<<<<<<*",  
>                 "*WARNING* <<<<< END <<<<<<<*",  
>                 "=* 1 passed in *=",  
>             ]  
>         )  
> >       assert (  
>             re.search(  
>                 r"(.+)live log teardown(.+)\n(.+)WARNING(.+)\n(.+)WARNING(.+)",  
>                 result.stdout.str(),  
>                 re.MULTILINE,  
>             )  
>             is not None  
>         )  
> E       AssertionError: assert None is not None  
> E        +  where None = <function search at 0x7f8a7c034af0>('(.+)live log teardown(.+)\\n(.+)WARNING(.+)\\n(.+)WARNING(.+)', '============================= test session starts ==============================\nplatform linux -- Python 3.9.19, py...onftest.py:9 <<<<< END <<<<<<<\n\n\n=========================== 1 passed in 0.01 seconds ===========================\n', re.MULTILINE)  
> E        +    where <function search at 0x7f8a7c034af0> = re.search  
> E        +    and   '============================= test session starts ==============================\nplatform linux -- Python 3.9.19, py...onftest.py:9 <<<<< END <<<<<<<\n\n\n=========================== 1 passed in 0.01 seconds ===========================\n' = <bound method LineMatcher.str of <_pytest.pytester.LineMatcher object at 0x7f8a7ad2ba60>>()  
> E        +      where <bound method LineMatcher.str of <_pytest.pytester.LineMatcher object at 0x7f8a7ad2ba60>> = <_pytest.pytester.LineMatcher object at 0x7f8a7ad2ba60>.str  
> E        +        where <_pytest.pytester.LineMatcher object at 0x7f8a7ad2ba60> = <RunResult ret=0 len(stdout.lines)=24 len(stderr.lines)=1 duration=0.03s>.stdout  
> E        +    and   re.MULTILINE = re.MULTILINE  
>   
> /home/swe-bench/pytest-dev__pytest/testing/logging/test_reporting.py:524: AssertionError  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_sections_single_new_line_after_test_outcome0, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> test_sections_single_new_line_after_test_outcome.py::test_log_1   
> -------------------------------- live log start --------------------------------  
> WARNING  root:conftest.py:5 >>>>> START >>>>>  
> -------------------------------- live log setup --------------------------------  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:6 log message from setup of test_log_1  
> -------------------------------- live log call ---------------------------------  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:12 log message from test_log_1  
> PASSED                                                                   [100%]  
> ------------------------------ live log teardown -------------------------------  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:8 log message from teardown of test_log_1  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:9 log message from teardown of test_log_1  
> ------------------------------- live log finish --------------------------------  
> WARNING  root:conftest.py:8 <<<<< END <<<<<<<  
> WARNING  root:conftest.py:9 <<<<< END <<<<<<<  
>   
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  root:conftest.py:5 >>>>> START >>>>>  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:6 log message from setup of test_log_1  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:12 log message from test_log_1  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:8 log message from teardown of test_log_1  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:9 log message from teardown of test_log_1  
> WARNING  root:conftest.py:8 <<<<< END <<<<<<<  
> WARNING  root:conftest.py:9 <<<<< END <<<<<<<  
> ______________________________ test_log_cli_level ______________________________  
>   
> testdir = <Testdir local('/tmp/pytest-of-swe-bench/pytest-0/test_log_cli_level0')>  
>   
>     def test_log_cli_level(testdir):  
>         # Default log file level  
>         testdir.makepyfile(  
>             """  
>             import pytest  
>             import logging  
>             def test_log_cli(request):  
>                 plugin = request.config.pluginmanager.getplugin('logging-plugin')  
>                 assert plugin.log_cli_handler.level == logging.INFO  
>                 logging.getLogger('catchlog').debug("This log message won't be shown")  
>                 logging.getLogger('catchlog').info("This log message will be shown")  
>                 print('PASSED')  
>         """  
>         )  
>         testdir.makeini(  
>             """  
>             [pytest]  
>             log_cli=true  
>         """  
>         )  
>       
>         result = testdir.runpytest("-s", "--log-cli-level=INFO")  
>       
>         # fnmatch_lines does an assertion internally  
> >       result.stdout.fnmatch_lines(  
>             [  
>                 "test_log_cli_level.py*This log message will be shown",  
>                 "PASSED",  # 'PASSED' on its own line because the log message prints a new line  
>             ]  
>         )  
> E       Failed: nomatch: 'test_log_cli_level.py*This log message will be shown'  
> E           and: '============================= test session starts =============================='  
> E           and: 'platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python'  
> E           and: 'cachedir: .pytest_cache'  
> E           and: 'rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_level0, inifile: tox.ini'  
> E           and: 'collecting ... collected 1 item'  
> E           and: ''  
> E           and: 'test_log_cli_level.py::test_log_cli '  
> E           and: '-------------------------------- live log call ---------------------------------'  
> E           and: 'INFO     catchlog:test_log_cli_level.py:7 This log message will be shown'  
> E           and: 'PASSED'  
> E           and: 'PASSED'  
> E           and: ''  
> E           and: '=========================== 1 passed in 0.01 seconds ==========================='  
> E           and: ''  
> E       remains unmatched: 'test_log_cli_level.py*This log message will be shown'  
>   
> /home/swe-bench/pytest-dev__pytest/testing/logging/test_reporting.py:566: Failed  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_level0, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> test_log_cli_level.py::test_log_cli   
> -------------------------------- live log call ---------------------------------  
> INFO     catchlog:test_log_cli_level.py:7 This log message will be shown  
> PASSED  
> PASSED  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     catchlog:test_log_cli_level.py:7 This log message will be shown  
> ____________________________ test_log_cli_ini_level ____________________________  
>   
> testdir = <Testdir local('/tmp/pytest-of-swe-bench/pytest-0/test_log_cli_ini_level0')>  
>   
>     def test_log_cli_ini_level(testdir):  
>         testdir.makeini(  
>             """  
>             [pytest]  
>             log_cli=true  
>             log_cli_level = INFO  
>             """  
>         )  
>         testdir.makepyfile(  
>             """  
>             import pytest  
>             import logging  
>             def test_log_cli(request):  
>                 plugin = request.config.pluginmanager.getplugin('logging-plugin')  
>                 assert plugin.log_cli_handler.level == logging.INFO  
>                 logging.getLogger('catchlog').debug("This log message won't be shown")  
>                 logging.getLogger('catchlog').info("This log message will be shown")  
>                 print('PASSED')  
>         """  
>         )  
>       
>         result = testdir.runpytest("-s")  
>       
>         # fnmatch_lines does an assertion internally  
> >       result.stdout.fnmatch_lines(  
>             [  
>                 "test_log_cli_ini_level.py* This log message will be shown",  
>                 "PASSED",  # 'PASSED' on its own line because the log message prints a new line  
>             ]  
>         )  
> E       Failed: nomatch: 'test_log_cli_ini_level.py* This log message will be shown'  
> E           and: '============================= test session starts =============================='  
> E           and: 'platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python'  
> E           and: 'cachedir: .pytest_cache'  
> E           and: 'rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_ini_level0, inifile: tox.ini'  
> E           and: 'collecting ... collected 1 item'  
> E           and: ''  
> E           and: 'test_log_cli_ini_level.py::test_log_cli '  
> E           and: '-------------------------------- live log call ---------------------------------'  
> E           and: 'INFO     catchlog:test_log_cli_ini_level.py:7 This log message will be shown'  
> E           and: 'PASSED'  
> E           and: 'PASSED'  
> E           and: ''  
> E           and: '=========================== 1 passed in 0.01 seconds ==========================='  
> E           and: ''  
> E       remains unmatched: 'test_log_cli_ini_level.py* This log message will be shown'  
>   
> /home/swe-bench/pytest-dev__pytest/testing/logging/test_reporting.py:616: Failed  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_ini_level0, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> test_log_cli_ini_level.py::test_log_cli   
> -------------------------------- live log call ---------------------------------  
> INFO     catchlog:test_log_cli_ini_level.py:7 This log message will be shown  
> PASSED  
> PASSED  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     catchlog:test_log_cli_ini_level.py:7 This log message will be shown  
> ==================================== PASSES ====================================  
> ___________________ test_live_logging_suspends_capture[True] ___________________  
> ------------------------------ Captured log call -------------------------------  
> CRITICAL test_reporting.test_live_logging_suspends_capture:test_reporting.py:905 some message  
> __________________ test_live_logging_suspends_capture[False] ___________________  
> ------------------------------ Captured log call -------------------------------  
> CRITICAL test_reporting.test_live_logging_suspends_capture:test_reporting.py:905 some message  
> _____________________________ test_nothing_logged ______________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_nothing_logged0  
> collected 1 item  
>   
> test_nothing_logged.py F                                                 [100%]  
>   
> =================================== FAILURES ===================================  
> ___________________________________ test_foo ___________________________________  
>   
>     def test_foo():  
>         sys.stdout.write('text going to stdout')  
>         sys.stderr.write('text going to stderr')  
> >       assert False  
> E       assert False  
>   
> test_nothing_logged.py:6: AssertionError  
> ----------------------------- Captured stdout call -----------------------------  
> text going to stdout  
> ----------------------------- Captured stderr call -----------------------------  
> text going to stderr  
> =========================== 1 failed in 0.02 seconds ===========================  
> _____________________________ test_messages_logged _____________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_messages_logged0  
> collected 1 item  
>   
> test_messages_logged.py F                                                [100%]  
>   
> =================================== FAILURES ===================================  
> ___________________________________ test_foo ___________________________________  
>   
>     def test_foo():  
>         sys.stdout.write('text going to stdout')  
>         sys.stderr.write('text going to stderr')  
>         logger.info('text going to logger')  
> >       assert False  
> E       assert False  
>   
> test_messages_logged.py:10: AssertionError  
> ----------------------------- Captured stdout call -----------------------------  
> text going to stdout  
> ----------------------------- Captured stderr call -----------------------------  
> text going to stderr  
> ------------------------------ Captured log call -------------------------------  
> INFO     test_messages_logged:test_messages_logged.py:9 text going to logger  
> =========================== 1 failed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     test_messages_logged:test_messages_logged.py:9 text going to logger  
> __________________________ test_root_logger_affected ___________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_root_logger_affected0  
> collected 1 item  
>   
> test_root_logger_affected.py F                                           [100%]  
>   
> =================================== FAILURES ===================================  
> ___________________________________ test_foo ___________________________________  
>   
>     def test_foo():  
>         logger.info('info text ' + 'going to logger')  
>         logger.warning('warning text ' + 'going to logger')  
>         logger.error('error text ' + 'going to logger')  
>       
> >       assert 0  
> E       assert 0  
>   
> test_root_logger_affected.py:9: AssertionError  
> ------------------------------ Captured log call -------------------------------  
> ERROR    root:test_root_logger_affected.py:7 error text going to logger  
> =========================== 1 failed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  root:test_root_logger_affected.py:6 warning text going to logger  
> ERROR    root:test_root_logger_affected.py:7 error text going to logger  
> ___________________ test_log_cli_level_log_level_interaction ___________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_level_log_level_interaction0  
> collecting ... collected 1 item  
>   
> test_log_cli_level_log_level_interaction.py::test_foo   
> -------------------------------- live log call ---------------------------------  
> INFO     root:test_log_cli_level_log_level_interaction.py:6 info text going to logger  
> WARNING  root:test_log_cli_level_log_level_interaction.py:7 warning text going to logger  
> ERROR    root:test_log_cli_level_log_level_interaction.py:8 error text going to logger  
> FAILED                                                                   [100%]  
>   
> =================================== FAILURES ===================================  
> ___________________________________ test_foo ___________________________________  
>   
>     def test_foo():  
>         logger.debug('debug text ' + 'going to logger')  
>         logger.info('info text ' + 'going to logger')  
>         logger.warning('warning text ' + 'going to logger')  
>         logger.error('error text ' + 'going to logger')  
> >       assert 0  
> E       assert 0  
>   
> test_log_cli_level_log_level_interaction.py:9: AssertionError  
> ------------------------------ Captured log call -------------------------------  
> ERROR    root:test_log_cli_level_log_level_interaction.py:8 error text going to logger  
> =========================== 1 failed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     root:test_log_cli_level_log_level_interaction.py:6 info text going to logger  
> WARNING  root:test_log_cli_level_log_level_interaction.py:7 warning text going to logger  
> ERROR    root:test_log_cli_level_log_level_interaction.py:8 error text going to logger  
> ______________________________ test_setup_logging ______________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_setup_logging0  
> collected 1 item  
>   
> test_setup_logging.py F                                                  [100%]  
>   
> =================================== FAILURES ===================================  
> ___________________________________ test_foo ___________________________________  
>   
>     def test_foo():  
>         logger.info('text going to logger from call')  
> >       assert False  
> E       assert False  
>   
> test_setup_logging.py:10: AssertionError  
> ------------------------------ Captured log setup ------------------------------  
> INFO     test_setup_logging:test_setup_logging.py:6 text going to logger from setup  
> ------------------------------ Captured log call -------------------------------  
> INFO     test_setup_logging:test_setup_logging.py:9 text going to logger from call  
> =========================== 1 failed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     test_setup_logging:test_setup_logging.py:6 text going to logger from setup  
> INFO     test_setup_logging:test_setup_logging.py:9 text going to logger from call  
> ____________________________ test_teardown_logging _____________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_teardown_logging0  
> collected 1 item  
>   
> test_teardown_logging.py .E                                              [100%]  
>   
> ==================================== ERRORS ====================================  
> ________________________ ERROR at teardown of test_foo _________________________  
>   
> function = <function test_foo at 0x7f8a7afe9670>  
>   
>     def teardown_function(function):  
>         logger.info('text going to logger from teardown')  
> >       assert False  
> E       assert False  
>   
> test_teardown_logging.py:10: AssertionError  
> ------------------------------ Captured log call -------------------------------  
> INFO     test_teardown_logging:test_teardown_logging.py:6 text going to logger from call  
> ---------------------------- Captured log teardown -----------------------------  
> INFO     test_teardown_logging:test_teardown_logging.py:9 text going to logger from teardown  
> ====================== 1 passed, 1 error in 0.01 seconds =======================  
> ------------------------------ Captured log call -------------------------------  
> INFO     test_teardown_logging:test_teardown_logging.py:6 text going to logger from call  
> INFO     test_teardown_logging:test_teardown_logging.py:9 text going to logger from teardown  
> __________________________ test_disable_log_capturing __________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_disable_log_capturing0  
> collected 1 item  
>   
> test_disable_log_capturing.py F                                          [100%]  
>   
> =================================== FAILURES ===================================  
> ___________________________________ test_foo ___________________________________  
>   
>     def test_foo():  
>         sys.stdout.write('text going to stdout')  
>         logger.warning('catch me if you can!')  
>         sys.stderr.write('text going to stderr')  
> >       assert False  
> E       assert False  
>   
> test_disable_log_capturing.py:10: AssertionError  
> ----------------------------- Captured stdout call -----------------------------  
> text going to stdout  
> ----------------------------- Captured stderr call -----------------------------  
> text going to stderr  
> =========================== 1 failed in 0.01 seconds ===========================  
> <_pytest.pytester.LineMatcher object at 0x7f8a7af477c0>  
> ------------------------------ Captured log call -------------------------------  
> WARNING  test_disable_log_capturing:test_disable_log_capturing.py:8 catch me if you can!  
> ________________________ test_disable_log_capturing_ini ________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_disable_log_capturing_ini0, inifile: tox.ini  
> collected 1 item  
>   
> test_disable_log_capturing_ini.py F                                      [100%]  
>   
> =================================== FAILURES ===================================  
> ___________________________________ test_foo ___________________________________  
>   
>     def test_foo():  
>         sys.stdout.write('text going to stdout')  
>         logger.warning('catch me if you can!')  
>         sys.stderr.write('text going to stderr')  
> >       assert False  
> E       assert False  
>   
> test_disable_log_capturing_ini.py:10: AssertionError  
> ----------------------------- Captured stdout call -----------------------------  
> text going to stdout  
> ----------------------------- Captured stderr call -----------------------------  
> text going to stderr  
> =========================== 1 failed in 0.01 seconds ===========================  
> <_pytest.pytester.LineMatcher object at 0x7f8a7af71310>  
> ------------------------------ Captured log call -------------------------------  
> WARNING  test_disable_log_capturing_ini:test_disable_log_capturing_ini.py:8 catch me if you can!  
> _____________________ test_log_cli_enabled_disabled[False] _____________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_enabled_disabled1  
> collected 1 item  
>   
> test_log_cli_enabled_disabled.py .                                       [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> CRITICAL root:test_log_cli_enabled_disabled.py:3 critical message logged by test  
> __________________ test_log_cli_default_level_multiple_tests ___________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_default_level_multiple_tests0, inifile: tox.ini  
> collecting ... collected 2 items  
>   
> test_log_cli_default_level_multiple_tests.py::test_log_1   
> -------------------------------- live log call ---------------------------------  
> WARNING  root:test_log_cli_default_level_multiple_tests.py:4 log message from test_log_1  
> PASSED                                                                   [ 50%]  
> test_log_cli_default_level_multiple_tests.py::test_log_2   
> -------------------------------- live log call ---------------------------------  
> WARNING  root:test_log_cli_default_level_multiple_tests.py:7 log message from test_log_2  
> PASSED                                                                   [100%]  
>   
> =========================== 2 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  root:test_log_cli_default_level_multiple_tests.py:4 log message from test_log_1  
> WARNING  root:test_log_cli_default_level_multiple_tests.py:7 log message from test_log_2  
> _____________________ test_log_cli_default_level_sections ______________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_default_level_sections0, inifile: tox.ini  
> collecting ... collected 2 items  
>   
> test_log_cli_default_level_sections.py::test_log_1   
> -------------------------------- live log start --------------------------------  
> WARNING  root:conftest.py:5 >>>>> START >>>>>  
> -------------------------------- live log setup --------------------------------  
> WARNING  root:test_log_cli_default_level_sections.py:6 log message from setup of test_log_1  
> -------------------------------- live log call ---------------------------------  
> WARNING  root:test_log_cli_default_level_sections.py:11 log message from test_log_1  
> PASSED                                                                   [ 50%]  
> ------------------------------ live log teardown -------------------------------  
> WARNING  root:test_log_cli_default_level_sections.py:8 log message from teardown of test_log_1  
> ------------------------------- live log finish --------------------------------  
> WARNING  root:conftest.py:8 <<<<< END <<<<<<<  
>   
> test_log_cli_default_level_sections.py::test_log_2   
> -------------------------------- live log start --------------------------------  
> WARNING  root:conftest.py:5 >>>>> START >>>>>  
> -------------------------------- live log setup --------------------------------  
> WARNING  root:test_log_cli_default_level_sections.py:6 log message from setup of test_log_2  
> -------------------------------- live log call ---------------------------------  
> WARNING  root:test_log_cli_default_level_sections.py:14 log message from test_log_2  
> PASSED                                                                   [100%]  
> ------------------------------ live log teardown -------------------------------  
> WARNING  root:test_log_cli_default_level_sections.py:8 log message from teardown of test_log_2  
> ------------------------------- live log finish --------------------------------  
> WARNING  root:conftest.py:8 <<<<< END <<<<<<<  
>   
>   
> =========================== 2 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  root:conftest.py:5 >>>>> START >>>>>  
> WARNING  root:test_log_cli_default_level_sections.py:6 log message from setup of test_log_1  
> WARNING  root:test_log_cli_default_level_sections.py:11 log message from test_log_1  
> WARNING  root:test_log_cli_default_level_sections.py:8 log message from teardown of test_log_1  
> WARNING  root:conftest.py:8 <<<<< END <<<<<<<  
> WARNING  root:conftest.py:5 >>>>> START >>>>>  
> WARNING  root:test_log_cli_default_level_sections.py:6 log message from setup of test_log_2  
> WARNING  root:test_log_cli_default_level_sections.py:14 log message from test_log_2  
> WARNING  root:test_log_cli_default_level_sections.py:8 log message from teardown of test_log_2  
> WARNING  root:conftest.py:8 <<<<< END <<<<<<<  
> _______________________ test_live_logs_unknown_sections ________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_live_logs_unknown_sections0, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> ----------------------------- live log collection ------------------------------  
> WARNING  root:conftest.py:5 Unknown Section!  
>   
> test_live_logs_unknown_sections.py::test_log_1   
> -------------------------------- live log start --------------------------------  
> WARNING  root:conftest.py:8 >>>>> START >>>>>  
> -------------------------------- live log setup --------------------------------  
> WARNING  root:test_live_logs_unknown_sections.py:6 log message from setup of test_log_1  
> -------------------------------- live log call ---------------------------------  
> WARNING  root:test_live_logs_unknown_sections.py:11 log message from test_log_1  
> PASSED                                                                   [100%]  
> ------------------------------ live log teardown -------------------------------  
> WARNING  root:test_live_logs_unknown_sections.py:8 log message from teardown of test_log_1  
> ------------------------------- live log finish --------------------------------  
> WARNING  root:conftest.py:11 <<<<< END <<<<<<<  
>   
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  root:conftest.py:5 Unknown Section!  
> WARNING  root:conftest.py:8 >>>>> START >>>>>  
> WARNING  root:test_live_logs_unknown_sections.py:6 log message from setup of test_log_1  
> WARNING  root:test_live_logs_unknown_sections.py:11 log message from test_log_1  
> WARNING  root:test_live_logs_unknown_sections.py:8 log message from teardown of test_log_1  
> WARNING  root:conftest.py:11 <<<<< END <<<<<<<  
> __________________________ test_log_cli_auto_enable[] __________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_auto_enable0, inifile: tox.ini  
> collected 1 item  
>   
> test_log_cli_auto_enable.py .                                            [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     root:test_log_cli_auto_enable.py:4 log message from test_log_1 not to be shown  
> WARNING  root:test_log_cli_auto_enable.py:5 log message from test_log_1  
> ________________ test_log_cli_auto_enable[--log-level=WARNING] _________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_auto_enable1, inifile: tox.ini  
> collected 1 item  
>   
> test_log_cli_auto_enable.py .                                            [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  root:test_log_cli_auto_enable.py:5 log message from test_log_1  
> ______________ test_log_cli_auto_enable[--log-file-level=WARNING] ______________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_auto_enable2, inifile: tox.ini  
> collected 1 item  
>   
> test_log_cli_auto_enable.py .                                            [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     root:test_log_cli_auto_enable.py:4 log message from test_log_1 not to be shown  
> WARNING  root:test_log_cli_auto_enable.py:5 log message from test_log_1  
> ______________ test_log_cli_auto_enable[--log-cli-level=WARNING] _______________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_auto_enable3, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> test_log_cli_auto_enable.py::test_log_1   
> -------------------------------- live log call ---------------------------------  
> WARNING  root:test_log_cli_auto_enable.py:5 log message from test_log_1  
> PASSED                                                                   [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     root:test_log_cli_auto_enable.py:4 log message from test_log_1 not to be shown  
> WARNING  root:test_log_cli_auto_enable.py:5 log message from test_log_1  
> ______________________________ test_log_file_cli _______________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_file_cli0  
> collected 1 item  
>   
> test_log_file_cli.py PASSED  
> .  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  catchlog:test_log_file_cli.py:7 This log message will be shown  
> ___________________________ test_log_file_cli_level ____________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_file_cli_level0  
> collected 1 item  
>   
> test_log_file_cli_level.py PASSED  
> .  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     catchlog:test_log_file_cli_level.py:7 This log message will be shown  
> ____________________ test_log_level_not_changed_by_default _____________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_level_not_changed_by_default0  
> collected 1 item  
>   
> test_log_level_not_changed_by_default.py .  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ______________________________ test_log_file_ini _______________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_file_ini0, inifile: tox.ini  
> collected 1 item  
>   
> test_log_file_ini.py PASSED  
> .  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  catchlog:test_log_file_ini.py:7 This log message will be shown  
> ___________________________ test_log_file_ini_level ____________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_file_ini_level0, inifile: tox.ini  
> collected 1 item  
>   
> test_log_file_ini_level.py PASSED  
> .  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     catchlog:test_log_file_ini_level.py:7 This log message will be shown  
> ____________________________ test_log_file_unicode _____________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_file_unicode0, inifile: tox.ini  
> collected 1 item  
>   
> test_log_file_unicode.py .                                               [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     catchlog:test_log_file_unicode.py:6 Normal message  
> INFO     catchlog:test_log_file_unicode.py:7 ├  
> INFO     catchlog:test_log_file_unicode.py:8 Another normal message  
> _________________________ test_collection_live_logging _________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_collection_live_logging0  
> collecting ...   
> ----------------------------- live log collection ------------------------------  
> INFO     root:test_collection_live_logging.py:3 Normal message  
> collected 0 items  
>   
> ========================= no tests ran in 0.01 seconds =========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     root:test_collection_live_logging.py:3 Normal message  
> _______________________ test_collection_logging_to_file ________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_collection_logging_to_file0, inifile: tox.ini  
> collected 1 item  
>   
> test_collection_logging_to_file.py .                                     [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     root:test_collection_logging_to_file.py:3 Normal message  
> INFO     root:test_collection_logging_to_file.py:7 info message in test_simple  
> ______________________________ test_log_in_hooks _______________________________  
> ----------------------------- Captured stdout call -----------------------------  
>   
> ---------------------------- live log sessionstart -----------------------------  
> INFO     root:conftest.py:7 sessionstart  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_in_hooks0, inifile: tox.ini  
> collecting ... collected 0 items  
> ----------------------------- live log collection ------------------------------  
> INFO     root:conftest.py:4 runtestloop  
> ---------------------------- live log sessionfinish ----------------------------  
> INFO     root:conftest.py:10 sessionfinish  
>   
> ========================= no tests ran in 0.00 seconds =========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     root:conftest.py:7 sessionstart  
> INFO     root:conftest.py:4 runtestloop  
> INFO     root:conftest.py:10 sessionfinish  
> ________________________ test_log_in_runtest_logreport _________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_in_runtest_logreport0, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> test_log_in_runtest_logreport.py::test_first   
> ------------------------------ live log logreport ------------------------------  
> INFO     conftest:conftest.py:5 logreport  
> PASSED                                                                   [100%]------------------------------ live log logreport ------------------------------  
> INFO     conftest:conftest.py:5 logreport  
> ------------------------------ live log logreport ------------------------------  
> INFO     conftest:conftest.py:5 logreport  
>   
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     conftest:conftest.py:5 logreport  
> INFO     conftest:conftest.py:5 logreport  
> INFO     conftest:conftest.py:5 logreport  
> ______________________________ test_log_set_path _______________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_set_path0, inifile: tox.ini  
> collecting ... collected 2 items  
>   
> test_log_set_path.py::test_first   
> -------------------------------- live log call ---------------------------------  
> INFO     testcase-logger:test_log_set_path.py:4 message from test 1  
> PASSED                                                                   [ 50%]  
> test_log_set_path.py::test_second   
> -------------------------------- live log call ---------------------------------  
> DEBUG    testcase-logger:test_log_set_path.py:8 message from test 2  
> PASSED                                                                   [100%]  
>   
> =========================== 2 passed in 0.01 seconds ===========================  
> ----------------------------- Captured stderr call -----------------------------  
> Exception ignored in: <_io.FileIO name='/tmp/pytest-of-swe-bench/pytest-0/test_log_set_path0/test_first' mode='wb' closefd=True>  
> Traceback (most recent call last):  
>   File "/home/swe-bench/pytest-dev__pytest/src/_pytest/logging.py", line 479, in set_log_path  
>     self.log_file_handler = logging.FileHandler(  
> ResourceWarning: unclosed file <_io.TextIOWrapper name='/tmp/pytest-of-swe-bench/pytest-0/test_log_set_path0/test_first' mode='w' encoding='UTF-8'>  
> ------------------------------ Captured log call -------------------------------  
> INFO     testcase-logger:test_log_set_path.py:4 message from test 1  
> DEBUG    testcase-logger:test_log_set_path.py:8 message from test 2  
> =========================== short test summary info ============================  
> FAILED testing/logging/test_reporting.py::test_log_cli_enabled_disabled[True]  
> FAILED testing/logging/test_reporting.py::test_log_cli_default_level  
> FAILED testing/logging/test_reporting.py::test_sections_single_new_line_after_test_outcome  
> FAILED testing/logging/test_reporting.py::test_log_cli_level  
> FAILED testing/logging/test_reporting.py::test_log_cli_ini_level  
> PASSED testing/logging/test_reporting.py::test_live_logging_suspends_capture[True]  
> PASSED testing/logging/test_reporting.py::test_live_logging_suspends_capture[False]  
> PASSED testing/logging/test_reporting.py::test_nothing_logged  
> PASSED testing/logging/test_reporting.py::test_messages_logged  
> PASSED testing/logging/test_reporting.py::test_root_logger_affected  
> PASSED testing/logging/test_reporting.py::test_log_cli_level_log_level_interaction  
> PASSED testing/logging/test_reporting.py::test_setup_logging  
> PASSED testing/logging/test_reporting.py::test_teardown_logging  
> PASSED testing/logging/test_reporting.py::test_disable_log_capturing  
> PASSED testing/logging/test_reporting.py::test_disable_log_capturing_ini  
> PASSED testing/logging/test_reporting.py::test_log_cli_enabled_disabled[False]  
> PASSED testing/logging/test_reporting.py::test_log_cli_default_level_multiple_tests  
> PASSED testing/logging/test_reporting.py::test_log_cli_default_level_sections  
> PASSED testing/logging/test_reporting.py::test_live_logs_unknown_sections  
> PASSED testing/logging/test_reporting.py::test_log_cli_auto_enable[]  
> PASSED testing/logging/test_reporting.py::test_log_cli_auto_enable[--log-level=WARNING]  
> PASSED testing/logging/test_reporting.py::test_log_cli_auto_enable[--log-file-level=WARNING]  
> PASSED testing/logging/test_reporting.py::test_log_cli_auto_enable[--log-cli-level=WARNING]  
> PASSED testing/logging/test_reporting.py::test_log_file_cli  
> PASSED testing/logging/test_reporting.py::test_log_file_cli_level  
> PASSED testing/logging/test_reporting.py::test_log_level_not_changed_by_default  
> PASSED testing/logging/test_reporting.py::test_log_file_ini  
> PASSED testing/logging/test_reporting.py::test_log_file_ini_level  
> PASSED testing/logging/test_reporting.py::test_log_file_unicode  
> PASSED testing/logging/test_reporting.py::test_collection_live_logging  
> PASSED testing/logging/test_reporting.py::test_collection_logging_to_file  
> PASSED testing/logging/test_reporting.py::test_log_in_hooks  
> PASSED testing/logging/test_reporting.py::test_log_in_runtest_logreport  
> PASSED testing/logging/test_reporting.py::test_log_set_path  
> ===================== 5 failed, 29 passed in 1.04 seconds ======================  
> ERROR conda.cli.main_run:execute(124): `conda run pytest -rA testing/logging/test_reporting.py` failed. (See above for error)  
>   
>    
> [pytest-dev__pytest__4.4] [pytest-dev__pytest-5227] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [pytest-dev__pytest__4.4] [pytest-dev__pytest-5227] Test script run successful   
> Attempt to fix test errors? yes  
> 21244 prompt tokens, 57 completion tokens, $0.107075 cost  

To fix the test failures, we need to update the expected log format in the test cases to match the new format. The most likely file to need changes is:

- `testing/logging/test_reporting.py`

Please add this file to the chat so I can proceed with the changes.

> testing/logging/test_reporting.py  
> Add these files to the chat? yes  
> 28473 prompt tokens, 385 completion tokens, $0.148140 cost  

Here are the changes to update the expected log format in the test cases to match the new format:

testing/logging/test_reporting.py
```python
<<<<<<< SEARCH
                    "test_log_cli_enabled_disabled.py* CRITICAL critical message logged by test",
=======
                    "CRITICAL root:test_log_cli_enabled_disabled.py:3 critical message logged by test",
>>>>>>> REPLACE
```

testing/logging/test_reporting.py
```python
<<<<<<< SEARCH
                "test_log_cli_default_level.py*WARNING message will be shown*",
=======
                "WARNING  catchlog:test_log_cli_default_level.py:7 WARNING message will be shown",
>>>>>>> REPLACE
```

testing/logging/test_reporting.py
```python
<<<<<<< SEARCH
                "*WARNING*log message from teardown of test_log_1*",
                "*-- live log finish --*",
                "*WARNING* <<<<< END <<<<<<<*",
                "*WARNING* <<<<< END <<<<<<<*",
=======
                "WARNING  root:test_sections_single_new_line_after_test_outcome.py:8 log message from teardown of test_log_1",
                "------------------------------- live log finish --------------------------------",
                "WARNING  root:conftest.py:8 <<<<< END <<<<<<<",
                "WARNING  root:conftest.py:9 <<<<< END <<<<<<<",
>>>>>>> REPLACE
```

testing/logging/test_reporting.py
```python
<<<<<<< SEARCH
                "test_log_cli_level.py*This log message will be shown",
=======
                "INFO     catchlog:test_log_cli_level.py:7 This log message will be shown",
>>>>>>> REPLACE
```

testing/logging/test_reporting.py
```python
<<<<<<< SEARCH
                "test_log_cli_ini_level.py* This log message will be shown",
=======
                "INFO     catchlog:test_log_cli_ini_level.py:7 This log message will be shown",
>>>>>>> REPLACE
```

> Applied edit to testing/logging/test_reporting.py  
>   
> Test Script: conda run -n pytest-dev__pytest__4.4  pytest -rA testing/logging/test_reporting.py;  
> [pytest-dev__pytest__4.4] [pytest-dev__pytest-5227] Command: conda run -n pytest-dev__pytest__4.4 pytest -rA testing/logging/test_reporting.py   
> [pytest-dev__pytest__4.4] [pytest-dev__pytest-5227] Subprocess args: {"cwd": "/home/swe-bench/pytest-dev__pytest", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [pytest-dev__pytest__4.4] [pytest-dev__pytest-5227] Std. Output:  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /home/swe-bench/pytest-dev__pytest, inifile: tox.ini  
> collected 34 items  
>   
> testing/logging/test_reporting.py ..........F.F...FFF...............     [100%]  
>   
> =================================== FAILURES ===================================  
> _____________________ test_log_cli_enabled_disabled[True] ______________________  
>   
> testdir = <Testdir local('/tmp/pytest-of-swe-bench/pytest-0/test_log_cli_enabled_disabled0')>  
> enabled = True  
>   
>     @pytest.mark.parametrize("enabled", [True, False])  
>     def test_log_cli_enabled_disabled(testdir, enabled):  
>         msg = "critical message logged by test"  
>         testdir.makepyfile(  
>             """  
>             import logging  
>             def test_log_cli():  
>                 logging.critical("{}")  
>         """.format(  
>                 msg  
>             )  
>         )  
>         if enabled:  
>             testdir.makeini(  
>                 """  
>                 [pytest]  
>                 log_cli=true  
>             """  
>             )  
>         result = testdir.runpytest()  
>         if enabled:  
> >           result.stdout.fnmatch_lines(  
>                 [  
>                     "test_log_cli_enabled_disabled.py::test_log_cli ",  
>                     "*-- live log call --*",  
>                     "test_log_cli_enabled_disabled.py* CRITICAL critical message logged by test",  
>                     "PASSED*",  
>                 ]  
>             )  
> E           Failed: nomatch: 'test_log_cli_enabled_disabled.py::test_log_cli '  
> E               and: '============================= test session starts =============================='  
> E               and: 'platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python'  
> E               and: 'cachedir: .pytest_cache'  
> E               and: 'rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_enabled_disabled0, inifile: tox.ini'  
> E               and: 'collecting ... collected 1 item'  
> E               and: ''  
> E           exact match: 'test_log_cli_enabled_disabled.py::test_log_cli '  
> E           fnmatch: '*-- live log call --*'  
> E              with: '-------------------------------- live log call ---------------------------------'  
> E           nomatch: 'test_log_cli_enabled_disabled.py* CRITICAL critical message logged by test'  
> E               and: 'CRITICAL root:test_log_cli_enabled_disabled.py:3 critical message logged by test'  
> E               and: 'PASSED                                                                   [100%]'  
> E               and: ''  
> E               and: '=========================== 1 passed in 0.01 seconds ==========================='  
> E               and: ''  
> E           remains unmatched: 'test_log_cli_enabled_disabled.py* CRITICAL critical message logged by test'  
>   
> /home/swe-bench/pytest-dev__pytest/testing/logging/test_reporting.py:247: Failed  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_enabled_disabled0, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> test_log_cli_enabled_disabled.py::test_log_cli   
> -------------------------------- live log call ---------------------------------  
> CRITICAL root:test_log_cli_enabled_disabled.py:3 critical message logged by test  
> PASSED                                                                   [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> CRITICAL root:test_log_cli_enabled_disabled.py:3 critical message logged by test  
> __________________________ test_log_cli_default_level __________________________  
>   
> testdir = <Testdir local('/tmp/pytest-of-swe-bench/pytest-0/test_log_cli_default_level0')>  
>   
>     def test_log_cli_default_level(testdir):  
>         # Default log file level  
>         testdir.makepyfile(  
>             """  
>             import pytest  
>             import logging  
>             def test_log_cli(request):  
>                 plugin = request.config.pluginmanager.getplugin('logging-plugin')  
>                 assert plugin.log_cli_handler.level == logging.NOTSET  
>                 logging.getLogger('catchlog').info("INFO message won't be shown")  
>                 logging.getLogger('catchlog').warning("WARNING message will be shown")  
>         """  
>         )  
>         testdir.makeini(  
>             """  
>             [pytest]  
>             log_cli=true  
>         """  
>         )  
>       
>         result = testdir.runpytest()  
>       
>         # fnmatch_lines does an assertion internally  
> >       result.stdout.fnmatch_lines(  
>             [  
>                 "test_log_cli_default_level.py::test_log_cli ",  
>                 "test_log_cli_default_level.py*WARNING message will be shown*",  
>             ]  
>         )  
> E       Failed: nomatch: 'test_log_cli_default_level.py::test_log_cli '  
> E           and: '============================= test session starts =============================='  
> E           and: 'platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python'  
> E           and: 'cachedir: .pytest_cache'  
> E           and: 'rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_default_level0, inifile: tox.ini'  
> E           and: 'collecting ... collected 1 item'  
> E           and: ''  
> E       exact match: 'test_log_cli_default_level.py::test_log_cli '  
> E       nomatch: 'test_log_cli_default_level.py*WARNING message will be shown*'  
> E           and: '-------------------------------- live log call ---------------------------------'  
> E           and: 'WARNING  catchlog:test_log_cli_default_level.py:7 WARNING message will be shown'  
> E           and: 'PASSED                                                                   [100%]'  
> E           and: ''  
> E           and: '=========================== 1 passed in 0.01 seconds ==========================='  
> E           and: ''  
> E       remains unmatched: 'test_log_cli_default_level.py*WARNING message will be shown*'  
>   
> /home/swe-bench/pytest-dev__pytest/testing/logging/test_reporting.py:282: Failed  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_default_level0, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> test_log_cli_default_level.py::test_log_cli   
> -------------------------------- live log call ---------------------------------  
> WARNING  catchlog:test_log_cli_default_level.py:7 WARNING message will be shown  
> PASSED                                                                   [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  catchlog:test_log_cli_default_level.py:7 WARNING message will be shown  
> _______________ test_sections_single_new_line_after_test_outcome _______________  
>   
> testdir = <Testdir local('/tmp/pytest-of-swe-bench/pytest-0/test_sections_single_new_line_after_test_outcome0')>  
> request = <FixtureRequest for <Function test_sections_single_new_line_after_test_outcome>>  
>   
>     def test_sections_single_new_line_after_test_outcome(testdir, request):  
>         """Check that only a single new line is written between log messages during  
>         teardown/finish."""  
>         filename = request.node.name + ".py"  
>         testdir.makeconftest(  
>             """  
>             import pytest  
>             import logging  
>       
>             def pytest_runtest_logstart():  
>                 logging.warning('>>>>> START >>>>>')  
>       
>             def pytest_runtest_logfinish():  
>                 logging.warning('<<<<< END <<<<<<<')  
>                 logging.warning('<<<<< END <<<<<<<')  
>         """  
>         )  
>       
>         testdir.makepyfile(  
>             """  
>             import pytest  
>             import logging  
>       
>             @pytest.fixture  
>             def fix(request):  
>                 logging.warning("log message from setup of {}".format(request.node.name))  
>                 yield  
>                 logging.warning("log message from teardown of {}".format(request.node.name))  
>                 logging.warning("log message from teardown of {}".format(request.node.name))  
>       
>             def test_log_1(fix):  
>                 logging.warning("log message from test_log_1")  
>         """  
>         )  
>         testdir.makeini(  
>             """  
>             [pytest]  
>             log_cli=true  
>         """  
>         )  
>       
>         result = testdir.runpytest()  
>         result.stdout.fnmatch_lines(  
>             [  
>                 "{}::test_log_1 ".format(filename),  
>                 "*-- live log start --*",  
>                 "*WARNING* >>>>> START >>>>>*",  
>                 "*-- live log setup --*",  
>                 "*WARNING*log message from setup of test_log_1*",  
>                 "*-- live log call --*",  
>                 "*WARNING*log message from test_log_1*",  
>                 "PASSED *100%*",  
>                 "*-- live log teardown --*",  
>                 "*WARNING*log message from teardown of test_log_1*",  
>                 "*-- live log finish --*",  
>                 "*WARNING* <<<<< END <<<<<<<*",  
>                 "*WARNING* <<<<< END <<<<<<<*",  
>                 "=* 1 passed in *=",  
>             ]  
>         )  
> >       assert (  
>             re.search(  
>                 r"(.+)live log teardown(.+)\n(.+)WARNING(.+)\n(.+)WARNING(.+)",  
>                 result.stdout.str(),  
>                 re.MULTILINE,  
>             )  
>             is not None  
>         )  
> E       AssertionError: assert None is not None  
> E        +  where None = <function search at 0x7fd944e18af0>('(.+)live log teardown(.+)\\n(.+)WARNING(.+)\\n(.+)WARNING(.+)', '============================= test session starts ==============================\nplatform linux -- Python 3.9.19, py...onftest.py:9 <<<<< END <<<<<<<\n\n\n=========================== 1 passed in 0.01 seconds ===========================\n', re.MULTILINE)  
> E        +    where <function search at 0x7fd944e18af0> = re.search  
> E        +    and   '============================= test session starts ==============================\nplatform linux -- Python 3.9.19, py...onftest.py:9 <<<<< END <<<<<<<\n\n\n=========================== 1 passed in 0.01 seconds ===========================\n' = <bound method LineMatcher.str of <_pytest.pytester.LineMatcher object at 0x7fd943c1a520>>()  
> E        +      where <bound method LineMatcher.str of <_pytest.pytester.LineMatcher object at 0x7fd943c1a520>> = <_pytest.pytester.LineMatcher object at 0x7fd943c1a520>.str  
> E        +        where <_pytest.pytester.LineMatcher object at 0x7fd943c1a520> = <RunResult ret=0 len(stdout.lines)=24 len(stderr.lines)=1 duration=0.02s>.stdout  
> E        +    and   re.MULTILINE = re.MULTILINE  
>   
> /home/swe-bench/pytest-dev__pytest/testing/logging/test_reporting.py:524: AssertionError  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_sections_single_new_line_after_test_outcome0, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> test_sections_single_new_line_after_test_outcome.py::test_log_1   
> -------------------------------- live log start --------------------------------  
> WARNING  root:conftest.py:5 >>>>> START >>>>>  
> -------------------------------- live log setup --------------------------------  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:6 log message from setup of test_log_1  
> -------------------------------- live log call ---------------------------------  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:12 log message from test_log_1  
> PASSED                                                                   [100%]  
> ------------------------------ live log teardown -------------------------------  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:8 log message from teardown of test_log_1  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:9 log message from teardown of test_log_1  
> ------------------------------- live log finish --------------------------------  
> WARNING  root:conftest.py:8 <<<<< END <<<<<<<  
> WARNING  root:conftest.py:9 <<<<< END <<<<<<<  
>   
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  root:conftest.py:5 >>>>> START >>>>>  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:6 log message from setup of test_log_1  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:12 log message from test_log_1  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:8 log message from teardown of test_log_1  
> WARNING  root:test_sections_single_new_line_after_test_outcome.py:9 log message from teardown of test_log_1  
> WARNING  root:conftest.py:8 <<<<< END <<<<<<<  
> WARNING  root:conftest.py:9 <<<<< END <<<<<<<  
> ______________________________ test_log_cli_level ______________________________  
>   
> testdir = <Testdir local('/tmp/pytest-of-swe-bench/pytest-0/test_log_cli_level0')>  
>   
>     def test_log_cli_level(testdir):  
>         # Default log file level  
>         testdir.makepyfile(  
>             """  
>             import pytest  
>             import logging  
>             def test_log_cli(request):  
>                 plugin = request.config.pluginmanager.getplugin('logging-plugin')  
>                 assert plugin.log_cli_handler.level == logging.INFO  
>                 logging.getLogger('catchlog').debug("This log message won't be shown")  
>                 logging.getLogger('catchlog').info("This log message will be shown")  
>                 print('PASSED')  
>         """  
>         )  
>         testdir.makeini(  
>             """  
>             [pytest]  
>             log_cli=true  
>         """  
>         )  
>       
>         result = testdir.runpytest("-s", "--log-cli-level=INFO")  
>       
>         # fnmatch_lines does an assertion internally  
> >       result.stdout.fnmatch_lines(  
>             [  
>                 "test_log_cli_level.py*This log message will be shown",  
>                 "PASSED",  # 'PASSED' on its own line because the log message prints a new line  
>             ]  
>         )  
> E       Failed: nomatch: 'test_log_cli_level.py*This log message will be shown'  
> E           and: '============================= test session starts =============================='  
> E           and: 'platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python'  
> E           and: 'cachedir: .pytest_cache'  
> E           and: 'rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_level0, inifile: tox.ini'  
> E           and: 'collecting ... collected 1 item'  
> E           and: ''  
> E           and: 'test_log_cli_level.py::test_log_cli '  
> E           and: '-------------------------------- live log call ---------------------------------'  
> E           and: 'INFO     catchlog:test_log_cli_level.py:7 This log message will be shown'  
> E           and: 'PASSED'  
> E           and: 'PASSED'  
> E           and: ''  
> E           and: '=========================== 1 passed in 0.01 seconds ==========================='  
> E           and: ''  
> E       remains unmatched: 'test_log_cli_level.py*This log message will be shown'  
>   
> /home/swe-bench/pytest-dev__pytest/testing/logging/test_reporting.py:566: Failed  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_level0, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> test_log_cli_level.py::test_log_cli   
> -------------------------------- live log call ---------------------------------  
> INFO     catchlog:test_log_cli_level.py:7 This log message will be shown  
> PASSED  
> PASSED  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     catchlog:test_log_cli_level.py:7 This log message will be shown  
> ____________________________ test_log_cli_ini_level ____________________________  
>   
> testdir = <Testdir local('/tmp/pytest-of-swe-bench/pytest-0/test_log_cli_ini_level0')>  
>   
>     def test_log_cli_ini_level(testdir):  
>         testdir.makeini(  
>             """  
>             [pytest]  
>             log_cli=true  
>             log_cli_level = INFO  
>             """  
>         )  
>         testdir.makepyfile(  
>             """  
>             import pytest  
>             import logging  
>             def test_log_cli(request):  
>                 plugin = request.config.pluginmanager.getplugin('logging-plugin')  
>                 assert plugin.log_cli_handler.level == logging.INFO  
>                 logging.getLogger('catchlog').debug("This log message won't be shown")  
>                 logging.getLogger('catchlog').info("This log message will be shown")  
>                 print('PASSED')  
>         """  
>         )  
>       
>         result = testdir.runpytest("-s")  
>       
>         # fnmatch_lines does an assertion internally  
> >       result.stdout.fnmatch_lines(  
>             [  
>                 "test_log_cli_ini_level.py* This log message will be shown",  
>                 "PASSED",  # 'PASSED' on its own line because the log message prints a new line  
>             ]  
>         )  
> E       Failed: nomatch: 'test_log_cli_ini_level.py* This log message will be shown'  
> E           and: '============================= test session starts =============================='  
> E           and: 'platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python'  
> E           and: 'cachedir: .pytest_cache'  
> E           and: 'rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_ini_level0, inifile: tox.ini'  
> E           and: 'collecting ... collected 1 item'  
> E           and: ''  
> E           and: 'test_log_cli_ini_level.py::test_log_cli '  
> E           and: '-------------------------------- live log call ---------------------------------'  
> E           and: 'INFO     catchlog:test_log_cli_ini_level.py:7 This log message will be shown'  
> E           and: 'PASSED'  
> E           and: 'PASSED'  
> E           and: ''  
> E           and: '=========================== 1 passed in 0.01 seconds ==========================='  
> E           and: ''  
> E       remains unmatched: 'test_log_cli_ini_level.py* This log message will be shown'  
>   
> /home/swe-bench/pytest-dev__pytest/testing/logging/test_reporting.py:616: Failed  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_ini_level0, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> test_log_cli_ini_level.py::test_log_cli   
> -------------------------------- live log call ---------------------------------  
> INFO     catchlog:test_log_cli_ini_level.py:7 This log message will be shown  
> PASSED  
> PASSED  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     catchlog:test_log_cli_ini_level.py:7 This log message will be shown  
> ==================================== PASSES ====================================  
> ___________________ test_live_logging_suspends_capture[True] ___________________  
> ------------------------------ Captured log call -------------------------------  
> CRITICAL test_reporting.test_live_logging_suspends_capture:test_reporting.py:905 some message  
> __________________ test_live_logging_suspends_capture[False] ___________________  
> ------------------------------ Captured log call -------------------------------  
> CRITICAL test_reporting.test_live_logging_suspends_capture:test_reporting.py:905 some message  
> _____________________________ test_nothing_logged ______________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_nothing_logged0  
> collected 1 item  
>   
> test_nothing_logged.py F                                                 [100%]  
>   
> =================================== FAILURES ===================================  
> ___________________________________ test_foo ___________________________________  
>   
>     def test_foo():  
>         sys.stdout.write('text going to stdout')  
>         sys.stderr.write('text going to stderr')  
> >       assert False  
> E       assert False  
>   
> test_nothing_logged.py:6: AssertionError  
> ----------------------------- Captured stdout call -----------------------------  
> text going to stdout  
> ----------------------------- Captured stderr call -----------------------------  
> text going to stderr  
> =========================== 1 failed in 0.02 seconds ===========================  
> _____________________________ test_messages_logged _____________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_messages_logged0  
> collected 1 item  
>   
> test_messages_logged.py F                                                [100%]  
>   
> =================================== FAILURES ===================================  
> ___________________________________ test_foo ___________________________________  
>   
>     def test_foo():  
>         sys.stdout.write('text going to stdout')  
>         sys.stderr.write('text going to stderr')  
>         logger.info('text going to logger')  
> >       assert False  
> E       assert False  
>   
> test_messages_logged.py:10: AssertionError  
> ----------------------------- Captured stdout call -----------------------------  
> text going to stdout  
> ----------------------------- Captured stderr call -----------------------------  
> text going to stderr  
> ------------------------------ Captured log call -------------------------------  
> INFO     test_messages_logged:test_messages_logged.py:9 text going to logger  
> =========================== 1 failed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     test_messages_logged:test_messages_logged.py:9 text going to logger  
> __________________________ test_root_logger_affected ___________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_root_logger_affected0  
> collected 1 item  
>   
> test_root_logger_affected.py F                                           [100%]  
>   
> =================================== FAILURES ===================================  
> ___________________________________ test_foo ___________________________________  
>   
>     def test_foo():  
>         logger.info('info text ' + 'going to logger')  
>         logger.warning('warning text ' + 'going to logger')  
>         logger.error('error text ' + 'going to logger')  
>       
> >       assert 0  
> E       assert 0  
>   
> test_root_logger_affected.py:9: AssertionError  
> ------------------------------ Captured log call -------------------------------  
> ERROR    root:test_root_logger_affected.py:7 error text going to logger  
> =========================== 1 failed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  root:test_root_logger_affected.py:6 warning text going to logger  
> ERROR    root:test_root_logger_affected.py:7 error text going to logger  
> ___________________ test_log_cli_level_log_level_interaction ___________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_level_log_level_interaction0  
> collecting ... collected 1 item  
>   
> test_log_cli_level_log_level_interaction.py::test_foo   
> -------------------------------- live log call ---------------------------------  
> INFO     root:test_log_cli_level_log_level_interaction.py:6 info text going to logger  
> WARNING  root:test_log_cli_level_log_level_interaction.py:7 warning text going to logger  
> ERROR    root:test_log_cli_level_log_level_interaction.py:8 error text going to logger  
> FAILED                                                                   [100%]  
>   
> =================================== FAILURES ===================================  
> ___________________________________ test_foo ___________________________________  
>   
>     def test_foo():  
>         logger.debug('debug text ' + 'going to logger')  
>         logger.info('info text ' + 'going to logger')  
>         logger.warning('warning text ' + 'going to logger')  
>         logger.error('error text ' + 'going to logger')  
> >       assert 0  
> E       assert 0  
>   
> test_log_cli_level_log_level_interaction.py:9: AssertionError  
> ------------------------------ Captured log call -------------------------------  
> ERROR    root:test_log_cli_level_log_level_interaction.py:8 error text going to logger  
> =========================== 1 failed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     root:test_log_cli_level_log_level_interaction.py:6 info text going to logger  
> WARNING  root:test_log_cli_level_log_level_interaction.py:7 warning text going to logger  
> ERROR    root:test_log_cli_level_log_level_interaction.py:8 error text going to logger  
> ______________________________ test_setup_logging ______________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_setup_logging0  
> collected 1 item  
>   
> test_setup_logging.py F                                                  [100%]  
>   
> =================================== FAILURES ===================================  
> ___________________________________ test_foo ___________________________________  
>   
>     def test_foo():  
>         logger.info('text going to logger from call')  
> >       assert False  
> E       assert False  
>   
> test_setup_logging.py:10: AssertionError  
> ------------------------------ Captured log setup ------------------------------  
> INFO     test_setup_logging:test_setup_logging.py:6 text going to logger from setup  
> ------------------------------ Captured log call -------------------------------  
> INFO     test_setup_logging:test_setup_logging.py:9 text going to logger from call  
> =========================== 1 failed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     test_setup_logging:test_setup_logging.py:6 text going to logger from setup  
> INFO     test_setup_logging:test_setup_logging.py:9 text going to logger from call  
> ____________________________ test_teardown_logging _____________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_teardown_logging0  
> collected 1 item  
>   
> test_teardown_logging.py .E                                              [100%]  
>   
> ==================================== ERRORS ====================================  
> ________________________ ERROR at teardown of test_foo _________________________  
>   
> function = <function test_foo at 0x7fd943dcd670>  
>   
>     def teardown_function(function):  
>         logger.info('text going to logger from teardown')  
> >       assert False  
> E       assert False  
>   
> test_teardown_logging.py:10: AssertionError  
> ------------------------------ Captured log call -------------------------------  
> INFO     test_teardown_logging:test_teardown_logging.py:6 text going to logger from call  
> ---------------------------- Captured log teardown -----------------------------  
> INFO     test_teardown_logging:test_teardown_logging.py:9 text going to logger from teardown  
> ====================== 1 passed, 1 error in 0.01 seconds =======================  
> ------------------------------ Captured log call -------------------------------  
> INFO     test_teardown_logging:test_teardown_logging.py:6 text going to logger from call  
> INFO     test_teardown_logging:test_teardown_logging.py:9 text going to logger from teardown  
> __________________________ test_disable_log_capturing __________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_disable_log_capturing0  
> collected 1 item  
>   
> test_disable_log_capturing.py F                                          [100%]  
>   
> =================================== FAILURES ===================================  
> ___________________________________ test_foo ___________________________________  
>   
>     def test_foo():  
>         sys.stdout.write('text going to stdout')  
>         logger.warning('catch me if you can!')  
>         sys.stderr.write('text going to stderr')  
> >       assert False  
> E       assert False  
>   
> test_disable_log_capturing.py:10: AssertionError  
> ----------------------------- Captured stdout call -----------------------------  
> text going to stdout  
> ----------------------------- Captured stderr call -----------------------------  
> text going to stderr  
> =========================== 1 failed in 0.01 seconds ===========================  
> <_pytest.pytester.LineMatcher object at 0x7fd943d2b820>  
> ------------------------------ Captured log call -------------------------------  
> WARNING  test_disable_log_capturing:test_disable_log_capturing.py:8 catch me if you can!  
> ________________________ test_disable_log_capturing_ini ________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_disable_log_capturing_ini0, inifile: tox.ini  
> collected 1 item  
>   
> test_disable_log_capturing_ini.py F                                      [100%]  
>   
> =================================== FAILURES ===================================  
> ___________________________________ test_foo ___________________________________  
>   
>     def test_foo():  
>         sys.stdout.write('text going to stdout')  
>         logger.warning('catch me if you can!')  
>         sys.stderr.write('text going to stderr')  
> >       assert False  
> E       assert False  
>   
> test_disable_log_capturing_ini.py:10: AssertionError  
> ----------------------------- Captured stdout call -----------------------------  
> text going to stdout  
> ----------------------------- Captured stderr call -----------------------------  
> text going to stderr  
> =========================== 1 failed in 0.01 seconds ===========================  
> <_pytest.pytester.LineMatcher object at 0x7fd943ce7a90>  
> ------------------------------ Captured log call -------------------------------  
> WARNING  test_disable_log_capturing_ini:test_disable_log_capturing_ini.py:8 catch me if you can!  
> _____________________ test_log_cli_enabled_disabled[False] _____________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_enabled_disabled1  
> collected 1 item  
>   
> test_log_cli_enabled_disabled.py .                                       [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> CRITICAL root:test_log_cli_enabled_disabled.py:3 critical message logged by test  
> __________________ test_log_cli_default_level_multiple_tests ___________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_default_level_multiple_tests0, inifile: tox.ini  
> collecting ... collected 2 items  
>   
> test_log_cli_default_level_multiple_tests.py::test_log_1   
> -------------------------------- live log call ---------------------------------  
> WARNING  root:test_log_cli_default_level_multiple_tests.py:4 log message from test_log_1  
> PASSED                                                                   [ 50%]  
> test_log_cli_default_level_multiple_tests.py::test_log_2   
> -------------------------------- live log call ---------------------------------  
> WARNING  root:test_log_cli_default_level_multiple_tests.py:7 log message from test_log_2  
> PASSED                                                                   [100%]  
>   
> =========================== 2 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  root:test_log_cli_default_level_multiple_tests.py:4 log message from test_log_1  
> WARNING  root:test_log_cli_default_level_multiple_tests.py:7 log message from test_log_2  
> _____________________ test_log_cli_default_level_sections ______________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_default_level_sections0, inifile: tox.ini  
> collecting ... collected 2 items  
>   
> test_log_cli_default_level_sections.py::test_log_1   
> -------------------------------- live log start --------------------------------  
> WARNING  root:conftest.py:5 >>>>> START >>>>>  
> -------------------------------- live log setup --------------------------------  
> WARNING  root:test_log_cli_default_level_sections.py:6 log message from setup of test_log_1  
> -------------------------------- live log call ---------------------------------  
> WARNING  root:test_log_cli_default_level_sections.py:11 log message from test_log_1  
> PASSED                                                                   [ 50%]  
> ------------------------------ live log teardown -------------------------------  
> WARNING  root:test_log_cli_default_level_sections.py:8 log message from teardown of test_log_1  
> ------------------------------- live log finish --------------------------------  
> WARNING  root:conftest.py:8 <<<<< END <<<<<<<  
>   
> test_log_cli_default_level_sections.py::test_log_2   
> -------------------------------- live log start --------------------------------  
> WARNING  root:conftest.py:5 >>>>> START >>>>>  
> -------------------------------- live log setup --------------------------------  
> WARNING  root:test_log_cli_default_level_sections.py:6 log message from setup of test_log_2  
> -------------------------------- live log call ---------------------------------  
> WARNING  root:test_log_cli_default_level_sections.py:14 log message from test_log_2  
> PASSED                                                                   [100%]  
> ------------------------------ live log teardown -------------------------------  
> WARNING  root:test_log_cli_default_level_sections.py:8 log message from teardown of test_log_2  
> ------------------------------- live log finish --------------------------------  
> WARNING  root:conftest.py:8 <<<<< END <<<<<<<  
>   
>   
> =========================== 2 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  root:conftest.py:5 >>>>> START >>>>>  
> WARNING  root:test_log_cli_default_level_sections.py:6 log message from setup of test_log_1  
> WARNING  root:test_log_cli_default_level_sections.py:11 log message from test_log_1  
> WARNING  root:test_log_cli_default_level_sections.py:8 log message from teardown of test_log_1  
> WARNING  root:conftest.py:8 <<<<< END <<<<<<<  
> WARNING  root:conftest.py:5 >>>>> START >>>>>  
> WARNING  root:test_log_cli_default_level_sections.py:6 log message from setup of test_log_2  
> WARNING  root:test_log_cli_default_level_sections.py:14 log message from test_log_2  
> WARNING  root:test_log_cli_default_level_sections.py:8 log message from teardown of test_log_2  
> WARNING  root:conftest.py:8 <<<<< END <<<<<<<  
> _______________________ test_live_logs_unknown_sections ________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_live_logs_unknown_sections0, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> ----------------------------- live log collection ------------------------------  
> WARNING  root:conftest.py:5 Unknown Section!  
>   
> test_live_logs_unknown_sections.py::test_log_1   
> -------------------------------- live log start --------------------------------  
> WARNING  root:conftest.py:8 >>>>> START >>>>>  
> -------------------------------- live log setup --------------------------------  
> WARNING  root:test_live_logs_unknown_sections.py:6 log message from setup of test_log_1  
> -------------------------------- live log call ---------------------------------  
> WARNING  root:test_live_logs_unknown_sections.py:11 log message from test_log_1  
> PASSED                                                                   [100%]  
> ------------------------------ live log teardown -------------------------------  
> WARNING  root:test_live_logs_unknown_sections.py:8 log message from teardown of test_log_1  
> ------------------------------- live log finish --------------------------------  
> WARNING  root:conftest.py:11 <<<<< END <<<<<<<  
>   
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  root:conftest.py:5 Unknown Section!  
> WARNING  root:conftest.py:8 >>>>> START >>>>>  
> WARNING  root:test_live_logs_unknown_sections.py:6 log message from setup of test_log_1  
> WARNING  root:test_live_logs_unknown_sections.py:11 log message from test_log_1  
> WARNING  root:test_live_logs_unknown_sections.py:8 log message from teardown of test_log_1  
> WARNING  root:conftest.py:11 <<<<< END <<<<<<<  
> __________________________ test_log_cli_auto_enable[] __________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_auto_enable0, inifile: tox.ini  
> collected 1 item  
>   
> test_log_cli_auto_enable.py .                                            [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     root:test_log_cli_auto_enable.py:4 log message from test_log_1 not to be shown  
> WARNING  root:test_log_cli_auto_enable.py:5 log message from test_log_1  
> ________________ test_log_cli_auto_enable[--log-level=WARNING] _________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_auto_enable1, inifile: tox.ini  
> collected 1 item  
>   
> test_log_cli_auto_enable.py .                                            [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  root:test_log_cli_auto_enable.py:5 log message from test_log_1  
> ______________ test_log_cli_auto_enable[--log-file-level=WARNING] ______________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_auto_enable2, inifile: tox.ini  
> collected 1 item  
>   
> test_log_cli_auto_enable.py .                                            [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     root:test_log_cli_auto_enable.py:4 log message from test_log_1 not to be shown  
> WARNING  root:test_log_cli_auto_enable.py:5 log message from test_log_1  
> ______________ test_log_cli_auto_enable[--log-cli-level=WARNING] _______________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_cli_auto_enable3, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> test_log_cli_auto_enable.py::test_log_1   
> -------------------------------- live log call ---------------------------------  
> WARNING  root:test_log_cli_auto_enable.py:5 log message from test_log_1  
> PASSED                                                                   [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     root:test_log_cli_auto_enable.py:4 log message from test_log_1 not to be shown  
> WARNING  root:test_log_cli_auto_enable.py:5 log message from test_log_1  
> ______________________________ test_log_file_cli _______________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_file_cli0  
> collected 1 item  
>   
> test_log_file_cli.py PASSED  
> .  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  catchlog:test_log_file_cli.py:7 This log message will be shown  
> ___________________________ test_log_file_cli_level ____________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_file_cli_level0  
> collected 1 item  
>   
> test_log_file_cli_level.py PASSED  
> .  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     catchlog:test_log_file_cli_level.py:7 This log message will be shown  
> ____________________ test_log_level_not_changed_by_default _____________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_level_not_changed_by_default0  
> collected 1 item  
>   
> test_log_level_not_changed_by_default.py .  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ______________________________ test_log_file_ini _______________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_file_ini0, inifile: tox.ini  
> collected 1 item  
>   
> test_log_file_ini.py PASSED  
> .  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> WARNING  catchlog:test_log_file_ini.py:7 This log message will be shown  
> ___________________________ test_log_file_ini_level ____________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_file_ini_level0, inifile: tox.ini  
> collected 1 item  
>   
> test_log_file_ini_level.py PASSED  
> .  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     catchlog:test_log_file_ini_level.py:7 This log message will be shown  
> ____________________________ test_log_file_unicode _____________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_file_unicode0, inifile: tox.ini  
> collected 1 item  
>   
> test_log_file_unicode.py .                                               [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     catchlog:test_log_file_unicode.py:6 Normal message  
> INFO     catchlog:test_log_file_unicode.py:7 ├  
> INFO     catchlog:test_log_file_unicode.py:8 Another normal message  
> _________________________ test_collection_live_logging _________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_collection_live_logging0  
> collecting ...   
> ----------------------------- live log collection ------------------------------  
> INFO     root:test_collection_live_logging.py:3 Normal message  
> collected 0 items  
>   
> ========================= no tests ran in 0.01 seconds =========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     root:test_collection_live_logging.py:3 Normal message  
> _______________________ test_collection_logging_to_file ________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_collection_logging_to_file0, inifile: tox.ini  
> collected 1 item  
>   
> test_collection_logging_to_file.py .                                     [100%]  
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     root:test_collection_logging_to_file.py:3 Normal message  
> INFO     root:test_collection_logging_to_file.py:7 info message in test_simple  
> ______________________________ test_log_in_hooks _______________________________  
> ----------------------------- Captured stdout call -----------------------------  
>   
> ---------------------------- live log sessionstart -----------------------------  
> INFO     root:conftest.py:7 sessionstart  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_in_hooks0, inifile: tox.ini  
> collecting ... collected 0 items  
> ----------------------------- live log collection ------------------------------  
> INFO     root:conftest.py:4 runtestloop  
> ---------------------------- live log sessionfinish ----------------------------  
> INFO     root:conftest.py:10 sessionfinish  
>   
> ========================= no tests ran in 0.00 seconds =========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     root:conftest.py:7 sessionstart  
> INFO     root:conftest.py:4 runtestloop  
> INFO     root:conftest.py:10 sessionfinish  
> ________________________ test_log_in_runtest_logreport _________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_in_runtest_logreport0, inifile: tox.ini  
> collecting ... collected 1 item  
>   
> test_log_in_runtest_logreport.py::test_first   
> ------------------------------ live log logreport ------------------------------  
> INFO     conftest:conftest.py:5 logreport  
> PASSED                                                                   [100%]------------------------------ live log logreport ------------------------------  
> INFO     conftest:conftest.py:5 logreport  
> ------------------------------ live log logreport ------------------------------  
> INFO     conftest:conftest.py:5 logreport  
>   
>   
> =========================== 1 passed in 0.01 seconds ===========================  
> ------------------------------ Captured log call -------------------------------  
> INFO     conftest:conftest.py:5 logreport  
> INFO     conftest:conftest.py:5 logreport  
> INFO     conftest:conftest.py:5 logreport  
> ______________________________ test_log_set_path _______________________________  
> ----------------------------- Captured stdout call -----------------------------  
> ============================= test session starts ==============================  
> platform linux -- Python 3.9.19, pytest-4.4.3.dev6+g4ccaa987d, py-1.11.0, pluggy-0.13.1 -- /home/swe-bench/miniconda3/envs/pytest-dev__pytest__4.4/bin/python  
> cachedir: .pytest_cache  
> rootdir: /tmp/pytest-of-swe-bench/pytest-0/test_log_set_path0, inifile: tox.ini  
> collecting ... collected 2 items  
>   
> test_log_set_path.py::test_first   
> -------------------------------- live log call ---------------------------------  
> INFO     testcase-logger:test_log_set_path.py:4 message from test 1  
> PASSED                                                                   [ 50%]  
> test_log_set_path.py::test_second   
> -------------------------------- live log call ---------------------------------  
> DEBUG    testcase-logger:test_log_set_path.py:8 message from test 2  
> PASSED                                                                   [100%]  
>   
> =========================== 2 passed in 0.01 seconds ===========================  
> ----------------------------- Captured stderr call -----------------------------  
> Exception ignored in: <_io.FileIO name='/tmp/pytest-of-swe-bench/pytest-0/test_log_set_path0/test_first' mode='wb' closefd=True>  
> Traceback (most recent call last):  
>   File "/home/swe-bench/pytest-dev__pytest/src/_pytest/logging.py", line 479, in set_log_path  
>     self.log_file_handler = logging.FileHandler(  
> ResourceWarning: unclosed file <_io.TextIOWrapper name='/tmp/pytest-of-swe-bench/pytest-0/test_log_set_path0/test_first' mode='w' encoding='UTF-8'>  
> ------------------------------ Captured log call -------------------------------  
> INFO     testcase-logger:test_log_set_path.py:4 message from test 1  
> DEBUG    testcase-logger:test_log_set_path.py:8 message from test 2  
> =========================== short test summary info ============================  
> FAILED testing/logging/test_reporting.py::test_log_cli_enabled_disabled[True]  
> FAILED testing/logging/test_reporting.py::test_log_cli_default_level  
> FAILED testing/logging/test_reporting.py::test_sections_single_new_line_after_test_outcome  
> FAILED testing/logging/test_reporting.py::test_log_cli_level  
> FAILED testing/logging/test_reporting.py::test_log_cli_ini_level  
> PASSED testing/logging/test_reporting.py::test_live_logging_suspends_capture[True]  
> PASSED testing/logging/test_reporting.py::test_live_logging_suspends_capture[False]  
> PASSED testing/logging/test_reporting.py::test_nothing_logged  
> PASSED testing/logging/test_reporting.py::test_messages_logged  
> PASSED testing/logging/test_reporting.py::test_root_logger_affected  
> PASSED testing/logging/test_reporting.py::test_log_cli_level_log_level_interaction  
> PASSED testing/logging/test_reporting.py::test_setup_logging  
> PASSED testing/logging/test_reporting.py::test_teardown_logging  
> PASSED testing/logging/test_reporting.py::test_disable_log_capturing  
> PASSED testing/logging/test_reporting.py::test_disable_log_capturing_ini  
> PASSED testing/logging/test_reporting.py::test_log_cli_enabled_disabled[False]  
> PASSED testing/logging/test_reporting.py::test_log_cli_default_level_multiple_tests  
> PASSED testing/logging/test_reporting.py::test_log_cli_default_level_sections  
> PASSED testing/logging/test_reporting.py::test_live_logs_unknown_sections  
> PASSED testing/logging/test_reporting.py::test_log_cli_auto_enable[]  
> PASSED testing/logging/test_reporting.py::test_log_cli_auto_enable[--log-level=WARNING]  
> PASSED testing/logging/test_reporting.py::test_log_cli_auto_enable[--log-file-level=WARNING]  
> PASSED testing/logging/test_reporting.py::test_log_cli_auto_enable[--log-cli-level=WARNING]  
> PASSED testing/logging/test_reporting.py::test_log_file_cli  
> PASSED testing/logging/test_reporting.py::test_log_file_cli_level  
> PASSED testing/logging/test_reporting.py::test_log_level_not_changed_by_default  
> PASSED testing/logging/test_reporting.py::test_log_file_ini  
> PASSED testing/logging/test_reporting.py::test_log_file_ini_level  
> PASSED testing/logging/test_reporting.py::test_log_file_unicode  
> PASSED testing/logging/test_reporting.py::test_collection_live_logging  
> PASSED testing/logging/test_reporting.py::test_collection_logging_to_file  
> PASSED testing/logging/test_reporting.py::test_log_in_hooks  
> PASSED testing/logging/test_reporting.py::test_log_in_runtest_logreport  
> PASSED testing/logging/test_reporting.py::test_log_set_path  
> ===================== 5 failed, 29 passed in 0.93 seconds ======================  
> ERROR conda.cli.main_run:execute(124): `conda run pytest -rA testing/logging/test_reporting.py` failed. (See above for error)  
>   
>    
> [pytest-dev__pytest__4.4] [pytest-dev__pytest-5227] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [pytest-dev__pytest__4.4] [pytest-dev__pytest-5227] Test script run successful   
> Attempt to fix test errors? yes  
> 41341 prompt tokens, 383 completion tokens, $0.212450 cost  

Here are the updated *SEARCH/REPLACE* blocks to fix the remaining test failures:

testing/logging/test_reporting.py
```python
<<<<<<< SEARCH
                    "test_log_cli_enabled_disabled.py* CRITICAL critical message logged by test",
=======
                    "CRITICAL root:test_log_cli_enabled_disabled.py:3 critical message logged by test",
>>>>>>> REPLACE
```

testing/logging/test_reporting.py
```python
<<<<<<< SEARCH
                "test_log_cli_default_level.py*WARNING message will be shown*",
=======
                "WARNING  catchlog:test_log_cli_default_level.py:7 WARNING message will be shown",
>>>>>>> REPLACE
```

testing/logging/test_reporting.py
```python
<<<<<<< SEARCH
                "*WARNING*log message from teardown of test_log_1*",
                "*-- live log finish --*",
                "*WARNING* <<<<< END <<<<<<<*",
                "*WARNING* <<<<< END <<<<<<<*",
=======
                "WARNING  root:test_sections_single_new_line_after_test_outcome.py:8 log message from teardown of test_log_1",
                "------------------------------- live log finish --------------------------------",
                "WARNING  root:conftest.py:8 <<<<< END <<<<<<<",
                "WARNING  root:conftest.py:9 <<<<< END <<<<<<<",
>>>>>>> REPLACE
```

testing/logging/test_reporting.py
```python
<<<<<<< SEARCH
                "test_log_cli_level.py*This log message will be shown",
=======
                "INFO     catchlog:test_log_cli_level.py:7 This log message will be shown",
>>>>>>> REPLACE
```

testing/logging/test_reporting.py
```python
<<<<<<< SEARCH
                "test_log_cli_ini_level.py* This log message will be shown",
=======
                "INFO     catchlog:test_log_cli_ini_level.py:7 This log message will be shown",
>>>>>>> REPLACE
```

> The LLM did not conform to the edit format.  
> For more info see: https://aider.chat/docs/faq.html#aider-isnt-editing-my-files  
> # 5 SEARCH/REPLACE blocks failed to match!  
>   
> ## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in testing/logging/test_reporting.py  
> <<<<<<< SEARCH  
>                     "test_log_cli_enabled_disabled.py* CRITICAL critical message logged by test",  
> =======  
>                     "CRITICAL root:test_log_cli_enabled_disabled.py:3 critical message logged by test",  
> >>>>>>> REPLACE  
>   
>   
> ## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in testing/logging/test_reporting.py  
> <<<<<<< SEARCH  
>                 "test_log_cli_default_level.py*WARNING message will be shown*",  
> =======  
>                 "WARNING  catchlog:test_log_cli_default_level.py:7 WARNING message will be shown",  
> >>>>>>> REPLACE  
>   
>   
> ## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in testing/logging/test_reporting.py  
> <<<<<<< SEARCH  
>                 "*WARNING*log message from teardown of test_log_1*",  
>                 "*-- live log finish --*",  
>                 "*WARNING* <<<<< END <<<<<<<*",  
>                 "*WARNING* <<<<< END <<<<<<<*",  
> =======  
>                 "WARNING  root:test_sections_single_new_line_after_test_outcome.py:8 log message from teardown of test_log_1",  
>                 "------------------------------- live log finish --------------------------------",  
>                 "WARNING  root:conftest.py:8 <<<<< END <<<<<<<",  
>                 "WARNING  root:conftest.py:9 <<<<< END <<<<<<<",  
> >>>>>>> REPLACE  
>   
>   
> ## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in testing/logging/test_reporting.py  
> <<<<<<< SEARCH  
>                 "test_log_cli_level.py*This log message will be shown",  
> =======  
>                 "INFO     catchlog:test_log_cli_level.py:7 This log message will be shown",  
> >>>>>>> REPLACE  
>   
>   
> ## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in testing/logging/test_reporting.py  
> <<<<<<< SEARCH  
>                 "test_log_cli_ini_level.py* This log message will be shown",  
> =======  
>                 "INFO     catchlog:test_log_cli_ini_level.py:7 This log message will be shown",  
> >>>>>>> REPLACE  
>   
> The SEARCH section must exactly match an existing block of lines including all white space, comments, indentation, docstrings, etc  
> Only 4 reflections allowed, stopping.  
