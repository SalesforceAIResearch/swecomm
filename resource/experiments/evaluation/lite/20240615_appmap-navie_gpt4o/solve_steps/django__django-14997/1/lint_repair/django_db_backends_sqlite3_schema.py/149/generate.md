```xml
<change>
<file change-number-for-this-file="1">django/db/backends/sqlite3/schema.py</file>
<original line-count="7" no-ellipsis="true"><![CDATA[
            """
            Shortcut to transform a model from old_model into new_model
    
            This follows the correct procedure to perform non-rename or column
            addition operations based on SQLite's documentation
    
            https://www.sqlite.org/lang_altertable.html#caution
            """
]]></original>
<modified no-ellipsis="true"><![CDATA[
    """
    Shortcut to transform a model from old_model into new_model

    This follows the correct procedure to perform non-rename or column
    addition operations based on SQLite's documentation

    https://www.sqlite.org/lang_altertable.html#caution
    """
]]></modified>
</change>
```