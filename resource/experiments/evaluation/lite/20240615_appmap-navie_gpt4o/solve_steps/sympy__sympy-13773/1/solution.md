<change>
<file change-number-for-this-file="1">sympy/matrices/expressions/matexpr.py</file>
<original line-count="14" no-ellipsis="true"><![CDATA[
@_sympifyit('other', NotImplemented)
@call_highest_priority('__rmul__')
def __matmul__(self, other):
    return MatMul(self, other).doit()
]]></original>
<modified no-ellipsis="true"><![CDATA[
@_sympifyit('other', NotImplemented)
@call_highest_priority('__rmul__')
def __matmul__(self, other):
    # Check if both operands are matrix types
    if not isinstance(self, MatrixExpr) or not isinstance(other, MatrixExpr):
        raise ValueError("Scalar operands are not allowed; use '*' instead")
    return MatMul(self, other).doit()
]]></modified>
</change>