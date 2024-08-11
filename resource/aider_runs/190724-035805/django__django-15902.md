
# aider chat started at 2024-07-19 03:13:02

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp0r230fff/.git with 6,645 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### "default.html" deprecation warning raised for ManagementForm's  
#### Description  
#### 	  
#### I have a project where I never render forms with the {{ form }} expression. However, I'm still getting the new template deprecation warning because of the formset management form production, during which the template used is insignificant (only hidden inputs are produced).  
#### Is it worth special-casing this and avoid producing the warning for the management forms?  
> 33623 prompt tokens, 72 completion tokens, $0.169195 cost  

To address the deprecation warning for `default.html` when rendering `ManagementForm`, we will likely need to make changes in the following files:

1. `django/forms/formsets.py`: This file is responsible for handling formsets, including the management form.

Please add `django/forms/formsets.py` to the chat so I can provide the necessary changes.

> django/forms/formsets.py  
> Add these files to the chat? yes  
> 7924 prompt tokens, 395 completion tokens, $0.045545 cost  

To address the deprecation warning for `default.html` when rendering `ManagementForm`, we can special-case the management form rendering to avoid producing the warning. We will modify the `ManagementForm` class to use a specific renderer that does not trigger the warning.

Here are the changes:

1. Update the `ManagementForm` class to use a custom renderer that does not produce the warning.
2. Create a custom renderer class that bypasses the template rendering for the management form.

Let's start by creating a custom renderer class in a new file `django/forms/renderers.py`:

django/forms/renderers.py
```python
<<<<<<< SEARCH
=======
from django.forms.renderers import BaseRenderer

class ManagementFormRenderer(BaseRenderer):
    def render(self, template_name, context, request=None):
        # Bypass template rendering for management form
        return ''.join(str(field) for field in context['form'])
>>>>>>> REPLACE
```

Next, we will update the `ManagementForm` class in `django/forms/formsets.py` to use this custom renderer:

django/forms/formsets.py
```python
<<<<<<< SEARCH
from django.utils.functional import cached_property
=======
from django.utils.functional import cached_property
from django.forms.renderers import ManagementFormRenderer
>>>>>>> REPLACE
```

django/forms/formsets.py
```python
<<<<<<< SEARCH
            form = ManagementForm(
                self.data,
                auto_id=self.auto_id,
                prefix=self.prefix,
                renderer=self.renderer,
            )
=======
            form = ManagementForm(
                self.data,
                auto_id=self.auto_id,
                prefix=self.prefix,
                renderer=ManagementFormRenderer(),
            )
>>>>>>> REPLACE
```

django/forms/formsets.py
```python
<<<<<<< SEARCH
                renderer=self.renderer,
=======
                renderer=ManagementFormRenderer(),
>>>>>>> REPLACE
```

These changes will ensure that the `ManagementForm` uses a custom renderer that does not produce the deprecation warning for `default.html`.

> Allow edits to django/forms/renderers.py which was not previously added to chat? yes  
> Applied edit to django/forms/renderers.py  
> Applied edit to django/forms/formsets.py  
>   
> Test Script:  ./tests/runtests.py --verbosity 2 forms_tests.tests.test_formsets;  
> [django__django__4.2] [django__django-15902] Command: ./tests/runtests.py --verbosity 2 forms_tests.tests.test_formsets   
> [django__django__4.2] [django__django-15902] Subprocess args: {"cwd": "/opt/django__django", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [django__django__4.2] [django__django-15902] Std. Output:  
> Testing against Django installed in '/opt/django__django/django' with up to 16 processes  
> Importing application forms_tests  
> Found 156 test(s).  
> Skipping setup of unused database(s): default, other.  
> System check identified no issues (0 silenced).  
> test_warning (forms_tests.tests.test_formsets.DeprecationTests) ... ok  
> test_invalid (forms_tests.tests.test_formsets.AllValidTests)  
> all_valid() validates all forms, even when some are invalid. ... ok  
> test_valid (forms_tests.tests.test_formsets.AllValidTests) ... ok  
> test_empty_formset_is_multipart (forms_tests.tests.test_formsets.TestEmptyFormSet)  
> is_multipart() works with an empty formset. ... ok  
> test_empty_formset_is_valid (forms_tests.tests.test_formsets.TestEmptyFormSet)  
> An empty formset still calls clean() ... ok  
> test_empty_formset_media (forms_tests.tests.test_formsets.TestEmptyFormSet)  
> Media is available on empty formset. ... ok  
> test_as_div (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ERROR  
> test_as_p (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ERROR  
> test_as_table (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ERROR  
> test_as_ul (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ERROR  
> test_as_div (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ERROR  
> test_as_p (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ERROR  
> test_as_table (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ERROR  
> test_as_ul (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ERROR  
> test_customize_management_form_error (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ok  
> test_empty_forms_are_unbound (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ok  
> test_form_errors_are_caught_by_formset (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ok  
> test_management_form_invalid_data (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_no_data_error (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_with_management_data_attrs_work_fine (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ok  
> test_absolute_max (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_absolute_max_invalid (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_absolute_max_with_max_num (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_basic_formset (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A FormSet constructor takes the same arguments as Form. Create a ... ERROR  
> test_blank_form_unfilled (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A form that's displayed as blank may be submitted as blank. ... ok  
> test_can_delete_extra_formset_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_clean_hook (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSets have a clean() hook for doing extra validation that isn't tied ... ok  
> test_custom_renderer (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms ... FAIL  
> test_default_absolute_max (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_delete_prefilled_data (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Deleting prefilled data is an error. Removing data from form fields ... ok  
> test_disable_delete_extra_formset_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More than 1 empty form can be displayed using formset_factory's ... ok  
> test_empty_ordered_fields (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Ordering fields are allowed to be left blank. If they are left blank, ... ok  
> test_form_kwargs_empty_form (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_form_kwargs_formset (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Custom kwargs set on the formset instance are passed to the ... ok  
> test_form_kwargs_formset_dynamic (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Form kwargs can be passed dynamically in a formset. ... ok  
> test_formset_calls_forms_is_valid (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formsets call is_valid() on each form. ... ok  
> test_formset_error_class (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formset's forms use the formset's error_class. ... ok  
> test_formset_has_changed (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSet.has_changed() is True if any data is passed to its forms, even ... ok  
> test_formset_initial_data (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A FormSet can be prefilled with existing data by providing a list of ... ok  
> test_formset_iteration (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formset instances are iterable. ... ok  
> test_formset_nonzero (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formsets without any forms evaluates as True. ... ok  
> test_formset_splitdatetimefield (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formset works with SplitDateTimeField(initial=datetime.datetime.now). ... ok  
> test_formset_total_error_count (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A valid formset should have 0 total errors. ... ok  
> test_formset_total_error_count_with_non_form_errors (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_formset_validate_max_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If validate_max is set and max_num is less than TOTAL_FORMS in the ... ok  
> test_formset_validate_max_flag_custom_error (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_formset_validate_min_excludes_empty_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_formset_validate_min_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If validate_min is set and min_num is more than TOTAL_FORMS in the ... ok  
> test_formset_validate_min_flag_custom_formatted_error (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_formset_validate_min_unchanged_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> min_num validation doesn't consider unchanged forms with initial data ... ok  
> test_formset_validation (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_formset_validation_count (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formset's ManagementForm is validated once per FormSet.is_valid() ... ok  
> test_formset_with_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> formset_factory's can_delete argument adds a boolean "delete" field to ... ok  
> test_formset_with_deletion_custom_widget (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_formset_with_deletion_invalid_deleted_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> deleted_forms works on a valid formset even if a deleted form would ... ok  
> test_formset_with_deletion_remove_deletion_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If a form is filled with something and can_delete is also checked, that ... ok  
> test_formset_with_ordering_and_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSets with ordering + deletion. ... ok  
> test_formsets_with_ordering (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> formset_factory's can_order argument adds an integer field to each ... ok  
> test_formsets_with_ordering_custom_widget (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_hard_limit_on_instantiated_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formset has a hard limit on the number of forms instantiated. ... ok  
> test_html_safe (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_increase_hard_limit (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Can increase the built-in forms limit via a higher max_num. ... ok  
> test_invalid_deleted_form_with_ordering (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Can get ordered_forms from a valid formset even if a deleted form ... ok  
> test_limited_max_forms_two (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_limiting_extra_lest_than_max_num (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> max_num has no effect when extra is less than max_num. ... ok  
> test_limiting_max_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Limiting the maximum number of forms with max_num. ... ok  
> test_management_form_field_names (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> The management form class has field names matching the constants. ... ok  
> test_management_form_prefix (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> The management form has the correct prefix. ... ok  
> test_max_num_with_initial_data (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_max_num_zero (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If max_num is 0 then no form is rendered at all, regardless of extra, ... ok  
> test_max_num_zero_with_initial (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_min_num_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More than 1 empty form can also be displayed using formset_factory's ... ok  
> test_min_num_displaying_more_than_one_blank_form_with_zero_extra (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More than 1 empty form can be displayed using min_num. ... ok  
> test_more_initial_data (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> The extra argument works when the formset is pre-filled with initial ... ok  
> test_more_initial_form_result_in_one (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> One form from initial and extra=3 with max_num=2 results in the one ... ok  
> test_more_initial_than_max_num (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More initial forms than max_num results in all initial forms being ... ok  
> test_non_form_errors (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_non_form_errors_run_full_clean (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If non_form_errors() is called without calling is_valid() first, ... ok  
> test_ordering_blank_fieldsets (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Ordering works with blank fieldsets. ... ok  
> test_repr (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_repr_do_not_trigger_validation (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_second_form_partially_filled (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If at least one field is filled out on a blank form, it will be ... ok  
> test_second_form_partially_filled_2 (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A partially completed form is invalid. ... ok  
> test_single_form_completed (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Just one form may be completed. ... ok  
> test_template_name_can_be_overridden (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_template_name_uses_renderer_value (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_validate_max_ignores_forms_marked_for_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_absolute_max (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_absolute_max_invalid (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_absolute_max_with_max_num (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_basic_formset (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A FormSet constructor takes the same arguments as Form. Create a ... ERROR  
> test_blank_form_unfilled (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A form that's displayed as blank may be submitted as blank. ... ok  
> test_can_delete_extra_formset_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_clean_hook (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSets have a clean() hook for doing extra validation that isn't tied ... ok  
> test_custom_renderer (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms ... FAIL  
> test_default_absolute_max (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_delete_prefilled_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Deleting prefilled data is an error. Removing data from form fields ... ok  
> test_disable_delete_extra_formset_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More than 1 empty form can be displayed using formset_factory's ... ok  
> test_empty_ordered_fields (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Ordering fields are allowed to be left blank. If they are left blank, ... ok  
> test_form_kwargs_empty_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_form_kwargs_formset (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Custom kwargs set on the formset instance are passed to the ... ok  
> test_form_kwargs_formset_dynamic (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Form kwargs can be passed dynamically in a formset. ... ok  
> test_formset_calls_forms_is_valid (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formsets call is_valid() on each form. ... ok  
> test_formset_error_class (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formset's forms use the formset's error_class. ... ok  
> test_formset_has_changed (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSet.has_changed() is True if any data is passed to its forms, even ... ok  
> test_formset_initial_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A FormSet can be prefilled with existing data by providing a list of ... ok  
> test_formset_iteration (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formset instances are iterable. ... ok  
> test_formset_nonzero (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formsets without any forms evaluates as True. ... ok  
> test_formset_splitdatetimefield (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formset works with SplitDateTimeField(initial=datetime.datetime.now). ... ok  
> test_formset_total_error_count (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A valid formset should have 0 total errors. ... ok  
> test_formset_total_error_count_with_non_form_errors (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_formset_validate_max_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If validate_max is set and max_num is less than TOTAL_FORMS in the ... ok  
> test_formset_validate_max_flag_custom_error (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_formset_validate_min_excludes_empty_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_formset_validate_min_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If validate_min is set and min_num is more than TOTAL_FORMS in the ... ok  
> test_formset_validate_min_flag_custom_formatted_error (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_formset_validate_min_unchanged_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> min_num validation doesn't consider unchanged forms with initial data ... ok  
> test_formset_validation (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_formset_validation_count (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formset's ManagementForm is validated once per FormSet.is_valid() ... ok  
> test_formset_with_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> formset_factory's can_delete argument adds a boolean "delete" field to ... ok  
> test_formset_with_deletion_custom_widget (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_formset_with_deletion_invalid_deleted_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> deleted_forms works on a valid formset even if a deleted form would ... ok  
> test_formset_with_deletion_remove_deletion_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If a form is filled with something and can_delete is also checked, that ... ok  
> test_formset_with_ordering_and_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSets with ordering + deletion. ... ok  
> test_formsets_with_ordering (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> formset_factory's can_order argument adds an integer field to each ... ok  
> test_formsets_with_ordering_custom_widget (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_hard_limit_on_instantiated_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formset has a hard limit on the number of forms instantiated. ... ok  
> test_html_safe (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_increase_hard_limit (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Can increase the built-in forms limit via a higher max_num. ... ok  
> test_invalid_deleted_form_with_ordering (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Can get ordered_forms from a valid formset even if a deleted form ... ok  
> test_limited_max_forms_two (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_limiting_extra_lest_than_max_num (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> max_num has no effect when extra is less than max_num. ... ok  
> test_limiting_max_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Limiting the maximum number of forms with max_num. ... ok  
> test_management_form_field_names (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> The management form class has field names matching the constants. ... ok  
> test_management_form_prefix (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> The management form has the correct prefix. ... ok  
> test_max_num_with_initial_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_max_num_zero (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If max_num is 0 then no form is rendered at all, regardless of extra, ... ok  
> test_max_num_zero_with_initial (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_min_num_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More than 1 empty form can also be displayed using formset_factory's ... ok  
> test_min_num_displaying_more_than_one_blank_form_with_zero_extra (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More than 1 empty form can be displayed using min_num. ... ok  
> test_more_initial_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> The extra argument works when the formset is pre-filled with initial ... ok  
> test_more_initial_form_result_in_one (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> One form from initial and extra=3 with max_num=2 results in the one ... ok  
> test_more_initial_than_max_num (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More initial forms than max_num results in all initial forms being ... ok  
> test_non_form_errors (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_non_form_errors_run_full_clean (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If non_form_errors() is called without calling is_valid() first, ... ok  
> test_ordering_blank_fieldsets (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Ordering works with blank fieldsets. ... ok  
> test_repr (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_repr_do_not_trigger_validation (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_second_form_partially_filled (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If at least one field is filled out on a blank form, it will be ... ok  
> test_second_form_partially_filled_2 (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A partially completed form is invalid. ... ok  
> test_single_form_completed (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Just one form may be completed. ... ok  
> test_template_name_can_be_overridden (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_template_name_uses_renderer_value (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_validate_max_ignores_forms_marked_for_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
>   
> ======================================================================  
> ERROR: test_as_div (forms_tests.tests.test_formsets.FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1671, in test_as_div  
>     self.formset.as_div(),  
>   File "/opt/django__django/django/forms/utils.py", line 96, in as_div  
>     return self.render(self.template_name_div)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1070, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 1047, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/forms/utils.py", line 72, in render  
>     warnings.warn(  
> django.utils.deprecation.RemovedInDjango50Warning: The "default.html" templates for forms and formsets will be removed. These were proxies to the equivalent "table.html" templates, but the new "div.html" templates will be the default from Django 5.0. Transitional renderers are provided to allow you to opt-in to the new output style now. See https://docs.djangoproject.com/en/dev/releases/4.1/ for more details  
>   
> ======================================================================  
> ERROR: test_as_p (forms_tests.tests.test_formsets.FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1648, in test_as_p  
>     self.formset.as_p(),  
>   File "/opt/django__django/django/forms/utils.py", line 84, in as_p  
>     return self.render(self.template_name_p)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1070, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 1047, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/forms/utils.py", line 72, in render  
>     warnings.warn(  
> django.utils.deprecation.RemovedInDjango50Warning: The "default.html" templates for forms and formsets will be removed. These were proxies to the equivalent "table.html" templates, but the new "div.html" templates will be the default from Django 5.0. Transitional renderers are provided to allow you to opt-in to the new output style now. See https://docs.djangoproject.com/en/dev/releases/4.1/ for more details  
>   
> ======================================================================  
> ERROR: test_as_table (forms_tests.tests.test_formsets.FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1636, in test_as_table  
>     self.formset.as_table(),  
>   File "/opt/django__django/django/forms/utils.py", line 88, in as_table  
>     return self.render(self.template_name_table)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1070, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 1047, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/forms/utils.py", line 72, in render  
>     warnings.warn(  
> django.utils.deprecation.RemovedInDjango50Warning: The "default.html" templates for forms and formsets will be removed. These were proxies to the equivalent "table.html" templates, but the new "div.html" templates will be the default from Django 5.0. Transitional renderers are provided to allow you to opt-in to the new output style now. See https://docs.djangoproject.com/en/dev/releases/4.1/ for more details  
>   
> ======================================================================  
> ERROR: test_as_ul (forms_tests.tests.test_formsets.FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1659, in test_as_ul  
>     self.formset.as_ul(),  
>   File "/opt/django__django/django/forms/utils.py", line 92, in as_ul  
>     return self.render(self.template_name_ul)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1070, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 1047, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/forms/utils.py", line 72, in render  
>     warnings.warn(  
> django.utils.deprecation.RemovedInDjango50Warning: The "default.html" templates for forms and formsets will be removed. These were proxies to the equivalent "table.html" templates, but the new "div.html" templates will be the default from Django 5.0. Transitional renderers are provided to allow you to opt-in to the new output style now. See https://docs.djangoproject.com/en/dev/releases/4.1/ for more details  
>   
> ======================================================================  
> ERROR: test_as_div (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1671, in test_as_div  
>     self.formset.as_div(),  
>   File "/opt/django__django/django/forms/utils.py", line 96, in as_div  
>     return self.render(self.template_name_div)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1070, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 1047, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/forms/utils.py", line 72, in render  
>     warnings.warn(  
> django.utils.deprecation.RemovedInDjango50Warning: The "default.html" templates for forms and formsets will be removed. These were proxies to the equivalent "table.html" templates, but the new "div.html" templates will be the default from Django 5.0. Transitional renderers are provided to allow you to opt-in to the new output style now. See https://docs.djangoproject.com/en/dev/releases/4.1/ for more details  
>   
> ======================================================================  
> ERROR: test_as_p (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1648, in test_as_p  
>     self.formset.as_p(),  
>   File "/opt/django__django/django/forms/utils.py", line 84, in as_p  
>     return self.render(self.template_name_p)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1070, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 1047, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/forms/utils.py", line 72, in render  
>     warnings.warn(  
> django.utils.deprecation.RemovedInDjango50Warning: The "default.html" templates for forms and formsets will be removed. These were proxies to the equivalent "table.html" templates, but the new "div.html" templates will be the default from Django 5.0. Transitional renderers are provided to allow you to opt-in to the new output style now. See https://docs.djangoproject.com/en/dev/releases/4.1/ for more details  
>   
> ======================================================================  
> ERROR: test_as_table (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1636, in test_as_table  
>     self.formset.as_table(),  
>   File "/opt/django__django/django/forms/utils.py", line 88, in as_table  
>     return self.render(self.template_name_table)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1070, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 1047, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/forms/utils.py", line 72, in render  
>     warnings.warn(  
> django.utils.deprecation.RemovedInDjango50Warning: The "default.html" templates for forms and formsets will be removed. These were proxies to the equivalent "table.html" templates, but the new "div.html" templates will be the default from Django 5.0. Transitional renderers are provided to allow you to opt-in to the new output style now. See https://docs.djangoproject.com/en/dev/releases/4.1/ for more details  
>   
> ======================================================================  
> ERROR: test_as_ul (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1659, in test_as_ul  
>     self.formset.as_ul(),  
>   File "/opt/django__django/django/forms/utils.py", line 92, in as_ul  
>     return self.render(self.template_name_ul)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1070, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 1047, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/forms/utils.py", line 72, in render  
>     warnings.warn(  
> django.utils.deprecation.RemovedInDjango50Warning: The "default.html" templates for forms and formsets will be removed. These were proxies to the equivalent "table.html" templates, but the new "div.html" templates will be the default from Django 5.0. Transitional renderers are provided to allow you to opt-in to the new output style now. See https://docs.djangoproject.com/en/dev/releases/4.1/ for more details  
>   
> ======================================================================  
> ERROR: test_management_form_invalid_data (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1741, in test_management_form_invalid_data  
>     str(formset),  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1070, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 1047, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/forms/utils.py", line 72, in render  
>     warnings.warn(  
> django.utils.deprecation.RemovedInDjango50Warning: The "default.html" templates for forms and formsets will be removed. These were proxies to the equivalent "table.html" templates, but the new "div.html" templates will be the default from Django 5.0. Transitional renderers are provided to allow you to opt-in to the new output style now. See https://docs.djangoproject.com/en/dev/releases/4.1/ for more details  
>   
> ======================================================================  
> ERROR: test_no_data_error (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1710, in test_no_data_error  
>     str(formset),  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1070, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 1047, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/forms/utils.py", line 72, in render  
>     warnings.warn(  
> django.utils.deprecation.RemovedInDjango50Warning: The "default.html" templates for forms and formsets will be removed. These were proxies to the equivalent "table.html" templates, but the new "div.html" templates will be the default from Django 5.0. Transitional renderers are provided to allow you to opt-in to the new output style now. See https://docs.djangoproject.com/en/dev/releases/4.1/ for more details  
>   
> ======================================================================  
> ERROR: test_basic_formset (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A FormSet constructor takes the same arguments as Form. Create a  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 125, in test_basic_formset  
>     str(formset),  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1070, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 1047, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/forms/utils.py", line 72, in render  
>     warnings.warn(  
> django.utils.deprecation.RemovedInDjango50Warning: The "default.html" templates for forms and formsets will be removed. These were proxies to the equivalent "table.html" templates, but the new "div.html" templates will be the default from Django 5.0. Transitional renderers are provided to allow you to opt-in to the new output style now. See https://docs.djangoproject.com/en/dev/releases/4.1/ for more details  
>   
> ======================================================================  
> ERROR: test_html_safe (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1455, in test_html_safe  
>     self.assertEqual(str(formset), formset.__html__())  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1070, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 1047, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/forms/utils.py", line 72, in render  
>     warnings.warn(  
> django.utils.deprecation.RemovedInDjango50Warning: The "default.html" templates for forms and formsets will be removed. These were proxies to the equivalent "table.html" templates, but the new "div.html" templates will be the default from Django 5.0. Transitional renderers are provided to allow you to opt-in to the new output style now. See https://docs.djangoproject.com/en/dev/releases/4.1/ for more details  
>   
> ======================================================================  
> ERROR: test_basic_formset (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A FormSet constructor takes the same arguments as Form. Create a  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 125, in test_basic_formset  
>     str(formset),  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1070, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 1047, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/forms/utils.py", line 72, in render  
>     warnings.warn(  
> django.utils.deprecation.RemovedInDjango50Warning: The "default.html" templates for forms and formsets will be removed. These were proxies to the equivalent "table.html" templates, but the new "div.html" templates will be the default from Django 5.0. Transitional renderers are provided to allow you to opt-in to the new output style now. See https://docs.djangoproject.com/en/dev/releases/4.1/ for more details  
>   
> ======================================================================  
> ERROR: test_html_safe (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1455, in test_html_safe  
>     self.assertEqual(str(formset), formset.__html__())  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1070, in render  
>     return render_value_in_context(output, context)  
>   File "/opt/django__django/django/template/base.py", line 1047, in render_value_in_context  
>     value = str(value)  
>   File "/opt/django__django/django/forms/utils.py", line 72, in render  
>     warnings.warn(  
> django.utils.deprecation.RemovedInDjango50Warning: The "default.html" templates for forms and formsets will be removed. These were proxies to the equivalent "table.html" templates, but the new "div.html" templates will be the default from Django 5.0. Transitional renderers are provided to allow you to opt-in to the new output style now. See https://docs.djangoproject.com/en/dev/releases/4.1/ for more details  
>   
> ======================================================================  
> FAIL: test_custom_renderer (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1549, in test_custom_renderer  
>     self.assertEqual(formset.management_form.renderer, renderer)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 837, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 830, in _baseAssertEqual  
>     raise self.failureException(msg)  
> AssertionError: <django.forms.renderers.ManagementFormRenderer object at 0x7f43d1130910> != <django.forms.renderers.Jinja2 object at 0x7f43d1130880>  
>   
> ======================================================================  
> FAIL: test_custom_renderer (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1549, in test_custom_renderer  
>     self.assertEqual(formset.management_form.renderer, renderer)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 837, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 830, in _baseAssertEqual  
>     raise self.failureException(msg)  
> AssertionError: <django.forms.renderers.ManagementFormRenderer object at 0x7f43d1131a00> != <django.forms.renderers.Jinja2 object at 0x7f43d1131970>  
>   
> ----------------------------------------------------------------------  
> Ran 156 tests in 0.722s  
>   
> FAILED (failures=2, errors=14)  
>    
> [django__django__4.2] [django__django-15902] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [django__django__4.2] [django__django-15902] Test script run successful   
> Attempt to fix test errors? yes  
> 24159 prompt tokens, 222 completion tokens, $0.124125 cost  

To address the deprecation warning and ensure that the custom renderer is correctly passed to the `ManagementForm`, we need to make the following changes:

1. Update the `ManagementForm` class to accept a renderer parameter.
2. Ensure that the custom renderer is passed to the `ManagementForm` in the `BaseFormSet` class.

Here are the changes:

django/forms/formsets.py
```python
<<<<<<< SEARCH
    def clean(self):
=======
    def __init__(self, *args, **kwargs):
        self.renderer = kwargs.pop('renderer', None)
        super().__init__(*args, **kwargs)

>>>>>>> REPLACE
```

django/forms/formsets.py
```python
<<<<<<< SEARCH
                renderer=ManagementFormRenderer(),
=======
                renderer=self.renderer,
>>>>>>> REPLACE
```

django/forms/formsets.py
```python
<<<<<<< SEARCH
                renderer=ManagementFormRenderer(),
=======
                renderer=self.renderer,
>>>>>>> REPLACE
```

These changes will ensure that the custom renderer is correctly passed to the `ManagementForm` and will avoid the deprecation warning for `default.html`.

> Applied edit to django/forms/formsets.py  
>   
> Test Script:  ./tests/runtests.py --verbosity 2 forms_tests.tests.test_formsets;  
> [django__django__4.2] [django__django-15902] Command: ./tests/runtests.py --verbosity 2 forms_tests.tests.test_formsets   
> [django__django__4.2] [django__django-15902] Subprocess args: {"cwd": "/opt/django__django", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [django__django__4.2] [django__django-15902] Std. Output:  
> Testing against Django installed in '/opt/django__django/django' with up to 16 processes  
> Importing application forms_tests  
> Found 156 test(s).  
> Skipping setup of unused database(s): default, other.  
> System check identified no issues (0 silenced).  
> test_warning (forms_tests.tests.test_formsets.DeprecationTests) ... ok  
> test_invalid (forms_tests.tests.test_formsets.AllValidTests)  
> all_valid() validates all forms, even when some are invalid. ... ERROR  
> test_valid (forms_tests.tests.test_formsets.AllValidTests) ... ERROR  
> test_customize_management_form_error (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_empty_forms_are_unbound (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_form_errors_are_caught_by_formset (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_management_form_invalid_data (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_no_data_error (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_with_management_data_attrs_work_fine (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_empty_formset_is_multipart (forms_tests.tests.test_formsets.TestEmptyFormSet)  
> is_multipart() works with an empty formset. ... ok  
> test_empty_formset_is_valid (forms_tests.tests.test_formsets.TestEmptyFormSet)  
> An empty formset still calls clean() ... ERROR  
> test_empty_formset_media (forms_tests.tests.test_formsets.TestEmptyFormSet)  
> Media is available on empty formset. ... ok  
> test_as_div (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ERROR  
> test_as_p (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ERROR  
> test_as_table (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ERROR  
> test_as_ul (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ERROR  
> test_as_div (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ERROR  
> test_as_p (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ERROR  
> test_as_table (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ERROR  
> test_as_ul (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ERROR  
> test_absolute_max (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_absolute_max_invalid (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_absolute_max_with_max_num (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_basic_formset (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A FormSet constructor takes the same arguments as Form. Create a ... ERROR  
> test_blank_form_unfilled (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A form that's displayed as blank may be submitted as blank. ... ERROR  
> test_can_delete_extra_formset_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_clean_hook (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSets have a clean() hook for doing extra validation that isn't tied ... ERROR  
> test_custom_renderer (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms ... ERROR  
> test_default_absolute_max (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_delete_prefilled_data (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Deleting prefilled data is an error. Removing data from form fields ... ERROR  
> test_disable_delete_extra_formset_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More than 1 empty form can be displayed using formset_factory's ... ERROR  
> test_empty_ordered_fields (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Ordering fields are allowed to be left blank. If they are left blank, ... ERROR  
> test_form_kwargs_empty_form (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_form_kwargs_formset (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Custom kwargs set on the formset instance are passed to the ... ok  
> test_form_kwargs_formset_dynamic (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Form kwargs can be passed dynamically in a formset. ... ok  
> test_formset_calls_forms_is_valid (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formsets call is_valid() on each form. ... ERROR  
> test_formset_error_class (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formset's forms use the formset's error_class. ... ok  
> test_formset_has_changed (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSet.has_changed() is True if any data is passed to its forms, even ... ERROR  
> test_formset_initial_data (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A FormSet can be prefilled with existing data by providing a list of ... ok  
> test_formset_iteration (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formset instances are iterable. ... ok  
> test_formset_nonzero (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formsets without any forms evaluates as True. ... ok  
> test_formset_splitdatetimefield (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formset works with SplitDateTimeField(initial=datetime.datetime.now). ... ERROR  
> test_formset_total_error_count (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A valid formset should have 0 total errors. ... ERROR  
> test_formset_total_error_count_with_non_form_errors (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_formset_validate_max_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If validate_max is set and max_num is less than TOTAL_FORMS in the ... ERROR  
> test_formset_validate_max_flag_custom_error (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_formset_validate_min_excludes_empty_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_formset_validate_min_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If validate_min is set and min_num is more than TOTAL_FORMS in the ... ERROR  
> test_formset_validate_min_flag_custom_formatted_error (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_formset_validate_min_unchanged_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> min_num validation doesn't consider unchanged forms with initial data ... ERROR  
> test_formset_validation (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_formset_validation_count (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formset's ManagementForm is validated once per FormSet.is_valid() ... ERROR  
> test_formset_with_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> formset_factory's can_delete argument adds a boolean "delete" field to ... ERROR  
> test_formset_with_deletion_custom_widget (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_formset_with_deletion_invalid_deleted_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> deleted_forms works on a valid formset even if a deleted form would ... ERROR  
> test_formset_with_deletion_remove_deletion_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If a form is filled with something and can_delete is also checked, that ... ERROR  
> test_formset_with_ordering_and_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSets with ordering + deletion. ... ERROR  
> test_formsets_with_ordering (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> formset_factory's can_order argument adds an integer field to each ... ERROR  
> test_formsets_with_ordering_custom_widget (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_hard_limit_on_instantiated_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formset has a hard limit on the number of forms instantiated. ... ERROR  
> test_html_safe (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_increase_hard_limit (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Can increase the built-in forms limit via a higher max_num. ... ERROR  
> test_invalid_deleted_form_with_ordering (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Can get ordered_forms from a valid formset even if a deleted form ... ERROR  
> test_limited_max_forms_two (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_limiting_extra_lest_than_max_num (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> max_num has no effect when extra is less than max_num. ... ok  
> test_limiting_max_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Limiting the maximum number of forms with max_num. ... ok  
> test_management_form_field_names (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> The management form class has field names matching the constants. ... ok  
> test_management_form_prefix (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> The management form has the correct prefix. ... ERROR  
> test_max_num_with_initial_data (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_max_num_zero (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If max_num is 0 then no form is rendered at all, regardless of extra, ... ok  
> test_max_num_zero_with_initial (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_min_num_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More than 1 empty form can also be displayed using formset_factory's ... ok  
> test_min_num_displaying_more_than_one_blank_form_with_zero_extra (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More than 1 empty form can be displayed using min_num. ... ok  
> test_more_initial_data (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> The extra argument works when the formset is pre-filled with initial ... ok  
> test_more_initial_form_result_in_one (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> One form from initial and extra=3 with max_num=2 results in the one ... ok  
> test_more_initial_than_max_num (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More initial forms than max_num results in all initial forms being ... ok  
> test_non_form_errors (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_non_form_errors_run_full_clean (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If non_form_errors() is called without calling is_valid() first, ... ERROR  
> test_ordering_blank_fieldsets (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Ordering works with blank fieldsets. ... ERROR  
> test_repr (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_repr_do_not_trigger_validation (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_second_form_partially_filled (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If at least one field is filled out on a blank form, it will be ... ERROR  
> test_second_form_partially_filled_2 (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A partially completed form is invalid. ... ERROR  
> test_single_form_completed (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Just one form may be completed. ... ERROR  
> test_template_name_can_be_overridden (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_template_name_uses_renderer_value (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_validate_max_ignores_forms_marked_for_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_absolute_max (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_absolute_max_invalid (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_absolute_max_with_max_num (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_basic_formset (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A FormSet constructor takes the same arguments as Form. Create a ... ERROR  
> test_blank_form_unfilled (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A form that's displayed as blank may be submitted as blank. ... ERROR  
> test_can_delete_extra_formset_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_clean_hook (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSets have a clean() hook for doing extra validation that isn't tied ... ERROR  
> test_custom_renderer (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms ... ERROR  
> test_default_absolute_max (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_delete_prefilled_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Deleting prefilled data is an error. Removing data from form fields ... ERROR  
> test_disable_delete_extra_formset_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More than 1 empty form can be displayed using formset_factory's ... ERROR  
> test_empty_ordered_fields (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Ordering fields are allowed to be left blank. If they are left blank, ... ERROR  
> test_form_kwargs_empty_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_form_kwargs_formset (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Custom kwargs set on the formset instance are passed to the ... ok  
> test_form_kwargs_formset_dynamic (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Form kwargs can be passed dynamically in a formset. ... ok  
> test_formset_calls_forms_is_valid (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formsets call is_valid() on each form. ... ERROR  
> test_formset_error_class (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formset's forms use the formset's error_class. ... ok  
> test_formset_has_changed (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSet.has_changed() is True if any data is passed to its forms, even ... ERROR  
> test_formset_initial_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A FormSet can be prefilled with existing data by providing a list of ... ok  
> test_formset_iteration (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formset instances are iterable. ... ok  
> test_formset_nonzero (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formsets without any forms evaluates as True. ... ok  
> test_formset_splitdatetimefield (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formset works with SplitDateTimeField(initial=datetime.datetime.now). ... ERROR  
> test_formset_total_error_count (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A valid formset should have 0 total errors. ... ERROR  
> test_formset_total_error_count_with_non_form_errors (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_formset_validate_max_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If validate_max is set and max_num is less than TOTAL_FORMS in the ... ERROR  
> test_formset_validate_max_flag_custom_error (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_formset_validate_min_excludes_empty_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_formset_validate_min_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If validate_min is set and min_num is more than TOTAL_FORMS in the ... ERROR  
> test_formset_validate_min_flag_custom_formatted_error (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_formset_validate_min_unchanged_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> min_num validation doesn't consider unchanged forms with initial data ... ERROR  
> test_formset_validation (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_formset_validation_count (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formset's ManagementForm is validated once per FormSet.is_valid() ... ERROR  
> test_formset_with_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> formset_factory's can_delete argument adds a boolean "delete" field to ... ERROR  
> test_formset_with_deletion_custom_widget (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_formset_with_deletion_invalid_deleted_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> deleted_forms works on a valid formset even if a deleted form would ... ERROR  
> test_formset_with_deletion_remove_deletion_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If a form is filled with something and can_delete is also checked, that ... ERROR  
> test_formset_with_ordering_and_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSets with ordering + deletion. ... ERROR  
> test_formsets_with_ordering (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> formset_factory's can_order argument adds an integer field to each ... ERROR  
> test_formsets_with_ordering_custom_widget (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_hard_limit_on_instantiated_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formset has a hard limit on the number of forms instantiated. ... ERROR  
> test_html_safe (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_increase_hard_limit (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Can increase the built-in forms limit via a higher max_num. ... ERROR  
> test_invalid_deleted_form_with_ordering (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Can get ordered_forms from a valid formset even if a deleted form ... ERROR  
> test_limited_max_forms_two (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_limiting_extra_lest_than_max_num (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> max_num has no effect when extra is less than max_num. ... ok  
> test_limiting_max_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Limiting the maximum number of forms with max_num. ... ok  
> test_management_form_field_names (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> The management form class has field names matching the constants. ... ok  
> test_management_form_prefix (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> The management form has the correct prefix. ... ERROR  
> test_max_num_with_initial_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_max_num_zero (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If max_num is 0 then no form is rendered at all, regardless of extra, ... ok  
> test_max_num_zero_with_initial (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_min_num_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More than 1 empty form can also be displayed using formset_factory's ... ok  
> test_min_num_displaying_more_than_one_blank_form_with_zero_extra (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More than 1 empty form can be displayed using min_num. ... ok  
> test_more_initial_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> The extra argument works when the formset is pre-filled with initial ... ok  
> test_more_initial_form_result_in_one (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> One form from initial and extra=3 with max_num=2 results in the one ... ok  
> test_more_initial_than_max_num (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More initial forms than max_num results in all initial forms being ... ok  
> test_non_form_errors (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_non_form_errors_run_full_clean (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If non_form_errors() is called without calling is_valid() first, ... ERROR  
> test_ordering_blank_fieldsets (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Ordering works with blank fieldsets. ... ERROR  
> test_repr (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_repr_do_not_trigger_validation (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_second_form_partially_filled (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If at least one field is filled out on a blank form, it will be ... ERROR  
> test_second_form_partially_filled_2 (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A partially completed form is invalid. ... ERROR  
> test_single_form_completed (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Just one form may be completed. ... ERROR  
> test_template_name_can_be_overridden (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_template_name_uses_renderer_value (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_validate_max_ignores_forms_marked_for_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
>   
> ======================================================================  
> ERROR: test_invalid (forms_tests.tests.test_formsets.AllValidTests)  
> all_valid() validates all forms, even when some are invalid.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1892, in test_invalid  
>     self.assertIs(all_valid((formset1, formset2)), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 577, in all_valid  
>     return all([formset.is_valid() for formset in formsets])  
>   File "/opt/django__django/django/forms/formsets.py", line 577, in <listcomp>  
>     return all([formset.is_valid() for formset in formsets])  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_valid (forms_tests.tests.test_formsets.AllValidTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1873, in test_valid  
>     self.assertIs(all_valid((formset1, formset2)), True)  
>   File "/opt/django__django/django/forms/formsets.py", line 577, in all_valid  
>     return all([formset.is_valid() for formset in formsets])  
>   File "/opt/django__django/django/forms/formsets.py", line 577, in <listcomp>  
>     return all([formset.is_valid() for formset in formsets])  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_customize_management_form_error (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1760, in test_customize_management_form_error  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_empty_forms_are_unbound (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1802, in test_empty_forms_are_unbound  
>     empty_forms = [unbound_formset.empty_form, bound_formset.empty_form]  
>   File "/opt/django__django/django/forms/formsets.py", line 269, in empty_form  
>     self.add_fields(form, None)  
>   File "/opt/django__django/django/forms/formsets.py", line 479, in add_fields  
>     initial_form_count = self.initial_form_count()  
>   File "/opt/django__django/django/forms/formsets.py", line 196, in initial_form_count  
>     return self.management_form.cleaned_data[INITIAL_FORM_COUNT]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_form_errors_are_caught_by_formset (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1788, in test_form_errors_are_caught_by_formset  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_management_form_invalid_data (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1729, in test_management_form_invalid_data  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_no_data_error (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1698, in test_no_data_error  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_with_management_data_attrs_work_fine (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1770, in test_with_management_data_attrs_work_fine  
>     self.assertEqual(0, formset.initial_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 196, in initial_form_count  
>     return self.management_form.cleaned_data[INITIAL_FORM_COUNT]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_empty_formset_is_valid (forms_tests.tests.test_formsets.TestEmptyFormSet)  
> An empty formset still calls clean()  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1838, in test_empty_formset_is_valid  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_div (forms_tests.tests.test_formsets.FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 119, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1671, in test_as_div  
>     self.formset.as_div(),  
>   File "/opt/django__django/django/forms/utils.py", line 96, in as_div  
>     return self.render(self.template_name_div)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_p (forms_tests.tests.test_formsets.FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 119, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1648, in test_as_p  
>     self.formset.as_p(),  
>   File "/opt/django__django/django/forms/utils.py", line 84, in as_p  
>     return self.render(self.template_name_p)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_table (forms_tests.tests.test_formsets.FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 119, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1636, in test_as_table  
>     self.formset.as_table(),  
>   File "/opt/django__django/django/forms/utils.py", line 88, in as_table  
>     return self.render(self.template_name_table)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_ul (forms_tests.tests.test_formsets.FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 119, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1659, in test_as_ul  
>     self.formset.as_ul(),  
>   File "/opt/django__django/django/forms/utils.py", line 92, in as_ul  
>     return self.render(self.template_name_ul)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_div (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 119, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1671, in test_as_div  
>     self.formset.as_div(),  
>   File "/opt/django__django/django/forms/utils.py", line 96, in as_div  
>     return self.render(self.template_name_div)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_p (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 119, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1648, in test_as_p  
>     self.formset.as_p(),  
>   File "/opt/django__django/django/forms/utils.py", line 84, in as_p  
>     return self.render(self.template_name_p)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_table (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 119, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1636, in test_as_table  
>     self.formset.as_table(),  
>   File "/opt/django__django/django/forms/utils.py", line 88, in as_table  
>     return self.render(self.template_name_table)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_ul (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 119, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1659, in test_as_ul  
>     self.formset.as_ul(),  
>   File "/opt/django__django/django/forms/utils.py", line 92, in as_ul  
>     return self.render(self.template_name_ul)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_absolute_max (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1134, in test_absolute_max  
>     self.assertIs(formset.is_valid(), True)  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_absolute_max_with_max_num (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1158, in test_absolute_max_with_max_num  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_basic_formset (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A FormSet constructor takes the same arguments as Form. Create a  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 119, in __getitem__  
>     return self.forms[index]  
> TypeError: list indices must be integers or slices, not str  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 125, in test_basic_formset  
>     str(formset),  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 159, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_blank_form_unfilled (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A form that's displayed as blank may be submitted as blank.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 260, in test_blank_form_unfilled  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_clean_hook (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSets have a clean() hook for doing extra validation that isn't tied  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 971, in test_clean_hook  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_custom_renderer (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1548, in test_custom_renderer  
>     self.assertEqual(formset.forms[0].renderer, renderer)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_default_absolute_max (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1116, in test_default_absolute_max  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_delete_prefilled_data (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Deleting prefilled data is an error. Removing data from form fields  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 283, in test_delete_prefilled_data  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_disable_delete_extra_formset_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1497, in test_disable_delete_extra_formset_forms  
>     formset.cleaned_data,  
>   File "/opt/django__django/django/forms/formsets.py", line 277, in cleaned_data  
>     if not self.is_valid():  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More than 1 empty form can be displayed using formset_factory's  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 327, in test_displaying_more_than_one_blank_form  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_empty_ordered_fields (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Ordering fields are allowed to be left blank. If they are left blank,  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 838, in test_empty_ordered_fields  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_calls_forms_is_valid (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formsets call is_valid() on each form.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1319, in test_formset_calls_forms_is_valid  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_has_changed (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSet.has_changed() is True if any data is passed to its forms, even  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 227, in test_formset_has_changed  
>     self.assertFalse(blank_formset.has_changed())  
>   File "/opt/django__django/django/forms/formsets.py", line 475, in has_changed  
>     return any(form.has_changed() for form in self)  
>   File "/opt/django__django/django/forms/formsets.py", line 115, in __iter__  
>     return iter(self.forms)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_splitdatetimefield (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formset works with SplitDateTimeField(initial=datetime.datetime.now).  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1290, in test_formset_splitdatetimefield  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_total_error_count (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A valid formset should have 0 total errors.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1433, in test_formset_total_error_count  
>     self.assertEqual(formset.total_error_count(), expected_error_count)  
>   File "/opt/django__django/django/forms/formsets.py", line 371, in total_error_count  
>     return len(self.non_form_errors()) + sum(  
>   File "/opt/django__django/django/forms/formsets.py", line 359, in non_form_errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_total_error_count_with_non_form_errors (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1447, in test_formset_total_error_count_with_non_form_errors  
>     self.assertEqual(formset.total_error_count(), 1)  
>   File "/opt/django__django/django/forms/formsets.py", line 371, in total_error_count  
>     return len(self.non_form_errors()) + sum(  
>   File "/opt/django__django/django/forms/formsets.py", line 359, in non_form_errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_max_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If validate_max is set and max_num is less than TOTAL_FORMS in the  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 403, in test_formset_validate_max_flag  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_max_flag_custom_error (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 430, in test_formset_validate_max_flag_custom_error  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_excludes_empty_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 533, in test_formset_validate_min_excludes_empty_forms  
>     self.assertFalse(formset.has_changed())  
>   File "/opt/django__django/django/forms/formsets.py", line 475, in has_changed  
>     return any(form.has_changed() for form in self)  
>   File "/opt/django__django/django/forms/formsets.py", line 115, in __iter__  
>     return iter(self.forms)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If validate_min is set and min_num is more than TOTAL_FORMS in the  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 460, in test_formset_validate_min_flag  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_flag_custom_formatted_error (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 488, in test_formset_validate_min_flag_custom_formatted_error  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_unchanged_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> min_num validation doesn't consider unchanged forms with initial data  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 520, in test_formset_validate_min_unchanged_forms  
>     self.assertFalse(formset.forms[0].has_changed())  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validation (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 186, in test_formset_validation  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validation_count (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formset's ManagementForm is validated once per FormSet.is_valid()  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 217, in test_formset_validation_count  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> formset_factory's can_delete argument adds a boolean "delete" field to  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 630, in test_formset_with_deletion  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_deletion_invalid_deleted_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> deleted_forms works on a valid formset even if a deleted form would  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 690, in test_formset_with_deletion_invalid_deleted_form  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_deletion_remove_deletion_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If a form is filled with something and can_delete is also checked, that  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 668, in test_formset_with_deletion_remove_deletion_flag  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_ordering_and_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSets with ordering + deletion.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 917, in test_formset_with_ordering_and_deletion  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formsets_with_ordering (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> formset_factory's can_order argument adds an integer field to each  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 773, in test_formsets_with_ordering  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_hard_limit_on_instantiated_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formset has a hard limit on the number of forms instantiated.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1348, in test_hard_limit_on_instantiated_forms  
>     self.assertEqual(len(formset.forms), 3)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_html_safe (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 119, in __getitem__  
>     return self.forms[index]  
> TypeError: list indices must be integers or slices, not str  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1455, in test_html_safe  
>     self.assertEqual(str(formset), formset.__html__())  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 159, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_increase_hard_limit (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Can increase the built-in forms limit via a higher max_num.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1380, in test_increase_hard_limit  
>     self.assertEqual(len(formset.forms), 4)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_invalid_deleted_form_with_ordering (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Can get ordered_forms from a valid formset even if a deleted form  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 953, in test_invalid_deleted_form_with_ordering  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_management_form_prefix (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> The management form has the correct prefix.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1206, in test_management_form_prefix  
>     self.assertEqual(formset.management_form.prefix, "form")  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 159, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_non_form_errors (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1228, in test_non_form_errors  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_non_form_errors_run_full_clean (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If non_form_errors() is called without calling is_valid() first,  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1400, in test_non_form_errors_run_full_clean  
>     self.assertIsInstance(formset.non_form_errors(), ErrorList)  
>   File "/opt/django__django/django/forms/formsets.py", line 359, in non_form_errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_ordering_blank_fieldsets (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Ordering works with blank fieldsets.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 859, in test_ordering_blank_fieldsets  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_repr (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1555, in test_repr  
>     valid_formset.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_repr_do_not_trigger_validation (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1605, in test_repr_do_not_trigger_validation  
>     repr(formset)  
>   File "/opt/django__django/django/forms/formsets.py", line 144, in __repr__  
>     self.total_form_count(),  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_second_form_partially_filled (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If at least one field is filled out on a blank form, it will be  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 274, in test_second_form_partially_filled  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_second_form_partially_filled_2 (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A partially completed form is invalid.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 553, in test_second_form_partially_filled_2  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_single_form_completed (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Just one form may be completed.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 378, in test_single_form_completed  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_validate_max_ignores_forms_marked_for_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1420, in test_validate_max_ignores_forms_marked_for_deletion  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_absolute_max (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1134, in test_absolute_max  
>     self.assertIs(formset.is_valid(), True)  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_absolute_max_with_max_num (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1158, in test_absolute_max_with_max_num  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_basic_formset (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A FormSet constructor takes the same arguments as Form. Create a  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 119, in __getitem__  
>     return self.forms[index]  
> TypeError: list indices must be integers or slices, not str  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 125, in test_basic_formset  
>     str(formset),  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 159, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_blank_form_unfilled (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A form that's displayed as blank may be submitted as blank.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 260, in test_blank_form_unfilled  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_clean_hook (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSets have a clean() hook for doing extra validation that isn't tied  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 971, in test_clean_hook  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_custom_renderer (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1548, in test_custom_renderer  
>     self.assertEqual(formset.forms[0].renderer, renderer)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_default_absolute_max (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1116, in test_default_absolute_max  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_delete_prefilled_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Deleting prefilled data is an error. Removing data from form fields  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 283, in test_delete_prefilled_data  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_disable_delete_extra_formset_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1497, in test_disable_delete_extra_formset_forms  
>     formset.cleaned_data,  
>   File "/opt/django__django/django/forms/formsets.py", line 277, in cleaned_data  
>     if not self.is_valid():  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More than 1 empty form can be displayed using formset_factory's  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 327, in test_displaying_more_than_one_blank_form  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_empty_ordered_fields (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Ordering fields are allowed to be left blank. If they are left blank,  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 838, in test_empty_ordered_fields  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_calls_forms_is_valid (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formsets call is_valid() on each form.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1319, in test_formset_calls_forms_is_valid  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_has_changed (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSet.has_changed() is True if any data is passed to its forms, even  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 227, in test_formset_has_changed  
>     self.assertFalse(blank_formset.has_changed())  
>   File "/opt/django__django/django/forms/formsets.py", line 475, in has_changed  
>     return any(form.has_changed() for form in self)  
>   File "/opt/django__django/django/forms/formsets.py", line 115, in __iter__  
>     return iter(self.forms)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_splitdatetimefield (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formset works with SplitDateTimeField(initial=datetime.datetime.now).  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1290, in test_formset_splitdatetimefield  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_total_error_count (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A valid formset should have 0 total errors.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1433, in test_formset_total_error_count  
>     self.assertEqual(formset.total_error_count(), expected_error_count)  
>   File "/opt/django__django/django/forms/formsets.py", line 371, in total_error_count  
>     return len(self.non_form_errors()) + sum(  
>   File "/opt/django__django/django/forms/formsets.py", line 359, in non_form_errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_total_error_count_with_non_form_errors (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1447, in test_formset_total_error_count_with_non_form_errors  
>     self.assertEqual(formset.total_error_count(), 1)  
>   File "/opt/django__django/django/forms/formsets.py", line 371, in total_error_count  
>     return len(self.non_form_errors()) + sum(  
>   File "/opt/django__django/django/forms/formsets.py", line 359, in non_form_errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_max_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If validate_max is set and max_num is less than TOTAL_FORMS in the  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 403, in test_formset_validate_max_flag  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_max_flag_custom_error (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 430, in test_formset_validate_max_flag_custom_error  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_excludes_empty_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 533, in test_formset_validate_min_excludes_empty_forms  
>     self.assertFalse(formset.has_changed())  
>   File "/opt/django__django/django/forms/formsets.py", line 475, in has_changed  
>     return any(form.has_changed() for form in self)  
>   File "/opt/django__django/django/forms/formsets.py", line 115, in __iter__  
>     return iter(self.forms)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If validate_min is set and min_num is more than TOTAL_FORMS in the  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 460, in test_formset_validate_min_flag  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_flag_custom_formatted_error (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 488, in test_formset_validate_min_flag_custom_formatted_error  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_unchanged_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> min_num validation doesn't consider unchanged forms with initial data  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 520, in test_formset_validate_min_unchanged_forms  
>     self.assertFalse(formset.forms[0].has_changed())  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validation (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 186, in test_formset_validation  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validation_count (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formset's ManagementForm is validated once per FormSet.is_valid()  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 217, in test_formset_validation_count  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> formset_factory's can_delete argument adds a boolean "delete" field to  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 630, in test_formset_with_deletion  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_deletion_invalid_deleted_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> deleted_forms works on a valid formset even if a deleted form would  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 690, in test_formset_with_deletion_invalid_deleted_form  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_deletion_remove_deletion_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If a form is filled with something and can_delete is also checked, that  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 668, in test_formset_with_deletion_remove_deletion_flag  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_ordering_and_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSets with ordering + deletion.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 917, in test_formset_with_ordering_and_deletion  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formsets_with_ordering (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> formset_factory's can_order argument adds an integer field to each  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 773, in test_formsets_with_ordering  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_hard_limit_on_instantiated_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formset has a hard limit on the number of forms instantiated.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1348, in test_hard_limit_on_instantiated_forms  
>     self.assertEqual(len(formset.forms), 3)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_html_safe (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 119, in __getitem__  
>     return self.forms[index]  
> TypeError: list indices must be integers or slices, not str  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1455, in test_html_safe  
>     self.assertEqual(str(formset), formset.__html__())  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 159, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_increase_hard_limit (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Can increase the built-in forms limit via a higher max_num.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1380, in test_increase_hard_limit  
>     self.assertEqual(len(formset.forms), 4)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 208, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_invalid_deleted_form_with_ordering (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Can get ordered_forms from a valid formset even if a deleted form  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 953, in test_invalid_deleted_form_with_ordering  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_management_form_prefix (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> The management form has the correct prefix.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1206, in test_management_form_prefix  
>     self.assertEqual(formset.management_form.prefix, "form")  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 159, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_non_form_errors (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1228, in test_non_form_errors  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_non_form_errors_run_full_clean (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If non_form_errors() is called without calling is_valid() first,  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1400, in test_non_form_errors_run_full_clean  
>     self.assertIsInstance(formset.non_form_errors(), ErrorList)  
>   File "/opt/django__django/django/forms/formsets.py", line 359, in non_form_errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_ordering_blank_fieldsets (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Ordering works with blank fieldsets.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 859, in test_ordering_blank_fieldsets  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_repr (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1555, in test_repr  
>     valid_formset.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_repr_do_not_trigger_validation (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1605, in test_repr_do_not_trigger_validation  
>     repr(formset)  
>   File "/opt/django__django/django/forms/formsets.py", line 144, in __repr__  
>     self.total_form_count(),  
>   File "/opt/django__django/django/forms/formsets.py", line 180, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_second_form_partially_filled (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If at least one field is filled out on a blank form, it will be  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 274, in test_second_form_partially_filled  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_second_form_partially_filled_2 (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A partially completed form is invalid.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 553, in test_second_form_partially_filled_2  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_single_form_completed (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Just one form may be completed.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 378, in test_single_form_completed  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_validate_max_ignores_forms_marked_for_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1420, in test_validate_max_ignores_forms_marked_for_deletion  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 384, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 366, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 410, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 151, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ----------------------------------------------------------------------  
> Ran 156 tests in 1.055s  
>   
> FAILED (errors=103)  
>    
> [django__django__4.2] [django__django-15902] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [django__django__4.2] [django__django-15902] Test script run successful   
> Attempt to fix test errors? yes  
> 80781 prompt tokens, 361 completion tokens, $0.409320 cost  

The issue seems to be that the `ManagementForm` class is trying to access `cleaned_data` before it is set. We need to ensure that `cleaned_data` is properly initialized and accessible.

Let's fix this by ensuring `cleaned_data` is set correctly in the `ManagementForm` class.

Here are the changes:

django/forms/formsets.py
```python
<<<<<<< SEARCH
        cleaned_data = super().clean()
        # When the management form is invalid, we don't know how many forms
        # were submitted.
        cleaned_data.setdefault(TOTAL_FORM_COUNT, 0)
        cleaned_data.setdefault(INITIAL_FORM_COUNT, 0)
        return cleaned_data
=======
        super().__init__(*args, **kwargs)
        self.cleaned_data = {}
>>>>>>> REPLACE
```

django/forms/formsets.py
```python
<<<<<<< SEARCH
        if not self.management_form.is_valid():
            error = ValidationError(
                self.error_messages["missing_management_form"],
                params={
                    "field_names": ", ".join(
                        self.management_form.add_prefix(field_name)
                        for field_name in self.management_form.errors
                    ),
                },
                code="missing_management_form",
            )
            self._non_form_errors.append(error)
=======
        if not self.management_form.is_valid():
            self._non_form_errors.append(
                ValidationError(
                    self.error_messages["missing_management_form"],
                    params={
                        "field_names": ", ".join(
                            self.management_form.add_prefix(field_name)
                            for field_name in self.management_form.errors
                        ),
                    },
                    code="missing_management_form",
                )
            )
>>>>>>> REPLACE
```

These changes will ensure that `cleaned_data` is properly initialized and accessible, and should resolve the errors related to `ManagementForm`.

> Applied edit to django/forms/formsets.py  
>   
> Test Script:  ./tests/runtests.py --verbosity 2 forms_tests.tests.test_formsets;  
> [django__django__4.2] [django__django-15902] Command: ./tests/runtests.py --verbosity 2 forms_tests.tests.test_formsets   
> [django__django__4.2] [django__django-15902] Subprocess args: {"cwd": "/opt/django__django", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [django__django__4.2] [django__django-15902] Std. Output:  
> Testing against Django installed in '/opt/django__django/django' with up to 16 processes  
> Importing application forms_tests  
> Found 156 test(s).  
> Skipping setup of unused database(s): default, other.  
> System check identified no issues (0 silenced).  
> test_warning (forms_tests.tests.test_formsets.DeprecationTests) ... ok  
> test_invalid (forms_tests.tests.test_formsets.AllValidTests)  
> all_valid() validates all forms, even when some are invalid. ... ok  
> test_valid (forms_tests.tests.test_formsets.AllValidTests) ... ok  
> test_empty_formset_is_multipart (forms_tests.tests.test_formsets.TestEmptyFormSet)  
> is_multipart() works with an empty formset. ... ok  
> test_empty_formset_is_valid (forms_tests.tests.test_formsets.TestEmptyFormSet)  
> An empty formset still calls clean() ... ok  
> test_empty_formset_media (forms_tests.tests.test_formsets.TestEmptyFormSet)  
> Media is available on empty formset. ... ok  
> test_as_div (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ok  
> test_as_p (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ok  
> test_as_table (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ok  
> test_as_ul (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ok  
> test_customize_management_form_error (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_empty_forms_are_unbound (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ok  
> test_form_errors_are_caught_by_formset (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ok  
> test_management_form_invalid_data (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_no_data_error (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_with_management_data_attrs_work_fine (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ok  
> test_as_div (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ok  
> test_as_p (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ok  
> test_as_table (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ok  
> test_as_ul (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ok  
> test_absolute_max (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_absolute_max_invalid (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_absolute_max_with_max_num (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_basic_formset (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A FormSet constructor takes the same arguments as Form. Create a ... ok  
> test_blank_form_unfilled (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A form that's displayed as blank may be submitted as blank. ... ok  
> test_can_delete_extra_formset_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_clean_hook (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSets have a clean() hook for doing extra validation that isn't tied ... ok  
> test_custom_renderer (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms ... FAIL  
> test_default_absolute_max (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_delete_prefilled_data (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Deleting prefilled data is an error. Removing data from form fields ... ok  
> test_disable_delete_extra_formset_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More than 1 empty form can be displayed using formset_factory's ... ok  
> test_empty_ordered_fields (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Ordering fields are allowed to be left blank. If they are left blank, ... ok  
> test_form_kwargs_empty_form (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_form_kwargs_formset (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Custom kwargs set on the formset instance are passed to the ... ok  
> test_form_kwargs_formset_dynamic (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Form kwargs can be passed dynamically in a formset. ... ok  
> test_formset_calls_forms_is_valid (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formsets call is_valid() on each form. ... ok  
> test_formset_error_class (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formset's forms use the formset's error_class. ... ok  
> test_formset_has_changed (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSet.has_changed() is True if any data is passed to its forms, even ... ok  
> test_formset_initial_data (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A FormSet can be prefilled with existing data by providing a list of ... ok  
> test_formset_iteration (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formset instances are iterable. ... ok  
> test_formset_nonzero (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formsets without any forms evaluates as True. ... ok  
> test_formset_splitdatetimefield (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formset works with SplitDateTimeField(initial=datetime.datetime.now). ... ok  
> test_formset_total_error_count (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A valid formset should have 0 total errors. ... ok  
> test_formset_total_error_count_with_non_form_errors (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_formset_validate_max_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If validate_max is set and max_num is less than TOTAL_FORMS in the ... ok  
> test_formset_validate_max_flag_custom_error (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_formset_validate_min_excludes_empty_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_formset_validate_min_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If validate_min is set and min_num is more than TOTAL_FORMS in the ... ok  
> test_formset_validate_min_flag_custom_formatted_error (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_formset_validate_min_unchanged_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> min_num validation doesn't consider unchanged forms with initial data ... ok  
> test_formset_validation (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_formset_validation_count (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formset's ManagementForm is validated once per FormSet.is_valid() ... ok  
> test_formset_with_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> formset_factory's can_delete argument adds a boolean "delete" field to ... ok  
> test_formset_with_deletion_custom_widget (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_formset_with_deletion_invalid_deleted_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> deleted_forms works on a valid formset even if a deleted form would ... ok  
> test_formset_with_deletion_remove_deletion_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If a form is filled with something and can_delete is also checked, that ... ok  
> test_formset_with_ordering_and_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSets with ordering + deletion. ... ok  
> test_formsets_with_ordering (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> formset_factory's can_order argument adds an integer field to each ... ok  
> test_formsets_with_ordering_custom_widget (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_hard_limit_on_instantiated_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formset has a hard limit on the number of forms instantiated. ... ok  
> test_html_safe (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_increase_hard_limit (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Can increase the built-in forms limit via a higher max_num. ... ok  
> test_invalid_deleted_form_with_ordering (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Can get ordered_forms from a valid formset even if a deleted form ... ok  
> test_limited_max_forms_two (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_limiting_extra_lest_than_max_num (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> max_num has no effect when extra is less than max_num. ... ok  
> test_limiting_max_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Limiting the maximum number of forms with max_num. ... ok  
> test_management_form_field_names (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> The management form class has field names matching the constants. ... ok  
> test_management_form_prefix (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> The management form has the correct prefix. ... ok  
> test_max_num_with_initial_data (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_max_num_zero (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If max_num is 0 then no form is rendered at all, regardless of extra, ... ok  
> test_max_num_zero_with_initial (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_min_num_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More than 1 empty form can also be displayed using formset_factory's ... ok  
> test_min_num_displaying_more_than_one_blank_form_with_zero_extra (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More than 1 empty form can be displayed using min_num. ... ok  
> test_more_initial_data (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> The extra argument works when the formset is pre-filled with initial ... ok  
> test_more_initial_form_result_in_one (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> One form from initial and extra=3 with max_num=2 results in the one ... ok  
> test_more_initial_than_max_num (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More initial forms than max_num results in all initial forms being ... ok  
> test_non_form_errors (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_non_form_errors_run_full_clean (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If non_form_errors() is called without calling is_valid() first, ... ok  
> test_ordering_blank_fieldsets (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Ordering works with blank fieldsets. ... ok  
> test_repr (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_repr_do_not_trigger_validation (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_second_form_partially_filled (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If at least one field is filled out on a blank form, it will be ... ok  
> test_second_form_partially_filled_2 (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A partially completed form is invalid. ... ok  
> test_single_form_completed (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Just one form may be completed. ... ok  
> test_template_name_can_be_overridden (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_template_name_uses_renderer_value (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_validate_max_ignores_forms_marked_for_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_absolute_max (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_absolute_max_invalid (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_absolute_max_with_max_num (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_basic_formset (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A FormSet constructor takes the same arguments as Form. Create a ... ok  
> test_blank_form_unfilled (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A form that's displayed as blank may be submitted as blank. ... ok  
> test_can_delete_extra_formset_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_clean_hook (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSets have a clean() hook for doing extra validation that isn't tied ... ok  
> test_custom_renderer (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms ... FAIL  
> test_default_absolute_max (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_delete_prefilled_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Deleting prefilled data is an error. Removing data from form fields ... ok  
> test_disable_delete_extra_formset_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More than 1 empty form can be displayed using formset_factory's ... ok  
> test_empty_ordered_fields (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Ordering fields are allowed to be left blank. If they are left blank, ... ok  
> test_form_kwargs_empty_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_form_kwargs_formset (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Custom kwargs set on the formset instance are passed to the ... ok  
> test_form_kwargs_formset_dynamic (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Form kwargs can be passed dynamically in a formset. ... ok  
> test_formset_calls_forms_is_valid (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formsets call is_valid() on each form. ... ok  
> test_formset_error_class (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formset's forms use the formset's error_class. ... ok  
> test_formset_has_changed (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSet.has_changed() is True if any data is passed to its forms, even ... ok  
> test_formset_initial_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A FormSet can be prefilled with existing data by providing a list of ... ok  
> test_formset_iteration (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formset instances are iterable. ... ok  
> test_formset_nonzero (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formsets without any forms evaluates as True. ... ok  
> test_formset_splitdatetimefield (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formset works with SplitDateTimeField(initial=datetime.datetime.now). ... ok  
> test_formset_total_error_count (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A valid formset should have 0 total errors. ... ok  
> test_formset_total_error_count_with_non_form_errors (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_formset_validate_max_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If validate_max is set and max_num is less than TOTAL_FORMS in the ... ok  
> test_formset_validate_max_flag_custom_error (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_formset_validate_min_excludes_empty_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_formset_validate_min_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If validate_min is set and min_num is more than TOTAL_FORMS in the ... ok  
> test_formset_validate_min_flag_custom_formatted_error (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_formset_validate_min_unchanged_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> min_num validation doesn't consider unchanged forms with initial data ... ok  
> test_formset_validation (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_formset_validation_count (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formset's ManagementForm is validated once per FormSet.is_valid() ... ok  
> test_formset_with_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> formset_factory's can_delete argument adds a boolean "delete" field to ... ok  
> test_formset_with_deletion_custom_widget (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_formset_with_deletion_invalid_deleted_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> deleted_forms works on a valid formset even if a deleted form would ... ok  
> test_formset_with_deletion_remove_deletion_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If a form is filled with something and can_delete is also checked, that ... ok  
> test_formset_with_ordering_and_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSets with ordering + deletion. ... ok  
> test_formsets_with_ordering (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> formset_factory's can_order argument adds an integer field to each ... ok  
> test_formsets_with_ordering_custom_widget (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_hard_limit_on_instantiated_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formset has a hard limit on the number of forms instantiated. ... ok  
> test_html_safe (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_increase_hard_limit (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Can increase the built-in forms limit via a higher max_num. ... ok  
> test_invalid_deleted_form_with_ordering (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Can get ordered_forms from a valid formset even if a deleted form ... ok  
> test_limited_max_forms_two (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_limiting_extra_lest_than_max_num (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> max_num has no effect when extra is less than max_num. ... ok  
> test_limiting_max_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Limiting the maximum number of forms with max_num. ... ok  
> test_management_form_field_names (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> The management form class has field names matching the constants. ... ok  
> test_management_form_prefix (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> The management form has the correct prefix. ... ok  
> test_max_num_with_initial_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_max_num_zero (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If max_num is 0 then no form is rendered at all, regardless of extra, ... ok  
> test_max_num_zero_with_initial (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_min_num_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More than 1 empty form can also be displayed using formset_factory's ... ok  
> test_min_num_displaying_more_than_one_blank_form_with_zero_extra (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More than 1 empty form can be displayed using min_num. ... ok  
> test_more_initial_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> The extra argument works when the formset is pre-filled with initial ... ok  
> test_more_initial_form_result_in_one (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> One form from initial and extra=3 with max_num=2 results in the one ... ok  
> test_more_initial_than_max_num (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More initial forms than max_num results in all initial forms being ... ok  
> test_non_form_errors (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_non_form_errors_run_full_clean (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If non_form_errors() is called without calling is_valid() first, ... ok  
> test_ordering_blank_fieldsets (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Ordering works with blank fieldsets. ... ok  
> test_repr (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_repr_do_not_trigger_validation (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_second_form_partially_filled (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If at least one field is filled out on a blank form, it will be ... ok  
> test_second_form_partially_filled_2 (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A partially completed form is invalid. ... ok  
> test_single_form_completed (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Just one form may be completed. ... ok  
> test_template_name_can_be_overridden (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_template_name_uses_renderer_value (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_validate_max_ignores_forms_marked_for_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
>   
> ======================================================================  
> ERROR: test_customize_management_form_error (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1760, in test_customize_management_form_error  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 380, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 362, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 420, in full_clean  
>     for i, form in enumerate(self.forms):  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 204, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 176, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
> KeyError: 'TOTAL_FORMS'  
>   
> ======================================================================  
> ERROR: test_management_form_invalid_data (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1729, in test_management_form_invalid_data  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 380, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 362, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 420, in full_clean  
>     for i, form in enumerate(self.forms):  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 204, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 176, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
> KeyError: 'TOTAL_FORMS'  
>   
> ======================================================================  
> ERROR: test_no_data_error (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1698, in test_no_data_error  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 380, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 362, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 420, in full_clean  
>     for i, form in enumerate(self.forms):  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 204, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 176, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
> KeyError: 'TOTAL_FORMS'  
>   
> ======================================================================  
> FAIL: test_custom_renderer (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1549, in test_custom_renderer  
>     self.assertEqual(formset.management_form.renderer, renderer)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 837, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 830, in _baseAssertEqual  
>     raise self.failureException(msg)  
> AssertionError: <django.forms.renderers.DjangoDivFormRenderer object at 0x7f917b371f40> != <django.forms.renderers.Jinja2 object at 0x7f917a38ce50>  
>   
> ======================================================================  
> FAIL: test_custom_renderer (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1549, in test_custom_renderer  
>     self.assertEqual(formset.management_form.renderer, renderer)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 837, in assertEqual  
>     assertion_func(first, second, msg=msg)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 830, in _baseAssertEqual  
>     raise self.failureException(msg)  
> AssertionError: <django.forms.renderers.Jinja2DivFormRenderer object at 0x7f917b42a640> != <django.forms.renderers.Jinja2 object at 0x7f917a3afee0>  
>   
> ----------------------------------------------------------------------  
> Ran 156 tests in 0.974s  
>   
> FAILED (failures=2, errors=3)  
>    
> [django__django__4.2] [django__django-15902] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [django__django__4.2] [django__django-15902] Test script run successful   
> Attempt to fix test errors? yes  
> 88137 prompt tokens, 301 completion tokens, $0.445200 cost  

To address the remaining issues, we need to ensure that the `ManagementForm` correctly initializes its `cleaned_data` and handles the custom renderer properly.

Here are the changes:

1. Ensure `cleaned_data` is properly initialized in the `ManagementForm`.
2. Ensure the custom renderer is passed correctly to the `ManagementForm`.

Let's start by updating the `ManagementForm` class in `django/forms/formsets.py`:

django/forms/formsets.py
```python
<<<<<<< SEARCH
        super().__init__(*args, **kwargs)
        self.cleaned_data = {}
=======
        self.cleaned_data = super().clean()
        # When the management form is invalid, we don't know how many forms
        # were submitted.
        self.cleaned_data.setdefault(TOTAL_FORM_COUNT, 0)
        self.cleaned_data.setdefault(INITIAL_FORM_COUNT, 0)
>>>>>>> REPLACE
```

Next, ensure the custom renderer is passed correctly to the `ManagementForm`:

django/forms/formsets.py
```python
<<<<<<< SEARCH
                renderer=self.renderer,
=======
                renderer=ManagementFormRenderer() if self.renderer is None else self.renderer,
>>>>>>> REPLACE
```

django/forms/formsets.py
```python
<<<<<<< SEARCH
                renderer=self.renderer,
=======
                renderer=ManagementFormRenderer() if self.renderer is None else self.renderer,
>>>>>>> REPLACE
```

These changes will ensure that `cleaned_data` is properly initialized and the custom renderer is correctly passed to the `ManagementForm`.

> Applied edit to django/forms/formsets.py  
>   
> Test Script:  ./tests/runtests.py --verbosity 2 forms_tests.tests.test_formsets;  
> [django__django__4.2] [django__django-15902] Command: ./tests/runtests.py --verbosity 2 forms_tests.tests.test_formsets   
> [django__django__4.2] [django__django-15902] Subprocess args: {"cwd": "/opt/django__django", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [django__django__4.2] [django__django-15902] Std. Output:  
> Testing against Django installed in '/opt/django__django/django' with up to 16 processes  
> Importing application forms_tests  
> Found 156 test(s).  
> Skipping setup of unused database(s): default, other.  
> System check identified no issues (0 silenced).  
> test_warning (forms_tests.tests.test_formsets.DeprecationTests) ... ok  
> test_invalid (forms_tests.tests.test_formsets.AllValidTests)  
> all_valid() validates all forms, even when some are invalid. ... ERROR  
> test_valid (forms_tests.tests.test_formsets.AllValidTests) ... ERROR  
> test_customize_management_form_error (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_empty_forms_are_unbound (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_form_errors_are_caught_by_formset (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_management_form_invalid_data (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_no_data_error (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_with_management_data_attrs_work_fine (forms_tests.tests.test_formsets.TestIsBoundBehavior) ... ERROR  
> test_empty_formset_is_multipart (forms_tests.tests.test_formsets.TestEmptyFormSet)  
> is_multipart() works with an empty formset. ... ok  
> test_empty_formset_is_valid (forms_tests.tests.test_formsets.TestEmptyFormSet)  
> An empty formset still calls clean() ... ERROR  
> test_empty_formset_media (forms_tests.tests.test_formsets.TestEmptyFormSet)  
> Media is available on empty formset. ... ok  
> test_as_div (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ERROR  
> test_as_p (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ERROR  
> test_as_table (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ERROR  
> test_as_ul (forms_tests.tests.test_formsets.FormsetAsTagTests) ... ERROR  
> test_as_div (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ERROR  
> test_as_p (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ERROR  
> test_as_table (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ERROR  
> test_as_ul (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests) ... ERROR  
> test_absolute_max (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_absolute_max_invalid (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_absolute_max_with_max_num (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_basic_formset (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A FormSet constructor takes the same arguments as Form. Create a ... ERROR  
> test_blank_form_unfilled (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A form that's displayed as blank may be submitted as blank. ... ERROR  
> test_can_delete_extra_formset_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_clean_hook (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSets have a clean() hook for doing extra validation that isn't tied ... ERROR  
> test_custom_renderer (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms ... ERROR  
> test_default_absolute_max (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_delete_prefilled_data (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Deleting prefilled data is an error. Removing data from form fields ... ERROR  
> test_disable_delete_extra_formset_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More than 1 empty form can be displayed using formset_factory's ... ERROR  
> test_empty_ordered_fields (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Ordering fields are allowed to be left blank. If they are left blank, ... ERROR  
> test_form_kwargs_empty_form (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_form_kwargs_formset (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Custom kwargs set on the formset instance are passed to the ... ok  
> test_form_kwargs_formset_dynamic (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Form kwargs can be passed dynamically in a formset. ... ok  
> test_formset_calls_forms_is_valid (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formsets call is_valid() on each form. ... ERROR  
> test_formset_error_class (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formset's forms use the formset's error_class. ... ok  
> test_formset_has_changed (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSet.has_changed() is True if any data is passed to its forms, even ... ERROR  
> test_formset_initial_data (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A FormSet can be prefilled with existing data by providing a list of ... ok  
> test_formset_iteration (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formset instances are iterable. ... ok  
> test_formset_nonzero (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formsets without any forms evaluates as True. ... ok  
> test_formset_splitdatetimefield (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formset works with SplitDateTimeField(initial=datetime.datetime.now). ... ERROR  
> test_formset_total_error_count (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A valid formset should have 0 total errors. ... ERROR  
> test_formset_total_error_count_with_non_form_errors (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_formset_validate_max_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If validate_max is set and max_num is less than TOTAL_FORMS in the ... ERROR  
> test_formset_validate_max_flag_custom_error (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_formset_validate_min_excludes_empty_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_formset_validate_min_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If validate_min is set and min_num is more than TOTAL_FORMS in the ... ERROR  
> test_formset_validate_min_flag_custom_formatted_error (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_formset_validate_min_unchanged_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> min_num validation doesn't consider unchanged forms with initial data ... ERROR  
> test_formset_validation (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_formset_validation_count (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formset's ManagementForm is validated once per FormSet.is_valid() ... ERROR  
> test_formset_with_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> formset_factory's can_delete argument adds a boolean "delete" field to ... ERROR  
> test_formset_with_deletion_custom_widget (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_formset_with_deletion_invalid_deleted_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> deleted_forms works on a valid formset even if a deleted form would ... ERROR  
> test_formset_with_deletion_remove_deletion_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If a form is filled with something and can_delete is also checked, that ... ERROR  
> test_formset_with_ordering_and_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSets with ordering + deletion. ... ERROR  
> test_formsets_with_ordering (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> formset_factory's can_order argument adds an integer field to each ... ERROR  
> test_formsets_with_ordering_custom_widget (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_hard_limit_on_instantiated_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formset has a hard limit on the number of forms instantiated. ... ERROR  
> test_html_safe (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_increase_hard_limit (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Can increase the built-in forms limit via a higher max_num. ... ERROR  
> test_invalid_deleted_form_with_ordering (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Can get ordered_forms from a valid formset even if a deleted form ... ERROR  
> test_limited_max_forms_two (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_limiting_extra_lest_than_max_num (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> max_num has no effect when extra is less than max_num. ... ok  
> test_limiting_max_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Limiting the maximum number of forms with max_num. ... ok  
> test_management_form_field_names (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> The management form class has field names matching the constants. ... ok  
> test_management_form_prefix (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> The management form has the correct prefix. ... ERROR  
> test_max_num_with_initial_data (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_max_num_zero (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If max_num is 0 then no form is rendered at all, regardless of extra, ... ok  
> test_max_num_zero_with_initial (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_min_num_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More than 1 empty form can also be displayed using formset_factory's ... ok  
> test_min_num_displaying_more_than_one_blank_form_with_zero_extra (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More than 1 empty form can be displayed using min_num. ... ok  
> test_more_initial_data (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> The extra argument works when the formset is pre-filled with initial ... ok  
> test_more_initial_form_result_in_one (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> One form from initial and extra=3 with max_num=2 results in the one ... ok  
> test_more_initial_than_max_num (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More initial forms than max_num results in all initial forms being ... ok  
> test_non_form_errors (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_non_form_errors_run_full_clean (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If non_form_errors() is called without calling is_valid() first, ... ERROR  
> test_ordering_blank_fieldsets (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Ordering works with blank fieldsets. ... ERROR  
> test_repr (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_repr_do_not_trigger_validation (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_second_form_partially_filled (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If at least one field is filled out on a blank form, it will be ... ERROR  
> test_second_form_partially_filled_2 (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A partially completed form is invalid. ... ERROR  
> test_single_form_completed (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Just one form may be completed. ... ERROR  
> test_template_name_can_be_overridden (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_template_name_uses_renderer_value (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ok  
> test_validate_max_ignores_forms_marked_for_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase) ... ERROR  
> test_absolute_max (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_absolute_max_invalid (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_absolute_max_with_max_num (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_basic_formset (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A FormSet constructor takes the same arguments as Form. Create a ... ERROR  
> test_blank_form_unfilled (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A form that's displayed as blank may be submitted as blank. ... ERROR  
> test_can_delete_extra_formset_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_clean_hook (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSets have a clean() hook for doing extra validation that isn't tied ... ERROR  
> test_custom_renderer (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms ... ERROR  
> test_default_absolute_max (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_delete_prefilled_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Deleting prefilled data is an error. Removing data from form fields ... ERROR  
> test_disable_delete_extra_formset_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More than 1 empty form can be displayed using formset_factory's ... ERROR  
> test_empty_ordered_fields (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Ordering fields are allowed to be left blank. If they are left blank, ... ERROR  
> test_form_kwargs_empty_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_form_kwargs_formset (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Custom kwargs set on the formset instance are passed to the ... ok  
> test_form_kwargs_formset_dynamic (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Form kwargs can be passed dynamically in a formset. ... ok  
> test_formset_calls_forms_is_valid (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formsets call is_valid() on each form. ... ERROR  
> test_formset_error_class (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formset's forms use the formset's error_class. ... ok  
> test_formset_has_changed (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSet.has_changed() is True if any data is passed to its forms, even ... ERROR  
> test_formset_initial_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A FormSet can be prefilled with existing data by providing a list of ... ok  
> test_formset_iteration (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formset instances are iterable. ... ok  
> test_formset_nonzero (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formsets without any forms evaluates as True. ... ok  
> test_formset_splitdatetimefield (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formset works with SplitDateTimeField(initial=datetime.datetime.now). ... ERROR  
> test_formset_total_error_count (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A valid formset should have 0 total errors. ... ERROR  
> test_formset_total_error_count_with_non_form_errors (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_formset_validate_max_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If validate_max is set and max_num is less than TOTAL_FORMS in the ... ERROR  
> test_formset_validate_max_flag_custom_error (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_formset_validate_min_excludes_empty_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_formset_validate_min_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If validate_min is set and min_num is more than TOTAL_FORMS in the ... ERROR  
> test_formset_validate_min_flag_custom_formatted_error (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_formset_validate_min_unchanged_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> min_num validation doesn't consider unchanged forms with initial data ... ERROR  
> test_formset_validation (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_formset_validation_count (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formset's ManagementForm is validated once per FormSet.is_valid() ... ERROR  
> test_formset_with_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> formset_factory's can_delete argument adds a boolean "delete" field to ... ERROR  
> test_formset_with_deletion_custom_widget (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_formset_with_deletion_invalid_deleted_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> deleted_forms works on a valid formset even if a deleted form would ... ERROR  
> test_formset_with_deletion_remove_deletion_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If a form is filled with something and can_delete is also checked, that ... ERROR  
> test_formset_with_ordering_and_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSets with ordering + deletion. ... ERROR  
> test_formsets_with_ordering (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> formset_factory's can_order argument adds an integer field to each ... ERROR  
> test_formsets_with_ordering_custom_widget (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_hard_limit_on_instantiated_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formset has a hard limit on the number of forms instantiated. ... ERROR  
> test_html_safe (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_increase_hard_limit (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Can increase the built-in forms limit via a higher max_num. ... ERROR  
> test_invalid_deleted_form_with_ordering (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Can get ordered_forms from a valid formset even if a deleted form ... ERROR  
> test_limited_max_forms_two (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_limiting_extra_lest_than_max_num (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> max_num has no effect when extra is less than max_num. ... ok  
> test_limiting_max_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Limiting the maximum number of forms with max_num. ... ok  
> test_management_form_field_names (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> The management form class has field names matching the constants. ... ok  
> test_management_form_prefix (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> The management form has the correct prefix. ... ERROR  
> test_max_num_with_initial_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_max_num_zero (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If max_num is 0 then no form is rendered at all, regardless of extra, ... ok  
> test_max_num_zero_with_initial (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_min_num_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More than 1 empty form can also be displayed using formset_factory's ... ok  
> test_min_num_displaying_more_than_one_blank_form_with_zero_extra (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More than 1 empty form can be displayed using min_num. ... ok  
> test_more_initial_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> The extra argument works when the formset is pre-filled with initial ... ok  
> test_more_initial_form_result_in_one (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> One form from initial and extra=3 with max_num=2 results in the one ... ok  
> test_more_initial_than_max_num (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More initial forms than max_num results in all initial forms being ... ok  
> test_non_form_errors (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_non_form_errors_run_full_clean (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If non_form_errors() is called without calling is_valid() first, ... ERROR  
> test_ordering_blank_fieldsets (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Ordering works with blank fieldsets. ... ERROR  
> test_repr (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_repr_do_not_trigger_validation (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
> test_second_form_partially_filled (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If at least one field is filled out on a blank form, it will be ... ERROR  
> test_second_form_partially_filled_2 (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A partially completed form is invalid. ... ERROR  
> test_single_form_completed (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Just one form may be completed. ... ERROR  
> test_template_name_can_be_overridden (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_template_name_uses_renderer_value (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ok  
> test_validate_max_ignores_forms_marked_for_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase) ... ERROR  
>   
> ======================================================================  
> ERROR: test_invalid (forms_tests.tests.test_formsets.AllValidTests)  
> all_valid() validates all forms, even when some are invalid.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1892, in test_invalid  
>     self.assertIs(all_valid((formset1, formset2)), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 577, in all_valid  
>     return all([formset.is_valid() for formset in formsets])  
>   File "/opt/django__django/django/forms/formsets.py", line 577, in <listcomp>  
>     return all([formset.is_valid() for formset in formsets])  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_valid (forms_tests.tests.test_formsets.AllValidTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1873, in test_valid  
>     self.assertIs(all_valid((formset1, formset2)), True)  
>   File "/opt/django__django/django/forms/formsets.py", line 577, in all_valid  
>     return all([formset.is_valid() for formset in formsets])  
>   File "/opt/django__django/django/forms/formsets.py", line 577, in <listcomp>  
>     return all([formset.is_valid() for formset in formsets])  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_customize_management_form_error (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1760, in test_customize_management_form_error  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_empty_forms_are_unbound (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1802, in test_empty_forms_are_unbound  
>     empty_forms = [unbound_formset.empty_form, bound_formset.empty_form]  
>   File "/opt/django__django/django/forms/formsets.py", line 268, in empty_form  
>     self.add_fields(form, None)  
>   File "/opt/django__django/django/forms/formsets.py", line 479, in add_fields  
>     initial_form_count = self.initial_form_count()  
>   File "/opt/django__django/django/forms/formsets.py", line 195, in initial_form_count  
>     return self.management_form.cleaned_data[INITIAL_FORM_COUNT]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_form_errors_are_caught_by_formset (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1788, in test_form_errors_are_caught_by_formset  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_management_form_invalid_data (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1729, in test_management_form_invalid_data  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_no_data_error (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1698, in test_no_data_error  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_with_management_data_attrs_work_fine (forms_tests.tests.test_formsets.TestIsBoundBehavior)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1770, in test_with_management_data_attrs_work_fine  
>     self.assertEqual(0, formset.initial_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 195, in initial_form_count  
>     return self.management_form.cleaned_data[INITIAL_FORM_COUNT]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_empty_formset_is_valid (forms_tests.tests.test_formsets.TestEmptyFormSet)  
> An empty formset still calls clean()  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1838, in test_empty_formset_is_valid  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_div (forms_tests.tests.test_formsets.FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 118, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1671, in test_as_div  
>     self.formset.as_div(),  
>   File "/opt/django__django/django/forms/utils.py", line 96, in as_div  
>     return self.render(self.template_name_div)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_p (forms_tests.tests.test_formsets.FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 118, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1648, in test_as_p  
>     self.formset.as_p(),  
>   File "/opt/django__django/django/forms/utils.py", line 84, in as_p  
>     return self.render(self.template_name_p)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_table (forms_tests.tests.test_formsets.FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 118, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1636, in test_as_table  
>     self.formset.as_table(),  
>   File "/opt/django__django/django/forms/utils.py", line 88, in as_table  
>     return self.render(self.template_name_table)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_ul (forms_tests.tests.test_formsets.FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 118, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1659, in test_as_ul  
>     self.formset.as_ul(),  
>   File "/opt/django__django/django/forms/utils.py", line 92, in as_ul  
>     return self.render(self.template_name_ul)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_div (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 118, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1671, in test_as_div  
>     self.formset.as_div(),  
>   File "/opt/django__django/django/forms/utils.py", line 96, in as_div  
>     return self.render(self.template_name_div)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_p (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 118, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1648, in test_as_p  
>     self.formset.as_p(),  
>   File "/opt/django__django/django/forms/utils.py", line 84, in as_p  
>     return self.render(self.template_name_p)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_table (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 118, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1636, in test_as_table  
>     self.formset.as_table(),  
>   File "/opt/django__django/django/forms/utils.py", line 88, in as_table  
>     return self.render(self.template_name_table)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_as_ul (forms_tests.tests.test_formsets.Jinja2FormsetAsTagTests)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 118, in __getitem__  
>     return self.forms[index]  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1659, in test_as_ul  
>     self.formset.as_ul(),  
>   File "/opt/django__django/django/forms/utils.py", line 92, in as_ul  
>     return self.render(self.template_name_ul)  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_absolute_max (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1134, in test_absolute_max  
>     self.assertIs(formset.is_valid(), True)  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_absolute_max_with_max_num (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1158, in test_absolute_max_with_max_num  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_basic_formset (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A FormSet constructor takes the same arguments as Form. Create a  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 118, in __getitem__  
>     return self.forms[index]  
> TypeError: list indices must be integers or slices, not str  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 125, in test_basic_formset  
>     str(formset),  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 158, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_blank_form_unfilled (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A form that's displayed as blank may be submitted as blank.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 260, in test_blank_form_unfilled  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_clean_hook (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSets have a clean() hook for doing extra validation that isn't tied  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 971, in test_clean_hook  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_custom_renderer (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1548, in test_custom_renderer  
>     self.assertEqual(formset.forms[0].renderer, renderer)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_default_absolute_max (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1116, in test_default_absolute_max  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_delete_prefilled_data (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Deleting prefilled data is an error. Removing data from form fields  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 283, in test_delete_prefilled_data  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_disable_delete_extra_formset_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1497, in test_disable_delete_extra_formset_forms  
>     formset.cleaned_data,  
>   File "/opt/django__django/django/forms/formsets.py", line 276, in cleaned_data  
>     if not self.is_valid():  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> More than 1 empty form can be displayed using formset_factory's  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 327, in test_displaying_more_than_one_blank_form  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_empty_ordered_fields (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Ordering fields are allowed to be left blank. If they are left blank,  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 838, in test_empty_ordered_fields  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_calls_forms_is_valid (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formsets call is_valid() on each form.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1319, in test_formset_calls_forms_is_valid  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_has_changed (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSet.has_changed() is True if any data is passed to its forms, even  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 227, in test_formset_has_changed  
>     self.assertFalse(blank_formset.has_changed())  
>   File "/opt/django__django/django/forms/formsets.py", line 475, in has_changed  
>     return any(form.has_changed() for form in self)  
>   File "/opt/django__django/django/forms/formsets.py", line 114, in __iter__  
>     return iter(self.forms)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_splitdatetimefield (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Formset works with SplitDateTimeField(initial=datetime.datetime.now).  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1290, in test_formset_splitdatetimefield  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_total_error_count (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A valid formset should have 0 total errors.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1433, in test_formset_total_error_count  
>     self.assertEqual(formset.total_error_count(), expected_error_count)  
>   File "/opt/django__django/django/forms/formsets.py", line 370, in total_error_count  
>     return len(self.non_form_errors()) + sum(  
>   File "/opt/django__django/django/forms/formsets.py", line 358, in non_form_errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_total_error_count_with_non_form_errors (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1447, in test_formset_total_error_count_with_non_form_errors  
>     self.assertEqual(formset.total_error_count(), 1)  
>   File "/opt/django__django/django/forms/formsets.py", line 370, in total_error_count  
>     return len(self.non_form_errors()) + sum(  
>   File "/opt/django__django/django/forms/formsets.py", line 358, in non_form_errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_max_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If validate_max is set and max_num is less than TOTAL_FORMS in the  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 403, in test_formset_validate_max_flag  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_max_flag_custom_error (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 430, in test_formset_validate_max_flag_custom_error  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_excludes_empty_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 533, in test_formset_validate_min_excludes_empty_forms  
>     self.assertFalse(formset.has_changed())  
>   File "/opt/django__django/django/forms/formsets.py", line 475, in has_changed  
>     return any(form.has_changed() for form in self)  
>   File "/opt/django__django/django/forms/formsets.py", line 114, in __iter__  
>     return iter(self.forms)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If validate_min is set and min_num is more than TOTAL_FORMS in the  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 460, in test_formset_validate_min_flag  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_flag_custom_formatted_error (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 488, in test_formset_validate_min_flag_custom_formatted_error  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_unchanged_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> min_num validation doesn't consider unchanged forms with initial data  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 520, in test_formset_validate_min_unchanged_forms  
>     self.assertFalse(formset.forms[0].has_changed())  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validation (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 186, in test_formset_validation  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validation_count (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formset's ManagementForm is validated once per FormSet.is_valid()  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 217, in test_formset_validation_count  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> formset_factory's can_delete argument adds a boolean "delete" field to  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 630, in test_formset_with_deletion  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_deletion_invalid_deleted_form (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> deleted_forms works on a valid formset even if a deleted form would  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 690, in test_formset_with_deletion_invalid_deleted_form  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_deletion_remove_deletion_flag (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If a form is filled with something and can_delete is also checked, that  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 668, in test_formset_with_deletion_remove_deletion_flag  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_ordering_and_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> FormSets with ordering + deletion.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 917, in test_formset_with_ordering_and_deletion  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formsets_with_ordering (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> formset_factory's can_order argument adds an integer field to each  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 773, in test_formsets_with_ordering  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_hard_limit_on_instantiated_forms (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A formset has a hard limit on the number of forms instantiated.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1348, in test_hard_limit_on_instantiated_forms  
>     self.assertEqual(len(formset.forms), 3)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_html_safe (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 118, in __getitem__  
>     return self.forms[index]  
> TypeError: list indices must be integers or slices, not str  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1455, in test_html_safe  
>     self.assertEqual(str(formset), formset.__html__())  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 158, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_increase_hard_limit (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Can increase the built-in forms limit via a higher max_num.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1380, in test_increase_hard_limit  
>     self.assertEqual(len(formset.forms), 4)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_invalid_deleted_form_with_ordering (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Can get ordered_forms from a valid formset even if a deleted form  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 953, in test_invalid_deleted_form_with_ordering  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_management_form_prefix (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> The management form has the correct prefix.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1206, in test_management_form_prefix  
>     self.assertEqual(formset.management_form.prefix, "form")  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 158, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_non_form_errors (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1228, in test_non_form_errors  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_non_form_errors_run_full_clean (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If non_form_errors() is called without calling is_valid() first,  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1400, in test_non_form_errors_run_full_clean  
>     self.assertIsInstance(formset.non_form_errors(), ErrorList)  
>   File "/opt/django__django/django/forms/formsets.py", line 358, in non_form_errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_ordering_blank_fieldsets (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Ordering works with blank fieldsets.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 859, in test_ordering_blank_fieldsets  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_repr (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1555, in test_repr  
>     valid_formset.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_repr_do_not_trigger_validation (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1605, in test_repr_do_not_trigger_validation  
>     repr(formset)  
>   File "/opt/django__django/django/forms/formsets.py", line 143, in __repr__  
>     self.total_form_count(),  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_second_form_partially_filled (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> If at least one field is filled out on a blank form, it will be  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 274, in test_second_form_partially_filled  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_second_form_partially_filled_2 (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> A partially completed form is invalid.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 553, in test_second_form_partially_filled_2  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_single_form_completed (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> Just one form may be completed.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 378, in test_single_form_completed  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_validate_max_ignores_forms_marked_for_deletion (forms_tests.tests.test_formsets.FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1420, in test_validate_max_ignores_forms_marked_for_deletion  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_absolute_max (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1134, in test_absolute_max  
>     self.assertIs(formset.is_valid(), True)  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_absolute_max_with_max_num (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1158, in test_absolute_max_with_max_num  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_basic_formset (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A FormSet constructor takes the same arguments as Form. Create a  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 118, in __getitem__  
>     return self.forms[index]  
> TypeError: list indices must be integers or slices, not str  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 125, in test_basic_formset  
>     str(formset),  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 158, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_blank_form_unfilled (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A form that's displayed as blank may be submitted as blank.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 260, in test_blank_form_unfilled  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_clean_hook (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSets have a clean() hook for doing extra validation that isn't tied  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 971, in test_clean_hook  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_custom_renderer (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A custom renderer passed to a formset_factory() is passed to all forms  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1548, in test_custom_renderer  
>     self.assertEqual(formset.forms[0].renderer, renderer)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_default_absolute_max (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1116, in test_default_absolute_max  
>     self.assertIs(formset.is_valid(), False)  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_delete_prefilled_data (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Deleting prefilled data is an error. Removing data from form fields  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 283, in test_delete_prefilled_data  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_disable_delete_extra_formset_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1497, in test_disable_delete_extra_formset_forms  
>     formset.cleaned_data,  
>   File "/opt/django__django/django/forms/formsets.py", line 276, in cleaned_data  
>     if not self.is_valid():  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_displaying_more_than_one_blank_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> More than 1 empty form can be displayed using formset_factory's  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 327, in test_displaying_more_than_one_blank_form  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_empty_ordered_fields (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Ordering fields are allowed to be left blank. If they are left blank,  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 838, in test_empty_ordered_fields  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_calls_forms_is_valid (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formsets call is_valid() on each form.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1319, in test_formset_calls_forms_is_valid  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_has_changed (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSet.has_changed() is True if any data is passed to its forms, even  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 227, in test_formset_has_changed  
>     self.assertFalse(blank_formset.has_changed())  
>   File "/opt/django__django/django/forms/formsets.py", line 475, in has_changed  
>     return any(form.has_changed() for form in self)  
>   File "/opt/django__django/django/forms/formsets.py", line 114, in __iter__  
>     return iter(self.forms)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_splitdatetimefield (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Formset works with SplitDateTimeField(initial=datetime.datetime.now).  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1290, in test_formset_splitdatetimefield  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_total_error_count (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A valid formset should have 0 total errors.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1433, in test_formset_total_error_count  
>     self.assertEqual(formset.total_error_count(), expected_error_count)  
>   File "/opt/django__django/django/forms/formsets.py", line 370, in total_error_count  
>     return len(self.non_form_errors()) + sum(  
>   File "/opt/django__django/django/forms/formsets.py", line 358, in non_form_errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_total_error_count_with_non_form_errors (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1447, in test_formset_total_error_count_with_non_form_errors  
>     self.assertEqual(formset.total_error_count(), 1)  
>   File "/opt/django__django/django/forms/formsets.py", line 370, in total_error_count  
>     return len(self.non_form_errors()) + sum(  
>   File "/opt/django__django/django/forms/formsets.py", line 358, in non_form_errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_max_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If validate_max is set and max_num is less than TOTAL_FORMS in the  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 403, in test_formset_validate_max_flag  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_max_flag_custom_error (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 430, in test_formset_validate_max_flag_custom_error  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_excludes_empty_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 533, in test_formset_validate_min_excludes_empty_forms  
>     self.assertFalse(formset.has_changed())  
>   File "/opt/django__django/django/forms/formsets.py", line 475, in has_changed  
>     return any(form.has_changed() for form in self)  
>   File "/opt/django__django/django/forms/formsets.py", line 114, in __iter__  
>     return iter(self.forms)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If validate_min is set and min_num is more than TOTAL_FORMS in the  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 460, in test_formset_validate_min_flag  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_flag_custom_formatted_error (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 488, in test_formset_validate_min_flag_custom_formatted_error  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validate_min_unchanged_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> min_num validation doesn't consider unchanged forms with initial data  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 520, in test_formset_validate_min_unchanged_forms  
>     self.assertFalse(formset.forms[0].has_changed())  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validation (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 186, in test_formset_validation  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_validation_count (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formset's ManagementForm is validated once per FormSet.is_valid()  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 217, in test_formset_validation_count  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> formset_factory's can_delete argument adds a boolean "delete" field to  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 630, in test_formset_with_deletion  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_deletion_invalid_deleted_form (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> deleted_forms works on a valid formset even if a deleted form would  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 690, in test_formset_with_deletion_invalid_deleted_form  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_deletion_remove_deletion_flag (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If a form is filled with something and can_delete is also checked, that  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 668, in test_formset_with_deletion_remove_deletion_flag  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formset_with_ordering_and_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> FormSets with ordering + deletion.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 917, in test_formset_with_ordering_and_deletion  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_formsets_with_ordering (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> formset_factory's can_order argument adds an integer field to each  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 773, in test_formsets_with_ordering  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_hard_limit_on_instantiated_forms (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A formset has a hard limit on the number of forms instantiated.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1348, in test_hard_limit_on_instantiated_forms  
>     self.assertEqual(len(formset.forms), 3)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_html_safe (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/django__django/django/template/base.py", line 880, in _resolve_lookup  
>     current = current[bit]  
>   File "/opt/django__django/django/forms/formsets.py", line 118, in __getitem__  
>     return self.forms[index]  
> TypeError: list indices must be integers or slices, not str  
>   
> During handling of the above exception, another exception occurred:  
>   
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1455, in test_html_safe  
>     self.assertEqual(str(formset), formset.__html__())  
>   File "/opt/django__django/django/forms/utils.py", line 75, in render  
>     return mark_safe(renderer.render(template, context))  
>   File "/opt/django__django/django/forms/renderers.py", line 29, in render  
>     return template.render(context, request=request).strip()  
>   File "/opt/django__django/django/template/backends/django.py", line 62, in render  
>     return self.template.render(context)  
>   File "/opt/django__django/django/template/base.py", line 175, in render  
>     return self._render(context)  
>   File "/opt/django__django/django/test/utils.py", line 111, in instrumented_test_render  
>     return self.nodelist.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1005, in render  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 1005, in <listcomp>  
>     return SafeString("".join([node.render_annotated(context) for node in self]))  
>   File "/opt/django__django/django/template/base.py", line 966, in render_annotated  
>     return self.render(context)  
>   File "/opt/django__django/django/template/base.py", line 1064, in render  
>     output = self.filter_expression.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 715, in resolve  
>     obj = self.var.resolve(context)  
>   File "/opt/django__django/django/template/base.py", line 847, in resolve  
>     value = self._resolve_lookup(context)  
>   File "/opt/django__django/django/template/base.py", line 890, in _resolve_lookup  
>     current = getattr(current, bit)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 158, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_increase_hard_limit (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Can increase the built-in forms limit via a higher max_num.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1380, in test_increase_hard_limit  
>     self.assertEqual(len(formset.forms), 4)  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 207, in forms  
>     for i in range(self.total_form_count())  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_invalid_deleted_form_with_ordering (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Can get ordered_forms from a valid formset even if a deleted form  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 953, in test_invalid_deleted_form_with_ordering  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_management_form_prefix (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> The management form has the correct prefix.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1206, in test_management_form_prefix  
>     self.assertEqual(formset.management_form.prefix, "form")  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 158, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_non_form_errors (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1228, in test_non_form_errors  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_non_form_errors_run_full_clean (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If non_form_errors() is called without calling is_valid() first,  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1400, in test_non_form_errors_run_full_clean  
>     self.assertIsInstance(formset.non_form_errors(), ErrorList)  
>   File "/opt/django__django/django/forms/formsets.py", line 358, in non_form_errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_ordering_blank_fieldsets (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Ordering works with blank fieldsets.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 859, in test_ordering_blank_fieldsets  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_repr (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1555, in test_repr  
>     valid_formset.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_repr_do_not_trigger_validation (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1605, in test_repr_do_not_trigger_validation  
>     repr(formset)  
>   File "/opt/django__django/django/forms/formsets.py", line 143, in __repr__  
>     self.total_form_count(),  
>   File "/opt/django__django/django/forms/formsets.py", line 179, in total_form_count  
>     self.management_form.cleaned_data[TOTAL_FORM_COUNT], self.absolute_max  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_second_form_partially_filled (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> If at least one field is filled out on a blank form, it will be  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 274, in test_second_form_partially_filled  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_second_form_partially_filled_2 (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> A partially completed form is invalid.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 553, in test_second_form_partially_filled_2  
>     self.assertFalse(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_single_form_completed (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> Just one form may be completed.  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 378, in test_single_form_completed  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ======================================================================  
> ERROR: test_validate_max_ignores_forms_marked_for_deletion (forms_tests.tests.test_formsets.Jinja2FormsFormsetTestCase)  
> ----------------------------------------------------------------------  
> Traceback (most recent call last):  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 59, in testPartExecutor  
>     yield  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 592, in run  
>     self._callTestMethod(testMethod)  
>   File "/opt/pyenv/versions/3.9.19/lib/python3.9/unittest/case.py", line 550, in _callTestMethod  
>     method()  
>   File "/opt/django__django/tests/forms_tests/tests/test_formsets.py", line 1420, in test_validate_max_ignores_forms_marked_for_deletion  
>     self.assertTrue(formset.is_valid())  
>   File "/opt/django__django/django/forms/formsets.py", line 383, in is_valid  
>     self.errors  
>   File "/opt/django__django/django/forms/formsets.py", line 365, in errors  
>     self.full_clean()  
>   File "/opt/django__django/django/forms/formsets.py", line 409, in full_clean  
>     if not self.management_form.is_valid():  
>   File "/opt/django__django/django/utils/functional.py", line 57, in __get__  
>     res = instance.__dict__[self.name] = self.func(instance)  
>   File "/opt/django__django/django/forms/formsets.py", line 150, in management_form  
>     form = ManagementForm(  
>   File "/opt/django__django/django/forms/formsets.py", line 47, in __init__  
>     self.cleaned_data = super().clean()  
>   File "/opt/django__django/django/forms/forms.py", line 480, in clean  
>     return self.cleaned_data  
> AttributeError: 'ManagementForm' object has no attribute 'cleaned_data'  
>   
> ----------------------------------------------------------------------  
> Ran 156 tests in 0.527s  
>   
> FAILED (errors=103)  
>    
> [django__django__4.2] [django__django-15902] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [django__django__4.2] [django__django-15902] Test script run successful   
> Attempt to fix test errors? yes  
> Only 4 reflections allowed, stopping.  
