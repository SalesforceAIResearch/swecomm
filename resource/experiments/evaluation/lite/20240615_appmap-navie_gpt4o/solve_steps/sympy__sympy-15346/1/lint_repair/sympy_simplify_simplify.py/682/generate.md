```xml
<change>
<file change-number-for-this-file="1">sympy/simplify/simplify.py</file>
<original line-count="10" no-ellipsis="true"><![CDATA[
for k in reversed(range(len(new_args))):
    if isinstance(new_args[k], (cos, sin)):
        for l in reversed(range(len(new_other_args))):
            if (isinstance(new_other_args[l], (cos, sin)) and
                    new_args[k].args == new_other_args[l].args):
                if isinstance(new_args[k], cos):
                    combined *= cos(new_args[k].args[0] - new_other_args[l].args[0])
                else:
                    combined *= sin(new_args[k].args[0] - new_other_args[l].args[0])
                del new_args[k]
]]></original>
<modified no-ellipsis="true"><![CDATA[
for k in reversed(range(len(new_args))):
    if isinstance(new_args[k], (cos, sin)):
        for m in reversed(range(len(new_other_args))):
            if (isinstance(new_other_args[m], (cos, sin)) and
                    new_args[k].args == new_other_args[m].args):
                if isinstance(new_args[k], cos):
                    combined *= cos(new_args[k].args[0] - new_other_args[m].args[0])
                else:
                    combined *= sin(new_args[k].args[0] - new_other_args[m].args[0])
                del new_args[k]
]]></modified>
</change>
```