<change>
<file change-number-for-this-file="1">django/utils/html.py</file>
<original line-count="10" no-ellipsis="true"><![CDATA[
{
}


def json_script(value, element_id=None, encoder=DjangoJSONEncoder):
    """
    Escape all the HTML/XML special characters with their unicode escapes, so
    value is safe to be output anywhere except for inside a tag attribute. Wrap
    the escaped JSON in a script tag.
    """
    json_str = json.dumps(value, cls=encoder).translate(_json_script_escapes)
    if element_id:
]]></original>
<modified no-ellipsis="true"><![CDATA[
{
}

from django.core.serializers.json import DjangoJSONEncoder


def json_script(value, element_id=None, encoder=DjangoJSONEncoder):
    """
    Escape all the HTML/XML special characters with their unicode escapes, so
    value is safe to be output anywhere except for inside a tag attribute. Wrap
    the escaped JSON in a script tag.
    """
    json_str = json.dumps(value, cls=encoder).translate(_json_script_escapes)
    if element_id:
]]></modified>
</change>