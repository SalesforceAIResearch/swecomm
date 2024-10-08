```xml
<change>
<file change-number-for-this-file="1">src/_pytest/outcomes.py</file>
<original line-count="14" no-ellipsis="true"><![CDATA[
@_with_exception(Skipped)
def skip(msg: str = "", *, allow_module_level: bool = False) -> "NoReturn":
    """Skip an executing test with the given message.

    This function should be called only during testing (setup, call or teardown) or
    during collection by using the ``allow_module_level`` flag.  This function can
    be called in doctests as well.

    :param bool allow_module_level:
        Allows this function to be called at module level, skipping the rest
        of the module. Defaults to False.

    .. note::
        It is better to use the :ref:`pytest.mark.skipif ref` marker when
        possible to declare a test to be skipped under certain conditions
        like mismatching platforms or dependencies.
        Similarly, use the ``# doctest: +SKIP`` directive (see `doctest.SKIP
        <https://docs.python.org/3/library/how-to/doctest.html#doctest.SKIP>`_)
        to skip a doctest statically.
    """
    __tracebackhide__ = True
    raise Skipped(msg=msg, allow_module_level=allow_module_level)
]]></original>
<modified no-ellipsis="true"><![CDATA[
@_with_exception(Skipped)
def skip(msg: str = "", *, allow_module_level: bool = False) -> "NoReturn":
    """Skip an executing test with the given message.

    This function should be called only during testing (setup, call or teardown) or
    during collection by using the ``allow_module_level`` flag.  This function can
    be called in doctests as well.

    :param bool allow_module_level:
        Allows this function to be called at module level, skipping the rest
        of the module. Defaults to False.

    .. note::
        It is better to use the :ref:`pytest.mark.skipif ref` marker when
        possible to declare a test to be skipped under certain conditions
        like mismatching platforms or dependencies.
        Similarly, use the ``# doctest: +SKIP`` directive (see `doctest.SKIP
        <https://docs.python.org/3/library/how-to/doctest.html#doctest.SKIP>`_)
        to skip a doctest statically.

    For module-level skips, consider using `skip_module(reason)` for clarity.
    """
    __tracebackhide__ = True
    raise Skipped(msg=msg, allow_module_level=allow_module_level)


def skip_module(reason: str) -> "NoReturn":
    """Skip the entire module with the given reason.

    This function should be called at the module level to skip the rest of the module.
    It utilizes the `allow_module_level=True` parameter internally.

    :param str reason:
        The reason for skipping the module.
    """
    __tracebackhide__ = True
    raise Skipped(msg=reason, allow_module_level=True)
]]></modified>
</change>

<change>
<file change-number-for-this-file="1">src/_pytest/mark/structures.py</file>
<original line-count="14" no-ellipsis="true"><![CDATA[
Warnings.warn_explicit(
            PytestUnknownMarkWarning(
                f"Unknown pytest.mark.{name} - is this a typo?  You can register "
                "custom marks to avoid this warning - for details, see "
                "https://docs.pytest.org/en/stable/how-to/mark.html"
            ),
            category=None,
            filename=caller_path,
            lineno=caller_lineno,
        )
``` will give me the warning Unknown mark

@final
class Mark:
    """:meth:`.Mark` class"""
]]></original>
<modified no-ellipsis="true"><![CDATA[
warnings.warn_explicit(
            PytestUnknownMarkWarning(
                f"Unknown pytest.mark.{name} - is this a typo?  You can register "
                "custom marks to avoid this warning - for details, see "
                "https://docs.pytest.org/en/stable/how-to/mark.html.\n"
                "For module-level skips, consider using `skip_module(reason)`."
            ),
            category=None,
            filename=caller_path,
            lineno=caller_lineno,
        )
@final
class Mark:
    """:meth:`.Mark` class"""
]]></modified>
</change>
```