
# aider chat started at 2024-07-20 12:44:51

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpr2ijejl5/.git with 6,141 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### django.utils.http.parse_http_date two digit year check is incorrect  
#### Description  
#### 	   
#### 		(last modified by Ad Timmering)  
#### 	   
#### RFC 850 does not mention this, but in RFC 7231 (and there's something similar in RFC 2822), there's the following quote:  
#### Recipients of a timestamp value in rfc850-date format, which uses a  
#### two-digit year, MUST interpret a timestamp that appears to be more  
#### than 50 years in the future as representing the most recent year in  
#### the past that had the same last two digits.  
#### Current logic is hard coded to consider 0-69 to be in 2000-2069, and 70-99 to be 1970-1999, instead of comparing versus the current year.  
> 33861 prompt tokens, 71 completion tokens, $0.170370 cost  

To address the issue with the two-digit year check in `django.utils.http.parse_http_date`, we will need to modify the logic to compare against the current year instead of using hard-coded values.

The file most likely to need changes is:
- `django/utils/http.py`

Please add this file to the chat so I can proceed with the necessary modifications.

> django/utils/http.py  
> Add these files to the chat? yes  
> 7976 prompt tokens, 162 completion tokens, $0.042310 cost  

To address the issue with the two-digit year check in `django.utils.http.parse_http_date`, we will modify the logic to compare against the current year instead of using hard-coded values.

Here is the *SEARCH/REPLACE* block:

django/utils/http.py
```python
<<<<<<< SEARCH
        if year < 100:
            if year < 70:
                year += 2000
            else:
                year += 1900
=======
        if year < 100:
            current_year = datetime.datetime.now().year
            current_century = current_year // 100 * 100
            if year > (current_year % 100) + 50:
                year += current_century - 100
            else:
                year += current_century
>>>>>>> REPLACE
```

> Applied edit to django/utils/http.py  
