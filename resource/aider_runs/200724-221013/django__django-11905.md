
# aider chat started at 2024-07-20 19:31:40

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpj_xw7ke6/.git with 6,148 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Prevent using __isnull lookup with non-boolean value.  
#### Description  
#### 	   
#### 		(last modified by Mariusz Felisiak)  
#### 	   
#### __isnull should not allow for non-boolean values. Using truthy/falsey doesn't promote INNER JOIN to an OUTER JOIN but works fine for a simple queries. Using non-boolean values is ​undocumented and untested. IMO we should raise an error for non-boolean values to avoid confusion and for consistency.  
> 33750 prompt tokens, 42 completion tokens, $0.169380 cost  

To implement this change, the most likely file that will need to be edited is:

- `django/db/models/lookups.py`

Please add this file to the chat so I can proceed with the necessary changes.

> django/db/models/lookups.py  
> Add these files to the chat? yes  
> 8334 prompt tokens, 170 completion tokens, $0.044220 cost  

To ensure that the `__isnull` lookup only allows boolean values, we need to modify the `IsNull` class in `django/db/models/lookups.py` to raise an error if a non-boolean value is provided.

Here are the necessary changes:

1. Add a check in the `as_sql` method of the `IsNull` class to ensure the `rhs` is a boolean value.

django/db/models/lookups.py
```python
<<<<<<< SEARCH
        if self.rhs:
=======
        if not isinstance(self.rhs, bool):
            raise ValueError("The value for __isnull must be a boolean.")
        if self.rhs:
>>>>>>> REPLACE
```

This change will ensure that a `ValueError` is raised if a non-boolean value is used with the `__isnull` lookup.

> Applied edit to django/db/models/lookups.py  
