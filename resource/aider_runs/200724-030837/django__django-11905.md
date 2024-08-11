
# aider chat started at 2024-07-20 00:57:14

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpxd9z4nlg/.git with 6,148 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Prevent using __isnull lookup with non-boolean value.  
#### Description  
#### 	   
#### 		(last modified by Mariusz Felisiak)  
#### 	   
#### __isnull should not allow for non-boolean values. Using truthy/falsey doesn't promote INNER JOIN to an OUTER JOIN but works fine for a simple queries. Using non-boolean values is ​undocumented and untested. IMO we should raise an error for non-boolean values to avoid confusion and for consistency.  
> 33737 prompt tokens, 60 completion tokens, $0.169585 cost  

To implement the change to prevent using `__isnull` lookup with non-boolean values, we will likely need to modify the following file:

1. `django/db/models/sql/query.py`

Please add this file to the chat so I can provide the necessary *SEARCH/REPLACE* blocks.

> django/db/models/sql/query.py  
> Add these files to the chat? yes  
> 25432 prompt tokens, 318 completion tokens, $0.131930 cost  

To implement the change to prevent using `__isnull` lookup with non-boolean values, we need to:

1. Modify the `build_lookup` method to check if the `lookup_name` is `isnull` and ensure the `rhs` value is a boolean.
2. Raise a `ValueError` if the `rhs` value is not a boolean.

Here are the *SEARCH/REPLACE* blocks:

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
        if lookup_name == 'isnull' and not isinstance(lookup.rhs, bool):
            raise ValueError("The '__isnull' lookup only supports boolean values.")
        if lookup.rhs is None and not lookup.can_use_none_as_rhs:
            if lookup_name not in ('exact', 'iexact'):
                raise ValueError("Cannot use None as a query value")
            return lhs.get_lookup('isnull')(lhs, True)
>>>>>>> REPLACE
```

> Applied edit to django/db/models/sql/query.py  
