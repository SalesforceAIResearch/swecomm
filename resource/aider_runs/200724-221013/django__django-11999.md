
# aider chat started at 2024-07-20 18:21:41

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp5_9nosxi/.git with 6,148 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Cannot override get_FOO_display() in Django 2.2+.  
#### Description  
#### 	  
#### I cannot override the get_FIELD_display function on models since version 2.2. It works in version 2.1.  
#### Example:  
#### class FooBar(models.Model):  
#### 	foo_bar = models.CharField(_("foo"), choices=[(1, 'foo'), (2, 'bar')])  
#### 	def __str__(self):  
#### 		return self.get_foo_bar_display() # This returns 'foo' or 'bar' in 2.2, but 'something' in 2.1  
#### 	def get_foo_bar_display(self):  
#### 		return "something"  
#### What I expect is that I should be able to override this function.  
> 33772 prompt tokens, 128 completion tokens, $0.170780 cost  

To address the issue of overriding the `get_FIELD_display` method in Django 2.2+, we will likely need to modify the Django model's method resolution order or the way the method is generated.

The most likely files to need changes are:
1. `django/db/models/base.py` - This file contains the base model class where the `get_FIELD_display` method is defined.
2. `django/db/models/fields/__init__.py` - This file contains the field definitions and might include the logic for generating the `get_FIELD_display` method.

Please add these files to the chat so I can propose the necessary changes.

> django/db/models/fields/__init__.py  
> django/db/models/base.py  
> Add these files to the chat? yes  
> 36775 prompt tokens, 188 completion tokens, $0.186695 cost  

To allow overriding the `get_FIELD_display` method, we need to modify the `contribute_to_class` method in `django/db/models/fields/__init__.py` to check if the method already exists before setting it.

Here are the necessary changes:

django/db/models/fields/__init__.py
```python
<<<<<<< SEARCH
        if self.choices is not None:
            setattr(cls, 'get_%s_display' % self.name,
                    partialmethod(cls._get_FIELD_display, field=self))
=======
        if self.choices is not None and not hasattr(cls, 'get_%s_display' % self.name):
            setattr(cls, 'get_%s_display' % self.name,
                    partialmethod(cls._get_FIELD_display, field=self))
>>>>>>> REPLACE
```

This change ensures that the `get_FIELD_display` method is only set if it doesn't already exist, allowing you to override it in your model.

> Applied edit to django/db/models/fields/__init__.py  
