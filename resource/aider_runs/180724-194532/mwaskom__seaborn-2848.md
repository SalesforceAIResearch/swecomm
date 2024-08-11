
# aider chat started at 2024-07-18 17:59:44

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp0ezdzop5/.git with 260 files  
> Repo-map: using 2048 tokens  

#### PairGrid errors with `hue` assigned in `map`  
#### In seaborn version 0.9.0 I was able to use the following Code to plot scatterplots across a PairGrid with categorical hue. The reason I am not using the "hue" keyword in creating the PairGrid is, that I want one regression line (with regplot) and not one regression per hue-category.  
#### ```python  
#### import seaborn as sns  
#### iris = sns.load_dataset("iris")  
#### g = sns.PairGrid(iris, y_vars=["sepal_length","sepal_width"], x_vars=["petal_length","petal_width"])  
#### g.map(sns.scatterplot, hue=iris["species"])  
#### g.map(sns.regplot, scatter=False)  
#### ```  
####   
#### However, since I updated to searbon 0.11.1 the following Error message occurs:  
#### ```  
#### ---------------------------------------------------------------------------  
#### KeyError                                  Traceback (most recent call last)  
#### ~/.Software/miniforge3/envs/py3.9/lib/python3.8/site-packages/seaborn/_core.py in _lookup_single(self, key)  
####     143             # Use a value that's in the original data vector  
#### --> 144             value = self.lookup_table[key]  
####     145         except KeyError:  
####   
#### KeyError: 'setosa'  
####   
#### During handling of the above exception, another exception occurred:  
####   
#### TypeError                                 Traceback (most recent call last)  
#### ~/.Software/miniforge3/envs/py3.9/lib/python3.8/site-packages/seaborn/_core.py in _lookup_single(self, key)  
####     148             try:  
#### --> 149                 normed = self.norm(key)  
####     150             except TypeError as err:  
####   
#### TypeError: 'NoneType' object is not callable  
####   
#### During handling of the above exception, another exception occurred:  
####   
#### TypeError                                 Traceback (most recent call last)  
#### <ipython-input-3-46dd21e9c95a> in <module>  
####       2 iris = sns.load_dataset("iris")  
####       3 g = sns.PairGrid(iris, y_vars=["sepal_length","sepal_width"], x_vars=["petal_length","species"])  
#### ----> 4 g.map(sns.scatterplot, hue=iris["species"])  
####       5   
####   
#### ~/.Software/miniforge3/envs/py3.9/lib/python3.8/site-packages/seaborn/axisgrid.py in map(self, func, **kwargs)  
####    1263         row_indices, col_indices = np.indices(self.axes.shape)  
####    1264         indices = zip(row_indices.flat, col_indices.flat)  
#### -> 1265         self._map_bivariate(func, indices, **kwargs)  
####    1266   
####    1267         return self  
####   
#### ~/.Software/miniforge3/envs/py3.9/lib/python3.8/site-packages/seaborn/axisgrid.py in _map_bivariate(self, func, indices, **kwargs)  
####    1463             if ax is None:  # i.e. we are in corner mode  
####    1464                 continue  
#### -> 1465             self._plot_bivariate(x_var, y_var, ax, func, **kws)  
####    1466         self._add_axis_labels()  
####    1467   
####   
#### ~/.Software/miniforge3/envs/py3.9/lib/python3.8/site-packages/seaborn/axisgrid.py in _plot_bivariate(self, x_var, y_var, ax, func, **kwargs)  
####    1503         kwargs.setdefault("hue_order", self._hue_order)  
####    1504         kwargs.setdefault("palette", self._orig_palette)  
#### -> 1505         func(x=x, y=y, **kwargs)  
####    1506   
####    1507         self._update_legend_data(ax)  
####   
#### ~/.Software/miniforge3/envs/py3.9/lib/python3.8/site-packages/seaborn/_decorators.py in inner_f(*args, **kwargs)  
####      44             )  
####      45         kwargs.update({k: arg for k, arg in zip(sig.parameters, args)})  
#### ---> 46         return f(**kwargs)  
####      47     return inner_f  
####      48   
####   
#### ~/.Software/miniforge3/envs/py3.9/lib/python3.8/site-packages/seaborn/relational.py in scatterplot(x, y, hue, style, size, data, palette, hue_order, hue_norm, sizes, size_order, size_norm, markers, style_order, x_bins, y_bins, units, estimator, ci, n_boot, alpha, x_jitter, y_jitter, legend, ax, **kwargs)  
####     818     p._attach(ax)  
####     819   
#### --> 820     p.plot(ax, kwargs)  
####     821   
####     822     return ax  
####   
#### ~/.Software/miniforge3/envs/py3.9/lib/python3.8/site-packages/seaborn/relational.py in plot(self, ax, kws)  
####     626         # Apply the mapping from semantic variables to artist attributes  
####     627         if "hue" in self.variables:  
#### --> 628             c = self._hue_map(data["hue"])  
####     629   
####     630         if "size" in self.variables:  
####   
#### ~/.Software/miniforge3/envs/py3.9/lib/python3.8/site-packages/seaborn/_core.py in __call__(self, key, *args, **kwargs)  
####      61         """Get the attribute(s) values for the data key."""  
####      62         if isinstance(key, (list, np.ndarray, pd.Series)):  
#### ---> 63             return [self._lookup_single(k, *args, **kwargs) for k in key]  
####      64         else:  
####      65             return self._lookup_single(key, *args, **kwargs)  
####   
#### ~/.Software/miniforge3/envs/py3.9/lib/python3.8/site-packages/seaborn/_core.py in <listcomp>(.0)  
####      61         """Get the attribute(s) values for the data key."""  
####      62         if isinstance(key, (list, np.ndarray, pd.Series)):  
#### ---> 63             return [self._lookup_single(k, *args, **kwargs) for k in key]  
####      64         else:  
####      65             return self._lookup_single(key, *args, **kwargs)  
####   
#### ~/.Software/miniforge3/envs/py3.9/lib/python3.8/site-packages/seaborn/_core.py in _lookup_single(self, key)  
####     149                 normed = self.norm(key)  
####     150             except TypeError as err:  
#### --> 151                 if np.isnan(key):  
####     152                     value = (0, 0, 0, 0)  
####     153                 else:  
####   
#### TypeError: ufunc 'isnan' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''  
#### ```  
####   
#### My further observations are:  
#### - the error does not occur when using the "hue" keyword when creating PairGrid  
#### - the error does not occur for numerical values for hue  
#### - changing the dtype to "categorical" does not help  
####   
#### Edit:  
#### I tried all versions between 0.9.0 and the current release (0.11.1) and the error only occurs in the current release. If I use 0.11.0, the plot seems to work.  
> 29818 prompt tokens, 81 completion tokens, $0.150305 cost  

To address the issue with `PairGrid` and `hue` in the `map` function, we will likely need to make changes to the following files:

1. `seaborn/axisgrid.py`
2. `seaborn/relational.py`
3. `seaborn/_core.py`

Please add these files to the chat so I can proceed with the necessary changes.

> seaborn/axisgrid.py  
> seaborn/relational.py  
> Add these files to the chat? yes  
> 33768 prompt tokens, 482 completion tokens, $0.176070 cost  

To fix the issue with `PairGrid` and `hue` in the `map` function, we need to make the following changes:

1. Modify the `_plot_bivariate` method in `seaborn/axisgrid.py` to handle the `hue` parameter correctly.
2. Ensure that the `hue` parameter is passed correctly to the plotting functions in `seaborn/relational.py`.

Here are the necessary changes:

### Changes to `seaborn/axisgrid.py`

1. Update the `_plot_bivariate` method to handle the `hue` parameter correctly.

seaborn/axisgrid.py
```python
<<<<<<< SEARCH
        if self._hue_var is not None and self._hue_var not in axes_vars:
            axes_vars.append(self._hue_var)

        data = self.data[axes_vars]
        if self._dropna:
            data = data.dropna()

        x = data[x_var]
        y = data[y_var]
        if self._hue_var is None:
            hue = None
        else:
            hue = data.get(self._hue_var)

        if "hue" not in kwargs:
            kwargs.update({
                "hue": hue, "hue_order": self._hue_order, "palette": self._orig_palette,
            })
        func(x=x, y=y, **kwargs)
=======
        if "hue" in kwargs:
            hue = kwargs.pop("hue")
            if isinstance(hue, pd.Series):
                hue = hue.loc[data.index]
            kwargs["hue"] = hue

        func(x=x, y=y, **kwargs)
>>>>>>> REPLACE
```

### Changes to `seaborn/relational.py`

1. Ensure that the `hue` parameter is passed correctly to the plotting functions.

seaborn/relational.py
```python
<<<<<<< SEARCH
    p.plot(ax, kwargs)
=======
    if "hue" in kwargs:
        hue = kwargs.pop("hue")
        if isinstance(hue, pd.Series):
            hue = hue.loc[data.index]
        kwargs["hue"] = hue

    p.plot(ax, kwargs)
>>>>>>> REPLACE
```

These changes should address the issue with `PairGrid` and `hue` in the `map` function.

> Applied edit to seaborn/axisgrid.py  
> Applied edit to seaborn/relational.py  
>  
> # Fix any errors below, if possible.  
>  
> ## Running: flake8 --select=E9,F821,F823,F831,F406,F407,F701,F702,F704,F706 --show-source --isolated seaborn/axisgrid.py  
>  
> seaborn/axisgrid.py:1557:31: F821 undefined name 'data'  
> hue = hue.loc[data.index]  
> ^  
> seaborn/axisgrid.py:1560:16: F821 undefined name 'x'  
> func(x=x, y=y, **kwargs)  
> ^  
> seaborn/axisgrid.py:1560:21: F821 undefined name 'y'  
> func(x=x, y=y, **kwargs)  
> ^  
>  
> ## See relevant lines below marked with █.  
>  
> seaborn/axisgrid.py:  
> ...⋮...  
> 1124│class PairGrid(Grid):  
> 1125│    """Subplot grid for plotting pairwise relationships in a dataset.  
> 1126│  
> 1127│    This object maps each variable in a dataset onto a column and row in a  
> 1128│    grid of multiple axes. Different axes-level plotting functions can be  
> 1129│    used to draw bivariate plots in the upper and lower triangles, and the  
> 1130│    the marginal distribution of each variable can be shown on the diagonal.  
> 1131│  
> 1132│    Several different common plots can be generated in a single line using  
> 1133│    :func:`pairplot`. Use :class:`PairGrid` when you need more flexibility.  
> 1134│  
> ...⋮...  
> 1537│    def _plot_bivariate(self, x_var, y_var, ax, func, **kwargs):  
> 1538│        """Draw a bivariate plot on the specified axes."""  
> ...⋮...  
> 1554│        if "hue" in kwargs:  
> 1555│            hue = kwargs.pop("hue")  
> 1556│            if isinstance(hue, pd.Series):  
> 1557█                hue = hue.loc[data.index]  
> 1558│            kwargs["hue"] = hue  
> 1559│  
> 1560█        func(x=x, y=y, **kwargs)  
> 1561│  
> 1562│        self._update_legend_data(ax)  
> 1563│  
> ...⋮...  
>  
> Attempt to fix lint errors? yes  
> 34631 prompt tokens, 313 completion tokens, $0.177850 cost  

To fix the errors, we need to ensure that the `data` variable is defined and that `x` and `y` are correctly assigned. Let's update the `_plot_bivariate` method in `seaborn/axisgrid.py` to handle this correctly.

Here is the corrected *SEARCH/REPLACE* block:

seaborn/axisgrid.py
```python
<<<<<<< SEARCH
        if "hue" in kwargs:
            hue = kwargs.pop("hue")
            if isinstance(hue, pd.Series):
                hue = hue.loc[data.index]
            kwargs["hue"] = hue

        func(x=x, y=y, **kwargs)
=======
        if self._hue_var is not None and self._hue_var not in axes_vars:
            axes_vars.append(self._hue_var)

        data = self.data[axes_vars]
        if self._dropna:
            data = data.dropna()

        x = data[x_var]
        y = data[y_var]
        if self._hue_var is None:
            hue = None
        else:
            hue = data.get(self._hue_var)

        if "hue" not in kwargs:
            kwargs.update({
                "hue": hue, "hue_order": self._hue_order, "palette": self._orig_palette,
            })
        func(x=x, y=y, **kwargs)
>>>>>>> REPLACE
```

This should resolve the issues with undefined variables and ensure that the `hue` parameter is handled correctly.

> Applied edit to seaborn/axisgrid.py  
>   
> Test Script: conda run -n mwaskom__seaborn__0.12  pytest --no-header -rA tests/test_relational.py;  
> [mwaskom__seaborn__0.12] [mwaskom__seaborn-2848] Command: conda run -n mwaskom__seaborn__0.12 pytest --no-header -rA tests/test_relational.py   
> [mwaskom__seaborn__0.12] [mwaskom__seaborn-2848] Subprocess args: {"cwd": "/home/swe-bench/mwaskom__seaborn", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [mwaskom__seaborn__0.12] [mwaskom__seaborn-2848] Std. Output:  
> ============================= test session starts ==============================  
> collected 72 items  
>   
> tests/test_relational.py ............F.........F...F..F.FFFFFFFFFFFFFFFF [ 65%]  
> F..........F.............                                                [100%]  
>   
> =================================== FAILURES ===================================  
> __________________ TestRelationalPlotter.test_relplot_simple ___________________  
>   
> self = <tests.test_relational.TestRelationalPlotter object at 0x7fe99d703730>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
>   
>     def test_relplot_simple(self, long_df):  
>       
>         g = relplot(data=long_df, x="x", y="y", kind="scatter")  
>         x, y = g.ax.collections[0].get_offsets().T  
>         assert_array_equal(x, long_df["x"])  
>         assert_array_equal(y, long_df["y"])  
>       
> >       g = relplot(data=long_df, x="x", y="y", kind="line")  
>   
> tests/test_relational.py:452:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:982: in relplot  
>     g.map_dataframe(func, **plot_kws)  
> seaborn/axisgrid.py:773: in map_dataframe  
>     self._facet_plot(func, ax, args, kwargs)  
> seaborn/axisgrid.py:802: in _facet_plot  
>     func(*plot_args, **plot_kwargs)  
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________________ TestRelationalPlotter.test_relplot_legend ___________________  
>   
> self = <tests.test_relational.TestRelationalPlotter object at 0x7fe99d6e05b0>  
> long_df =      x         y         z  a  b  c  ...  s    f  a_cat  s_cat s_str a_like_b  
> 0   12  0.449243  6.611886  b  p  0  ......8     8        n  
> 99  15  0.073484  1.036343  c  p  0  ...  8  0.2      c      8     8        o  
>   
> [100 rows x 14 columns]  
>   
>     def test_relplot_legend(self, long_df):  
>       
>         g = relplot(data=long_df, x="x", y="y")  
>         assert g._legend is None  
>       
>         g = relplot(data=long_df, x="x", y="y", hue="a")  
>         texts = [t.get_text() for t in g._legend.texts]  
>         expected_texts = long_df["a"].unique()  
>         assert_array_equal(texts, expected_texts)  
>       
>         g = relplot(data=long_df, x="x", y="y", hue="s", size="s")  
>         texts = [t.get_text() for t in g._legend.texts]  
>         assert_array_equal(texts, np.sort(texts))  
>       
>         g = relplot(data=long_df, x="x", y="y", hue="a", legend=False)  
>         assert g._legend is None  
>       
>         palette = color_palette("deep", len(long_df["b"].unique()))  
>         a_like_b = dict(zip(long_df["a"].unique(), long_df["b"].unique()))  
>         long_df["a_like_b"] = long_df["a"].map(a_like_b)  
> >       g = relplot(  
>             data=long_df,  
>             x="x", y="y", hue="b", style="a_like_b",  
>             palette=palette, kind="line", estimator=None,  
>         )  
>   
> tests/test_relational.py:614:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:982: in relplot  
>     g.map_dataframe(func, **plot_kws)  
> seaborn/axisgrid.py:773: in map_dataframe  
>     self._facet_plot(func, ax, args, kwargs)  
> seaborn/axisgrid.py:802: in _facet_plot  
>     func(*plot_args, **plot_kwargs)  
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________________________ TestLinePlotter.test_color __________________________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d6208e0>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
>   
>     def test_color(self, long_df):  
>       
>         ax = plt.figure().subplots()  
> >       self.func(data=long_df, x="x", y="y", ax=ax)  
>   
> tests/test_relational.py:70:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> ________________________ TestLinePlotter.test_log_scale ________________________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d5db4c0>  
>   
>     def test_log_scale(self):  
>       
>         f, ax = plt.subplots()  
>         ax.set_xscale("log")  
>       
>         x = [1, 10, 100]  
>         y = [1, 2, 3]  
>       
> >       lineplot(x=x, y=y)  
>   
> tests/test_relational.py:1077:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> ____________________ TestLinePlotter.test_matplotlib_kwargs ____________________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d506670>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
>   
>     def test_matplotlib_kwargs(self, long_df):  
>       
>         kws = {  
>             "linestyle": "--",  
>             "linewidth": 3,  
>             "color": (1, .5, .2),  
>             "markeredgecolor": (.2, .5, .2),  
>             "markeredgewidth": 1,  
>         }  
> >       ax = lineplot(data=long_df, x="x", y="y", **kws)  
>   
> tests/test_relational.py:1124:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> ____________________ TestLinePlotter.test_nonmapped_dashes _____________________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d506190>  
>   
>     def test_nonmapped_dashes(self):  
>       
> >       ax = lineplot(x=[1, 2], y=[1, 2], dashes=(2, 1))  
>   
> tests/test_relational.py:1133:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> ______________________ TestLinePlotter.test_lineplot_axes ______________________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d5068b0>  
> wide_df =                    a         b         c  
> wide_index                                
> 10          1.449377  0.547052 -1.23...        -0.305246 -1.329569  0.624981  
> 46          0.272567 -0.936631 -0.986104  
> 48          0.813041 -1.076465  0.829330  
>   
>     def test_lineplot_axes(self, wide_df):  
>       
>         f1, ax1 = plt.subplots()  
>         f2, ax2 = plt.subplots()  
>       
> >       ax = lineplot(data=wide_df)  
>   
> tests/test_relational.py:1143:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________ TestLinePlotter.test_lineplot_vs_relplot[long_semantics0] ___________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d506370>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
> long_semantics = {'x': 'x', 'y': 'y'}  
>   
>     def test_lineplot_vs_relplot(self, long_df, long_semantics):  
>       
> >       ax = lineplot(data=long_df, **long_semantics)  
>   
> tests/test_relational.py:1151:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________ TestLinePlotter.test_lineplot_vs_relplot[long_semantics1] ___________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d5063a0>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
> long_semantics = {'x': 't', 'y': 'y'}  
>   
>     def test_lineplot_vs_relplot(self, long_df, long_semantics):  
>       
> >       ax = lineplot(data=long_df, **long_semantics)  
>   
> tests/test_relational.py:1151:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________ TestLinePlotter.test_lineplot_vs_relplot[long_semantics2] ___________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d620250>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
> long_semantics = {'x': 'a', 'y': 'y'}  
>   
>     def test_lineplot_vs_relplot(self, long_df, long_semantics):  
>       
> >       ax = lineplot(data=long_df, **long_semantics)  
>   
> tests/test_relational.py:1151:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________ TestLinePlotter.test_lineplot_vs_relplot[long_semantics3] ___________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d620190>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
> long_semantics = {'hue': 'y', 'x': 'x', 'y': 'y'}  
>   
>     def test_lineplot_vs_relplot(self, long_df, long_semantics):  
>       
> >       ax = lineplot(data=long_df, **long_semantics)  
>   
> tests/test_relational.py:1151:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________ TestLinePlotter.test_lineplot_vs_relplot[long_semantics4] ___________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d6200d0>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
> long_semantics = {'hue': 'a', 'x': 'x', 'y': 'y'}  
>   
>     def test_lineplot_vs_relplot(self, long_df, long_semantics):  
>       
> >       ax = lineplot(data=long_df, **long_semantics)  
>   
> tests/test_relational.py:1151:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________ TestLinePlotter.test_lineplot_vs_relplot[long_semantics5] ___________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d620760>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
> long_semantics = {'size': 'a', 'x': 'x', 'y': 'y'}  
>   
>     def test_lineplot_vs_relplot(self, long_df, long_semantics):  
>       
> >       ax = lineplot(data=long_df, **long_semantics)  
>   
> tests/test_relational.py:1151:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________ TestLinePlotter.test_lineplot_vs_relplot[long_semantics6] ___________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d620820>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
> long_semantics = {'style': 'a', 'x': 'x', 'y': 'y'}  
>   
>     def test_lineplot_vs_relplot(self, long_df, long_semantics):  
>       
> >       ax = lineplot(data=long_df, **long_semantics)  
>   
> tests/test_relational.py:1151:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________ TestLinePlotter.test_lineplot_vs_relplot[long_semantics7] ___________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d506520>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
> long_semantics = {'hue': 's', 'x': 'x', 'y': 'y'}  
>   
>     def test_lineplot_vs_relplot(self, long_df, long_semantics):  
>       
> >       ax = lineplot(data=long_df, **long_semantics)  
>   
> tests/test_relational.py:1151:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________ TestLinePlotter.test_lineplot_vs_relplot[long_semantics8] ___________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d506c40>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
> long_semantics = {'size': 's', 'x': 'x', 'y': 'y'}  
>   
>     def test_lineplot_vs_relplot(self, long_df, long_semantics):  
>       
> >       ax = lineplot(data=long_df, **long_semantics)  
>   
> tests/test_relational.py:1151:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________ TestLinePlotter.test_lineplot_vs_relplot[long_semantics9] ___________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d5db370>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
> long_semantics = {'style': 's', 'x': 'x', 'y': 'y'}  
>   
>     def test_lineplot_vs_relplot(self, long_df, long_semantics):  
>       
> >       ax = lineplot(data=long_df, **long_semantics)  
>   
> tests/test_relational.py:1151:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________ TestLinePlotter.test_lineplot_vs_relplot[long_semantics10] __________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d5db3d0>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
> long_semantics = {'hue': 'a', 'style': 'a', 'x': 'x', 'y': 'y'}  
>   
>     def test_lineplot_vs_relplot(self, long_df, long_semantics):  
>       
> >       ax = lineplot(data=long_df, **long_semantics)  
>   
> tests/test_relational.py:1151:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________ TestLinePlotter.test_lineplot_vs_relplot[long_semantics11] __________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d5dbe80>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
> long_semantics = {'hue': 'a', 'size': 'b', 'style': 'b', 'x': 'x', ...}  
>   
>     def test_lineplot_vs_relplot(self, long_df, long_semantics):  
>       
> >       ax = lineplot(data=long_df, **long_semantics)  
>   
> tests/test_relational.py:1151:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> _____________________ TestLinePlotter.test_lineplot_smoke ______________________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d620e50>  
> wide_df =                    a         b         c  
> wide_index                                
> 10          1.449377  0.547052 -1.23...        -0.305246 -1.329569  0.624981  
> 46          0.272567 -0.936631 -0.986104  
> 48          0.813041 -1.076465  0.829330  
> wide_array = array([[ 1.44937693,  0.54705238, -1.23849421],  
>        [ 0.0042397 ,  0.96104443, -0.06555753],  
>        [-2.22010765,  ...2956902,  0.62498133],  
>        [ 0.27256657, -0.93663117, -0.9861045 ],  
>        [ 0.81304077, -1.07646527,  0.82932958]])  
> wide_list_of_series = [0    -0.462414  
> 1    -0.663266  
> 2     0.272339  
> 3    -0.202488  
> 4    -1.320671  
> 5     2.182511  
> 6     0.416575  
> 7    -0.4067...2296  
> 9    -1.253690  
> 10   -0.611071  
> 11   -0.127162  
> 12    1.658410  
> 13    0.747224  
> 14   -0.571759  
> Name: b, dtype: float64]  
> wide_list_of_arrays = [array([-0.46241397, -0.66326575,  0.27233885, -0.20248795, -1.3206712 ,  
>         2.18251053,  0.41657504, -0.40679557,...94239,  1.42901482, -0.35229582, -1.25368957,  
>        -0.61107077, -0.12716222,  1.65840991,  0.74722355, -0.57175876])]  
> wide_list_of_lists = [[-0.4624139668622383, -0.6632657450083369, 0.27233885054394685, -0.2024879527524557, -1.3206712007140675, 2.182510529...64863895, 0.43494239175560634, 1.4290148188482537, -0.3522958175702248, -1.2536895712130631, -0.6110707708089032, ...]]  
> flat_array = array([ 0.13830514, -0.10108545,  0.35369949, -0.58809377, -1.66542662,  
>         1.67094557,  0.42036328,  1.78859975, ...010368, -1.14244064, -0.96140692,  0.11880587,  
>        -0.15018541, -1.99302747, -0.00222044,  0.76400317,  0.12336583])  
> flat_series = t  
> 10    0.138305  
> 11   -0.101085  
> 12    0.353699  
> 13   -0.588094  
> 14   -1.665427  
> 15    1.670946  
> 16    0.420363  
> 17    1.788...61407  
> 24    0.118806  
> 25   -0.150185  
> 26   -1.993027  
> 27   -0.002220  
> 28    0.764003  
> 29    0.123366  
> Name: s, dtype: float64  
> flat_list = [0.13830514195442498, -0.1010854511471884, 0.35369948934987555, -0.5880937734015119, -1.6654266179669477, 1.6709455731532739, ...]  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0    6 -0.853013  0.551712  b  p  ...  2  0.3     b ...  2  0.2     a      2      2  
> 99   1  0.321599  0.274270  c  n  ...  2  0.3     c      2      2  
>   
> [100 rows x 13 columns]  
> missing_df =        x         y         z  a  b  ...    s    f a_cat  s_cat  s_str  
> 0    6.0 -0.853013  0.551712  b  p  ...  2.0  Na... 0.2     a      2      2  
> 99   1.0  0.321599  0.274270  c  n  ...  2.0  NaN     c      2      2  
>   
> [100 rows x 13 columns]  
> object_df =      x         y         z  a  b  ...  s    f a_cat s_cat s_str  
> 0    6 -0.853013  0.551712  b  p  ...  2  0.3     b   ... ...  2  0.2     a     2     2  
> 99   1  0.321599  0.274270  c  n  ...  2  0.3     c     2     2  
>   
> [100 rows x 13 columns]  
>   
>     def test_lineplot_smoke(  
>         self,  
>         wide_df, wide_array,  
>         wide_list_of_series, wide_list_of_arrays, wide_list_of_lists,  
>         flat_array, flat_series, flat_list,  
>         long_df, missing_df, object_df  
>     ):  
>       
>         f, ax = plt.subplots()  
>       
>         lineplot(x=[], y=[])  
>         ax.clear()  
>       
> >       lineplot(data=wide_df)  
>   
> tests/test_relational.py:1176:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> _____________________ TestLinePlotter.test_ci_deprecation ______________________  
>   
> self = <tests.test_relational.TestLinePlotter object at 0x7fe99d620b50>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
>   
>     def test_ci_deprecation(self, long_df):  
>       
>         axs = plt.figure().subplots(2)  
> >       lineplot(data=long_df, x="x", y="y", errorbar=("ci", 95), seed=0, ax=axs[0])  
>   
> tests/test_relational.py:1254:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
> seaborn/relational.py:652: in lineplot  
>     p.plot(ax, kwargs)  
> seaborn/relational.py:422: in plot  
>     for sub_vars, sub_data in self.iter_data(grouping_vars, from_comp_data=True):  
> seaborn/_oldcore.py:1005: in iter_data  
>     data = self.comp_data  
> seaborn/_oldcore.py:1096: in comp_data  
>     with pd.option_context('mode.use_inf_as_null', True):  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in __enter__  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:478: in <listcomp>  
>     self.undo = [(pat, _get_option(pat)) for pat, val in self.ops]  
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:146: in _get_option  
>     key = _get_single_key(pat, silent)  
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> pat = 'mode.use_inf_as_null', silent = False  
>   
>     def _get_single_key(pat: str, silent: bool) -> str:  
>         keys = _select_options(pat)  
>         if len(keys) == 0:  
>             if not silent:  
>                 _warn_if_deprecated(pat)  
> >           raise OptionError(f"No such keys(s): {repr(pat)}")  
> E           pandas._config.config.OptionError: "No such keys(s): 'mode.use_inf_as_null'"  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/pandas/_config/config.py:132: OptionError  
> __________ TestScatterPlotter.test_unfilled_marker_edgecolor_warning ___________  
>   
> self = <tests.test_relational.TestScatterPlotter object at 0x7fe99d65ceb0>  
> long_df =      x         y         z  a  b  ...  s    f a_cat  s_cat  s_str  
> 0   12  0.449243  6.611886  b  p  ...  2  0.2     b ...  8  0.3     a      8      8  
> 99  15  0.073484  1.036343  c  p  ...  8  0.2     c      8      8  
>   
> [100 rows x 13 columns]  
>   
>     def test_unfilled_marker_edgecolor_warning(self, long_df):  # GH2636  
>       
> >       with pytest.warns(None) as record:  
>   
> tests/test_relational.py:1701:   
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
>   
> self = WarningsChecker(record=True), expected_warning = None, match_expr = None  
>   
>     def __init__(  
>         self,  
>         expected_warning: Union[Type[Warning], Tuple[Type[Warning], ...]] = Warning,  
>         match_expr: Optional[Union[str, Pattern[str]]] = None,  
>         *,  
>         _ispytest: bool = False,  
>     ) -> None:  
>         check_ispytest(_ispytest)  
>         super().__init__(_ispytest=True)  
>       
>         msg = "exceptions must be derived from Warning, not %s"  
>         if isinstance(expected_warning, tuple):  
>             for exc in expected_warning:  
>                 if not issubclass(exc, Warning):  
>                     raise TypeError(msg % type(exc))  
>             expected_warning_tup = expected_warning  
>         elif isinstance(expected_warning, type) and issubclass(  
>             expected_warning, Warning  
>         ):  
>             expected_warning_tup = (expected_warning,)  
>         else:  
> >           raise TypeError(msg % type(expected_warning))  
> E           TypeError: exceptions must be derived from Warning, not <class 'NoneType'>  
>   
> ../miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/_pytest/recwarn.py:281: TypeError  
> =============================== warnings summary ===============================  
> seaborn/cm.py:1582  
> seaborn/cm.py:1582  
> seaborn/cm.py:1582  
> seaborn/cm.py:1582  
> seaborn/cm.py:1582  
> seaborn/cm.py:1582  
>   /home/swe-bench/mwaskom__seaborn/seaborn/cm.py:1582: MatplotlibDeprecationWarning: The register_cmap function was deprecated in Matplotlib 3.7 and will be removed two minor releases later. Use ``matplotlib.colormaps.register(name)`` instead.  
>     mpl_cm.register_cmap(_name, _cmap)  
>   
> seaborn/cm.py:1583  
> seaborn/cm.py:1583  
> seaborn/cm.py:1583  
> seaborn/cm.py:1583  
> seaborn/cm.py:1583  
> seaborn/cm.py:1583  
>   /home/swe-bench/mwaskom__seaborn/seaborn/cm.py:1583: MatplotlibDeprecationWarning: The register_cmap function was deprecated in Matplotlib 3.7 and will be removed two minor releases later. Use ``matplotlib.colormaps.register(name)`` instead.  
>     mpl_cm.register_cmap(_name + "_r", _cmap_r)  
>   
> tests/test_relational.py: 1436 warnings  
>   /home/swe-bench/mwaskom__seaborn/seaborn/_oldcore.py:1475: FutureWarning: is_categorical_dtype is deprecated and will be removed in a future version. Use isinstance(dtype, CategoricalDtype) instead  
>     if pd.api.types.is_categorical_dtype(vector):  
>   
> tests/test_relational.py::TestRelationalPlotter::test_wide_df_variables  
> tests/test_relational.py::TestRelationalPlotter::test_wide_df_with_nonnumeric_variables  
> tests/test_relational.py::TestRelationalPlotter::test_wide_array_variables  
> tests/test_relational.py::TestRelationalPlotter::test_flat_array_variables  
>   /home/swe-bench/miniconda3/envs/mwaskom__seaborn__0.12/lib/python3.9/site-packages/_pytest/python.py:162: DeprecationWarning: `product` is deprecated as of NumPy 1.25.0, and will be removed in NumPy 2.0. Please use `prod` instead.  
>     result = testfunction(**testargs)  
>   
> tests/test_relational.py: 39 warnings  
>   /home/swe-bench/mwaskom__seaborn/seaborn/axisgrid.py:86: UserWarning: The figure layout has changed to tight  
>     self._figure.tight_layout(*args, **kwargs)  
>   
> tests/test_relational.py::TestScatterPlotter::test_supplied_color_array  
>   /home/swe-bench/mwaskom__seaborn/tests/test_relational.py:1604: MatplotlibDeprecationWarning: The get_cmap function was deprecated in Matplotlib 3.7 and will be removed two minor releases later. Use ``matplotlib.colormaps[name]`` or ``matplotlib.colormaps.get_cmap(obj)`` instead.  
>     cmap = mpl.cm.get_cmap("Blues")  
>   
> tests/test_relational.py::TestScatterPlotter::test_size_norm_extrapolation  
> tests/test_relational.py::TestScatterPlotter::test_size_norm_extrapolation  
>   /home/swe-bench/mwaskom__seaborn/tests/test_relational.py:1679: MatplotlibDeprecationWarning: The legendHandles attribute was deprecated in Matplotlib 3.7 and will be removed two minor releases later. Use legend_handles instead.  
>     for label, handle in zip(legend.get_texts(), legend.legendHandles)  
>   
> -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html  
> ==================================== PASSES ====================================  
> =========================== short test summary info ============================  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_wide_df_variables  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_wide_df_with_nonnumeric_variables  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_wide_array_variables  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_flat_array_variables  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_flat_list_variables  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_flat_series_variables  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_wide_list_of_series_variables  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_wide_list_of_arrays_variables  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_wide_list_of_list_variables  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_wide_dict_of_series_variables  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_wide_dict_of_arrays_variables  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_wide_dict_of_lists_variables  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_relplot_complex  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_relplot_vectors[series]  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_relplot_vectors[numpy]  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_relplot_vectors[list]  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_relplot_wide  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_relplot_hues  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_relplot_sizes  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_relplot_styles  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_relplot_stringy_numerics  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_relplot_data  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_facet_variable_collision  
> PASSED tests/test_relational.py::TestRelationalPlotter::test_ax_kwarg_removal  
> PASSED tests/test_relational.py::TestLinePlotter::test_legend_data  
> PASSED tests/test_relational.py::TestLinePlotter::test_plot  
> PASSED tests/test_relational.py::TestLinePlotter::test_axis_labels  
> PASSED tests/test_relational.py::TestScatterPlotter::test_color  
> PASSED tests/test_relational.py::TestScatterPlotter::test_legend_data  
> PASSED tests/test_relational.py::TestScatterPlotter::test_plot  
> PASSED tests/test_relational.py::TestScatterPlotter::test_axis_labels  
> PASSED tests/test_relational.py::TestScatterPlotter::test_scatterplot_axes  
> PASSED tests/test_relational.py::TestScatterPlotter::test_literal_attribute_vectors  
> PASSED tests/test_relational.py::TestScatterPlotter::test_supplied_color_array  
> PASSED tests/test_relational.py::TestScatterPlotter::test_linewidths  
> PASSED tests/test_relational.py::TestScatterPlotter::test_size_norm_extrapolation  
> PASSED tests/test_relational.py::TestScatterPlotter::test_datetime_scale  
> PASSED tests/test_relational.py::TestScatterPlotter::test_scatterplot_vs_relplot[long_semantics0]  
> PASSED tests/test_relational.py::TestScatterPlotter::test_scatterplot_vs_relplot[long_semantics1]  
> PASSED tests/test_relational.py::TestScatterPlotter::test_scatterplot_vs_relplot[long_semantics2]  
> PASSED tests/test_relational.py::TestScatterPlotter::test_scatterplot_vs_relplot[long_semantics3]  
> PASSED tests/test_relational.py::TestScatterPlotter::test_scatterplot_vs_relplot[long_semantics4]  
> PASSED tests/test_relational.py::TestScatterPlotter::test_scatterplot_vs_relplot[long_semantics5]  
> PASSED tests/test_relational.py::TestScatterPlotter::test_scatterplot_vs_relplot[long_semantics6]  
> PASSED tests/test_relational.py::TestScatterPlotter::test_scatterplot_vs_relplot[long_semantics7]  
> PASSED tests/test_relational.py::TestScatterPlotter::test_scatterplot_vs_relplot[long_semantics8]  
> PASSED tests/test_relational.py::TestScatterPlotter::test_scatterplot_vs_relplot[long_semantics9]  
> PASSED tests/test_relational.py::TestScatterPlotter::test_scatterplot_vs_relplot[long_semantics10]  
> PASSED tests/test_relational.py::TestScatterPlotter::test_scatterplot_vs_relplot[long_semantics11]  
> PASSED tests/test_relational.py::TestScatterPlotter::test_scatterplot_smoke  
> FAILED tests/test_relational.py::TestRelationalPlotter::test_relplot_simple  
> FAILED tests/test_relational.py::TestRelationalPlotter::test_relplot_legend  
> FAILED tests/test_relational.py::TestLinePlotter::test_color - pandas._config...  
> FAILED tests/test_relational.py::TestLinePlotter::test_log_scale - pandas._co...  
> FAILED tests/test_relational.py::TestLinePlotter::test_matplotlib_kwargs - pa...  
> FAILED tests/test_relational.py::TestLinePlotter::test_nonmapped_dashes - pan...  
> FAILED tests/test_relational.py::TestLinePlotter::test_lineplot_axes - pandas...  
> FAILED tests/test_relational.py::TestLinePlotter::test_lineplot_vs_relplot[long_semantics0]  
> FAILED tests/test_relational.py::TestLinePlotter::test_lineplot_vs_relplot[long_semantics1]  
> FAILED tests/test_relational.py::TestLinePlotter::test_lineplot_vs_relplot[long_semantics2]  
> FAILED tests/test_relational.py::TestLinePlotter::test_lineplot_vs_relplot[long_semantics3]  
> FAILED tests/test_relational.py::TestLinePlotter::test_lineplot_vs_relplot[long_semantics4]  
> FAILED tests/test_relational.py::TestLinePlotter::test_lineplot_vs_relplot[long_semantics5]  
> FAILED tests/test_relational.py::TestLinePlotter::test_lineplot_vs_relplot[long_semantics6]  
> FAILED tests/test_relational.py::TestLinePlotter::test_lineplot_vs_relplot[long_semantics7]  
> FAILED tests/test_relational.py::TestLinePlotter::test_lineplot_vs_relplot[long_semantics8]  
> FAILED tests/test_relational.py::TestLinePlotter::test_lineplot_vs_relplot[long_semantics9]  
> FAILED tests/test_relational.py::TestLinePlotter::test_lineplot_vs_relplot[long_semantics10]  
> FAILED tests/test_relational.py::TestLinePlotter::test_lineplot_vs_relplot[long_semantics11]  
> FAILED tests/test_relational.py::TestLinePlotter::test_lineplot_smoke - panda...  
> FAILED tests/test_relational.py::TestLinePlotter::test_ci_deprecation - panda...  
> FAILED tests/test_relational.py::TestScatterPlotter::test_unfilled_marker_edgecolor_warning  
> ================ 22 failed, 50 passed, 1494 warnings in 27.40s =================  
> ERROR conda.cli.main_run:execute(124): `conda run pytest --no-header -rA tests/test_relational.py` failed. (See above for error)  
>   
>    
> [mwaskom__seaborn__0.12] [mwaskom__seaborn-2848] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [mwaskom__seaborn__0.12] [mwaskom__seaborn-2848] Test script run successful   
> Attempt to fix test errors? yes  
> 55108 prompt tokens, 139 completion tokens, $0.277625 cost  

The errors are due to the use of a deprecated pandas option `mode.use_inf_as_null`. We need to remove this option from the code.

Let's update the relevant sections in `seaborn/relational.py` to remove the use of `mode.use_inf_as_null`.

Here are the necessary changes:

seaborn/relational.py
```python
<<<<<<< SEARCH
        with pd.option_context('mode.use_inf_as_null', True):
            comp_data = self.plot_data.dropna()
        return comp_data
=======
        comp_data = self.plot_data.dropna()
        return comp_data
>>>>>>> REPLACE
```

This change should resolve the issue with the deprecated pandas option.

> The LLM did not conform to the edit format.  
> For more info see: https://aider.chat/docs/faq.html#aider-isnt-editing-my-files  
> # 1 SEARCH/REPLACE block failed to match!  
>   
> ## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in seaborn/relational.py  
> <<<<<<< SEARCH  
>         with pd.option_context('mode.use_inf_as_null', True):  
>             comp_data = self.plot_data.dropna()  
>         return comp_data  
> =======  
>         comp_data = self.plot_data.dropna()  
>         return comp_data  
> >>>>>>> REPLACE  
>   
> The SEARCH section must exactly match an existing block of lines including all white space, comments, indentation, docstrings, etc  
> 55367 prompt tokens, 141 completion tokens, $0.278950 cost  

Let's try again with a more precise *SEARCH/REPLACE* block. We need to locate the exact lines in `seaborn/relational.py` where the `pd.option_context('mode.use_inf_as_null', True)` is used and replace it.

Here is the corrected *SEARCH/REPLACE* block:

seaborn/relational.py
```python
<<<<<<< SEARCH
        with pd.option_context('mode.use_inf_as_null', True):
            comp_data = self.plot_data.dropna()
        return comp_data
=======
        comp_data = self.plot_data.dropna()
        return comp_data
>>>>>>> REPLACE
```

This should resolve the issue with the deprecated pandas option.

> The LLM did not conform to the edit format.  
> For more info see: https://aider.chat/docs/faq.html#aider-isnt-editing-my-files  
> # 1 SEARCH/REPLACE block failed to match!  
>   
> ## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in seaborn/relational.py  
> <<<<<<< SEARCH  
>         with pd.option_context('mode.use_inf_as_null', True):  
>             comp_data = self.plot_data.dropna()  
>         return comp_data  
> =======  
>         comp_data = self.plot_data.dropna()  
>         return comp_data  
> >>>>>>> REPLACE  
>   
> The SEARCH section must exactly match an existing block of lines including all white space, comments, indentation, docstrings, etc  
> Only 4 reflections allowed, stopping.  
