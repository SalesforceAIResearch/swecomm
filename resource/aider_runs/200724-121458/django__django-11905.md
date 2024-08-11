
# aider chat started at 2024-07-20 11:43:31

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp1jvjf_cy/.git with 6,148 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Prevent using __isnull lookup with non-boolean value.  
#### Description  
#### 	   
#### 		(last modified by Mariusz Felisiak)  
#### 	   
#### __isnull should not allow for non-boolean values. Using truthy/falsey doesn't promote INNER JOIN to an OUTER JOIN but works fine for a simple queries. Using non-boolean values is ​undocumented and untested. IMO we should raise an error for non-boolean values to avoid confusion and for consistency.  
> 33706 prompt tokens, 56 completion tokens, $0.169370 cost  

To implement the change to prevent using `__isnull` lookup with non-boolean values, the most likely file that will need to be edited is:

- `django/db/models/sql/query.py`

Please add this file to the chat so I can proceed with the necessary changes.

> django/db/models/sql/query.py  
> Add these files to the chat? yes  
> 25404 prompt tokens, 219 completion tokens, $0.130305 cost  

To implement the change to prevent using `__isnull` lookup with non-boolean values, we need to modify the `build_lookup` method in `django/db/models/sql/query.py`. Specifically, we need to add a check to ensure that the value for `__isnull` is a boolean.

Here are the *SEARCH/REPLACE* blocks:

django/db/models/sql/query.py
```python
<<<<<<< SEARCH
        # Interpret '__exact=None' as the sql 'is NULL'; otherwise, reject all
=======
        # Interpret '__isnull' with non-boolean value as an error.
        if lookup_name == 'isnull' and not isinstance(lookup.rhs, bool):
            raise ValueError("The value for '__isnull' must be a boolean.")
        # Interpret '__exact=None' as the sql 'is NULL'; otherwise, reject all
>>>>>>> REPLACE
```

This change ensures that if a non-boolean value is used with the `__isnull` lookup, a `ValueError` will be raised, preventing the query from being executed.

> Applied edit to django/db/models/sql/query.py  
