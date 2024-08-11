
# aider chat started at 2024-07-19 16:48:51

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp8_57h2bw/.git with 6,141 files  
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
> 33878 prompt tokens, 71 completion tokens, $0.170455 cost  

To address the issue with the two-digit year check in `django.utils.http.parse_http_date`, we will need to modify the logic in that function. The file that needs to be edited is:

- `django/utils/http.py`

Please add `django/utils/http.py` to the chat so I can provide the necessary *SEARCH/REPLACE* block.

> django/utils/http.py  
> Add these files to the chat? yes  
> 7937 prompt tokens, 132 completion tokens, $0.041665 cost  

Here is the necessary change to the `parse_http_date` function in `django/utils/http.py` to correctly handle two-digit years according to RFC 7231:

django/utils/http.py
```python
<<<<<<< SEARCH
            if year < 70:
                year += 2000
            else:
                year += 1900
=======
            current_year = datetime.datetime.utcnow().year
            current_century = current_year // 100 * 100
            if year + current_century > current_year + 50:
                year += current_century - 100
            else:
                year += current_century
>>>>>>> REPLACE
```

> Applied edit to django/utils/http.py  
