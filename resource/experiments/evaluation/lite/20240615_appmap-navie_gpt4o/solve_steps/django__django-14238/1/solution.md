<change>
<file change-number-for-this-file="1">django/db/models/fields/__init__.py</file>
<original line-count="14" no-ellipsis="true"><![CDATA[
class AutoFieldMeta(type):
    """
    Metaclass to maintain backward inheritance compatibility for AutoField.

    It is intended that AutoFieldMixin become public API when it is possible to
    create a non-integer automatically-generated field using column defaults
    stored in the database.

    In many areas Django also relies on using isinstance() to check for an
    automatically-generated field as a subclass of AutoField. A new flag needs
    to be implemented on Field to be used instead.

    When these issues have been addressed, this metaclass could be used to
    deprecate inheritance from AutoField and use of isinstance() with AutoField
    for detecting automatically-generated fields.
    """

    @property
    def _subclasses(self):
        return (BigAutoField, SmallAutoField)

    def __instancecheck__(self, instance):
        return isinstance(instance, self._subclasses) or super().__instancecheck__(instance)

    def __subclasscheck__(self, subclass):
        return subclass in self._subclasses or super().__subclasscheck__(subclass)
]]></original>
<modified no-ellipsis="true"><![CDATA[
class AutoFieldMeta(type):
    """
    Metaclass to maintain backward inheritance compatibility for AutoField.

    It is intended that AutoFieldMixin become public API when it is possible to
    create a non-integer automatically-generated field using column defaults
    stored in the database.

    In many areas Django also relies on using isinstance() to check for an
    automatically-generated field as a subclass of AutoField. A new flag needs
    to be implemented on Field to be used instead.

    When these issues have been addressed, this metaclass could be used to
    deprecate inheritance from AutoField and use of isinstance() with AutoField
    for detecting automatically-generated fields.
    """

    @property
    def _subclasses(self):
        return (BigAutoField, SmallAutoField) + tuple(cls for cls in globals().values() 
                                                      if isinstance(cls, type) 
                                                      and issubclass(cls, (BigAutoField, SmallAutoField))
                                                      and cls not in (BigAutoField, SmallAutoField))

    def __instancecheck__(self, instance):
        return isinstance(instance, self._subclasses) or super().__instancecheck__(instance)

    def __subclasscheck__(self, subclass):
        return issubclass(subclass, self._subclasses) or super().__subclasscheck__(subclass)
]]></modified>
</change>