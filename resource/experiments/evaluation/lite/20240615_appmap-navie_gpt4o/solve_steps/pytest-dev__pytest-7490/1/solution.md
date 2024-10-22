```xml
<change>
<file change-number-for-this-file="1">src/_pytest/mark/structures.py</file>
<original line-count="14" no-ellipsis="true"><![CDATA[
def __getattr__(self, name: str) -> MarkDecorator:
    if name[0] == "_":
        raise AttributeError("Marker name must NOT start with underscore")

    if self._config is not None:
        # We store a set of markers as a performance optimisation - if a mark
        # name is in the set we definitely know it, but a mark may be known and
        # not in the set.  We therefore start by updating the set!
        if name not in self._markers:
            for line in self._config.getini("markers"):
                # example lines: "skipif(condition): skip the given test if..."
                # or "hypothesis: tests which use Hypothesis", so to get the
                # marker name we split on both `:` and `(`.
                marker = line.split(":")[0].split("(")[0].strip()
                self._markers.add(marker)

            # If the name is not in the set of known marks after updating,
            # then it really is time to issue a warning or an error.
            if name not in self._markers:
                if self._config.option.strict_markers:
                    fail(
                        "{!r} not found in `markers` configuration option".format(name),
                        pytrace=False,
                    )

                # Raise a specific error for common misspellings of "parametrize".
                if name in ["parameterize", "parametrise", "parameterise"]:
                    __tracebackhide__ = True
                    fail("Unknown '{}' mark, did you mean 'parametrize'?".format(name))

                warnings.warn(
                    "Unknown pytest.mark.%s - is this a typo?  You can register "
                    "custom marks to avoid this warning - for details, see "
                    "https://docs.pytest.org/en/stable/mark.html" % name,
                    PytestUnknownMarkWarning,
                    2,
                )

    return MarkDecorator(Mark(name, (), {}))
]]></original>
<modified no-ellipsis="true"><![CDATA[
def __getattr__(self, name: str) -> MarkDecorator:
    if name[0] == "_":
        raise AttributeError("Marker name must NOT start with underscore")

    if self._config is not None:
        # We store a set of markers as a performance optimisation - if a mark
        # name is in the set we definitely know it, but a mark may be known and
        # not in the set.  We therefore start by updating the set!
        if name not in self._markers:
            for line in self._config.getini("markers"):
                # example lines: "skipif(condition): skip the given test if..."
                # or "hypothesis: tests which use Hypothesis", so to get the
                # marker name we split on both `:` and `(`.
                marker = line.split(":")[0].split("(")[0].strip()
                self._markers.add(marker)

            # If the name is not in the set of known marks after updating,
            # then it really is time to issue a warning or an error.
            if name not in self._markers:
                if self._config.option.strict_markers:
                    fail(
                        "{!r} not found in `markers` configuration option".format(name),
                        pytrace=False,
                    )

                # Raise a specific error for common misspellings of "parametrize".
                if name in ["parameterize", "parametrise", "parameterise"]:
                    __tracebackhide__ = True
                    fail("Unknown '{}' mark, did you mean 'parametrize'?".format(name))

                warnings.warn(
                    "Unknown pytest.mark.%s - is this a typo?  You can register "
                    "custom marks to avoid this warning - for details, see "
                    "https://docs.pytest.org/en/stable/mark.html" % name,
                    PytestUnknownMarkWarning,
                    2,
                )

        # Integrate dynamically added markers correctly
        if hasattr(self._config, "_store_additional_markers"):
            dynamic_markers = self._config._store_additional_markers.get(name)
            if dynamic_markers:
                return MarkDecorator(Mark(name, dynamic_markers, {}))

    return MarkDecorator(Mark(name, (), {}))
]]></modified>
</change>

<change>
<file change-number-for-this-file="2">src/_pytest/mark/structures.py</file>
<original line-count="14" no-ellipsis="true"><![CDATA[
def get_empty_parameterset_mark(
    config: Config, argnames: Sequence[str], func
) -> "MarkDecorator":
    from ..nodes import Collector

    fs, lineno = getfslineno(func)
    reason = "got empty parameter set %r, function %s at %s:%d" % (
        argnames,
        func.__name__,
        fs,
        lineno,
    )

    requested_mark = config.getini(EMPTY_PARAMETERSET_OPTION)
    if requested_mark in ("", None, "skip"):
        mark = MARK_GEN.skip(reason=reason)
    elif requested_mark == "xfail":
        mark = MARK_GEN.xfail(reason=reason, run=False)
    elif requested_mark == "fail_at_collect":
        f_name = func.__name__
        _, lineno = getfslineno(func)
        raise Collector.CollectError(
            "Empty parameter set in '%s' at line %d" % (f_name, lineno + 1)
        )
    else:
        raise LookupError(requested_mark)
    return mark
]]></original>
<modified no-ellipsis="true"><![CDATA[
def get_empty_parameterset_mark(
    config: Config, argnames: Sequence[str], func
) -> "MarkDecorator":
    from ..nodes import Collector

    fs, lineno = getfslineno(func)
    reason = "got empty parameter set %r, function %s at %s:%d" % (
        argnames,
        func.__name__,
        fs,
        lineno,
    )

    requested_mark = config.getini(EMPTY_PARAMETERSET_OPTION)
    if requested_mark in ("", None, "skip"):
        mark = MARK_GEN.skip(reason=reason)
    elif requested_mark == "xfail":
        mark = MARK_GEN.xfail(reason=reason, run=False)
    elif requested_mark == "fail_at_collect":
        f_name = func.__name__
        _, lineno = getfslineno(func)
        raise Collector.CollectError(
            "Empty parameter set in '%s' at line %d" % (f_name, lineno + 1)
        )
    else:
        raise LookupError(requested_mark)

    # Integrate dynamically added xfail markers correctly
    if hasattr(config, "_store_additional_markers"):
        additional_markers = config._store_additional_markers.get('xfail')
        if additional_markers:
            mark = MARK_GEN.xfail(reason=additional_markers, run=False)

    return mark
]]></modified>
</change>
```