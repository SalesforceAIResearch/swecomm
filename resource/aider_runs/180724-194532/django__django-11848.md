
# aider chat started at 2024-07-18 16:58:17

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpy7oq3m8h/.git with 6,141 files  
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
> 33805 prompt tokens, 70 completion tokens, $0.170075 cost  

To address the issue with the `parse_http_date` function in `django/utils/http.py`, we will need to:

1. Update the logic to correctly interpret two-digit years based on the current year, as specified in RFC 7231.

Please add the file `django/utils/http.py` to the chat so I can provide the necessary changes.

> django/utils/http.py  
> Add these files to the chat? yes  
> 7975 prompt tokens, 132 completion tokens, $0.041855 cost  

Here is the updated `parse_http_date` function to correctly interpret two-digit years based on the current year, as specified in RFC 7231:

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
            current_year = datetime.datetime.utcnow().year
            current_century = current_year // 100 * 100
            year += current_century
            if year > current_year + 50:
                year -= 100
>>>>>>> REPLACE
```

> Applied edit to django/utils/http.py  
