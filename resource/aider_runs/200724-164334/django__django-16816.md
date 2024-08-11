
# aider chat started at 2024-07-20 14:23:37

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp7jwi9bzx/.git with 6,698 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Error E108 does not cover some cases  
#### Description  
#### 	   
#### 		(last modified by Baha Sdtbekov)  
#### 	   
#### I have two models, Question and Choice. And if I write list_display = ["choice"] in QuestionAdmin, I get no errors.  
#### But when I visit /admin/polls/question/, the following trace is returned:  
#### Internal Server Error: /admin/polls/question/  
#### Traceback (most recent call last):  
####  File "/some/path/django/contrib/admin/utils.py", line 334, in label_for_field  
#### 	field = _get_non_gfk_field(model._meta, name)  
####  File "/some/path/django/contrib/admin/utils.py", line 310, in _get_non_gfk_field  
#### 	raise FieldDoesNotExist()  
#### django.core.exceptions.FieldDoesNotExist  
#### During handling of the above exception, another exception occurred:  
#### Traceback (most recent call last):  
####  File "/some/path/django/core/handlers/exception.py", line 55, in inner  
#### 	response = get_response(request)  
####  File "/some/path/django/core/handlers/base.py", line 220, in _get_response  
#### 	response = response.render()  
####  File "/some/path/django/template/response.py", line 111, in render  
#### 	self.content = self.rendered_content  
####  File "/some/path/django/template/response.py", line 89, in rendered_content  
#### 	return template.render(context, self._request)  
####  File "/some/path/django/template/backends/django.py", line 61, in render  
#### 	return self.template.render(context)  
####  File "/some/path/django/template/base.py", line 175, in render  
#### 	return self._render(context)  
####  File "/some/path/django/template/base.py", line 167, in _render  
#### 	return self.nodelist.render(context)  
####  File "/some/path/django/template/base.py", line 1005, in render  
#### 	return SafeString("".join([node.render_annotated(context) for node in self]))  
####  File "/some/path/django/template/base.py", line 1005, in <listcomp>  
#### 	return SafeString("".join([node.render_annotated(context) for node in self]))  
####  File "/some/path/django/template/base.py", line 966, in render_annotated  
#### 	return self.render(context)  
####  File "/some/path/django/template/loader_tags.py", line 157, in render  
#### 	return compiled_parent._render(context)  
####  File "/some/path/django/template/base.py", line 167, in _render  
#### 	return self.nodelist.render(context)  
####  File "/some/path/django/template/base.py", line 1005, in render  
#### 	return SafeString("".join([node.render_annotated(context) for node in self]))  
####  File "/some/path/django/template/base.py", line 1005, in <listcomp>  
#### 	return SafeString("".join([node.render_annotated(context) for node in self]))  
####  File "/some/path/django/template/base.py", line 966, in render_annotated  
#### 	return self.render(context)  
####  File "/some/path/django/template/loader_tags.py", line 157, in render  
#### 	return compiled_parent._render(context)  
####  File "/some/path/django/template/base.py", line 167, in _render  
#### 	return self.nodelist.render(context)  
####  File "/some/path/django/template/base.py", line 1005, in render  
#### 	return SafeString("".join([node.render_annotated(context) for node in self]))  
####  File "/some/path/django/template/base.py", line 1005, in <listcomp>  
#### 	return SafeString("".join([node.render_annotated(context) for node in self]))  
####  File "/some/path/django/template/base.py", line 966, in render_annotated  
#### 	return self.render(context)  
####  File "/some/path/django/template/loader_tags.py", line 63, in render  
#### 	result = block.nodelist.render(context)  
####  File "/some/path/django/template/base.py", line 1005, in render  
#### 	return SafeString("".join([node.render_annotated(context) for node in self]))  
####  File "/some/path/django/template/base.py", line 1005, in <listcomp>  
#### 	return SafeString("".join([node.render_annotated(context) for node in self]))  
####  File "/some/path/django/template/base.py", line 966, in render_annotated  
#### 	return self.render(context)  
####  File "/some/path/django/template/loader_tags.py", line 63, in render  
#### 	result = block.nodelist.render(context)  
####  File "/some/path/django/template/base.py", line 1005, in render  
#### 	return SafeString("".join([node.render_annotated(context) for node in self]))  
####  File "/some/path/django/template/base.py", line 1005, in <listcomp>  
#### 	return SafeString("".join([node.render_annotated(context) for node in self]))  
####  File "/some/path/django/template/base.py", line 966, in render_annotated  
#### 	return self.render(context)  
####  File "/some/path/django/contrib/admin/templatetags/base.py", line 45, in render  
#### 	return super().render(context)  
####  File "/some/path/django/template/library.py", line 258, in render  
#### 	_dict = self.func(*resolved_args, **resolved_kwargs)  
####  File "/some/path/django/contrib/admin/templatetags/admin_list.py", line 326, in result_list  
#### 	headers = list(result_headers(cl))  
####  File "/some/path/django/contrib/admin/templatetags/admin_list.py", line 90, in result_headers  
#### 	text, attr = label_for_field(  
####  File "/some/path/django/contrib/admin/utils.py", line 362, in label_for_field  
#### 	raise AttributeError(message)  
#### AttributeError: Unable to lookup 'choice' on Question or QuestionAdmin  
#### [24/Apr/2023 15:43:32] "GET /admin/polls/question/ HTTP/1.1" 500 349913  
#### I suggest that error E108 be updated to cover this case as well  
#### For reproduce see ​github  
> 34884 prompt tokens, 98 completion tokens, $0.175890 cost  

To address the issue with error E108 not covering some cases, we will likely need to make changes to the following files:

1. `django/contrib/admin/validation.py` - This file is responsible for validating admin configurations, including `list_display`. We will need to update the validation logic to catch the case where a non-existent field is specified in `list_display`.

Please add `django/contrib/admin/validation.py` to the chat so we can proceed with the necessary changes.

