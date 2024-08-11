
# aider chat started at 2024-07-20 16:02:23

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp3f898rw4/.git with 6,148 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Prevent using __isnull lookup with non-boolean value.  
#### Description  
#### 	   
#### 		(last modified by Mariusz Felisiak)  
#### 	   
#### __isnull should not allow for non-boolean values. Using truthy/falsey doesn't promote INNER JOIN to an OUTER JOIN but works fine for a simple queries. Using non-boolean values is ​undocumented and untested. IMO we should raise an error for non-boolean values to avoid confusion and for consistency.  
> 33815 prompt tokens, 56 completion tokens, $0.169915 cost  

To implement the change to prevent using `__isnull` lookup with non-boolean values, the most likely file that will need to be edited is:

- `django/db/models/sql/query.py`

Please add this file to the chat so I can proceed with the necessary changes.

> django/db/models/sql/query.py  
> Add these files to the chat? yes  
> 25354 prompt tokens, 345 completion tokens, $0.131945 cost  

To implement the change to prevent using `__isnull` lookup with non-boolean values, we need to modify the `build_lookup` method in `django/db/models/sql/query.py`. Specifically, we need to add a check to ensure that the value for `__isnull` is a boolean.

Here are the necessary changes:

django/db/models/sql/query.py
```python
<<<<<<< SEARCH
        # Interpret '__exact=None' as the sql 'is NULL'; otherwise, reject all
        # uses of None as a query value unless the lookup supports it.
        if lookup.rhs is None and not lookup.can_use_none_as_rhs:
            if lookup_name not in ('exact', 'iexact'):
                raise ValueError("Cannot use None as a query value")
            return lhs.get_lookup('isnull')(lhs, True)
=======
        # Interpret '__exact=None' as the sql 'is NULL'; otherwise, reject all
        # uses of None as a query value unless the lookup supports it.
        if lookup.rhs is None and not lookup.can_use_none_as_rhs:
            if lookup_name not in ('exact', 'iexact'):
                raise ValueError("Cannot use None as a query value")
            return lhs.get_lookup('isnull')(lhs, True)

        # Ensure '__isnull' lookup uses a boolean value.
        if lookup_name == 'isnull' and not isinstance(lookup.rhs, bool):
            raise ValueError("The '__isnull' lookup value must be a boolean.")
>>>>>>> REPLACE
```

This change ensures that the `__isnull` lookup only accepts boolean values, raising a `ValueError` if a non-boolean value is provided.

> Applied edit to django/db/models/sql/query.py  
