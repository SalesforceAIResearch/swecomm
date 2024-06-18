```xml
<change>
<file change-number-for-this-file="1">sympy/printing/mathml.py</file>
<original line-count="9" no-ellipsis="true"><![CDATA[
    def _print_Symbol(self, sym):
        ci = self.dom.createElement(self.mathml_tag(sym))
        def join(items):
            if len(items) > 1:
                mrow = self.dom.createElement('mml:mrow')
                for i, item in enumerate(items):
                    if i > 0:
                        mo = self.dom.createElement('mml:mo')
                        mo.appendChild(self.dom.createTextNode(" "))
                        mrow.appendChild(mo)
                    mi = self.dom.createElement('mml:mi')
]]></original>
<modified no-ellipsis="true"><![CDATA[
    def _print_Symbol(self, sym):
        ci = self.dom.createElement(self.mathml_tag(sym))

        def join(items):
            if len(items) > 1:
                mrow = self.dom.createElement('mml:mrow')
                for i, item in enumerate(items):
                    if i > 0:
                        mo = self.dom.createElement('mml:mo')
                        mo.appendChild(self.dom.createTextNode(" "))
                        mrow.appendChild(mo)
                    mi = self.dom.createElement('mml:mi')
]]></modified>
</change>
```