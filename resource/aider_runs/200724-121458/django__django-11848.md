
# aider chat started at 2024-07-20 09:36:47

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpc8nmv1wr/.git with 6,141 files  
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
> 33784 prompt tokens, 52 completion tokens, $0.169700 cost  

To address the issue with the two-digit year check in `django.utils.http.parse_http_date`, the most likely file that needs to be edited is:

- `django/utils/http.py`

Please add this file to the chat so I can provide the necessary changes.

> django/utils/http.py  
> Add these files to the chat? yes  
> 7887 prompt tokens, 167 completion tokens, $0.041940 cost  

To address the issue with the two-digit year check in `django.utils.http.parse_http_date`, we need to modify the logic to compare the year against the current year and adjust accordingly.

Here are the changes:

django/utils/http.py
```python
<<<<<<< SEARCH
            if year < 70:
                year += 2000
            else:
                year += 1900
=======
            current_year = datetime.datetime.now().year
            current_century = current_year // 100 * 100
            if year + current_century > current_year + 50:
                year += current_century - 100
            else:
                year += current_century
>>>>>>> REPLACE
```

This change ensures that the two-digit year is interpreted correctly based on the current year, as specified by RFC 7231.

> Applied edit to django/utils/http.py  
