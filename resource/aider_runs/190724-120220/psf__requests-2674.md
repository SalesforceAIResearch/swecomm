
# aider chat started at 2024-07-19 10:24:20

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpx8rga6da/.git with 132 files  
> Repo-map: using 2048 tokens  

#### urllib3 exceptions passing through requests API  
#### I don't know if it's a design goal of requests to hide urllib3's exceptions and wrap them around requests.exceptions types.  
####   
#### (If it's not IMHO it should be, but that's another discussion)  
####   
#### If it is, I have at least two of them passing through that I have to catch in addition to requests' exceptions. They are requests.packages.urllib3.exceptions.DecodeError and requests.packages.urllib3.exceptions.TimeoutError (this one I get when a proxy timeouts)  
####   
#### Thanks!  
####  
> 14875 prompt tokens, 96 completion tokens, $0.075815 cost  

To address the issue of urllib3 exceptions passing through the requests API, we will need to modify the following files:

1. `requests/exceptions.py` - To add new exception classes that wrap around `urllib3.exceptions.DecodeError` and `urllib3.exceptions.TimeoutError`.
2. `requests/adapters.py` - To catch the `urllib3` exceptions and raise the corresponding `requests` exceptions.

Please add these files to the chat so I can provide the necessary changes.

> requests/adapters.py  
> requests/exceptions.py  
> Add these files to the chat? yes  
> 7594 prompt tokens, 423 completion tokens, $0.044315 cost  

Here are the necessary changes to handle `urllib3.exceptions.DecodeError` and `urllib3.exceptions.TimeoutError`:

1. Add new exception classes in `requests/exceptions.py`.
2. Catch the `urllib3` exceptions and raise the corresponding `requests` exceptions in `requests/adapters.py`.

Let's start with `requests/exceptions.py`:

requests/exceptions.py
```python
<<<<<<< SEARCH
class RetryError(RequestException):
    """Custom retries logic failed"""
=======
class RetryError(RequestException):
    """Custom retries logic failed"""

class DecodeError(RequestException):
    """Failed to decode response content"""

class TimeoutError(RequestException):
    """The request timed out."""
>>>>>>> REPLACE
```

Next, we need to update `requests/adapters.py` to catch these exceptions:

requests/adapters.py
```python
from .exceptions import (ConnectionError, ConnectTimeout, ReadTimeout, SSLError,
                         ProxyError, RetryError)
=======
from .exceptions import (ConnectionError, ConnectTimeout, ReadTimeout, SSLError,
                         ProxyError, RetryError, DecodeError, TimeoutError)
>>>>>>> REPLACE
```

requests/adapters.py
```python
        except (_SSLError, _HTTPError) as e:
            if isinstance(e, _SSLError):
                raise SSLError(e, request=request)
            elif isinstance(e, ReadTimeoutError):
                raise ReadTimeout(e, request=request)
            else:
                raise
=======
        except (_SSLError, _HTTPError, DecodeError, TimeoutError) as e:
            if isinstance(e, _SSLError):
                raise SSLError(e, request=request)
            elif isinstance(e, ReadTimeoutError):
                raise ReadTimeout(e, request=request)
            elif isinstance(e, DecodeError):
                raise DecodeError(e, request=request)
            elif isinstance(e, TimeoutError):
                raise TimeoutError(e, request=request)
            else:
                raise
>>>>>>> REPLACE
```

These changes will ensure that `urllib3.exceptions.DecodeError` and `urllib3.exceptions.TimeoutError` are properly wrapped and raised as `requests` exceptions.

> Applied edit to requests/exceptions.py  
>   
> Test Script:  pytest --no-header -rA --tb=no -p no:cacheprovider test_requests.py;  
> [psf__requests__2.7] [psf__requests-2674] Command: pytest --no-header -rA --tb=no -p no:cacheprovider test_requests.py   
> [psf__requests__2.7] [psf__requests-2674] Subprocess args: {"cwd": "/opt/psf__requests", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [psf__requests__2.7] [psf__requests-2674] Std. Output:  
> ============================= test session starts ==============================  
> collected 161 items  
>   
> test_requests.py F.........................F............................ [ 34%]  
> ............................X........................................... [ 78%]  
> .......................FF.........                                       [100%]  
>   
> =============================== warnings summary ===============================  
> requests/packages/urllib3/connectionpool.py:95  
>   /opt/psf__requests/requests/packages/urllib3/connectionpool.py:95: DeprecationWarning: invalid escape sequence \*  
>     """  
>   
> requests/packages/urllib3/connectionpool.py:424  
>   /opt/psf__requests/requests/packages/urllib3/connectionpool.py:424: DeprecationWarning: invalid escape sequence \*  
>     """  
>   
> requests/packages/urllib3/connectionpool.py:772  
>   /opt/psf__requests/requests/packages/urllib3/connectionpool.py:772: DeprecationWarning: invalid escape sequence \*  
>     """  
>   
> requests/packages/urllib3/_collections.py:1  
> requests/packages/urllib3/_collections.py:1  
>   /opt/psf__requests/requests/packages/urllib3/_collections.py:1: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3, and in 3.10 it will stop working  
>     from collections import Mapping, MutableMapping  
>   
> requests/packages/urllib3/poolmanager.py:32  
>   /opt/psf__requests/requests/packages/urllib3/poolmanager.py:32: DeprecationWarning: invalid escape sequence \*  
>     """  
>   
> requests/models.py:783  
>   /opt/psf__requests/requests/models.py:783: DeprecationWarning: invalid escape sequence \*  
>     """Returns the json-encoded content of a response, if any.  
>   
> requests/api.py:59  
>   /opt/psf__requests/requests/api.py:59: DeprecationWarning: invalid escape sequence \*  
>     """Sends a GET request.  
>   
> requests/api.py:73  
>   /opt/psf__requests/requests/api.py:73: DeprecationWarning: invalid escape sequence \*  
>     """Sends a OPTIONS request.  
>   
> requests/api.py:86  
>   /opt/psf__requests/requests/api.py:86: DeprecationWarning: invalid escape sequence \*  
>     """Sends a HEAD request.  
>   
> requests/api.py:99  
>   /opt/psf__requests/requests/api.py:99: DeprecationWarning: invalid escape sequence \*  
>     """Sends a POST request.  
>   
> requests/api.py:113  
>   /opt/psf__requests/requests/api.py:113: DeprecationWarning: invalid escape sequence \*  
>     """Sends a PUT request.  
>   
> requests/api.py:126  
>   /opt/psf__requests/requests/api.py:126: DeprecationWarning: invalid escape sequence \*  
>     """Sends a PATCH request.  
>   
> requests/api.py:139  
>   /opt/psf__requests/requests/api.py:139: DeprecationWarning: invalid escape sequence \*  
>     """Sends a DELETE request.  
>   
> requests/sessions.py:470  
>   /opt/psf__requests/requests/sessions.py:470: DeprecationWarning: invalid escape sequence \*  
>     """Sends a GET request. Returns :class:`Response` object.  
>   
> requests/sessions.py:480  
>   /opt/psf__requests/requests/sessions.py:480: DeprecationWarning: invalid escape sequence \*  
>     """Sends a OPTIONS request. Returns :class:`Response` object.  
>   
> requests/sessions.py:490  
>   /opt/psf__requests/requests/sessions.py:490: DeprecationWarning: invalid escape sequence \*  
>     """Sends a HEAD request. Returns :class:`Response` object.  
>   
> requests/sessions.py:500  
>   /opt/psf__requests/requests/sessions.py:500: DeprecationWarning: invalid escape sequence \*  
>     """Sends a POST request. Returns :class:`Response` object.  
>   
> requests/sessions.py:511  
>   /opt/psf__requests/requests/sessions.py:511: DeprecationWarning: invalid escape sequence \*  
>     """Sends a PUT request. Returns :class:`Response` object.  
>   
> requests/sessions.py:521  
>   /opt/psf__requests/requests/sessions.py:521: DeprecationWarning: invalid escape sequence \*  
>     """Sends a PATCH request. Returns :class:`Response` object.  
>   
> requests/sessions.py:531  
>   /opt/psf__requests/requests/sessions.py:531: DeprecationWarning: invalid escape sequence \*  
>     """Sends a DELETE request. Returns :class:`Response` object.  
>   
> test_requests.py::RequestsTestCase::test_BASICAUTH_TUPLE_HTTP_200_OK_GET  
>   /opt/psf__requests/requests/models.py:168: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3, and in 3.10 it will stop working  
>     if isinstance(hook, collections.Callable):  
>   
> test_requests.py::TestContentEncodingDetection::test_html4_pragma  
> test_requests.py::TestContentEncodingDetection::test_html_charset  
> test_requests.py::TestContentEncodingDetection::test_none  
> test_requests.py::TestContentEncodingDetection::test_precedence  
> test_requests.py::TestContentEncodingDetection::test_xhtml_pragma  
> test_requests.py::TestContentEncodingDetection::test_xml  
>   /opt/psf__requests/requests/utils.py:294: DeprecationWarning: In requests 3.0, get_encodings_from_content will be removed. For more information, please see the discussion on issue #2266. (This warning should only appear once.)  
>     warnings.warn((  
>   
> -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html  
> =========================== short test summary info ============================  
> PASSED test_requests.py::RequestsTestCase::test_DIGESTAUTH_QUOTES_QOP_VALUE  
> PASSED test_requests.py::RequestsTestCase::test_DIGESTAUTH_WRONG_HTTP_401_GET  
> PASSED test_requests.py::RequestsTestCase::test_DIGEST_AUTH_RETURNS_COOKIE  
> PASSED test_requests.py::RequestsTestCase::test_DIGEST_AUTH_SETS_SESSION_COOKIES  
> PASSED test_requests.py::RequestsTestCase::test_DIGEST_HTTP_200_OK_GET  
> PASSED test_requests.py::RequestsTestCase::test_DIGEST_STREAM  
> PASSED test_requests.py::RequestsTestCase::test_HTTP_200_OK_GET_ALTERNATIVE  
> PASSED test_requests.py::RequestsTestCase::test_HTTP_200_OK_GET_WITH_MIXED_PARAMS  
> PASSED test_requests.py::RequestsTestCase::test_HTTP_200_OK_GET_WITH_PARAMS  
> PASSED test_requests.py::RequestsTestCase::test_HTTP_200_OK_HEAD  
> PASSED test_requests.py::RequestsTestCase::test_HTTP_200_OK_PUT  
> PASSED test_requests.py::RequestsTestCase::test_HTTP_302_ALLOW_REDIRECT_GET  
> PASSED test_requests.py::RequestsTestCase::test_LocationParseError  
> PASSED test_requests.py::RequestsTestCase::test_POSTBIN_GET_POST_FILES  
> PASSED test_requests.py::RequestsTestCase::test_POSTBIN_GET_POST_FILES_WITH_DATA  
> PASSED test_requests.py::RequestsTestCase::test_auth_is_retained_for_redirect_on_host  
> PASSED test_requests.py::RequestsTestCase::test_auth_is_stripped_on_redirect_off_host  
> PASSED test_requests.py::RequestsTestCase::test_autoset_header_values_are_native  
> PASSED test_requests.py::RequestsTestCase::test_basic_auth_str_is_always_native  
> PASSED test_requests.py::RequestsTestCase::test_basic_building  
> PASSED test_requests.py::RequestsTestCase::test_basicauth_with_netrc  
> PASSED test_requests.py::RequestsTestCase::test_can_send_bytes_bytearray_objects_with_files  
> PASSED test_requests.py::RequestsTestCase::test_can_send_file_object_with_non_string_filename  
> PASSED test_requests.py::RequestsTestCase::test_can_send_nonstring_objects_with_files  
> PASSED test_requests.py::RequestsTestCase::test_cannot_send_unprepared_requests  
> PASSED test_requests.py::RequestsTestCase::test_connection_error_invalid_domain  
> PASSED test_requests.py::RequestsTestCase::test_connection_error_invalid_port  
> PASSED test_requests.py::RequestsTestCase::test_cookie_as_dict_items  
> PASSED test_requests.py::RequestsTestCase::test_cookie_as_dict_keeps_items  
> PASSED test_requests.py::RequestsTestCase::test_cookie_as_dict_keeps_len  
> PASSED test_requests.py::RequestsTestCase::test_cookie_as_dict_keys  
> PASSED test_requests.py::RequestsTestCase::test_cookie_as_dict_values  
> PASSED test_requests.py::RequestsTestCase::test_cookie_parameters  
> PASSED test_requests.py::RequestsTestCase::test_cookie_persists_via_api  
> PASSED test_requests.py::RequestsTestCase::test_cookie_quote_wrapped  
> PASSED test_requests.py::RequestsTestCase::test_cookie_removed_on_expire  
> PASSED test_requests.py::RequestsTestCase::test_cookie_sent_on_redirect  
> PASSED test_requests.py::RequestsTestCase::test_custom_content_type  
> PASSED test_requests.py::RequestsTestCase::test_decompress_gzip  
> PASSED test_requests.py::RequestsTestCase::test_different_encodings_dont_break_post  
> PASSED test_requests.py::RequestsTestCase::test_entry_points  
> PASSED test_requests.py::RequestsTestCase::test_fixes_1329  
> PASSED test_requests.py::RequestsTestCase::test_generic_cookiejar_works  
> PASSED test_requests.py::RequestsTestCase::test_get_auth_from_url  
> PASSED test_requests.py::RequestsTestCase::test_get_auth_from_url_encoded_hashes  
> PASSED test_requests.py::RequestsTestCase::test_get_auth_from_url_encoded_spaces  
> PASSED test_requests.py::RequestsTestCase::test_get_auth_from_url_not_encoded_spaces  
> PASSED test_requests.py::RequestsTestCase::test_get_auth_from_url_percent_chars  
> PASSED test_requests.py::RequestsTestCase::test_header_keys_are_native  
> PASSED test_requests.py::RequestsTestCase::test_header_remove_is_case_insensitive  
> PASSED test_requests.py::RequestsTestCase::test_headers_on_session_with_None_are_not_sent  
> PASSED test_requests.py::RequestsTestCase::test_history_is_always_a_list  
> PASSED test_requests.py::RequestsTestCase::test_hook_receives_request_arguments  
> PASSED test_requests.py::RequestsTestCase::test_http_error  
> PASSED test_requests.py::RequestsTestCase::test_invalid_url  
> PASSED test_requests.py::RequestsTestCase::test_json_param_post_content_type_works  
> PASSED test_requests.py::RequestsTestCase::test_links  
> PASSED test_requests.py::RequestsTestCase::test_long_authinfo_in_url  
> PASSED test_requests.py::RequestsTestCase::test_manual_redirect_with_partial_body_read  
> PASSED test_requests.py::RequestsTestCase::test_mixed_case_scheme_acceptable  
> PASSED test_requests.py::RequestsTestCase::test_no_content_length  
> PASSED test_requests.py::RequestsTestCase::test_nonhttp_schemes_dont_check_URLs  
> PASSED test_requests.py::RequestsTestCase::test_override_content_length  
> PASSED test_requests.py::RequestsTestCase::test_param_cookiejar_works  
> PASSED test_requests.py::RequestsTestCase::test_params_are_added_before_fragment  
> PASSED test_requests.py::RequestsTestCase::test_params_are_merged_case_sensitive  
> PASSED test_requests.py::RequestsTestCase::test_path_is_not_double_encoded  
> PASSED test_requests.py::RequestsTestCase::test_prepare_request_with_bytestring_url  
> PASSED test_requests.py::RequestsTestCase::test_prepared_from_session  
> PASSED test_requests.py::RequestsTestCase::test_prepared_request_hook  
> PASSED test_requests.py::RequestsTestCase::test_pyopenssl_redirect  
> PASSED test_requests.py::RequestsTestCase::test_redirect_with_wrong_gzipped_header  
> PASSED test_requests.py::RequestsTestCase::test_request_and_response_are_pickleable  
> PASSED test_requests.py::RequestsTestCase::test_request_cookie_overrides_session_cookie  
> PASSED test_requests.py::RequestsTestCase::test_request_cookies_not_persisted  
> PASSED test_requests.py::RequestsTestCase::test_request_ok_set  
> PASSED test_requests.py::RequestsTestCase::test_requests_history_is_saved  
> PASSED test_requests.py::RequestsTestCase::test_requests_in_history_are_not_overridden  
> PASSED test_requests.py::RequestsTestCase::test_response_decode_unicode  
> PASSED test_requests.py::RequestsTestCase::test_response_is_iterable  
> PASSED test_requests.py::RequestsTestCase::test_response_iter_lines  
> PASSED test_requests.py::RequestsTestCase::test_session_hooks_are_overriden_by_request_hooks  
> PASSED test_requests.py::RequestsTestCase::test_session_hooks_are_used_with_no_request_hooks  
> PASSED test_requests.py::RequestsTestCase::test_session_pickling  
> PASSED test_requests.py::RequestsTestCase::test_set_cookie_on_301  
> PASSED test_requests.py::RequestsTestCase::test_status_raising  
> PASSED test_requests.py::RequestsTestCase::test_time_elapsed_blank  
> PASSED test_requests.py::RequestsTestCase::test_transport_adapter_ordering  
> PASSED test_requests.py::RequestsTestCase::test_unconsumed_session_response_closes_connection  
> PASSED test_requests.py::RequestsTestCase::test_unicode_get  
> PASSED test_requests.py::RequestsTestCase::test_unicode_header_name  
> PASSED test_requests.py::RequestsTestCase::test_unicode_method_name  
> PASSED test_requests.py::RequestsTestCase::test_unicode_multipart_post  
> PASSED test_requests.py::RequestsTestCase::test_unicode_multipart_post_fieldnames  
> PASSED test_requests.py::RequestsTestCase::test_uppercase_scheme_redirect  
> PASSED test_requests.py::RequestsTestCase::test_urlencoded_get_query_multivalued_param  
> PASSED test_requests.py::RequestsTestCase::test_user_agent_transfers  
> PASSED test_requests.py::TestContentEncodingDetection::test_html4_pragma  
> PASSED test_requests.py::TestContentEncodingDetection::test_html_charset  
> PASSED test_requests.py::TestContentEncodingDetection::test_none  
> PASSED test_requests.py::TestContentEncodingDetection::test_precedence  
> PASSED test_requests.py::TestContentEncodingDetection::test_xhtml_pragma  
> PASSED test_requests.py::TestContentEncodingDetection::test_xml  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_contains  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_copy  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_delitem  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_docstring_example  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_equality  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_fixes_649  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_get  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_getitem  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_iter  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_iterable_init  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_kwargs_init  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_len  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_lower_items  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_mapping_init  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_preserve_key_case  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_preserve_last_key_case  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_repr  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_setdefault  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_update  
> PASSED test_requests.py::TestCaseInsensitiveDict::test_update_retains_unchanged  
> PASSED test_requests.py::UtilsTestCase::test_address_in_network  
> PASSED test_requests.py::UtilsTestCase::test_dotted_netmask  
> PASSED test_requests.py::UtilsTestCase::test_get_auth_from_url  
> PASSED test_requests.py::UtilsTestCase::test_get_environ_proxies  
> PASSED test_requests.py::UtilsTestCase::test_get_environ_proxies_ip_ranges  
> PASSED test_requests.py::UtilsTestCase::test_guess_filename_when_filename_is_an_int  
> PASSED test_requests.py::UtilsTestCase::test_guess_filename_when_int  
> PASSED test_requests.py::UtilsTestCase::test_guess_filename_with_file_like_obj  
> PASSED test_requests.py::UtilsTestCase::test_guess_filename_with_unicode_name  
> PASSED test_requests.py::UtilsTestCase::test_is_ipv4_address  
> PASSED test_requests.py::UtilsTestCase::test_is_valid_cidr  
> PASSED test_requests.py::UtilsTestCase::test_requote_uri_properly_requotes  
> PASSED test_requests.py::UtilsTestCase::test_requote_uri_with_unquoted_percents  
> PASSED test_requests.py::UtilsTestCase::test_super_len_io_streams  
> PASSED test_requests.py::TestMorselToCookieExpires::test_expires_invalid_int  
> PASSED test_requests.py::TestMorselToCookieExpires::test_expires_invalid_str  
> PASSED test_requests.py::TestMorselToCookieExpires::test_expires_none  
> PASSED test_requests.py::TestMorselToCookieExpires::test_expires_valid_str  
> PASSED test_requests.py::TestMorselToCookieMaxAge::test_max_age_invalid_str  
> PASSED test_requests.py::TestMorselToCookieMaxAge::test_max_age_valid_int  
> PASSED test_requests.py::TestTimeout::test_stream_timeout  
> PASSED test_requests.py::TestTimeout::test_invalid_timeout  
> PASSED test_requests.py::TestTimeout::test_none_timeout  
> PASSED test_requests.py::TestTimeout::test_read_timeout  
> PASSED test_requests.py::TestTimeout::test_encoded_methods  
> PASSED test_requests.py::TestRedirects::test_requests_are_updated_each_time  
> PASSED test_requests.py::test_data_argument_accepts_tuples  
> PASSED test_requests.py::test_prepared_request_empty_copy  
> PASSED test_requests.py::test_prepared_request_no_cookies_copy  
> PASSED test_requests.py::test_prepared_request_complete_copy  
> PASSED test_requests.py::test_prepare_unicode_url  
> PASSED test_requests.py::test_urllib3_retries  
> PASSED test_requests.py::test_vendor_aliases  
> XPASS test_requests.py::RequestsTestCase::test_response_iter_lines_reentrant  
> FAILED test_requests.py::RequestsTestCase::test_BASICAUTH_TUPLE_HTTP_200_OK_GET  
> FAILED test_requests.py::RequestsTestCase::test_conflicting_post_params - Typ...  
> FAILED test_requests.py::TestTimeout::test_connect_timeout - requests.excepti...  
> FAILED test_requests.py::TestTimeout::test_total_timeout_connect - requests.e...  
> ============ 4 failed, 156 passed, 1 xpassed, 28 warnings in 55.60s ============  
>    
> [psf__requests__2.7] [psf__requests-2674] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [psf__requests__2.7] [psf__requests-2674] Test script run successful   
> Attempt to fix test errors? yes  
> 12269 prompt tokens, 408 completion tokens, $0.067465 cost  

To address the test failures, we need to ensure that the `DecodeError` and `TimeoutError` exceptions are properly caught and wrapped in the `requests` exceptions. Let's make the necessary adjustments:

1. Update `requests/exceptions.py` to include the new exception classes.
2. Update `requests/adapters.py` to catch and raise the new exceptions.

Here are the changes:

requests/exceptions.py
```python
class RetryError(RequestException):
    """Custom retries logic failed"""
=======
class RetryError(RequestException):
    """Custom retries logic failed"""

class DecodeError(RequestException):
    """Failed to decode response content"""

class TimeoutError(RequestException):
    """The request timed out."""
>>>>>>> REPLACE
```

requests/adapters.py
```python
from .exceptions import (ConnectionError, ConnectTimeout, ReadTimeout, SSLError,
                         ProxyError, RetryError)
=======
from .exceptions import (ConnectionError, ConnectTimeout, ReadTimeout, SSLError,
                         ProxyError, RetryError, DecodeError, TimeoutError)
>>>>>>> REPLACE
```

requests/adapters.py
```python
        except (_SSLError, _HTTPError) as e:
            if isinstance(e, _SSLError):
                raise SSLError(e, request=request)
            elif isinstance(e, ReadTimeoutError):
                raise ReadTimeout(e, request=request)
            else:
                raise
=======
        except (_SSLError, _HTTPError, DecodeError, TimeoutError) as e:
            if isinstance(e, _SSLError):
                raise SSLError(e, request=request)
            elif isinstance(e, ReadTimeoutError):
                raise ReadTimeout(e, request=request)
            elif isinstance(e, DecodeError):
                raise DecodeError(e, request=request)
            elif isinstance(e, TimeoutError):
                raise TimeoutError(e, request=request)
            else:
                raise
>>>>>>> REPLACE
```

These changes should ensure that the `DecodeError` and `TimeoutError` exceptions are properly handled. Please run the tests again to verify.

