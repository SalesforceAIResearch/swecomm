
# aider chat started at 2024-07-19 09:11:38

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpquzw77uh/.git with 6,148 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Prevent using __isnull lookup with non-boolean value.  
#### Description  
#### 	   
#### 		(last modified by Mariusz Felisiak)  
#### 	   
#### __isnull should not allow for non-boolean values. Using truthy/falsey doesn't promote INNER JOIN to an OUTER JOIN but works fine for a simple queries. Using non-boolean values is ​undocumented and untested. IMO we should raise an error for non-boolean values to avoid confusion and for consistency.  
> 33754 prompt tokens, 56 completion tokens, $0.169610 cost  

To implement the change to prevent using `__isnull` lookup with non-boolean values, the most likely file that will need to be edited is:

- `django/db/models/sql/query.py`

Please add this file to the chat so I can proceed with the necessary changes.

> django/db/models/sql/query.py  
> Add these files to the chat? yes  
> 25291 prompt tokens, 367 completion tokens, $0.131960 cost  

To prevent using `__isnull` lookup with non-boolean values, we need to add a check in the `build_lookup` method of the `Query` class in `django/db/models/sql/query.py`.

Here are the necessary changes:

django/db/models/sql/query.py
```python
<<<<<<< SEARCH
        # For Oracle '' is equivalent to null. The check must be done at this
        # stage because join promotion can't be done in the compiler. Using
        # DEFAULT_DB_ALIAS isn't nice but it's the best that can be done here.
        # A similar thing is done in is_nullable(), too.
        if (connections[DEFAULT_DB_ALIAS].features.interprets_empty_strings_as_nulls and
                lookup_name == 'exact' and lookup.rhs == ''):
            return lhs.get_lookup('isnull')(lhs, True)
=======
        # Ensure __isnull lookup uses a boolean value.
        if lookup_name == 'isnull' and not isinstance(lookup.rhs, bool):
            raise ValueError("The '__isnull' lookup only accepts boolean values.")

        # For Oracle '' is equivalent to null. The check must be done at this
        # stage because join promotion can't be done in the compiler. Using
        # DEFAULT_DB_ALIAS isn't nice but it's the best that can be done here.
        # A similar thing is done in is_nullable(), too.
        if (connections[DEFAULT_DB_ALIAS].features.interprets_empty_strings_as_nulls and
                lookup_name == 'exact' and lookup.rhs == ''):
            return lhs.get_lookup('isnull')(lhs, True)
>>>>>>> REPLACE
```

This change ensures that the `__isnull` lookup only accepts boolean values and raises a `ValueError` if a non-boolean value is provided.

> Applied edit to django/db/models/sql/query.py  
