```xml
<change>
<file change-number-for-this-file="1">sympy/printing/pretty/pretty.py</file>
<original line-count="14" no-ellipsis="true"><![CDATA[
        for lim in expr.limits:
            width = (func_height + 2) // 2   # updated width calculation
            height = func_height + 1         # updated height calculation

            pretty_sign = generate_product_symbol(width, height, self._use_unicode)

            pretty_upper = self._print(lim[2])
            pretty_lower = self._print(Equality(lim[0], lim[1]))

            max_upper = max(max_upper, pretty_upper.height())

            if first:
                pretty_func = prettyFuncPicture
                pretty_func.baseline = 0
                first = False

            height = pretty_sign.height()
            padding = stringPict('')
            padding = prettyForm(*padding.stack(*[' ']*(height - 1)))
            pretty_sign = prettyForm(*pretty_sign.right(padding))
]]></original>
<modified no-ellipsis="true"><![CDATA[
        # Add import for generate_product_symbol
        from .pretty_symbology import generate_product_symbol

        for lim in expr.limits:
            width = (func_height + 2) // 2   # updated width calculation
            height = func_height + 1         # updated height calculation

            pretty_sign = generate_product_symbol(width, height, self._use_unicode)

            pretty_upper = self._print(lim[2])
            pretty_lower = self._print(Equality(lim[0], lim[1]))

            max_upper = max(max_upper, pretty_upper.height())

            if first:
                pretty_func = prettyFuncPicture
                pretty_func.baseline = 0
                first = False

            height = pretty_sign.height()
            padding = stringPict('')
            padding = prettyForm(*padding.stack(*[' ']*(height - 1)))
            pretty_sign = prettyForm(*pretty_sign.right(padding))
]]></modified>
</change>
```