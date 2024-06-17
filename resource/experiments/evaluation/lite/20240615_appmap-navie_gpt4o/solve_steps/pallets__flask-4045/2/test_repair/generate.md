<change>
<file change-number-for-this-file="1">src/flask/blueprints.py</file>
<original line-count="14" no-ellipsis="true"><![CDATA[
        self.deferred_functions: t.List[DeferredSetupFunction] = []
        if url_defaults is None:
            url_defaults = {}
        self.url_values_defaults = url_defaults
        self.cli_group = cli_group
        self._blueprints: t.List[t.Tuple["Blueprint", dict]] = []
]]></original>
<modified no-ellipsis="true"><![CDATA[
        self.deferred_functions: t.List[DeferredSetupFunction] = []
        if url_defaults is None:
            url_defaults = {}
        self.url_values_defaults = url_defaults
        self.cli_group = cli_group
        self._blueprints: t.List[t.Tuple["Blueprint", dict]] = []

        # Validation to check if the blueprint name contains a dot
        if '.' in self.name:
            raise ValueError("Blueprint name should not contain dots ('.').")
]]></modified>
</change>

<change>
<file change-number-for-this-file="2">src/flask/blueprints.py</file>
<original line-count="10" no-ellipsis="true"><![CDATA[
        if url_defaults is None:
            url_defaults = {}
        self.url_values_defaults = url_defaults
        self.cli_group = cli_group
        self._blueprints: t.List[t.Tuple["Blueprint", dict]] = []
        if url_defaults is None:
            url_defaults = {}
        if '.' in self.name:
            raise ValueError("Blueprint name should not contain dots ('.').")
]]></original>
<modified no-ellipsis="true"><![CDATA[
        if url_defaults is None:
            url_defaults = {}
        self.url_values_defaults = url_defaults
        self.cli_group = cli_group
        self._blueprints: t.List[t.Tuple["Blueprint", dict]] = []
]]></modified>
</change>
</change>