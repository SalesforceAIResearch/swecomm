
# aider chat started at 2024-07-19 14:36:48

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpet22cq99/.git with 6,061 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Merging 3 or more media objects can throw unnecessary MediaOrderConflictWarnings  
#### Description  
#### 	  
#### Consider the following form definition, where text-editor-extras.js depends on text-editor.js but all other JS files are independent:  
#### from django import forms  
#### class ColorPicker(forms.Widget):  
#### 	class Media:  
#### 		js = ['color-picker.js']  
#### class SimpleTextWidget(forms.Widget):  
#### 	class Media:  
#### 		js = ['text-editor.js']  
#### class FancyTextWidget(forms.Widget):  
#### 	class Media:  
#### 		js = ['text-editor.js', 'text-editor-extras.js', 'color-picker.js']  
#### class MyForm(forms.Form):  
#### 	background_color = forms.CharField(widget=ColorPicker())  
#### 	intro = forms.CharField(widget=SimpleTextWidget())  
#### 	body = forms.CharField(widget=FancyTextWidget())  
#### Django should be able to resolve the JS files for the final form into the order text-editor.js, text-editor-extras.js, color-picker.js. However, accessing MyForm().media results in:  
#### /projects/django/django/forms/widgets.py:145: MediaOrderConflictWarning: Detected duplicate Media files in an opposite order:  
#### text-editor-extras.js  
#### text-editor.js  
####  MediaOrderConflictWarning,  
#### Media(css={}, js=['text-editor-extras.js', 'color-picker.js', 'text-editor.js'])  
#### The MediaOrderConflictWarning is a result of the order that the additions happen in: ColorPicker().media + SimpleTextWidget().media produces Media(css={}, js=['color-picker.js', 'text-editor.js']), which (wrongly) imposes the constraint that color-picker.js must appear before text-editor.js.  
#### The final result is particularly unintuitive here, as it's worse than the "naïve" result produced by Django 1.11 before order-checking was added (color-picker.js, text-editor.js, text-editor-extras.js), and the pair of files reported in the warning message seems wrong too (aren't color-picker.js and text-editor.js the wrong-ordered ones?)  
> 34145 prompt tokens, 49 completion tokens, $0.171460 cost  

To address the issue with `MediaOrderConflictWarning` when merging media objects, the most likely file that will need changes is:

- `django/forms/widgets.py`

Please add this file to the chat so I can proceed with the necessary changes.

> django/forms/widgets.py  
> Add these files to the chat? yes  
> 12214 prompt tokens, 588 completion tokens, $0.069890 cost  

To address the issue with `MediaOrderConflictWarning` when merging media objects, we need to modify the `merge` method in the `Media` class to handle the order of media files more intelligently. Specifically, we should avoid raising warnings when the order of independent files is not critical.

Here are the changes:

1. Modify the `merge` method to use a more sophisticated algorithm that can handle the order of media files better.
2. Ensure that the new algorithm only raises warnings when there is a genuine conflict in the order of dependent files.

django/forms/widgets.py
```python
<<<<<<< SEARCH
        # Start with a copy of list_1.
        combined_list = list(list_1)
        last_insert_index = len(list_1)
        # Walk list_2 in reverse, inserting each element into combined_list if
        # it doesn't already exist.
        for path in reversed(list_2):
            try:
                # Does path already exist in the list?
                index = combined_list.index(path)
            except ValueError:
                # Add path to combined_list since it doesn't exist.
                combined_list.insert(last_insert_index, path)
            else:
                if index > last_insert_index:
                    warnings.warn(
                        'Detected duplicate Media files in an opposite order:\n'
                        '%s\n%s' % (combined_list[last_insert_index], combined_list[index]),
                        MediaOrderConflictWarning,
                    )
                # path already exists in the list. Update last_insert_index so
                # that the following elements are inserted in front of this one.
                last_insert_index = index
        return combined_list
=======
        combined_list = []
        seen = set()
        conflict_pairs = set()

        for item in list_1 + list_2:
            if item not in seen:
                combined_list.append(item)
                seen.add(item)
            else:
                # Check for conflicts
                if item in list_1 and item in list_2:
                    index_1 = list_1.index(item)
                    index_2 = list_2.index(item)
                    for earlier_item in list_1[:index_1]:
                        if earlier_item in list_2[index_2 + 1:]:
                            conflict_pairs.add((earlier_item, item))
                    for later_item in list_1[index_1 + 1:]:
                        if later_item in list_2[:index_2]:
                            conflict_pairs.add((item, later_item))

        for pair in conflict_pairs:
            warnings.warn(
                'Detected duplicate Media files in an opposite order:\n'
                '%s\n%s' % pair,
                MediaOrderConflictWarning,
            )

        return combined_list
>>>>>>> REPLACE
```

This change will ensure that the `merge` method only raises warnings when there is a genuine conflict in the order of dependent files, and it will handle the order of independent files more intelligently.

> Applied edit to django/forms/widgets.py  
>   
> Test Script:  ./tests/runtests.py --verbosity 2 admin_inlines.tests admin_widgets.test_autocomplete_widget forms_tests.tests.test_media;  
> [django__django__3.0] [django__django-11019] Command: ./tests/runtests.py --verbosity 2 admin_inlines.tests admin_widgets.test_autocomplete_widget forms_tests.tests.test_media   
> [django__django__3.0] [django__django-11019] Subprocess args: {"cwd": "/opt/django__django", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [django__django__3.0] [django__django-11019] Std. Output:  
> Testing against Django installed in '/opt/django__django/django' with up to 16 processes  
> Importing application forms_tests  
> Importing application admin_inlines  
> Importing application admin_widgets  
> Skipping setup of unused database(s): other.  
> Operations to perform:  
>   Synchronize unmigrated apps: admin_inlines, admin_widgets, auth, contenttypes, forms_tests, messages, sessions, staticfiles  
>   Apply all migrations: admin, sites  
> Synchronizing apps without migrations:  
>   Creating tables...  
>     Creating table django_content_type  
>     Creating table auth_permission  
>     Creating table auth_group  
>     Creating table auth_user  
>     Creating table django_session  
>     Creating table forms_tests_boundarymodel  
>     Creating table forms_tests_defaults  
>     Creating table forms_tests_choicemodel  
>     Creating table forms_tests_choiceoptionmodel  
>     Creating table forms_tests_choicefieldmodel  
>     Creating table forms_tests_optionalmultichoicemodel  
>     Creating table forms_tests_filemodel  
>     Creating table forms_tests_article  
>     Creating table admin_inlines_parent  
>     Creating table admin_inlines_teacher  
>     Creating table admin_inlines_child  
>     Creating table admin_inlines_book  
>     Creating table admin_inlines_author  
>     Creating table admin_inlines_nonautopkbook  
>     Creating table admin_inlines_nonautopkbookchild  
>     Creating table admin_inlines_editablepkbook  
>     Creating table admin_inlines_holder  
>     Creating table admin_inlines_inner  
>     Creating table admin_inlines_holder2  
>     Creating table admin_inlines_inner2  
>     Creating table admin_inlines_holder3  
>     Creating table admin_inlines_inner3  
>     Creating table admin_inlines_holder4  
>     Creating table admin_inlines_inner4stacked  
>     Creating table admin_inlines_inner4tabular  
>     Creating table admin_inlines_person  
>     Creating table admin_inlines_outfititem  
>     Creating table admin_inlines_fashionista  
>     Creating table admin_inlines_shoppingweakness  
>     Creating table admin_inlines_titlecollection  
>     Creating table admin_inlines_title  
>     Creating table admin_inlines_poll  
>     Creating table admin_inlines_question  
>     Creating table admin_inlines_novel  
>     Creating table admin_inlines_chapter  
>     Creating table admin_inlines_footnote  
>     Creating table admin_inlines_capofamiglia  
>     Creating table admin_inlines_consigliere  
>     Creating table admin_inlines_sottocapo  
>     Creating table admin_inlines_readonlyinline  
>     Creating table admin_inlines_parentmodelwithcustompk  
>     Creating table admin_inlines_childmodel1  
>     Creating table admin_inlines_childmodel2  
>     Creating table admin_inlines_binarytree  
>     Creating table admin_inlines_lifeform  
>     Creating table admin_inlines_extraterrestrial  
>     Creating table admin_inlines_sighting  
>     Creating table admin_inlines_someparentmodel  
>     Creating table admin_inlines_somechildmodel  
>     Creating table admin_inlines_profilecollection  
>     Creating table admin_inlines_profile  
>     Creating table admin_widgets_member  
>     Creating table admin_widgets_band  
>     Creating table admin_widgets_album  
>     Creating table admin_widgets_inventory  
>     Creating table admin_widgets_event  
>     Creating table admin_widgets_car  
>     Creating table admin_widgets_cartire  
>     Creating table admin_widgets_honeycomb  
>     Creating table admin_widgets_bee  
>     Creating table admin_widgets_individual  
>     Creating table admin_widgets_company  
>     Creating table admin_widgets_advisor  
>     Creating table admin_widgets_student  
>     Creating table admin_widgets_school  
>     Creating table admin_widgets_profile  
>     Running deferred SQL...  
> Running migrations:  
>   Applying admin.0001_initial... OK  
>   Applying admin.0002_logentry_remove_auto_add... OK  
>   Applying admin.0003_logentry_add_action_flag_choices... OK  
>   Applying sites.0001_initial... OK  
>   Applying sites.0002_alter_domain_unique... OK  
> System check identified no issues (0 silenced).  
> Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> test_add_inlines (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_add_stackeds (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_alternating_rows (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_collapsed_inlines (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_delete_inlines (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_delete_stackeds (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_immutable_content_type (admin_inlines.tests.TestInlineAdminForm)  
> Regression for #9362 ... ok  
> test_combine_media (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_construction (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_form_media (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_html_safe (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_media_dsl (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_media_inheritance (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_media_inheritance_extends (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_media_inheritance_from_property (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_media_inheritance_single_type (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_media_property (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_media_property_parent_references (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_merge (forms_tests.tests.test_media.FormsMediaTestCase) ... test_merge_css_three_way (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_merge_js_three_way (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_merge_warning (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_multi_media (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_multi_widget (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_build_attrs (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_build_attrs_no_custom_class (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_build_attrs_not_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_build_attrs_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_get_url (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_media (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_render_options (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_render_options_not_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests)  
> Empty option isn't present if the field isn't required. ... ok  
> test_render_options_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests)  
> Empty option is present if the field isn't required. ... ok  
> test_deleting_inline_with_protected_delete_does_not_validate (admin_inlines.tests.TestInlineProtectedOnDelete) ... ok  
> test_all_inline_media (admin_inlines.tests.TestInlineMedia) ... ERROR  
> test_inline_media_only_base (admin_inlines.tests.TestInlineMedia) ... ERROR  
> test_inline_media_only_inline (admin_inlines.tests.TestInlineMedia) ... ERROR  
> test_inline_add_fk_add_perm (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_add_fk_noperm (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_add_m2m_add_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_add_m2m_noperm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_fk_add_change_perm (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_change_fk_add_perm (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_change_fk_all_perms (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_change_fk_change_del_perm (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_change_fk_change_perm (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_change_fk_noperm (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_change_m2m_add_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_m2m_change_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_m2m_noperm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_callable_lookup (admin_inlines.tests.TestInline)  
> Admin inline should invoke local callable when its name is listed in readonly_fields ... ok  
> test_can_delete (admin_inlines.tests.TestInline) ... ERROR  
> test_create_inlines_on_inherited_model (admin_inlines.tests.TestInline) ... ok  
> test_custom_form_tabular_inline_label (admin_inlines.tests.TestInline) ... ok  
> test_custom_form_tabular_inline_overridden_label (admin_inlines.tests.TestInline) ... ok  
> test_custom_get_extra_form (admin_inlines.tests.TestInline) ... ok  
> test_custom_min_num (admin_inlines.tests.TestInline) ... ok  
> test_custom_pk_shortcut (admin_inlines.tests.TestInline) ... ok  
> test_help_text (admin_inlines.tests.TestInline) ... ok  
> test_inline_editable_pk (admin_inlines.tests.TestInline) ... ok  
> test_inline_hidden_field_no_column (admin_inlines.tests.TestInline)  
> #18263 -- Make sure hidden fields don't get a column in tabular inlines ... ok  
> test_inline_nonauto_noneditable_inherited_pk (admin_inlines.tests.TestInline) ... ok  
> test_inline_nonauto_noneditable_pk (admin_inlines.tests.TestInline) ... ok  
> test_inline_primary (admin_inlines.tests.TestInline) ... ok  
> test_inlines_show_change_link_registered (admin_inlines.tests.TestInline)  
> Inlines `show_change_link` for registered models when enabled. ... ok  
> test_inlines_show_change_link_unregistered (admin_inlines.tests.TestInline)  
> Inlines `show_change_link` disabled for unregistered models. ... ok  
> test_localize_pk_shortcut (admin_inlines.tests.TestInline) ... ERROR  
> test_many_to_many_inlines (admin_inlines.tests.TestInline)  
> Autogenerated many-to-many inlines are displayed correctly (#13407) ... ok  
> test_min_num (admin_inlines.tests.TestInline) ... ok  
> test_no_parent_callable_lookup (admin_inlines.tests.TestInline)  
> Admin inline `readonly_field` shouldn't invoke parent ModelAdmin callable ... ok  
> test_non_related_name_inline (admin_inlines.tests.TestInline) ... ok  
> test_noneditable_inline_has_field_inputs (admin_inlines.tests.TestInline)  
> Inlines without change permission shows field inputs on add form. ... ok  
> test_readonly_stacked_inline_label (admin_inlines.tests.TestInline)  
> Bug #13174. ... ERROR  
> test_stacked_inline_edit_form_contains_has_original_class (admin_inlines.tests.TestInline) ... ERROR  
> test_tabular_inline_column_css_class (admin_inlines.tests.TestInline) ... ok  
> test_tabular_inline_show_change_link_false_registered (admin_inlines.tests.TestInline)  
> Inlines `show_change_link` disabled by default. ... ok  
> test_tabular_model_form_meta_readonly_field (admin_inlines.tests.TestInline) ... ok  
> test_tabular_non_field_errors (admin_inlines.tests.TestInline) ... ok  
>   
> ======================================================================  
> ERROR: test_combine_media (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 122, in test_combine_media  
>     str(w1.media + w2.media + w3.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_form_media (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 459, in test_form_media  
>     str(f1.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_media_dsl (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 72, in test_media_dsl  
>     str(w1.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_media_inheritance (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 226, in test_media_inheritance  
>     str(w7.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_media_inheritance_extends (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 319, in test_media_inheritance_extends  
>     str(w11.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_media_inheritance_single_type (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 348, in test_media_inheritance_single_type  
>     str(w12.media),  
>   File "/opt/django__django/django/forms/widgets.py", line 183, in _media  
>     m = m + base[medium]  
>   File "/opt/django__django/django/forms/widgets.py", line 114, in __getitem__  
>     return Media(**{str(name): getattr(self, '_' + name)})  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_media_property_parent_references (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 198, in test_media_property_parent_references  
>     str(w6.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_multi_media (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 373, in test_multi_media  
>     str(multimedia.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_multi_widget (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 417, in test_multi_widget  
>     str(mymulti.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_all_inline_media (admin_inlines.tests.TestInlineMedia)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 513, in test_all_inline_media  
>     response = self.client.get(change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_media_only_base (admin_inlines.tests.TestInlineMedia)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 487, in test_inline_media_only_base  
>     response = self.client.get(change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_media_only_inline (admin_inlines.tests.TestInlineMedia)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 495, in test_inline_media_only_inline  
>     response = self.client.get(change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_add_fk_add_perm (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 651, in test_inline_add_fk_add_perm  
>     response = self.client.get(reverse('admin:admin_inlines_holder2_add'))  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_add_fk_noperm (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 619, in test_inline_add_fk_noperm  
>     response = self.client.get(reverse('admin:admin_inlines_holder2_add'))  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_change_fk_add_change_perm (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 741, in test_inline_change_fk_add_change_perm  
>     response = self.client.get(self.holder_change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_change_fk_add_perm (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 688, in test_inline_change_fk_add_perm  
>     response = self.client.get(self.holder_change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_change_fk_all_perms (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 783, in test_inline_change_fk_all_perms  
>     response = self.client.get(self.holder_change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_change_fk_change_del_perm (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 760, in test_inline_change_fk_change_del_perm  
>     response = self.client.get(self.holder_change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_change_fk_change_perm (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 708, in test_inline_change_fk_change_perm  
>     response = self.client.get(self.holder_change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_change_fk_noperm (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 633, in test_inline_change_fk_noperm  
>     response = self.client.get(self.holder_change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_can_delete (admin_inlines.tests.TestInline)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 46, in test_can_delete  
>     reverse('admin:admin_inlines_holder_change', args=(self.holder.id,))  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_localize_pk_shortcut (admin_inlines.tests.TestInline)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/django/test/utils.py", line 371, in inner  
>     return func(*args, **kwargs)  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 257, in test_localize_pk_shortcut  
>     response = self.client.get(reverse('admin:admin_inlines_holder_change', args=(holder.id,)))  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_readonly_stacked_inline_label (admin_inlines.tests.TestInline)  
> Bug #13174.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 58, in test_readonly_stacked_inline_label  
>     reverse('admin:admin_inlines_holder_change', args=(holder.id,))  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_stacked_inline_edit_form_contains_has_original_class (admin_inlines.tests.TestInline)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 421, in test_stacked_inline_edit_form_contains_has_original_class  
>     response = self.client.get(reverse('admin:admin_inlines_holder_change', args=(holder.pk,)))  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> FAIL: test_merge (forms_tests.tests.test_media.FormsMediaTestCase) [<object object at 0x7f5e5776cf30>] (list1=[2, 3], list2=[1, 2])  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 523, in subTest  
>     yield  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 538, in test_merge  
>     self.assertEqual(Media.merge(list1, list2), expected)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1028, in assertListEqual  
>     self.assertSequenceEqual(list1, list2, msg, seq_type=list)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1010, in assertSequenceEqual  
>     self.fail(msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 670, in fail  
>     raise self.failureException(msg)  
> AssertionError: Lists differ: [2, 3, 1] != [1, 2, 3]  
>   
> First differing element 0:  
> 2  
> 1  
>   
> - [2, 3, 1]  
> + [1, 2, 3]  
>   
> ======================================================================  
> FAIL: test_merge (forms_tests.tests.test_media.FormsMediaTestCase) [<object object at 0x7f5e5776cf30>] (list1=[1, 3], list2=[2, 3])  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 523, in subTest  
>     yield  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 538, in test_merge  
>     self.assertEqual(Media.merge(list1, list2), expected)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1028, in assertListEqual  
>     self.assertSequenceEqual(list1, list2, msg, seq_type=list)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1010, in assertSequenceEqual  
>     self.fail(msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 670, in fail  
>     raise self.failureException(msg)  
> AssertionError: Lists differ: [1, 3, 2] != [1, 2, 3]  
>   
> First differing element 1:  
> 3  
> 2  
>   
> - [1, 3, 2]  
> + [1, 2, 3]  
>   
> ======================================================================  
> FAIL: test_merge (forms_tests.tests.test_media.FormsMediaTestCase) [<object object at 0x7f5e5776cf30>] (list1=[1, 2], list2=[3, 2])  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 523, in subTest  
>     yield  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 538, in test_merge  
>     self.assertEqual(Media.merge(list1, list2), expected)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1028, in assertListEqual  
>     self.assertSequenceEqual(list1, list2, msg, seq_type=list)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1010, in assertSequenceEqual  
>     self.fail(msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 670, in fail  
>     raise self.failureException(msg)  
> AssertionError: Lists differ: [1, 2, 3] != [1, 3, 2]  
>   
> First differing element 1:  
> 2  
> 3  
>   
> - [1, 2, 3]  
> + [1, 3, 2]  
>   
> ----------------------------------------------------------------------  
> Ran 78 tests in 2.181s  
>   
> FAILED (failures=3, errors=24, skipped=6)  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
>    
> [django__django__3.0] [django__django-11019] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [django__django__3.0] [django__django-11019] Test script run successful   
> Attempt to fix test errors? yes  
> 39854 prompt tokens, 170 completion tokens, $0.201820 cost  

The error `TypeError: can only concatenate list (not "tuple") to list` indicates that there is an issue with the `merge` method in the `Media` class. Specifically, it seems that the method is trying to concatenate a list with a tuple, which is not allowed in Python.

To fix this, we need to ensure that both `list_1` and `list_2` are lists before concatenating them. Here are the changes:

django/forms/widgets.py
```python
<<<<<<< SEARCH
        for item in list_1 + list_2:
=======
        for item in list(list_1) + list(list_2):
>>>>>>> REPLACE
```

This change will ensure that both `list_1` and `list_2` are converted to lists before concatenation, preventing the `TypeError`.

> Applied edit to django/forms/widgets.py  
>   
> Test Script:  ./tests/runtests.py --verbosity 2 admin_inlines.tests admin_widgets.test_autocomplete_widget forms_tests.tests.test_media;  
> [django__django__3.0] [django__django-11019] Command: ./tests/runtests.py --verbosity 2 admin_inlines.tests admin_widgets.test_autocomplete_widget forms_tests.tests.test_media   
> [django__django__3.0] [django__django-11019] Subprocess args: {"cwd": "/opt/django__django", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [django__django__3.0] [django__django-11019] Std. Output:  
> Testing against Django installed in '/opt/django__django/django' with up to 16 processes  
> Importing application forms_tests  
> Importing application admin_inlines  
> Importing application admin_widgets  
> Skipping setup of unused database(s): other.  
> Operations to perform:  
>   Synchronize unmigrated apps: admin_inlines, admin_widgets, auth, contenttypes, forms_tests, messages, sessions, staticfiles  
>   Apply all migrations: admin, sites  
> Synchronizing apps without migrations:  
>   Creating tables...  
>     Creating table django_content_type  
>     Creating table auth_permission  
>     Creating table auth_group  
>     Creating table auth_user  
>     Creating table django_session  
>     Creating table forms_tests_boundarymodel  
>     Creating table forms_tests_defaults  
>     Creating table forms_tests_choicemodel  
>     Creating table forms_tests_choiceoptionmodel  
>     Creating table forms_tests_choicefieldmodel  
>     Creating table forms_tests_optionalmultichoicemodel  
>     Creating table forms_tests_filemodel  
>     Creating table forms_tests_article  
>     Creating table admin_inlines_parent  
>     Creating table admin_inlines_teacher  
>     Creating table admin_inlines_child  
>     Creating table admin_inlines_book  
>     Creating table admin_inlines_author  
>     Creating table admin_inlines_nonautopkbook  
>     Creating table admin_inlines_nonautopkbookchild  
>     Creating table admin_inlines_editablepkbook  
>     Creating table admin_inlines_holder  
>     Creating table admin_inlines_inner  
>     Creating table admin_inlines_holder2  
>     Creating table admin_inlines_inner2  
>     Creating table admin_inlines_holder3  
>     Creating table admin_inlines_inner3  
>     Creating table admin_inlines_holder4  
>     Creating table admin_inlines_inner4stacked  
>     Creating table admin_inlines_inner4tabular  
>     Creating table admin_inlines_person  
>     Creating table admin_inlines_outfititem  
>     Creating table admin_inlines_fashionista  
>     Creating table admin_inlines_shoppingweakness  
>     Creating table admin_inlines_titlecollection  
>     Creating table admin_inlines_title  
>     Creating table admin_inlines_poll  
>     Creating table admin_inlines_question  
>     Creating table admin_inlines_novel  
>     Creating table admin_inlines_chapter  
>     Creating table admin_inlines_footnote  
>     Creating table admin_inlines_capofamiglia  
>     Creating table admin_inlines_consigliere  
>     Creating table admin_inlines_sottocapo  
>     Creating table admin_inlines_readonlyinline  
>     Creating table admin_inlines_parentmodelwithcustompk  
>     Creating table admin_inlines_childmodel1  
>     Creating table admin_inlines_childmodel2  
>     Creating table admin_inlines_binarytree  
>     Creating table admin_inlines_lifeform  
>     Creating table admin_inlines_extraterrestrial  
>     Creating table admin_inlines_sighting  
>     Creating table admin_inlines_someparentmodel  
>     Creating table admin_inlines_somechildmodel  
>     Creating table admin_inlines_profilecollection  
>     Creating table admin_inlines_profile  
>     Creating table admin_widgets_member  
>     Creating table admin_widgets_band  
>     Creating table admin_widgets_album  
>     Creating table admin_widgets_inventory  
>     Creating table admin_widgets_event  
>     Creating table admin_widgets_car  
>     Creating table admin_widgets_cartire  
>     Creating table admin_widgets_honeycomb  
>     Creating table admin_widgets_bee  
>     Creating table admin_widgets_individual  
>     Creating table admin_widgets_company  
>     Creating table admin_widgets_advisor  
>     Creating table admin_widgets_student  
>     Creating table admin_widgets_school  
>     Creating table admin_widgets_profile  
>     Running deferred SQL...  
> Running migrations:  
>   Applying admin.0001_initial... OK  
>   Applying admin.0002_logentry_remove_auto_add... OK  
>   Applying admin.0003_logentry_add_action_flag_choices... OK  
>   Applying sites.0001_initial... OK  
>   Applying sites.0002_alter_domain_unique... OK  
> System check identified no issues (0 silenced).  
> Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> test_add_inlines (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_add_stackeds (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_alternating_rows (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_collapsed_inlines (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_delete_inlines (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_delete_stackeds (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_immutable_content_type (admin_inlines.tests.TestInlineAdminForm)  
> Regression for #9362 ... ok  
> test_combine_media (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_construction (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_form_media (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_html_safe (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_media_dsl (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_media_inheritance (forms_tests.tests.test_media.FormsMediaTestCase) ... FAIL  
> test_media_inheritance_extends (forms_tests.tests.test_media.FormsMediaTestCase) ... FAIL  
> test_media_inheritance_from_property (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_media_inheritance_single_type (forms_tests.tests.test_media.FormsMediaTestCase) ... FAIL  
> test_media_property (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_media_property_parent_references (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_merge (forms_tests.tests.test_media.FormsMediaTestCase) ... test_merge_css_three_way (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_merge_js_three_way (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_merge_warning (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_multi_media (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_multi_widget (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_build_attrs (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_build_attrs_no_custom_class (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_build_attrs_not_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_build_attrs_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_get_url (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_media (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_render_options (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_render_options_not_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests)  
> Empty option isn't present if the field isn't required. ... ok  
> test_render_options_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests)  
> Empty option is present if the field isn't required. ... ok  
> test_deleting_inline_with_protected_delete_does_not_validate (admin_inlines.tests.TestInlineProtectedOnDelete) ... ok  
> test_all_inline_media (admin_inlines.tests.TestInlineMedia) ... ok  
> test_inline_media_only_base (admin_inlines.tests.TestInlineMedia) ... ok  
> test_inline_media_only_inline (admin_inlines.tests.TestInlineMedia) ... ok  
> test_inline_add_fk_add_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_add_fk_noperm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_add_m2m_add_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_add_m2m_noperm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_fk_add_change_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_fk_add_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_fk_all_perms (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_fk_change_del_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_fk_change_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_fk_noperm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_m2m_add_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_m2m_change_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_m2m_noperm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_callable_lookup (admin_inlines.tests.TestInline)  
> Admin inline should invoke local callable when its name is listed in readonly_fields ... ok  
> test_can_delete (admin_inlines.tests.TestInline) ... ok  
> test_create_inlines_on_inherited_model (admin_inlines.tests.TestInline) ... ok  
> test_custom_form_tabular_inline_label (admin_inlines.tests.TestInline) ... ok  
> test_custom_form_tabular_inline_overridden_label (admin_inlines.tests.TestInline) ... ok  
> test_custom_get_extra_form (admin_inlines.tests.TestInline) ... ok  
> test_custom_min_num (admin_inlines.tests.TestInline) ... ok  
> test_custom_pk_shortcut (admin_inlines.tests.TestInline) ... ok  
> test_help_text (admin_inlines.tests.TestInline) ... ok  
> test_inline_editable_pk (admin_inlines.tests.TestInline) ... ok  
> test_inline_hidden_field_no_column (admin_inlines.tests.TestInline)  
> #18263 -- Make sure hidden fields don't get a column in tabular inlines ... ok  
> test_inline_nonauto_noneditable_inherited_pk (admin_inlines.tests.TestInline) ... ok  
> test_inline_nonauto_noneditable_pk (admin_inlines.tests.TestInline) ... ok  
> test_inline_primary (admin_inlines.tests.TestInline) ... ok  
> test_inlines_show_change_link_registered (admin_inlines.tests.TestInline)  
> Inlines `show_change_link` for registered models when enabled. ... ok  
> test_inlines_show_change_link_unregistered (admin_inlines.tests.TestInline)  
> Inlines `show_change_link` disabled for unregistered models. ... ok  
> test_localize_pk_shortcut (admin_inlines.tests.TestInline) ... ok  
> test_many_to_many_inlines (admin_inlines.tests.TestInline)  
> Autogenerated many-to-many inlines are displayed correctly (#13407) ... ok  
> test_min_num (admin_inlines.tests.TestInline) ... ok  
> test_no_parent_callable_lookup (admin_inlines.tests.TestInline)  
> Admin inline `readonly_field` shouldn't invoke parent ModelAdmin callable ... ok  
> test_non_related_name_inline (admin_inlines.tests.TestInline) ... ok  
> test_noneditable_inline_has_field_inputs (admin_inlines.tests.TestInline)  
> Inlines without change permission shows field inputs on add form. ... ok  
> test_readonly_stacked_inline_label (admin_inlines.tests.TestInline)  
> Bug #13174. ... ok  
> test_stacked_inline_edit_form_contains_has_original_class (admin_inlines.tests.TestInline) ... ok  
> test_tabular_inline_column_css_class (admin_inlines.tests.TestInline) ... ok  
> test_tabular_inline_show_change_link_false_registered (admin_inlines.tests.TestInline)  
> Inlines `show_change_link` disabled by default. ... ok  
> test_tabular_model_form_meta_readonly_field (admin_inlines.tests.TestInline) ... ok  
> test_tabular_non_field_errors (admin_inlines.tests.TestInline) ... ok  
>   
> ======================================================================  
> FAIL: test_media_inheritance (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 251, in test_media_inheritance  
>     <script type="text/javascript" src="/path/to/js4"></script>"""  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 822, in _baseAssertEqual  
>     raise self.failureException(msg)  
> AssertionError: '<link href="http://media.example.com/static/path/to/c[484 chars]ipt>' != '<link href="/path/to/css3" type="text/css" media="all[484 chars]ipt>'  
>   
> ======================================================================  
> FAIL: test_media_inheritance_extends (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 326, in test_media_inheritance_extends  
>     <script type="text/javascript" src="/path/to/js4"></script>"""  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 822, in _baseAssertEqual  
>     raise self.failureException(msg)  
> AssertionError: '<link href="http://media.example.com/static/path/to/c[484 chars]ipt>' != '<link href="/path/to/css3" type="text/css" media="all[484 chars]ipt>'  
>   
> ======================================================================  
> FAIL: test_media_inheritance_single_type (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 353, in test_media_inheritance_single_type  
>     <script type="text/javascript" src="/path/to/js4"></script>"""  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 822, in _baseAssertEqual  
>     raise self.failureException(msg)  
> AssertionError: '<link href="http://media.example.com/static/path/to/c[316 chars]ipt>' != '<link href="/path/to/css3" type="text/css" media="all[316 chars]ipt>'  
>   
> ======================================================================  
> FAIL: test_merge (forms_tests.tests.test_media.FormsMediaTestCase) [<object object at 0x7f3233d2ef50>] (list1=[2, 3], list2=[1, 2])  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 523, in subTest  
>     yield  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 538, in test_merge  
>     self.assertEqual(Media.merge(list1, list2), expected)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1028, in assertListEqual  
>     self.assertSequenceEqual(list1, list2, msg, seq_type=list)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1010, in assertSequenceEqual  
>     self.fail(msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 670, in fail  
>     raise self.failureException(msg)  
> AssertionError: Lists differ: [2, 3, 1] != [1, 2, 3]  
>   
> First differing element 0:  
> 2  
> 1  
>   
> - [2, 3, 1]  
> + [1, 2, 3]  
>   
> ======================================================================  
> FAIL: test_merge (forms_tests.tests.test_media.FormsMediaTestCase) [<object object at 0x7f3233d2ef50>] (list1=[1, 3], list2=[2, 3])  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 523, in subTest  
>     yield  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 538, in test_merge  
>     self.assertEqual(Media.merge(list1, list2), expected)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1028, in assertListEqual  
>     self.assertSequenceEqual(list1, list2, msg, seq_type=list)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1010, in assertSequenceEqual  
>     self.fail(msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 670, in fail  
>     raise self.failureException(msg)  
> AssertionError: Lists differ: [1, 3, 2] != [1, 2, 3]  
>   
> First differing element 1:  
> 3  
> 2  
>   
> - [1, 3, 2]  
> + [1, 2, 3]  
>   
> ======================================================================  
> FAIL: test_merge (forms_tests.tests.test_media.FormsMediaTestCase) [<object object at 0x7f3233d2ef50>] (list1=[1, 2], list2=[3, 2])  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 523, in subTest  
>     yield  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 538, in test_merge  
>     self.assertEqual(Media.merge(list1, list2), expected)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1028, in assertListEqual  
>     self.assertSequenceEqual(list1, list2, msg, seq_type=list)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1010, in assertSequenceEqual  
>     self.fail(msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 670, in fail  
>     raise self.failureException(msg)  
> AssertionError: Lists differ: [1, 2, 3] != [1, 3, 2]  
>   
> First differing element 1:  
> 2  
> 3  
>   
> - [1, 2, 3]  
> + [1, 3, 2]  
>   
> ----------------------------------------------------------------------  
> Ran 78 tests in 1.966s  
>   
> FAILED (failures=6, skipped=6)  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
>    
> [django__django__3.0] [django__django-11019] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [django__django__3.0] [django__django-11019] Test script run successful   
> Attempt to fix test errors? yes  
> 45178 prompt tokens, 836 completion tokens, $0.238430 cost  

The test failures indicate that there are still issues with the `merge` method and the media inheritance logic. Let's address these issues step-by-step.

1. Fix the `merge` method to handle the order of media files better.
2. Ensure that the media inheritance logic correctly handles the extension of media definitions.

Here are the changes:

django/forms/widgets.py
```python
<<<<<<< SEARCH
        combined_list = []
        seen = set()
        conflict_pairs = set()

        for item in list(list_1) + list(list_2):
            if item not in seen:
                combined_list.append(item)
                seen.add(item)
            else:
                # Check for conflicts
                if item in list_1 and item in list_2:
                    index_1 = list_1.index(item)
                    index_2 = list_2.index(item)
                    for earlier_item in list_1[:index_1]:
                        if earlier_item in list_2[index_2 + 1:]:
                            conflict_pairs.add((earlier_item, item))
                    for later_item in list_1[index_1 + 1:]:
                        if later_item in list_2[:index_2]:
                            conflict_pairs.add((item, later_item))

        for pair in conflict_pairs:
            warnings.warn(
                'Detected duplicate Media files in an opposite order:\n'
                '%s\n%s' % pair,
                MediaOrderConflictWarning,
            )

        return combined_list
=======
        combined_list = []
        seen = set()
        conflict_pairs = set()

        for item in list_1 + list_2:
            if item not in seen:
                combined_list.append(item)
                seen.add(item)
            else:
                # Check for conflicts
                if item in list_1 and item in list_2:
                    index_1 = list_1.index(item)
                    index_2 = list_2.index(item)
                    for earlier_item in list_1[:index_1]:
                        if earlier_item in list_2[index_2 + 1:]:
                            conflict_pairs.add((earlier_item, item))
                    for later_item in list_1[index_1 + 1:]:
                        if later_item in list_2[:index_2]:
                            conflict_pairs.add((item, later_item))

        for pair in conflict_pairs:
            warnings.warn(
                'Detected duplicate Media files in an opposite order:\n'
                '%s\n%s' % pair,
                MediaOrderConflictWarning,
            )

        return combined_list
>>>>>>> REPLACE
```

django/forms/widgets.py
```python
<<<<<<< SEARCH
        # Get the media property of the superclass, if it exists
        sup_cls = super(cls, self)
        try:
            base = sup_cls.media
        except AttributeError:
            base = Media()

        # Get the media definition for this class
        definition = getattr(cls, 'Media', None)
        if definition:
            extend = getattr(definition, 'extend', True)
            if extend:
                if extend is True:
                    m = base
                else:
                    m = Media()
                    for medium in extend:
                        m = m + base[medium]
                return m + Media(definition)
            return Media(definition)
        return base
=======
        # Get the media property of the superclass, if it exists.
        sup_cls = super(cls, self)
        try:
            base = sup_cls.media
        except AttributeError:
            base = Media()

        # Get the media definition for this class.
        definition = getattr(cls, 'Media', None)
        if definition:
            extend = getattr(definition, 'extend', True)
            if extend:
                if extend is True:
                    m = base
                else:
                    m = Media()
                    for medium in extend:
                        m = m + base[medium]
                return m + Media(definition)
            return Media(definition)
        return base
>>>>>>> REPLACE
```

These changes should address the issues with the `merge` method and the media inheritance logic. Please run the tests again to verify.

> Applied edit to django/forms/widgets.py  
>   
> Test Script:  ./tests/runtests.py --verbosity 2 admin_inlines.tests admin_widgets.test_autocomplete_widget forms_tests.tests.test_media;  
> [django__django__3.0] [django__django-11019] Command: ./tests/runtests.py --verbosity 2 admin_inlines.tests admin_widgets.test_autocomplete_widget forms_tests.tests.test_media   
> [django__django__3.0] [django__django-11019] Subprocess args: {"cwd": "/opt/django__django", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [django__django__3.0] [django__django-11019] Std. Output:  
> Testing against Django installed in '/opt/django__django/django' with up to 16 processes  
> Importing application forms_tests  
> Importing application admin_inlines  
> Importing application admin_widgets  
> Skipping setup of unused database(s): other.  
> Operations to perform:  
>   Synchronize unmigrated apps: admin_inlines, admin_widgets, auth, contenttypes, forms_tests, messages, sessions, staticfiles  
>   Apply all migrations: admin, sites  
> Synchronizing apps without migrations:  
>   Creating tables...  
>     Creating table django_content_type  
>     Creating table auth_permission  
>     Creating table auth_group  
>     Creating table auth_user  
>     Creating table django_session  
>     Creating table forms_tests_boundarymodel  
>     Creating table forms_tests_defaults  
>     Creating table forms_tests_choicemodel  
>     Creating table forms_tests_choiceoptionmodel  
>     Creating table forms_tests_choicefieldmodel  
>     Creating table forms_tests_optionalmultichoicemodel  
>     Creating table forms_tests_filemodel  
>     Creating table forms_tests_article  
>     Creating table admin_inlines_parent  
>     Creating table admin_inlines_teacher  
>     Creating table admin_inlines_child  
>     Creating table admin_inlines_book  
>     Creating table admin_inlines_author  
>     Creating table admin_inlines_nonautopkbook  
>     Creating table admin_inlines_nonautopkbookchild  
>     Creating table admin_inlines_editablepkbook  
>     Creating table admin_inlines_holder  
>     Creating table admin_inlines_inner  
>     Creating table admin_inlines_holder2  
>     Creating table admin_inlines_inner2  
>     Creating table admin_inlines_holder3  
>     Creating table admin_inlines_inner3  
>     Creating table admin_inlines_holder4  
>     Creating table admin_inlines_inner4stacked  
>     Creating table admin_inlines_inner4tabular  
>     Creating table admin_inlines_person  
>     Creating table admin_inlines_outfititem  
>     Creating table admin_inlines_fashionista  
>     Creating table admin_inlines_shoppingweakness  
>     Creating table admin_inlines_titlecollection  
>     Creating table admin_inlines_title  
>     Creating table admin_inlines_poll  
>     Creating table admin_inlines_question  
>     Creating table admin_inlines_novel  
>     Creating table admin_inlines_chapter  
>     Creating table admin_inlines_footnote  
>     Creating table admin_inlines_capofamiglia  
>     Creating table admin_inlines_consigliere  
>     Creating table admin_inlines_sottocapo  
>     Creating table admin_inlines_readonlyinline  
>     Creating table admin_inlines_parentmodelwithcustompk  
>     Creating table admin_inlines_childmodel1  
>     Creating table admin_inlines_childmodel2  
>     Creating table admin_inlines_binarytree  
>     Creating table admin_inlines_lifeform  
>     Creating table admin_inlines_extraterrestrial  
>     Creating table admin_inlines_sighting  
>     Creating table admin_inlines_someparentmodel  
>     Creating table admin_inlines_somechildmodel  
>     Creating table admin_inlines_profilecollection  
>     Creating table admin_inlines_profile  
>     Creating table admin_widgets_member  
>     Creating table admin_widgets_band  
>     Creating table admin_widgets_album  
>     Creating table admin_widgets_inventory  
>     Creating table admin_widgets_event  
>     Creating table admin_widgets_car  
>     Creating table admin_widgets_cartire  
>     Creating table admin_widgets_honeycomb  
>     Creating table admin_widgets_bee  
>     Creating table admin_widgets_individual  
>     Creating table admin_widgets_company  
>     Creating table admin_widgets_advisor  
>     Creating table admin_widgets_student  
>     Creating table admin_widgets_school  
>     Creating table admin_widgets_profile  
>     Running deferred SQL...  
> Running migrations:  
>   Applying admin.0001_initial... OK  
>   Applying admin.0002_logentry_remove_auto_add... OK  
>   Applying admin.0003_logentry_add_action_flag_choices... OK  
>   Applying sites.0001_initial... OK  
>   Applying sites.0002_alter_domain_unique... OK  
> System check identified no issues (0 silenced).  
> Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> test_add_inlines (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_add_stackeds (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_alternating_rows (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_collapsed_inlines (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_delete_inlines (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_delete_stackeds (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_immutable_content_type (admin_inlines.tests.TestInlineAdminForm)  
> Regression for #9362 ... ok  
> test_combine_media (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_construction (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_form_media (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_html_safe (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_media_dsl (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_media_inheritance (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_media_inheritance_extends (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_media_inheritance_from_property (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_media_inheritance_single_type (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_media_property (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_media_property_parent_references (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_merge (forms_tests.tests.test_media.FormsMediaTestCase) ... test_merge_css_three_way (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_merge_js_three_way (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_merge_warning (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_multi_media (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_multi_widget (forms_tests.tests.test_media.FormsMediaTestCase) ... ERROR  
> test_build_attrs (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_build_attrs_no_custom_class (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_build_attrs_not_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_build_attrs_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_get_url (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_media (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_render_options (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_render_options_not_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests)  
> Empty option isn't present if the field isn't required. ... ok  
> test_render_options_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests)  
> Empty option is present if the field isn't required. ... ok  
> test_deleting_inline_with_protected_delete_does_not_validate (admin_inlines.tests.TestInlineProtectedOnDelete) ... ok  
> test_all_inline_media (admin_inlines.tests.TestInlineMedia) ... ERROR  
> test_inline_media_only_base (admin_inlines.tests.TestInlineMedia) ... ERROR  
> test_inline_media_only_inline (admin_inlines.tests.TestInlineMedia) ... ERROR  
> test_inline_add_fk_add_perm (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_add_fk_noperm (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_add_m2m_add_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_add_m2m_noperm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_fk_add_change_perm (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_change_fk_add_perm (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_change_fk_all_perms (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_change_fk_change_del_perm (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_change_fk_change_perm (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_change_fk_noperm (admin_inlines.tests.TestInlinePermissions) ... ERROR  
> test_inline_change_m2m_add_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_m2m_change_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_m2m_noperm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_callable_lookup (admin_inlines.tests.TestInline)  
> Admin inline should invoke local callable when its name is listed in readonly_fields ... ok  
> test_can_delete (admin_inlines.tests.TestInline) ... ERROR  
> test_create_inlines_on_inherited_model (admin_inlines.tests.TestInline) ... ok  
> test_custom_form_tabular_inline_label (admin_inlines.tests.TestInline) ... ok  
> test_custom_form_tabular_inline_overridden_label (admin_inlines.tests.TestInline) ... ok  
> test_custom_get_extra_form (admin_inlines.tests.TestInline) ... ok  
> test_custom_min_num (admin_inlines.tests.TestInline) ... ok  
> test_custom_pk_shortcut (admin_inlines.tests.TestInline) ... ok  
> test_help_text (admin_inlines.tests.TestInline) ... ok  
> test_inline_editable_pk (admin_inlines.tests.TestInline) ... ok  
> test_inline_hidden_field_no_column (admin_inlines.tests.TestInline)  
> #18263 -- Make sure hidden fields don't get a column in tabular inlines ... ok  
> test_inline_nonauto_noneditable_inherited_pk (admin_inlines.tests.TestInline) ... ok  
> test_inline_nonauto_noneditable_pk (admin_inlines.tests.TestInline) ... ok  
> test_inline_primary (admin_inlines.tests.TestInline) ... ok  
> test_inlines_show_change_link_registered (admin_inlines.tests.TestInline)  
> Inlines `show_change_link` for registered models when enabled. ... ok  
> test_inlines_show_change_link_unregistered (admin_inlines.tests.TestInline)  
> Inlines `show_change_link` disabled for unregistered models. ... ok  
> test_localize_pk_shortcut (admin_inlines.tests.TestInline) ... ERROR  
> test_many_to_many_inlines (admin_inlines.tests.TestInline)  
> Autogenerated many-to-many inlines are displayed correctly (#13407) ... ok  
> test_min_num (admin_inlines.tests.TestInline) ... ok  
> test_no_parent_callable_lookup (admin_inlines.tests.TestInline)  
> Admin inline `readonly_field` shouldn't invoke parent ModelAdmin callable ... ok  
> test_non_related_name_inline (admin_inlines.tests.TestInline) ... ok  
> test_noneditable_inline_has_field_inputs (admin_inlines.tests.TestInline)  
> Inlines without change permission shows field inputs on add form. ... ok  
> test_readonly_stacked_inline_label (admin_inlines.tests.TestInline)  
> Bug #13174. ... ERROR  
> test_stacked_inline_edit_form_contains_has_original_class (admin_inlines.tests.TestInline) ... ERROR  
> test_tabular_inline_column_css_class (admin_inlines.tests.TestInline) ... ok  
> test_tabular_inline_show_change_link_false_registered (admin_inlines.tests.TestInline)  
> Inlines `show_change_link` disabled by default. ... ok  
> test_tabular_model_form_meta_readonly_field (admin_inlines.tests.TestInline) ... ok  
> test_tabular_non_field_errors (admin_inlines.tests.TestInline) ... ok  
>   
> ======================================================================  
> ERROR: test_combine_media (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 122, in test_combine_media  
>     str(w1.media + w2.media + w3.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_form_media (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 459, in test_form_media  
>     str(f1.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_media_dsl (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 72, in test_media_dsl  
>     str(w1.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_media_inheritance (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 226, in test_media_inheritance  
>     str(w7.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_media_inheritance_extends (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 319, in test_media_inheritance_extends  
>     str(w11.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_media_inheritance_single_type (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 348, in test_media_inheritance_single_type  
>     str(w12.media),  
>   File "/opt/django__django/django/forms/widgets.py", line 183, in _media  
>     m = m + base[medium]  
>   File "/opt/django__django/django/forms/widgets.py", line 114, in __getitem__  
>     return Media(**{str(name): getattr(self, '_' + name)})  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_media_property_parent_references (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 198, in test_media_property_parent_references  
>     str(w6.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_multi_media (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 373, in test_multi_media  
>     str(multimedia.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_multi_widget (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 417, in test_multi_widget  
>     str(mymulti.media),  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 93, in render_css  
>     media = sorted(self._css)  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in _css  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 67, in <dictcomp>  
>     for medium in css.keys() | obj.keys()  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_all_inline_media (admin_inlines.tests.TestInlineMedia)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 513, in test_all_inline_media  
>     response = self.client.get(change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_media_only_base (admin_inlines.tests.TestInlineMedia)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 487, in test_inline_media_only_base  
>     response = self.client.get(change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_media_only_inline (admin_inlines.tests.TestInlineMedia)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 495, in test_inline_media_only_inline  
>     response = self.client.get(change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_add_fk_add_perm (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 651, in test_inline_add_fk_add_perm  
>     response = self.client.get(reverse('admin:admin_inlines_holder2_add'))  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_add_fk_noperm (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 619, in test_inline_add_fk_noperm  
>     response = self.client.get(reverse('admin:admin_inlines_holder2_add'))  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_change_fk_add_change_perm (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 741, in test_inline_change_fk_add_change_perm  
>     response = self.client.get(self.holder_change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_change_fk_add_perm (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 688, in test_inline_change_fk_add_perm  
>     response = self.client.get(self.holder_change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_change_fk_all_perms (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 783, in test_inline_change_fk_all_perms  
>     response = self.client.get(self.holder_change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_change_fk_change_del_perm (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 760, in test_inline_change_fk_change_del_perm  
>     response = self.client.get(self.holder_change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_change_fk_change_perm (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 708, in test_inline_change_fk_change_perm  
>     response = self.client.get(self.holder_change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_inline_change_fk_noperm (admin_inlines.tests.TestInlinePermissions)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 633, in test_inline_change_fk_noperm  
>     response = self.client.get(self.holder_change_url)  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_can_delete (admin_inlines.tests.TestInline)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 46, in test_can_delete  
>     reverse('admin:admin_inlines_holder_change', args=(self.holder.id,))  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_localize_pk_shortcut (admin_inlines.tests.TestInline)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/django/test/utils.py", line 371, in inner  
>     return func(*args, **kwargs)  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 257, in test_localize_pk_shortcut  
>     response = self.client.get(reverse('admin:admin_inlines_holder_change', args=(holder.id,)))  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_readonly_stacked_inline_label (admin_inlines.tests.TestInline)  
> Bug #13174.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 58, in test_readonly_stacked_inline_label  
>     reverse('admin:admin_inlines_holder_change', args=(holder.id,))  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> ERROR: test_stacked_inline_edit_form_contains_has_original_class (admin_inlines.tests.TestInline)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/admin_inlines/tests.py", line 421, in test_stacked_inline_edit_form_contains_has_original_class  
>     response = self.client.get(reverse('admin:admin_inlines_holder_change', args=(holder.pk,)))  
>   File "/opt/django__django/django/test/client.py", line 538, in get  
>     response = super().get(path, data=data, secure=secure, **extra)  
>   File "/opt/django__django/django/test/client.py", line 347, in get  
>     **extra,  
>   File "/opt/django__django/django/test/client.py", line 422, in generic  
>     return self.request(**r)  
>   File "/opt/django__django/django/test/client.py", line 506, in request  
>     raise exc_value  
>   File "/opt/django__django/django/core/handlers/exception.py", line 34, in inner  
>     response = get_response(request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 145, in _get_response  
>     response = self.process_exception_by_middleware(e, request)  
>   File "/opt/django__django/django/core/handlers/base.py", line 143, in _get_response  
>     response = response.render()  
>   File "/opt/django__django/django/template/response.py", line 106, in render  
>     self.content = self.rendered_content  
>   File "/opt/django__django/django/template/response.py", line 83, in rendered_content  
>     content = template.render(context, self._request)  
>   File "/opt/django__django/django/template/backends/django.py", line 61, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 171, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 150, in render  
>     return compiled_parent._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 95, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/loader_tags.py", line 62, in render  
>     result = block.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 937, in render  
>     bit = node.render_annotated(context)  
>   File "/opt/django__django/django/template/base.py", line 904, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 993, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 972, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/utils/html.py", line 388, in <lambda>  
>     klass.__str__ = lambda self: mark_safe(klass_str(self))  
>   File "/opt/django__django/django/forms/widgets.py", line 58, in __str__  
>     return self.render()  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in render  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 80, in <genexpr>  
>     return mark_safe('\n'.join(chain.from_iterable(getattr(self, 'render_' + name)() for name in MEDIA_TYPES)))  
>   File "/opt/django__django/django/forms/widgets.py", line 87, in render_js  
>     ) for path in self._js  
>   File "/opt/django__django/django/forms/widgets.py", line 76, in _js  
>     js = self.merge(js, obj)  
>   File "/opt/django__django/django/forms/widgets.py", line 132, in merge  
>     for item in list_1 + list_2:  
> TypeError: can only concatenate list (not "tuple") to list  
>   
> ======================================================================  
> FAIL: test_merge (forms_tests.tests.test_media.FormsMediaTestCase) [<object object at 0x7ff34cbf1f30>] (list1=[2, 3], list2=[1, 2])  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 523, in subTest  
>     yield  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 538, in test_merge  
>     self.assertEqual(Media.merge(list1, list2), expected)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1028, in assertListEqual  
>     self.assertSequenceEqual(list1, list2, msg, seq_type=list)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1010, in assertSequenceEqual  
>     self.fail(msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 670, in fail  
>     raise self.failureException(msg)  
> AssertionError: Lists differ: [2, 3, 1] != [1, 2, 3]  
>   
> First differing element 0:  
> 2  
> 1  
>   
> - [2, 3, 1]  
> + [1, 2, 3]  
>   
> ======================================================================  
> FAIL: test_merge (forms_tests.tests.test_media.FormsMediaTestCase) [<object object at 0x7ff34cbf1f30>] (list1=[1, 3], list2=[2, 3])  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 523, in subTest  
>     yield  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 538, in test_merge  
>     self.assertEqual(Media.merge(list1, list2), expected)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1028, in assertListEqual  
>     self.assertSequenceEqual(list1, list2, msg, seq_type=list)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1010, in assertSequenceEqual  
>     self.fail(msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 670, in fail  
>     raise self.failureException(msg)  
> AssertionError: Lists differ: [1, 3, 2] != [1, 2, 3]  
>   
> First differing element 1:  
> 3  
> 2  
>   
> - [1, 3, 2]  
> + [1, 2, 3]  
>   
> ======================================================================  
> FAIL: test_merge (forms_tests.tests.test_media.FormsMediaTestCase) [<object object at 0x7ff34cbf1f30>] (list1=[1, 2], list2=[3, 2])  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 523, in subTest  
>     yield  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 538, in test_merge  
>     self.assertEqual(Media.merge(list1, list2), expected)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1028, in assertListEqual  
>     self.assertSequenceEqual(list1, list2, msg, seq_type=list)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1010, in assertSequenceEqual  
>     self.fail(msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 670, in fail  
>     raise self.failureException(msg)  
> AssertionError: Lists differ: [1, 2, 3] != [1, 3, 2]  
>   
> First differing element 1:  
> 2  
> 3  
>   
> - [1, 2, 3]  
> + [1, 3, 2]  
>   
> ----------------------------------------------------------------------  
> Ran 78 tests in 2.171s  
>   
> FAILED (failures=3, errors=24, skipped=6)  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
>    
> [django__django__3.0] [django__django-11019] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [django__django__3.0] [django__django-11019] Test script run successful   
> Attempt to fix test errors? yes  
> 73231 prompt tokens, 170 completion tokens, $0.368705 cost  

The error `TypeError: can only concatenate list (not "tuple") to list` indicates that there is an issue with the `merge` method in the `Media` class. Specifically, it seems that the method is trying to concatenate a list with a tuple, which is not allowed in Python.

To fix this, we need to ensure that both `list_1` and `list_2` are lists before concatenating them. Here are the changes:

django/forms/widgets.py
```python
<<<<<<< SEARCH
        for item in list_1 + list_2:
=======
        for item in list(list_1) + list(list_2):
>>>>>>> REPLACE
```

This change will ensure that both `list_1` and `list_2` are converted to lists before concatenation, preventing the `TypeError`.

> Applied edit to django/forms/widgets.py  
>   
> Test Script:  ./tests/runtests.py --verbosity 2 admin_inlines.tests admin_widgets.test_autocomplete_widget forms_tests.tests.test_media;  
> [django__django__3.0] [django__django-11019] Command: ./tests/runtests.py --verbosity 2 admin_inlines.tests admin_widgets.test_autocomplete_widget forms_tests.tests.test_media   
> [django__django__3.0] [django__django-11019] Subprocess args: {"cwd": "/opt/django__django", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [django__django__3.0] [django__django-11019] Std. Output:  
> Testing against Django installed in '/opt/django__django/django' with up to 16 processes  
> Importing application forms_tests  
> Importing application admin_inlines  
> Importing application admin_widgets  
> Skipping setup of unused database(s): other.  
> Operations to perform:  
>   Synchronize unmigrated apps: admin_inlines, admin_widgets, auth, contenttypes, forms_tests, messages, sessions, staticfiles  
>   Apply all migrations: admin, sites  
> Synchronizing apps without migrations:  
>   Creating tables...  
>     Creating table django_content_type  
>     Creating table auth_permission  
>     Creating table auth_group  
>     Creating table auth_user  
>     Creating table django_session  
>     Creating table forms_tests_boundarymodel  
>     Creating table forms_tests_defaults  
>     Creating table forms_tests_choicemodel  
>     Creating table forms_tests_choiceoptionmodel  
>     Creating table forms_tests_choicefieldmodel  
>     Creating table forms_tests_optionalmultichoicemodel  
>     Creating table forms_tests_filemodel  
>     Creating table forms_tests_article  
>     Creating table admin_inlines_parent  
>     Creating table admin_inlines_teacher  
>     Creating table admin_inlines_child  
>     Creating table admin_inlines_book  
>     Creating table admin_inlines_author  
>     Creating table admin_inlines_nonautopkbook  
>     Creating table admin_inlines_nonautopkbookchild  
>     Creating table admin_inlines_editablepkbook  
>     Creating table admin_inlines_holder  
>     Creating table admin_inlines_inner  
>     Creating table admin_inlines_holder2  
>     Creating table admin_inlines_inner2  
>     Creating table admin_inlines_holder3  
>     Creating table admin_inlines_inner3  
>     Creating table admin_inlines_holder4  
>     Creating table admin_inlines_inner4stacked  
>     Creating table admin_inlines_inner4tabular  
>     Creating table admin_inlines_person  
>     Creating table admin_inlines_outfititem  
>     Creating table admin_inlines_fashionista  
>     Creating table admin_inlines_shoppingweakness  
>     Creating table admin_inlines_titlecollection  
>     Creating table admin_inlines_title  
>     Creating table admin_inlines_poll  
>     Creating table admin_inlines_question  
>     Creating table admin_inlines_novel  
>     Creating table admin_inlines_chapter  
>     Creating table admin_inlines_footnote  
>     Creating table admin_inlines_capofamiglia  
>     Creating table admin_inlines_consigliere  
>     Creating table admin_inlines_sottocapo  
>     Creating table admin_inlines_readonlyinline  
>     Creating table admin_inlines_parentmodelwithcustompk  
>     Creating table admin_inlines_childmodel1  
>     Creating table admin_inlines_childmodel2  
>     Creating table admin_inlines_binarytree  
>     Creating table admin_inlines_lifeform  
>     Creating table admin_inlines_extraterrestrial  
>     Creating table admin_inlines_sighting  
>     Creating table admin_inlines_someparentmodel  
>     Creating table admin_inlines_somechildmodel  
>     Creating table admin_inlines_profilecollection  
>     Creating table admin_inlines_profile  
>     Creating table admin_widgets_member  
>     Creating table admin_widgets_band  
>     Creating table admin_widgets_album  
>     Creating table admin_widgets_inventory  
>     Creating table admin_widgets_event  
>     Creating table admin_widgets_car  
>     Creating table admin_widgets_cartire  
>     Creating table admin_widgets_honeycomb  
>     Creating table admin_widgets_bee  
>     Creating table admin_widgets_individual  
>     Creating table admin_widgets_company  
>     Creating table admin_widgets_advisor  
>     Creating table admin_widgets_student  
>     Creating table admin_widgets_school  
>     Creating table admin_widgets_profile  
>     Running deferred SQL...  
> Running migrations:  
>   Applying admin.0001_initial... OK  
>   Applying admin.0002_logentry_remove_auto_add... OK  
>   Applying admin.0003_logentry_add_action_flag_choices... OK  
>   Applying sites.0001_initial... OK  
>   Applying sites.0002_alter_domain_unique... OK  
> System check identified no issues (0 silenced).  
> Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Cloning test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> test_add_inlines (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_add_stackeds (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_alternating_rows (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_collapsed_inlines (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_delete_inlines (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_delete_stackeds (admin_inlines.tests.SeleniumTests) ... skipped 'No browsers specified.'  
> test_immutable_content_type (admin_inlines.tests.TestInlineAdminForm)  
> Regression for #9362 ... ok  
> test_combine_media (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_construction (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_form_media (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_html_safe (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_media_dsl (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_media_inheritance (forms_tests.tests.test_media.FormsMediaTestCase) ... FAIL  
> test_media_inheritance_extends (forms_tests.tests.test_media.FormsMediaTestCase) ... FAIL  
> test_media_inheritance_from_property (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_media_inheritance_single_type (forms_tests.tests.test_media.FormsMediaTestCase) ... FAIL  
> test_media_property (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_media_property_parent_references (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_merge (forms_tests.tests.test_media.FormsMediaTestCase) ... test_merge_css_three_way (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_merge_js_three_way (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_merge_warning (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_multi_media (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_multi_widget (forms_tests.tests.test_media.FormsMediaTestCase) ... ok  
> test_build_attrs (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_build_attrs_no_custom_class (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_build_attrs_not_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_build_attrs_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_get_url (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_media (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_render_options (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests) ... ok  
> test_render_options_not_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests)  
> Empty option isn't present if the field isn't required. ... ok  
> test_render_options_required_field (admin_widgets.test_autocomplete_widget.AutocompleteMixinTests)  
> Empty option is present if the field isn't required. ... ok  
> test_deleting_inline_with_protected_delete_does_not_validate (admin_inlines.tests.TestInlineProtectedOnDelete) ... ok  
> test_all_inline_media (admin_inlines.tests.TestInlineMedia) ... ok  
> test_inline_media_only_base (admin_inlines.tests.TestInlineMedia) ... ok  
> test_inline_media_only_inline (admin_inlines.tests.TestInlineMedia) ... ok  
> test_inline_add_fk_add_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_add_fk_noperm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_add_m2m_add_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_add_m2m_noperm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_fk_add_change_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_fk_add_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_fk_all_perms (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_fk_change_del_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_fk_change_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_fk_noperm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_m2m_add_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_m2m_change_perm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_inline_change_m2m_noperm (admin_inlines.tests.TestInlinePermissions) ... ok  
> test_callable_lookup (admin_inlines.tests.TestInline)  
> Admin inline should invoke local callable when its name is listed in readonly_fields ... ok  
> test_can_delete (admin_inlines.tests.TestInline) ... ok  
> test_create_inlines_on_inherited_model (admin_inlines.tests.TestInline) ... ok  
> test_custom_form_tabular_inline_label (admin_inlines.tests.TestInline) ... ok  
> test_custom_form_tabular_inline_overridden_label (admin_inlines.tests.TestInline) ... ok  
> test_custom_get_extra_form (admin_inlines.tests.TestInline) ... ok  
> test_custom_min_num (admin_inlines.tests.TestInline) ... ok  
> test_custom_pk_shortcut (admin_inlines.tests.TestInline) ... ok  
> test_help_text (admin_inlines.tests.TestInline) ... ok  
> test_inline_editable_pk (admin_inlines.tests.TestInline) ... ok  
> test_inline_hidden_field_no_column (admin_inlines.tests.TestInline)  
> #18263 -- Make sure hidden fields don't get a column in tabular inlines ... ok  
> test_inline_nonauto_noneditable_inherited_pk (admin_inlines.tests.TestInline) ... ok  
> test_inline_nonauto_noneditable_pk (admin_inlines.tests.TestInline) ... ok  
> test_inline_primary (admin_inlines.tests.TestInline) ... ok  
> test_inlines_show_change_link_registered (admin_inlines.tests.TestInline)  
> Inlines `show_change_link` for registered models when enabled. ... ok  
> test_inlines_show_change_link_unregistered (admin_inlines.tests.TestInline)  
> Inlines `show_change_link` disabled for unregistered models. ... ok  
> test_localize_pk_shortcut (admin_inlines.tests.TestInline) ... ok  
> test_many_to_many_inlines (admin_inlines.tests.TestInline)  
> Autogenerated many-to-many inlines are displayed correctly (#13407) ... ok  
> test_min_num (admin_inlines.tests.TestInline) ... ok  
> test_no_parent_callable_lookup (admin_inlines.tests.TestInline)  
> Admin inline `readonly_field` shouldn't invoke parent ModelAdmin callable ... ok  
> test_non_related_name_inline (admin_inlines.tests.TestInline) ... ok  
> test_noneditable_inline_has_field_inputs (admin_inlines.tests.TestInline)  
> Inlines without change permission shows field inputs on add form. ... ok  
> test_readonly_stacked_inline_label (admin_inlines.tests.TestInline)  
> Bug #13174. ... ok  
> test_stacked_inline_edit_form_contains_has_original_class (admin_inlines.tests.TestInline) ... ok  
> test_tabular_inline_column_css_class (admin_inlines.tests.TestInline) ... ok  
> test_tabular_inline_show_change_link_false_registered (admin_inlines.tests.TestInline)  
> Inlines `show_change_link` disabled by default. ... ok  
> test_tabular_model_form_meta_readonly_field (admin_inlines.tests.TestInline) ... ok  
> test_tabular_non_field_errors (admin_inlines.tests.TestInline) ... ok  
>   
> ======================================================================  
> FAIL: test_media_inheritance (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 251, in test_media_inheritance  
>     <script type="text/javascript" src="/path/to/js4"></script>"""  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 822, in _baseAssertEqual  
>     raise self.failureException(msg)  
> AssertionError: '<link href="http://media.example.com/static/path/to/c[484 chars]ipt>' != '<link href="/path/to/css3" type="text/css" media="all[484 chars]ipt>'  
>   
> ======================================================================  
> FAIL: test_media_inheritance_extends (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 326, in test_media_inheritance_extends  
>     <script type="text/javascript" src="/path/to/js4"></script>"""  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 822, in _baseAssertEqual  
>     raise self.failureException(msg)  
> AssertionError: '<link href="http://media.example.com/static/path/to/c[484 chars]ipt>' != '<link href="/path/to/css3" type="text/css" media="all[484 chars]ipt>'  
>   
> ======================================================================  
> FAIL: test_media_inheritance_single_type (forms_tests.tests.test_media.FormsMediaTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 605, in run  
>     testMethod()  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 353, in test_media_inheritance_single_type  
>     <script type="text/javascript" src="/path/to/js4"></script>"""  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 822, in _baseAssertEqual  
>     raise self.failureException(msg)  
> AssertionError: '<link href="http://media.example.com/static/path/to/c[316 chars]ipt>' != '<link href="/path/to/css3" type="text/css" media="all[316 chars]ipt>'  
>   
> ======================================================================  
> FAIL: test_merge (forms_tests.tests.test_media.FormsMediaTestCase) [<object object at 0x7f473a9a9f50>] (list1=[2, 3], list2=[1, 2])  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 523, in subTest  
>     yield  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 538, in test_merge  
>     self.assertEqual(Media.merge(list1, list2), expected)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1028, in assertListEqual  
>     self.assertSequenceEqual(list1, list2, msg, seq_type=list)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1010, in assertSequenceEqual  
>     self.fail(msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 670, in fail  
>     raise self.failureException(msg)  
> AssertionError: Lists differ: [2, 3, 1] != [1, 2, 3]  
>   
> First differing element 0:  
> 2  
> 1  
>   
> - [2, 3, 1]  
> + [1, 2, 3]  
>   
> ======================================================================  
> FAIL: test_merge (forms_tests.tests.test_media.FormsMediaTestCase) [<object object at 0x7f473a9a9f50>] (list1=[1, 3], list2=[2, 3])  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 523, in subTest  
>     yield  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 538, in test_merge  
>     self.assertEqual(Media.merge(list1, list2), expected)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1028, in assertListEqual  
>     self.assertSequenceEqual(list1, list2, msg, seq_type=list)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1010, in assertSequenceEqual  
>     self.fail(msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 670, in fail  
>     raise self.failureException(msg)  
> AssertionError: Lists differ: [1, 3, 2] != [1, 2, 3]  
>   
> First differing element 1:  
> 3  
> 2  
>   
> - [1, 3, 2]  
> + [1, 2, 3]  
>   
> ======================================================================  
> FAIL: test_merge (forms_tests.tests.test_media.FormsMediaTestCase) [<object object at 0x7f473a9a9f50>] (list1=[1, 2], list2=[3, 2])  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 523, in subTest  
>     yield  
>   File "/opt/django__django/tests/forms_tests/tests/test_media.py", line 538, in test_merge  
>     self.assertEqual(Media.merge(list1, list2), expected)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 829, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1028, in assertListEqual  
>     self.assertSequenceEqual(list1, list2, msg, seq_type=list)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 1010, in assertSequenceEqual  
>     self.fail(msg)  
>   File "/opt/pyenv/versions/3.6.15/lib/python3.6/unittest/case.py", line 670, in fail  
>     raise self.failureException(msg)  
> AssertionError: Lists differ: [1, 2, 3] != [1, 3, 2]  
>   
> First differing element 1:  
> 2  
> 3  
>   
> - [1, 2, 3]  
> + [1, 3, 2]  
>   
> ----------------------------------------------------------------------  
> Ran 78 tests in 2.064s  
>   
> FAILED (failures=6, skipped=6)  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
> Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
>    
> [django__django__3.0] [django__django-11019] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [django__django__3.0] [django__django-11019] Test script run successful   
> Attempt to fix test errors? yes  
> Only 4 reflections allowed, stopping.  
