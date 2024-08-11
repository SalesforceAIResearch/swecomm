
# aider chat started at 2024-07-18 23:40:09

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpwb6c12mt/.git with 6,432 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Saving parent object after setting on child leads to data loss for parents with non-numeric primary key.  
#### Description  
#### 	   
#### 		(last modified by Charlie DeTar)  
#### 	   
#### Given a model with a foreign key relation to another model that has a non-auto CharField as its primary key:  
#### class Product(models.Model):  
#### 	sku = models.CharField(primary_key=True, max_length=50)  
#### class Order(models.Model):  
#### 	product = models.ForeignKey(Product, on_delete=models.CASCADE)  
#### If the relation is initialized on the parent with an empty instance that does not yet specify its primary key, and the primary key is subsequently defined, the parent does not "see" the primary key's change:  
#### with transaction.atomic():  
#### 	order = Order()  
#### 	order.product = Product()  
#### 	order.product.sku = "foo"  
#### 	order.product.save()  
#### 	order.save()  
#### 	assert Order.objects.filter(product_id="").exists() # Succeeds, but shouldn't  
#### 	assert Order.objects.filter(product=order.product).exists() # Fails  
#### Instead of product_id being populated with product.sku, it is set to emptystring. The foreign key constraint which would enforce the existence of a product with sku="" is deferred until the transaction commits. The transaction does correctly fail on commit with a ForeignKeyViolation due to the non-existence of a product with emptystring as its primary key.  
#### On the other hand, if the related unsaved instance is initialized with its primary key before assignment to the parent, it is persisted correctly:  
#### with transaction.atomic():  
#### 	order = Order()  
#### 	order.product = Product(sku="foo")  
#### 	order.product.save()  
#### 	order.save()  
#### 	assert Order.objects.filter(product=order.product).exists() # succeeds  
#### Committing the transaction also succeeds.  
#### This may have something to do with how the Order.product_id field is handled at assignment, together with something about handling fetching of auto vs non-auto primary keys from the related instance.  
> 34108 prompt tokens, 125 completion tokens, $0.172415 cost  

To address the issue described, we need to ensure that the parent object's primary key is correctly set before saving the child object. This likely involves changes to the model's save method or the way foreign keys are handled during assignment.

The files most likely to need changes are:
1. `django/db/models/fields/related.py` - This file handles the ForeignKey field logic.
2. `django/db/models/fields/related_descriptors.py` - This file manages the descriptors for related fields, which could be involved in setting the foreign key.

Please add these files to the chat so I can propose the necessary changes.

> django/db/models/fields/related.py  
> django/db/models/fields/related_descriptors.py  
> Add these files to the chat? yes  
> 28494 prompt tokens, 294 completion tokens, $0.146880 cost  

To address the issue, we need to ensure that the primary key of the related object is correctly set before saving the parent object. This involves modifying the `ForwardManyToOneDescriptor` class in `django/db/models/fields/related_descriptors.py` to handle the assignment of the foreign key correctly.

Here are the changes:

1. Modify the `__set__` method in `ForwardManyToOneDescriptor` to ensure the primary key is set before saving the parent object.

django/db/models/fields/related_descriptors.py
```python
<<<<<<< SEARCH
        # Set the values of the related field.
        else:
            for lh_field, rh_field in self.field.related_fields:
                setattr(instance, lh_field.attname, getattr(value, rh_field.attname))
=======
        # Ensure the primary key is set before saving the parent object.
        else:
            if value._state.adding and value._meta.pk.attname in value.__dict__:
                value.save()
            for lh_field, rh_field in self.field.related_fields:
                setattr(instance, lh_field.attname, getattr(value, rh_field.attname))
>>>>>>> REPLACE
```

This change ensures that if the related object is new and its primary key is set, it will be saved before setting the foreign key on the parent object. This prevents the issue of the foreign key being set to an empty string.

Please review and let me know if you need any further changes.

> Applied edit to django/db/models/fields/related_descriptors.py  
>   
> Test Script:  ./tests/runtests.py --verbosity 2 many_to_one.models many_to_one.tests;  
> [django__django__4.0] [django__django-13964] Command: ./tests/runtests.py --verbosity 2 many_to_one.models many_to_one.tests   
> [django__django__4.0] [django__django-13964] Subprocess args: {"cwd": "/opt/django__django", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [django__django__4.0] [django__django-13964] Std. Output:  
> Testing against Django installed in '/opt/django__django/django' with up to 16 processes  
> Importing application many_to_one  
> Skipping setup of unused database(s): other.  
> Operations to perform:  
>   Synchronize unmigrated apps: auth, contenttypes, many_to_one, messages, sessions, staticfiles  
>   Apply all migrations: admin, sites  
> Synchronizing apps without migrations:  
>   Creating tables...  
>     Creating table django_content_type  
>     Creating table auth_permission  
>     Creating table auth_group  
>     Creating table auth_user  
>     Creating table django_session  
>     Creating table many_to_one_reporter  
>     Creating table many_to_one_article  
>     Creating table many_to_one_country  
>     Creating table many_to_one_city  
>     Creating table many_to_one_district  
>     Creating table many_to_one_first  
>     Creating table many_to_one_second  
>     Creating table many_to_one_third  
>     Creating table many_to_one_parent  
>     Creating table many_to_one_child  
>     Creating table many_to_one_childnullableparent  
>     Creating table many_to_one_tofieldchild  
>     Creating table many_to_one_category  
>     Creating table many_to_one_record  
>     Creating table many_to_one_relation  
>     Creating table many_to_one_school  
>     Creating table many_to_one_student  
>     Running deferred SQL...  
> Running migrations:  
>   Applying admin.0001_initial... OK  
>   Applying admin.0002_logentry_remove_auto_add... OK  
>   Applying admin.0003_logentry_add_action_flag_choices... OK  
>   Applying sites.0001_initial... OK  
>   Applying sites.0002_alter_domain_unique... OK  
> Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> System check identified no issues (0 silenced).  
> test_add (many_to_one.tests.ManyToOneTests) ... ok  
> test_add_after_prefetch (many_to_one.tests.ManyToOneTests) ... ok  
> test_add_remove_set_by_pk_raises (many_to_one.tests.ManyToOneTests) ... ok  
> test_add_then_remove_after_prefetch (many_to_one.tests.ManyToOneTests) ... ok  
> test_assign (many_to_one.tests.ManyToOneTests) ... ok  
> test_assign_fk_id_none (many_to_one.tests.ManyToOneTests) ... ok  
> test_assign_fk_id_value (many_to_one.tests.ManyToOneTests) ... ok  
> test_cached_foreign_key_with_to_field_not_cleared_by_save (many_to_one.tests.ManyToOneTests) ... ok  
> test_cached_relation_invalidated_on_save (many_to_one.tests.ManyToOneTests)  
> Model.save() invalidates stale ForeignKey relations after a primary key ... ok  
> test_clear_after_prefetch (many_to_one.tests.ManyToOneTests) ... ok  
> test_create (many_to_one.tests.ManyToOneTests) ... ok  
> test_create_relation_with_gettext_lazy (many_to_one.tests.ManyToOneTests) ... ok  
> test_deepcopy_and_circular_references (many_to_one.tests.ManyToOneTests) ... ok  
> test_delete (many_to_one.tests.ManyToOneTests) ... ok  
> test_explicit_fk (many_to_one.tests.ManyToOneTests) ... ok  
> test_fk_assignment_and_related_object_cache (many_to_one.tests.ManyToOneTests) ... FAIL  
> test_fk_instantiation_outside_model (many_to_one.tests.ManyToOneTests) ... ok  
> test_fk_to_bigautofield (many_to_one.tests.ManyToOneTests) ... ok  
> test_fk_to_smallautofield (many_to_one.tests.ManyToOneTests) ... ok  
> test_get (many_to_one.tests.ManyToOneTests) ... ok  
> test_hasattr_related_object (many_to_one.tests.ManyToOneTests) ... ok  
> test_manager_class_caching (many_to_one.tests.ManyToOneTests) ... ok  
> test_multiple_foreignkeys (many_to_one.tests.ManyToOneTests) ... ok  
> test_related_object (many_to_one.tests.ManyToOneTests) ... ok  
> test_relation_unsaved (many_to_one.tests.ManyToOneTests) ... ok  
> test_remove_after_prefetch (many_to_one.tests.ManyToOneTests) ... ok  
> test_reverse_assignment_deprecation (many_to_one.tests.ManyToOneTests) ... ok  
> test_reverse_foreign_key_instance_to_field_caching (many_to_one.tests.ManyToOneTests) ... ok  
> test_reverse_selects (many_to_one.tests.ManyToOneTests) ... ok  
> test_save_nullable_fk_after_parent (many_to_one.tests.ManyToOneTests) ... ok  
> test_save_nullable_fk_after_parent_with_to_field (many_to_one.tests.ManyToOneTests) ... ok  
> test_select_related (many_to_one.tests.ManyToOneTests) ... ok  
> test_selects (many_to_one.tests.ManyToOneTests) ... ok  
> test_set (many_to_one.tests.ManyToOneTests) ... ok  
> test_set_after_prefetch (many_to_one.tests.ManyToOneTests) ... ok  
> test_values_list_exception (many_to_one.tests.ManyToOneTests) ... ok  
>   
> ======================================================================  
> FAIL: test_fk_assignment_and_related_object_cache (many_to_one.tests.ManyToOneTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/tests/many_to_one/tests.py", line 522, in test_fk_assignment_and_related_object_cache  
>     Child.objects.create(parent=p)  
>   File "/opt/pyenv/versions/3.8.19/lib/python3.8/contextlib.py", line 120, in __exit__  
>     next(self.gen)  
>   File "/opt/django__django/django/test/testcases.py", line 692, in _assert_raises_or_warns_cm  
>     yield cm  
> AssertionError: ValueError not raised  
>   
> ----------------------------------------------------------------------  
> Ran 36 tests in 0.194s  
>   
> FAILED (failures=1)  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
>    
> [django__django__4.0] [django__django-13964] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [django__django__4.0] [django__django-13964] Test script run successful   
> Attempt to fix test errors? yes  
> 30254 prompt tokens, 302 completion tokens, $0.155800 cost  

To address the issue and ensure that the primary key of the related object is correctly set before saving the parent object, we need to make sure that the related object is saved before setting the foreign key on the parent object. This involves modifying the `ForwardManyToOneDescriptor` class in `django/db/models/fields/related_descriptors.py`.

Here are the changes:

1. Modify the `__set__` method in `ForwardManyToOneDescriptor` to ensure the primary key is set before saving the parent object.

django/db/models/fields/related_descriptors.py
```python
<<<<<<< SEARCH
        # Set the values of the related field.
        else:
            for lh_field, rh_field in self.field.related_fields:
                setattr(instance, lh_field.attname, getattr(value, rh_field.attname))
=======
        # Ensure the primary key is set before saving the parent object.
        else:
            if value._state.adding and value._meta.pk.attname in value.__dict__:
                value.save()
            for lh_field, rh_field in self.field.related_fields:
                setattr(instance, lh_field.attname, getattr(value, rh_field.attname))
>>>>>>> REPLACE
```

This change ensures that if the related object is new and its primary key is set, it will be saved before setting the foreign key on the parent object. This prevents the issue of the foreign key being set to an empty string.

Please review and let me know if you need any further changes.

> The LLM did not conform to the edit format.  
> For more info see: https://aider.chat/docs/faq.html#aider-isnt-editing-my-files  
> # 1 SEARCH/REPLACE block failed to match!  
>   
> ## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in django/db/models/fields/related_descriptors.py  
> <<<<<<< SEARCH  
>         # Set the values of the related field.  
>         else:  
>             for lh_field, rh_field in self.field.related_fields:  
>                 setattr(instance, lh_field.attname, getattr(value, rh_field.attname))  
> =======  
>         # Ensure the primary key is set before saving the parent object.  
>         else:  
>             if value._state.adding and value._meta.pk.attname in value.__dict__:  
>                 value.save()  
>             for lh_field, rh_field in self.field.related_fields:  
>                 setattr(instance, lh_field.attname, getattr(value, rh_field.attname))  
> >>>>>>> REPLACE  
>   
> Are you sure you need this SEARCH/REPLACE block?  
> The REPLACE lines are already in django/db/models/fields/related_descriptors.py!  
>   
> The SEARCH section must exactly match an existing block of lines including all white space, comments, indentation, docstrings, etc  
> 30780 prompt tokens, 941 completion tokens, $0.168015 cost  

Let's ensure we have the correct block of code to modify. I'll provide a more precise *SEARCH/REPLACE* block for the `ForwardManyToOneDescriptor` class in `django/db/models/fields/related_descriptors.py`.

Here is the updated *SEARCH/REPLACE* block:

django/db/models/fields/related_descriptors.py
```python
<<<<<<< SEARCH
        # If we're setting the value of a OneToOneField to None, we need to clear
        # out the cache on any old related object. Otherwise, deleting the
        # previously-related object will also cause this object to be deleted,
        # which is wrong.
        if value is None:
            # Look up the previously-related object, which may still be available
            # since we've not yet cleared out the related field.
            # Use the cache directly, instead of the accessor; if we haven't
            # populated the cache, then we don't care - we're only accessing
            # the object to invalidate the accessor cache, so there's no
            # need to populate the cache just to expire it again.
            related = self.field.get_cached_value(instance, default=None)

            # If we've got an old related object, we need to clear out its
            # cache. This cache also might not exist if the related object
            # hasn't been accessed yet.
            if related is not None:
                self.field.remote_field.set_cached_value(related, None)

            for lh_field, rh_field in self.field.related_fields:
                setattr(instance, lh_field.attname, None)

        # Set the values of the related field.
        else:
            for lh_field, rh_field in self.field.related_fields:
                setattr(instance, lh_field.attname, getattr(value, rh_field.attname))

        # Set the related instance cache used by __get__ to avoid an SQL query
        # when accessing the attribute we just set.
        self.field.set_cached_value(instance, value)

        # If this is a one-to-one relation, set the reverse accessor cache on
        # the related object to the current instance to avoid an extra SQL
        # query if it's accessed later on.
        if value is not None and not self.field.remote_field.multiple:
            self.field.remote_field.set_cached_value(value, instance)
=======
        # If we're setting the value of a OneToOneField to None, we need to clear
        # out the cache on any old related object. Otherwise, deleting the
        # previously-related object will also cause this object to be deleted,
        # which is wrong.
        if value is None:
            # Look up the previously-related object, which may still be available
            # since we've not yet cleared out the related field.
            # Use the cache directly, instead of the accessor; if we haven't
            # populated the cache, then we don't care - we're only accessing
            # the object to invalidate the accessor cache, so there's no
            # need to populate the cache just to expire it again.
            related = self.field.get_cached_value(instance, default=None)

            # If we've got an old related object, we need to clear out its
            # cache. This cache also might not exist if the related object
            # hasn't been accessed yet.
            if related is not None:
                self.field.remote_field.set_cached_value(related, None)

            for lh_field, rh_field in self.field.related_fields:
                setattr(instance, lh_field.attname, None)

        # Ensure the primary key is set before saving the parent object.
        else:
            if value._state.adding and value._meta.pk.attname in value.__dict__:
                value.save()
            for lh_field, rh_field in self.field.related_fields:
                setattr(instance, lh_field.attname, getattr(value, rh_field.attname))

        # Set the related instance cache used by __get__ to avoid an SQL query
        # when accessing the attribute we just set.
        self.field.set_cached_value(instance, value)

        # If this is a one-to-one relation, set the reverse accessor cache on
        # the related object to the current instance to avoid an extra SQL
        # query if it's accessed later on.
        if value is not None and not self.field.remote_field.multiple:
            self.field.remote_field.set_cached_value(value, instance)
>>>>>>> REPLACE
```

This should ensure that the primary key is set before saving the parent object, preventing the issue of the foreign key being set to an empty string. Please review and let me know if you need any further changes.

> The LLM did not conform to the edit format.  
> For more info see: https://aider.chat/docs/faq.html#aider-isnt-editing-my-files  
> # 1 SEARCH/REPLACE block failed to match!  
>   
> ## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in django/db/models/fields/related_descriptors.py  
> <<<<<<< SEARCH  
>         # If we're setting the value of a OneToOneField to None, we need to clear  
>         # out the cache on any old related object. Otherwise, deleting the  
>         # previously-related object will also cause this object to be deleted,  
>         # which is wrong.  
>         if value is None:  
>             # Look up the previously-related object, which may still be available  
>             # since we've not yet cleared out the related field.  
>             # Use the cache directly, instead of the accessor; if we haven't  
>             # populated the cache, then we don't care - we're only accessing  
>             # the object to invalidate the accessor cache, so there's no  
>             # need to populate the cache just to expire it again.  
>             related = self.field.get_cached_value(instance, default=None)  
>   
>             # If we've got an old related object, we need to clear out its  
>             # cache. This cache also might not exist if the related object  
>             # hasn't been accessed yet.  
>             if related is not None:  
>                 self.field.remote_field.set_cached_value(related, None)  
>   
>             for lh_field, rh_field in self.field.related_fields:  
>                 setattr(instance, lh_field.attname, None)  
>   
>         # Set the values of the related field.  
>         else:  
>             for lh_field, rh_field in self.field.related_fields:  
>                 setattr(instance, lh_field.attname, getattr(value, rh_field.attname))  
>   
>         # Set the related instance cache used by __get__ to avoid an SQL query  
>         # when accessing the attribute we just set.  
>         self.field.set_cached_value(instance, value)  
>   
>         # If this is a one-to-one relation, set the reverse accessor cache on  
>         # the related object to the current instance to avoid an extra SQL  
>         # query if it's accessed later on.  
>         if value is not None and not self.field.remote_field.multiple:  
>             self.field.remote_field.set_cached_value(value, instance)  
> =======  
>         # If we're setting the value of a OneToOneField to None, we need to clear  
>         # out the cache on any old related object. Otherwise, deleting the  
>         # previously-related object will also cause this object to be deleted,  
>         # which is wrong.  
>         if value is None:  
>             # Look up the previously-related object, which may still be available  
>             # since we've not yet cleared out the related field.  
>             # Use the cache directly, instead of the accessor; if we haven't  
>             # populated the cache, then we don't care - we're only accessing  
>             # the object to invalidate the accessor cache, so there's no  
>             # need to populate the cache just to expire it again.  
>             related = self.field.get_cached_value(instance, default=None)  
>   
>             # If we've got an old related object, we need to clear out its  
>             # cache. This cache also might not exist if the related object  
>             # hasn't been accessed yet.  
>             if related is not None:  
>                 self.field.remote_field.set_cached_value(related, None)  
>   
>             for lh_field, rh_field in self.field.related_fields:  
>                 setattr(instance, lh_field.attname, None)  
>   
>         # Ensure the primary key is set before saving the parent object.  
>         else:  
>             if value._state.adding and value._meta.pk.attname in value.__dict__:  
>                 value.save()  
>             for lh_field, rh_field in self.field.related_fields:  
>                 setattr(instance, lh_field.attname, getattr(value, rh_field.attname))  
>   
>         # Set the related instance cache used by __get__ to avoid an SQL query  
>         # when accessing the attribute we just set.  
>         self.field.set_cached_value(instance, value)  
>   
>         # If this is a one-to-one relation, set the reverse accessor cache on  
>         # the related object to the current instance to avoid an extra SQL  
>         # query if it's accessed later on.  
>         if value is not None and not self.field.remote_field.multiple:  
>             self.field.remote_field.set_cached_value(value, instance)  
> >>>>>>> REPLACE  
>   
> Did you mean to match some of these actual lines from django/db/models/fields/related_descriptors.py?  
>   
> ```  
>                 value._state.db = router.db_for_write(value.__class__, instance=instance)  
>             if not router.allow_relation(value, instance):  
>                 raise ValueError('Cannot assign "%r": the current database router prevents this relation.' % value)  
>   
>         remote_field = self.field.remote_field  
>         # If we're setting the value of a OneToOneField to None, we need to clear  
>         # out the cache on any old related object. Otherwise, deleting the  
>         # previously-related object will also cause this object to be deleted,  
>         # which is wrong.  
>         if value is None:  
>             # Look up the previously-related object, which may still be available  
>             # since we've not yet cleared out the related field.  
>             # Use the cache directly, instead of the accessor; if we haven't  
>             # populated the cache, then we don't care - we're only accessing  
>             # the object to invalidate the accessor cache, so there's no  
>             # need to populate the cache just to expire it again.  
>             related = self.field.get_cached_value(instance, default=None)  
>   
>             # If we've got an old related object, we need to clear out its  
>             # cache. This cache also might not exist if the related object  
>             # hasn't been accessed yet.  
>             if related is not None:  
>                 remote_field.set_cached_value(related, None)  
>   
>             for lh_field, rh_field in self.field.related_fields:  
>                 setattr(instance, lh_field.attname, None)  
>   
>         # Ensure the primary key is set before saving the parent object.  
>         else:  
>             if value._state.adding and value._meta.pk.attname in value.__dict__:  
>                 value.save()  
>             for lh_field, rh_field in self.field.related_fields:  
>                 setattr(instance, lh_field.attname, getattr(value, rh_field.attname))  
>   
>         # Set the related instance cache used by __get__ to avoid an SQL query  
>         # when accessing the attribute we just set.  
>         self.field.set_cached_value(instance, value)  
>   
>         # If this is a one-to-one relation, set the reverse accessor cache on  
>         # the related object to the current instance to avoid an extra SQL  
>         # query if it's accessed later on.  
>         if value is not None and not remote_field.multiple:  
>             remote_field.set_cached_value(value, instance)  
>   
>     def __reduce__(self):  
>         """  
> ```  
>   
> The SEARCH section must exactly match an existing block of lines including all white space, comments, indentation, docstrings, etc  
> 33126 prompt tokens, 194 completion tokens, $0.168540 cost  

Thank you for providing the additional context. Let's ensure we have the correct block of code to modify. I'll provide a more precise *SEARCH/REPLACE* block for the `ForwardManyToOneDescriptor` class in `django/db/models/fields/related_descriptors.py`.

Here is the updated *SEARCH/REPLACE* block:

django/db/models/fields/related_descriptors.py
```python
<<<<<<< SEARCH
        remote_field = self.field.remote_field
=======
        remote_field = self.field.remote_field
        # Ensure the primary key is set before saving the parent object.
        if value is not None and value._state.adding and value._meta.pk.attname in value.__dict__:
            value.save()
>>>>>>> REPLACE
```

This should ensure that the primary key is set before saving the parent object, preventing the issue of the foreign key being set to an empty string. Please review and let me know if you need any further changes.

> Applied edit to django/db/models/fields/related_descriptors.py  
>  
> # Fix any errors below, if possible.  
>  
> ## Running: flake8 --select=E9,F821,F823,F831,F406,F407,F701,F702,F704,F706 --show-source --isolated django/db/models/fields/related_descriptors.py  
>  
> django/db/models/fields/related_descriptors.py:131:12: F821 undefined name 'value'  
> if value is not None and value._state.adding and value._meta.pk.attname in value.__dict__:  
> ^  
> django/db/models/fields/related_descriptors.py:131:34: F821 undefined name 'value'  
> if value is not None and value._state.adding and value._meta.pk.attname in value.__dict__:  
> ^  
> django/db/models/fields/related_descriptors.py:131:58: F821 undefined name 'value'  
> if value is not None and value._state.adding and value._meta.pk.attname in value.__dict__:  
> ^  
> django/db/models/fields/related_descriptors.py:131:84: F821 undefined name 'value'  
> if value is not None and value._state.adding and value._meta.pk.attname in value.__dict__:  
> ^  
> django/db/models/fields/related_descriptors.py:132:13: F821 undefined name 'value'  
> value.save()  
> ^  
>  
> ## See relevant lines below marked with █.  
>  
> django/db/models/fields/related_descriptors.py:  
> ...⋮...  
> 82│class ForwardManyToOneDescriptor:  
> 83│    """  
> 84│    Accessor to the related object on the forward side of a many-to-one or  
> 85│    one-to-one (via ForwardOneToOneDescriptor subclass) relation.  
> 86│  
> 87│    In the example::  
> 88│  
> 89│        class Child(Model):  
> 90│            parent = ForeignKey(Parent, related_name='children')  
> 91│  
> 92│    ``Child.parent`` is a ``ForwardManyToOneDescriptor`` instance.  
> ...⋮...  
> 120│    def get_prefetch_queryset(self, instances, queryset=None):  
> 121│        if queryset is None:  
> ...⋮...  
> 128│        related_field = self.field.foreign_related_fields[0]  
> 129│        remote_field = self.field.remote_field  
> 130│        # Ensure the primary key is set before saving the parent object.  
> 131█        if value is not None and value._state.adding and value._meta.pk.attname in value.__dict__:  
> 132█            value.save()  
> 133│  
> 134│        # FIXME: This will need to be revisited when we introduce support for  
> 135│        # composite fields. In the meantime we take this practical approach to  
> ...⋮...  
>  
> Attempt to fix lint errors? yes  
> Only 4 reflections allowed, stopping.  
