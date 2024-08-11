
# aider chat started at 2024-07-19 12:27:59

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp7r212p1y/.git with 6,197 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Inherited model doesn't correctly order by "-pk" when specified on Parent.Meta.ordering  
#### Description  
#### 	  
#### Given the following model definition:  
#### from django.db import models  
#### class Parent(models.Model):  
#### 	class Meta:  
#### 		ordering = ["-pk"]  
#### class Child(Parent):  
#### 	pass  
#### Querying the Child class results in the following:  
#### >>> print(Child.objects.all().query)  
#### SELECT "myapp_parent"."id", "myapp_child"."parent_ptr_id" FROM "myapp_child" INNER JOIN "myapp_parent" ON ("myapp_child"."parent_ptr_id" = "myapp_parent"."id") ORDER BY "myapp_parent"."id" ASC  
#### The query is ordered ASC but I expect the order to be DESC.  
> 33881 prompt tokens, 49 completion tokens, $0.170140 cost  

To address the issue with the inherited model not correctly ordering by `-pk`, we will likely need to modify the following file:

- `django/db/models/base.py`

Please add this file to the chat so I can provide the necessary changes.

> django/db/models/base.py  
> Add these files to the chat? yes  
> 19087 prompt tokens, 240 completion tokens, $0.099035 cost  

To fix the issue with the inherited model not correctly ordering by `-pk`, we need to ensure that the ordering specified in the parent model's `Meta` class is correctly inherited and applied in the child model.

We will modify the `_prepare` method in the `ModelBase` class to ensure that the ordering is correctly inherited and applied.

Here are the necessary changes:

django/db/models/base.py
```python
<<<<<<< SEARCH
                if not hasattr(meta, 'ordering'):
                    new_class._meta.ordering = base_meta.ordering
                if not hasattr(meta, 'get_latest_by'):
                    new_class._meta.get_latest_by = base_meta.get_latest_by
=======
                if not hasattr(meta, 'ordering') or not meta.ordering:
                    new_class._meta.ordering = base_meta.ordering
                if not hasattr(meta, 'get_latest_by') or not meta.get_latest_by:
                    new_class._meta.get_latest_by = base_meta.get_latest_by
>>>>>>> REPLACE
```

This change ensures that the ordering specified in the parent model's `Meta` class is correctly inherited and applied in the child model, even if the ordering is specified as `-pk`.

> Applied edit to django/db/models/base.py  
