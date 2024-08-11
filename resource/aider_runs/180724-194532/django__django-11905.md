
# aider chat started at 2024-07-18 16:16:05

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp19w1hvmp/.git with 6,148 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Prevent using __isnull lookup with non-boolean value.  
#### Description  
#### 	   
#### 		(last modified by Mariusz Felisiak)  
#### 	   
#### __isnull should not allow for non-boolean values. Using truthy/falsey doesn't promote INNER JOIN to an OUTER JOIN but works fine for a simple queries. Using non-boolean values is ​undocumented and untested. IMO we should raise an error for non-boolean values to avoid confusion and for consistency.  
> 33715 prompt tokens, 68 completion tokens, $0.169595 cost  

To implement the change to prevent using `__isnull` lookup with non-boolean values, we will likely need to modify the file that handles query lookups in Django. The most probable file for this change is:

- `django/db/models/lookups.py`

Please add this file to the chat so I can provide the necessary changes.

> django/db/models/lookups.py  
> Add these files to the chat? yes  
> 8373 prompt tokens, 166 completion tokens, $0.044355 cost  

To prevent using `__isnull` lookup with non-boolean values, we need to modify the `IsNull` class in `django/db/models/lookups.py`. We will add a check in the `as_sql` method to ensure that the `rhs` value is a boolean.

Here are the *SEARCH/REPLACE* blocks:

django/db/models/lookups.py
```python
<<<<<<< SEARCH
        sql, params = compiler.compile(self.lhs)
=======
        if not isinstance(self.rhs, bool):
            raise ValueError("The value for __isnull must be a boolean.")
        sql, params = compiler.compile(self.lhs)
>>>>>>> REPLACE
```

This change will ensure that a `ValueError` is raised if a non-boolean value is used with the `__isnull` lookup.

> Applied edit to django/db/models/lookups.py  
