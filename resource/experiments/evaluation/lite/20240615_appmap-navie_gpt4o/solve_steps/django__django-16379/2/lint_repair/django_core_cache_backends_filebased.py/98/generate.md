```xml
<change>
    <file change-number-for-this-file="1">django/core/cache/backends/filebased.py</file>
    <original line-count="7" no-ellipsis="true"><![CDATA[
    def has_key(self, key, version=None):
            fname = self._key_to_file(key, version)
            try:
                with open(fname, "rb") as f:
                    return not self._is_expired(f)
            except FileNotFoundError:
                return False
    ]]></original>
    <modified no-ellipsis="true"><![CDATA[
    def has_key(self, key, version=None):
        fname = self._key_to_file(key, version)
        try:
            with open(fname, "rb") as f:
                return not self._is_expired(f)
        except FileNotFoundError:
            return False
    ]]></modified>
</change>
```