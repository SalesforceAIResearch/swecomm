<change>
<file change-number-for-this-file="1">sympy/simplify/trigsimp.py</file>
<original line-count="14" no-ellipsis="true"><![CDATA[
def _match_div_rewrite(expr, i):
    """helper for __trigsimp"""
    if i == 0:
        expr = _replace_mul_fpowxgpow(expr, sin, cos,
            _midn, tan, _idn)
    elif i == 1:
        expr = _replace_mul_fpowxgpow(expr, tan, cos,
            _idn, sin, _idn)
    elif i == 2:
        expr = _replace_mul_fpowxgpow(expr, cot, sin,
            _idn, cos, _idn)
    elif i == 3:
        expr = _replace_mul_fpowxgpow(expr, tan, sin,
            _midn, cos, _midn)
    elif i == 4:
        expr = _replace_mul_fpowxgpow(expr, cot, cos,
            _midn, sin, _midn)
    elif i == 5:
        expr = _replace_mul_fpowxgpow(expr, cot, tan,
            _idn, _one, _idn)
    # i in (6, 7) is skipped
    elif i == 8:
        expr = _replace_mul_fpowxgpow(expr, sinh, cosh,
            _midn, tanh, _idn)
    elif i == 9:
        expr = _replace_mul_fpowxgpow(expr, tanh, cosh,
            _idn, sinh, _idn)
    elif i == 10:
        expr = _replace_mul_fpowxgpow(expr, coth, sinh,
            _idn, cosh, _idn)
]]></original>
<modified no-ellipsis="true"><![CDATA[
def _match_div_rewrite(expr, i):
    """helper for __trigsimp"""
    if i == 0:
        expr = _replace_mul_fpowxgpow(expr, sin, cos,
            _midn, tan, _idn)
    elif i == 1:
        expr = _replace_mul_fpowxgpow(expr, tan, cos,
            _idn, sin, _idn)
    elif i == 2:
        expr = _replace_mul_fpowxgpow(expr, cot, sin,
            _idn, cos, _idn)
    elif i == 3:
        expr = _replace_mul_fpowxgpow(expr, tan, sin,
            _midn, cos, _midn)
    elif i == 4:
        expr = _replace_mul_fpowxgpow(expr, cot, cos,
            _midn, sin, _midn)
    elif i == 5:
        expr = _replace_mul_fpowxgpow(expr, cot, tan,
            _idn, _one, _idn)
    # i in (6, 7) is skipped
    elif i == 8:
        expr = _replace_mul_fpowxgpow(expr, sinh, cosh,
            _midn, tanh, _idn)
    elif i == 9:
        expr = _replace_mul_fpowxgpow(expr, tanh, cosh,
            _idn, sinh, _idn)
    elif i == 10:
        expr = _replace_mul_fpowxgpow(expr, coth, sinh,
            _idn, cosh, _idn)
    elif i == 14:  # Add new case for recognizing sqrt(sin(x)**2)
        expr = expr.replace(lambda e: e.is_Pow and e.exp == S.Half and
            e.base.is_Pow and e.base.base == sin(e.base.exp), lambda e: Abs(sin(e.base.exp)))
]]></modified>
</change>

<change>
<file change-number-for-this-file="2">sympy/simplify/trigsimp.py</file>
<original line-count="14" no-ellipsis="true"><![CDATA[
def _trigsimp(expr, deep=False):
    # protect the cache from non-trig patterns; we only allow
    # trig patterns to enter the cache
    if expr.has(*_trigs):
        return __trigsimp(expr, deep)
    
    # Ensure that sqrt(sin(x)**2) is handled explicitly for simplification
    if expr.is_Pow and expr.exp == S.Half and expr.base.is_Pow and expr.base.base == sin(expr.base.exp):
        return Abs(sin(expr.base.exp))
    
    return expr

@cacheit
def __trigsimp(expr, deep=False):
    """recursive helper for trigsimp"""
]]></original>
<modified no-ellipsis="true"><![CDATA[
from sympy import Abs

def _trigsimp(expr, deep=False):
    # protect the cache from non-trig patterns; we only allow
    # trig patterns to enter the cache
    if expr.has(*_trigs):
        return __trigsimp(expr, deep)
    
    # Ensure that sqrt(sin(x)**2) is handled explicitly for simplification
    if expr.is_Pow and expr.exp == S.Half and expr.base.is_Pow and expr.base.base == sin(expr.base.exp):
        return Abs(sin(expr.base.exp))
    
    return expr

@cacheit
def __trigsimp(expr, deep=False):
    """recursive helper for trigsimp"""
]]></modified>
</change>