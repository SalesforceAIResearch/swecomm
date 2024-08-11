
# aider chat started at 2024-07-20 23:06:40

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp1liv15h7/.git with 4,407 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### [Bug]: Attribute Error combining matplotlib 3.7.1 and mplcursor on data selection  
#### ### Bug summary  
####   
#### If you combine mplcursor and matplotlib 3.7.1, you'll get an `AttributeError: 'NoneType' object has no attribute 'canvas'` after clicking a few data points. Henceforth, selecting a new data point will trigger the same traceback. Otherwise, it works fine.   
####   
#### ### Code for reproduction  
####   
#### ```python  
#### import numpy as np  
#### import matplotlib.pyplot as plt  
#### import mplcursors as mpl  
####   
#### x = np.arange(1, 11)      
#### y1 = x  
####   
#### plt.scatter(x,y1)  
####   
#### mpl.cursor()  
#### plt.show()  
#### ```  
####   
####   
#### ### Actual outcome  
####   
#### ```  
#### Traceback (most recent call last):  
####   File "C:\Users\MrAni\Python\miniconda3\lib\site-packages\matplotlib\cbook\__init__.py", line 304, in process  
####     func(*args, **kwargs)  
####   File "C:\Users\MrAni\Python\miniconda3\lib\site-packages\matplotlib\offsetbox.py", line 1550, in on_release  
####     if self._check_still_parented() and self.got_artist:  
####   File "C:\Users\MrAni\Python\miniconda3\lib\site-packages\matplotlib\offsetbox.py", line 1560, in _check_still_parented  
####     self.disconnect()  
####   File "C:\Users\MrAni\Python\miniconda3\lib\site-packages\matplotlib\offsetbox.py", line 1568, in disconnect  
####     self.canvas.mpl_disconnect(cid)  
####   File "C:\Users\MrAni\Python\miniconda3\lib\site-packages\matplotlib\offsetbox.py", line 1517, in <lambda>  
####     canvas = property(lambda self: self.ref_artist.figure.canvas)  
#### AttributeError: 'NoneType' object has no attribute 'canvas'  
#### ```  
####   
#### ### Expected outcome  
####   
#### No terminal output  
####   
#### ### Additional information  
####   
#### Using matplotlib 3.7.0 or lower works fine. Using a conda install or pip install doesn't affect the output.   
####   
#### ### Operating system  
####   
#### Windows 11 and Windwos 10   
####   
#### ### Matplotlib Version  
####   
#### 3.7.1  
####   
#### ### Matplotlib Backend  
####   
#### QtAgg  
####   
#### ### Python version  
####   
#### 3.9.16  
####   
#### ### Jupyter version  
####   
#### _No response_  
####   
#### ### Installation  
####   
#### conda  
> 34271 prompt tokens, 95 completion tokens, $0.172780 cost  

To address the `AttributeError: 'NoneType' object has no attribute 'canvas'` issue, we need to investigate and potentially modify the `offsetbox.py` file in the `matplotlib` library. This file is likely where the error is originating from, specifically in the `disconnect` method and the `canvas` property.

Please add the following file to the chat so I can propose the necessary changes:

- `lib/matplotlib/offsetbox.py`

> lib/matplotlib/offsetbox.py  
> Add these files to the chat? yes  
> 16629 prompt tokens, 208 completion tokens, $0.086265 cost  

To fix the `AttributeError: 'NoneType' object has no attribute 'canvas'`, we need to add a check to ensure that `self.ref_artist.figure` is not `None` before accessing `self.ref_artist.figure.canvas`. This will prevent the error when the figure is not available.

Here are the necessary changes:

lib/matplotlib/offsetbox.py
```python
<<<<<<< SEARCH
    canvas = property(lambda self: self.ref_artist.figure.canvas)
=======
    canvas = property(lambda self: self.ref_artist.figure.canvas if self.ref_artist.figure else None)
>>>>>>> REPLACE
```

lib/matplotlib/offsetbox.py
```python
<<<<<<< SEARCH
            self.canvas.mpl_disconnect(cid)
=======
            if self.canvas:
                self.canvas.mpl_disconnect(cid)
>>>>>>> REPLACE
```

lib/matplotlib/offsetbox.py
```python
<<<<<<< SEARCH
            self.canvas.mpl_disconnect(c1)
=======
            if self.canvas:
                self.canvas.mpl_disconnect(c1)
>>>>>>> REPLACE
```

> Applied edit to lib/matplotlib/offsetbox.py  
>   
> Test Script: conda run -n matplotlib__matplotlib__3.7 pytest --no-header -rA --tb=no -p no:cacheprovider lib/matplotlib/tests/test_offsetbox.py;  
> [matplotlib__matplotlib__3.7] [matplotlib__matplotlib-25442] Command: conda run -n matplotlib__matplotlib__3.7 pytest --no-header -rA --tb=no -p no:cacheprovider lib/matplotlib/tests/test_offsetbox.py   
> [matplotlib__matplotlib__3.7] [matplotlib__matplotlib-25442] Subprocess args: {"cwd": "/home/swe-bench/matplotlib__matplotlib", "check": false, "shell": false, "capture_output": false, "text": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [matplotlib__matplotlib__3.7] [matplotlib__matplotlib-25442] Std. Output:  
> ERROR conda.cli.main_run:execute(124): `conda run pytest --no-header -rA --tb=no -p no:cacheprovider lib/matplotlib/tests/test_offsetbox.py` failed. (See above for error)  
> ============================= test session starts ==============================  
> collected 0 items / 1 error  
>   
> =========================== short test summary info ============================  
> ERROR lib/matplotlib/tests/test_offsetbox.py - DeprecationWarning: pkg_resour...  
> !!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!  
> =============================== 1 error in 2.21s ===============================  
>   
>    
> [matplotlib__matplotlib__3.7] [matplotlib__matplotlib-25442] Return Code: 2   
>   
> >>>>> Some Tests Failed  
> [matplotlib__matplotlib__3.7] [matplotlib__matplotlib-25442] Test script run successful   
> Attempt to fix test errors? yes  
> 17255 prompt tokens, 90 completion tokens, $0.087625 cost  

It seems there was an error during the test collection phase. The error message indicates a `DeprecationWarning` related to `pkg_resources`.

To proceed, we need to ensure that the test script runs correctly. Let's address the `DeprecationWarning` and any other potential issues in the test file.

Please add the following file to the chat so I can propose the necessary changes:

- `lib/matplotlib/tests/test_offsetbox.py`

> lib/matplotlib/tests/test_offsetbox.py  
> Add these files to the chat? yes  
> 21965 prompt tokens, 4096 completion tokens, $0.171265 cost  

To address the `DeprecationWarning` related to `pkg_resources`, we need to ensure that the test file is not using deprecated or outdated imports. However, the provided test file does not seem to directly use `pkg_resources`.

Let's add a try-except block to handle potential deprecation warnings and ensure the test file runs correctly.

lib/matplotlib/tests/test_offsetbox.py
```python
<<<<<<< SEARCH
from collections import namedtuple
=======
import warnings
from collections import namedtuple
>>>>>>> REPLACE
```

lib/matplotlib/tests/test_offsetbox.py
```python
<<<<<<< SEARCH
@image_comparison(['offsetbox_clipping'], remove_text=True)
=======
with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)
    
    @image_comparison(['offsetbox_clipping'], remove_text=True)
>>>>>>> REPLACE
```

lib/matplotlib/tests/test_offsetbox.py
```python
<<<<<<< SEARCH
def test_offsetbox_clip_children():
=======
    def test_offsetbox_clip_children():
>>>>>>> REPLACE
```

lib/matplotlib/tests/test_offsetbox.py
```python
<<<<<<< SEARCH
def test_offsetbox_loc_codes():
=======
    def test_offsetbox_loc_codes():
>>>>>>> REPLACE
```

lib/matplotlib/tests/test_offsetbox.py
```python
<<<<<<< SEARCH
def test_expand_with_tight_layout():
=======
    def test_expand_with_tight_layout():
>>>>>>> REPLACE
```

lib/matplotlib/tests/test_offsetbox.py
```python
<<<<<<< SEARCH
@pytest.mark.parametrize('widths',
                         ([150], [150, 150, 150], [0.1], [0.1, 0.1]))
@pytest.mark.parametrize('total', (250, 100, 0, -1, None))
@pytest.mark.parametrize('sep', (250, 1, 0, -1))
@pytest.mark.parametrize('mode', ("expand", "fixed", "equal"))
def test_get_packed_offsets(widths, total, sep, mode):
    # Check a (rather arbitrary) set of parameters due to successive similar
    # issue tickets (at least #10476 and #10784) related to corner cases
    # triggered inside this function when calling higher-level functions
    # (e.g. `Axes.legend`).
    # These are just some additional smoke tests. The output is untested.
    _get_packed_offsets(widths, total, sep, mode=mode)
=======
    @pytest.mark.parametrize('widths',
                             ([150], [150, 150, 150], [0.1], [0.1, 0.1]))
    @pytest.mark.parametrize('total', (250, 100, 0, -1, None))
    @pytest.mark.parametrize('sep', (250, 1, 0, -1))
    @pytest.mark.parametrize('mode', ("expand", "fixed", "equal"))
    def test_get_packed_offsets(widths, total, sep, mode):
        # Check a (rather arbitrary) set of parameters due to successive similar
        # issue tickets (at least #10476 and #10784) related to corner cases
        # triggered inside this function when calling higher-level functions
        # (e.g. `Axes.legend`).
        # These are just some additional smoke tests. The output is untested.
        _get_packed_offsets(widths, total, sep, mode=mode)
>>>>>>> REPLACE
```

lib/matplotlib/tests/test_offsetbox.py
```python
<<<<<<< SEARCH
_Params = namedtuple('_params', 'wd_list, total, sep, expected')
=======
    _Params = namedtuple('_params', 'wd_list, total, sep, expected')
>>>>>>> REPLACE
```

lib/matplotlib/tests/test_offsetbox.py
```python
<<<<<<< SEARCH
@pytest.mark.parametrize('widths, total, sep, expected', [
    _Params(  # total=None
        [3, 1, 2], total=None, sep=1, expected=(8, [0, 4, 6])),
    _Params(  # total larger than required
        [3, 1, 2], total=10, sep=1, expected=(10, [0, 4, 6])),
    _Params(  # total smaller than required
        [3, 1, 2], total=5, sep=1, expected=(5, [0, 4, 6])),
])
def test_get_packed_offsets_fixed(widths, total, sep, expected):
    result = _get_packed_offsets(widths, total, sep, mode='fixed')
    assert result[0] == expected[0]
    assert_allclose(result[1], expected[1])
=======
    @pytest.mark.parametrize('widths, total, sep, expected', [
        _Params(  # total=None
            [3, 1, 2], total=None, sep=1, expected=(8, [0, 4, 6])),
        _Params(  # total larger than required
            [3, 1, 2], total=10, sep=1, expected=(10, [0, 4, 6])),
        _Params(  # total smaller than required
            [3, 1, 2], total=5, sep=1, expected=(5, [0, 4, 6])),
    ])
    def test_get_packed_offsets_fixed(widths, total, sep, expected):
        result = _get_packed_offsets(widths, total, sep, mode='fixed')
        assert result[0] == expected[0]
        assert_allclose(result[1], expected[1])
>>>>>>> REPLACE
```

lib/matplotlib/tests/test_offsetbox.py
```python
<<<<<<< SEARCH
@pytest.mark.parametrize('widths, total, sep, expected', [
    _Params(  # total=None (implicit 1)
        [.1, .1, .1], total=None, sep=None, expected=(1, [0, .45, .9])),
    _Params(  # total larger than sum of widths
        [3, 1, 2], total=10, sep=1, expected=(10, [0, 5, 8])),
    _Params(  # total smaller sum of widths: overlapping boxes
        [3, 1, 2], total=5, sep=1, expected=(5, [0, 2.5, 3])),
])
def test_get_packed_offsets_expand(widths, total, sep, expected):
    result = _get_packed_offsets(widths, total, sep, mode='expand')
    assert result[0] == expected[0]
    assert_allclose(result[1], expected[1])
=======
    @pytest.mark.parametrize('widths, total, sep, expected', [
        _Params(  # total=None (implicit 1)
            [.1, .1, .1], total=None, sep=None, expected=(1, [0, .45, .9])),
        _Params(  # total larger than sum of widths
            [3, 1, 2], total=10, sep=1, expected=(10, [0, 5, 8])),
        _Params(  # total smaller sum of widths: overlapping boxes
            [3, 1, 2], total=5, sep=1, expected=(5, [0, 2.5, 3])),
    ])
    def test_get_packed_offsets_expand(widths, total, sep, expected):
        result = _get_packed_offsets(widths, total, sep, mode='expand')
        assert result[0] == expected[0]
        assert_allclose(result[1], expected[1])
>>>>>>> REPLACE
```

lib/matplotlib/tests/test_offsetbox.py
```python
<<<<<<< SEARCH
@pytest.mark.parametrize('widths, total, sep, expected', [
    _Params(  # total larger than required
        [3, 2, 1], total=6, sep=None, expected=(6, [0, 2, 4])),
    _Params(  # total smaller sum of widths: overlapping boxes
        [3, 2, 1, .5], total=2, sep=None, expected=(2, [0, 0.5, 1, 1.5])),
    _Params(  # total larger than required
        [.5, 1, .2], total=None, sep=1, expected=(6, [0, 2, 4])),
    # the case total=None, sep=None is tested separately below
])
def test_get_packed_offsets_equal(widths, total, sep, expected):
    result = _get_packed_offsets(widths, total, sep, mode='equal')
    assert result[0] == expected[0]
    assert_allclose(result[1], expected[1])
=======
    @pytest.mark.parametrize('widths, total, sep, expected', [
        _Params(  # total larger than required
            [3, 2, 1], total=6, sep=None, expected=(6, [0, 2, 4])),
        _Params(  # total smaller sum of widths: overlapping boxes
            [3, 2, 1, .5], total=2, sep=None, expected=(2, [0, 0.5, 1, 1.5])),
        _Params(  # total larger than required
            [.5, 1, .2], total=None, sep=1, expected=(6, [0, 2, 4])),
        # the case total=None, sep=None is tested separately below
    ])
    def test_get_packed_offsets_equal(widths, total, sep, expected):
        result = _get_packed_offsets(widths, total, sep, mode='equal')
        assert result[0] == expected[0]
        assert_allclose(result[1], expected[1])
>>>>>>> REPLACE
```

lib/matplotlib/tests/test_offsetbox.py
```python
<<<<<<< SEARCH
def test_get_packed_offsets_equal_total_none_sep_none():
    with pytest.raises(ValueError):
        _get_packed_offsets([1, 1, 1], total=None, sep=None, mode='equal')
=======
    def test_get_packed_offsets_equal_total_none_sep_none():
        with pytest.raises(ValueError):
            _get_packed_offsets([1, 1, 1], total=None, sep=None, mode='equal')
>>>>>>> REPLACE
```

lib/matplotlib/tests/test_offsetbox.py
```python
<<<<<<< SEARCH
@pytest.mark.parametrize('child_type', ['draw', 'image', 'text'])
@pytest.mark.parametrize('boxcoords',
                         ['axes fraction', 'axes pixels', 'axes points',
                          'data'])
def test_picking(child_type, boxcoords):
    # These all take up approximately the same area.
    if child_type == 'draw':
        picking_child = DrawingArea(5, 5)
        picking_child.add_artist(mpatches.Rectangle((0, 0), 5, 5, linewidth=0))
    elif child_type == 'image':
        im = np.ones((5, 5))
        im[2, 2] = 0
        picking_child = OffsetImage(im)
    elif child_type == 'text':
        picking_child = TextArea('\N{Black Square}', textprops={'fontsize': 5})
    else:
        assert False, f'Unknown picking child type {child_type}'

    fig, ax = plt.subplots()
    ab = AnnotationBbox(picking_child, (0.5, 0.5), boxcoords=boxcoords)
    ab.set_picker(True)
    ax.add_artist(ab)

    calls = []
    fig.canvas.mpl_connect('pick_event', lambda event: calls.append(event))

    # Annotation should be picked by an event occurring at its center.
    if boxcoords == 'axes points':
        x, y = ax.transAxes.transform_point((0, 0))
        x += 0.5 * fig.dpi / 72
        y += 0.5 * fig.dpi / 72
    elif boxcoords == 'axes pixels':
        x, y = ax.transAxes.transform_point((0, 0))
        x += 0.5
        y += 0.5
    else:
        x, y = ax.transAxes.transform_point((0.5, 0.5))
    fig.canvas.draw()
    calls.clear()
    MouseEvent(
        "button_press_event", fig.canvas, x, y, MouseButton.LEFT)._process()
    assert len(calls) == 1 and calls[0].artist == ab

    # Annotation should *not* be picked by an event at its original center
    # point when the limits have changed enough to hide the *xy* point.
    ax.set_xlim(-1, 0)
    ax.set_ylim(-1, 0)
    fig.canvas.draw()
    calls.clear()
    MouseEvent(
        "button_press_event", fig.canvas, x, y, MouseButton.LEFT)._process()
    assert len(calls) == 0
=======
    @pytest.mark.parametrize('child_type', ['draw', 'image', 'text'])
    @pytest.mark.parametrize('boxcoords',
                             ['axes fraction', 'axes pixels', 'axes points',
                              'data'])
    def test_picking(child_type, boxcoords):
        # These all take up approximately the same area.
        if child_type == 'draw':
            picking_child = DrawingArea(5, 5)
            picking_child.add_artist(mpatches.Rectangle((0, 0), 5, 5, linewidth=0))
        elif child_type == 'image':
            im = np.ones((5, 5))
            im[2, 2] = 0
            picking_child = OffsetImage(im)
        elif child_type == 'text':
            picking_child = TextArea('\N{Black Square}', textprops={'fontsize': 5})
        else:
            assert False, f'Unknown picking child type {child_type}'

        fig, ax = plt.subplots()
        ab = AnnotationBbox(picking_child, (0.5, 0.5), boxcoords=boxcoords)
        ab.set_picker(True)
        ax.add_artist(ab)

        calls = []
        fig.canvas.mpl_connect('pick_event', lambda event: calls.append(event))

        # Annotation should be picked by an event occurring at its center.
        if boxcoords == 'axes points':
            x, y = ax.transAxes.transform_point((0, 0))
            x += 0.5 * fig.dpi / 72
            y += 0.5 * fig.dpi / 72
        elif boxcoords == 'axes pixels':
            x, y = ax.transAxes.transform_point((0, 0))
            x += 0.5
            y += 0.5
        else:
            x, y = ax.transAxes.transform_point((0.5, 0.5))
        fig.canvas.draw()
        calls.clear()
        MouseEvent(
            "button_press_event", fig.canvas, x, y, MouseButton.LEFT)._process()
        assert len(calls) == 1 and calls[0].artist == ab

        # Annotation should *not* be picked by an event at its original center
        # point when the limits have changed enough to hide the *xy* point.
        ax.set_xlim(-1, 0)
        ax.set_ylim(-1, 0)
        fig.canvas.draw()
        calls.clear()
        MouseEvent(
            "button_press_event", fig.canvas, x, y, MouseButton.LEFT)._process()
        assert len(calls) == 0
>>>>>>> REPLACE
```

lib/matplotlib/tests/test_offsetbox.py
```python
<<<<<<< SEARCH
@image_comparison(['anchoredtext_align.png'], remove_text=True, style='mpl20')
def test_anchoredtext_horizontal_alignment():
    fig, ax = plt.subplots()

    text0 = AnchoredText("test\ntest long text", loc="center left",
                         pad=0.2, prop={"ha": "left"})
    ax.add_artist(text0)
    text1 = AnchoredText("test\ntest long text", loc="center",
                         pad=0.2, prop={"ha": "center"})
    ax.add_artist(text1)
    text2 = AnchoredText("test\ntest long text", loc="center right",
                         pad=0.2, prop={"ha": "right"})
    ax.add_artist(text2)
=======
    @image_comparison(['anchoredtext_align.png'], remove_text=True, style='mpl20')
    def test_anchoredtext_horizontal_alignment():
        fig, ax = plt.subplots()

        text0 = AnchoredText("test\ntest long text", loc="center left",
                             pad=0.2, prop={"ha": "left"})
        ax.add_artist(text0)
        text1 = AnchoredText("test\ntest long text", loc="center",
                             pad=0.2, prop={"ha": "center"})
        ax.add_artist(text1)
        text2 = AnchoredText("test\ntest long text", loc="center right",
                             pad=0.2, prop={"ha": "right"})
        ax.add_artist(text2)
>>>>>>> REPLACE
```

lib/matplotlib/tests/test_offsetbox.py
```python
<<<<<<< SEARCH
def test_annotationbbox_extents():
    plt.rcParams.update(plt.rcParamsDefault)
    fig, ax = plt.subplots(figsize=(4, 3), dpi=100)

    ax.axis([0, 1, 0, 1])

    an1 = ax.annotate("Annotation", xy=(.9, .9), xytext=(1.1, 1.1),
                      arrowprops=dict(arrowstyle="->"), clip_on=False,
                      va="baseline", ha="left")

    da = DrawingArea(20, 20, 0, 0, clip=True)
    p = mpatches.Circle((-10, 30), 32)
    da.add_artist(p)

    ab3 = AnnotationBbox(da, [.5, .5], xybox=(-0.2, 0.5), xycoords='data',
                         boxcoords="axes fraction", box_alignment=(0., .5),
                         arrowprops=dict(arrowstyle="->"))
    ax.add_artist(ab3)

    im = OffsetImage(np.random.rand(10, 10), zoom=3)
    im.image.axes = ax
    ab6 = AnnotationBbox(im, (0.5, -.3), xybox=(0, 75),
                         xycoords='axes fraction',
                         boxcoords="offset points", pad=0.3,
                         arrowprops=dict(arrowstyle="->"))
    ax.add_artist(ab6)

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()

    # Test Annotation
    bb1w = an1.get_window_extent(renderer)
    bb1e = an1.get_tightbbox(renderer)

    target1 = [332.9, 242.8, 467.0, 298.9]
    assert_allclose(bb1w.extents, target1, atol=2)
    assert_allclose(bb1e.extents, target1, atol

> The LLM did not conform to the edit format.  
> For more info see: https://aider.chat/docs/faq.html#aider-isnt-editing-my-files  
> To address the `DeprecationWarning` related to `pkg_resources`, we need to ensure that the test file is not using deprecated or outdated imports. However, the provided test file does not seem to directly use `pkg_resources`.  
>   
> Let's add a try-except block to handle potential deprecation warnings and ensure the test file runs correctly.  
>   
> lib/matplotlib/tests/test_offsetbox.py  
> ```python  
> <<<<<<< SEARCH  
> from collections import namedtuple  
> =======  
> import warnings  
> from collections import namedtuple  
> >>>>>>> REPLACE  
> ```  
>   
> lib/matplotlib/tests/test_offsetbox.py  
> ```python  
> <<<<<<< SEARCH  
> @image_comparison(['offsetbox_clipping'], remove_text=True)  
> =======  
> with warnings.catch_warnings():  
>     warnings.simplefilter("ignore", DeprecationWarning)  
>       
>     @image_comparison(['offsetbox_clipping'], remove_text=True)  
> >>>>>>> REPLACE  
> ```  
>   
> lib/matplotlib/tests/test_offsetbox.py  
> ```python  
> <<<<<<< SEARCH  
> def test_offsetbox_clip_children():  
> =======  
>     def test_offsetbox_clip_children():  
> >>>>>>> REPLACE  
> ```  
>   
> lib/matplotlib/tests/test_offsetbox.py  
> ```python  
> <<<<<<< SEARCH  
> def test_offsetbox_loc_codes():  
> =======  
>     def test_offsetbox_loc_codes():  
> >>>>>>> REPLACE  
> ```  
>   
> lib/matplotlib/tests/test_offsetbox.py  
> ```python  
> <<<<<<< SEARCH  
> def test_expand_with_tight_layout():  
> =======  
>     def test_expand_with_tight_layout():  
> >>>>>>> REPLACE  
> ```  
>   
> lib/matplotlib/tests/test_offsetbox.py  
> ```python  
> <<<<<<< SEARCH  
> @pytest.mark.parametrize('widths',  
>                          ([150], [150, 150, 150], [0.1], [0.1, 0.1]))  
> @pytest.mark.parametrize('total', (250, 100, 0, -1, None))  
> @pytest.mark.parametrize('sep', (250, 1, 0, -1))  
> @pytest.mark.parametrize('mode', ("expand", "fixed", "equal"))  
> def test_get_packed_offsets(widths, total, sep, mode):  
>     # Check a (rather arbitrary) set of parameters due to successive similar  
>     # issue tickets (at least #10476 and #10784) related to corner cases  
>     # triggered inside this function when calling higher-level functions  
>     # (e.g. `Axes.legend`).  
>     # These are just some additional smoke tests. The output is untested.  
>     _get_packed_offsets(widths, total, sep, mode=mode)  
> =======  
>     @pytest.mark.parametrize('widths',  
>                              ([150], [150, 150, 150], [0.1], [0.1, 0.1]))  
>     @pytest.mark.parametrize('total', (250, 100, 0, -1, None))  
>     @pytest.mark.parametrize('sep', (250, 1, 0, -1))  
>     @pytest.mark.parametrize('mode', ("expand", "fixed", "equal"))  
>     def test_get_packed_offsets(widths, total, sep, mode):  
>         # Check a (rather arbitrary) set of parameters due to successive similar  
>         # issue tickets (at least #10476 and #10784) related to corner cases  
>         # triggered inside this function when calling higher-level functions  
>         # (e.g. `Axes.legend`).  
>         # These are just some additional smoke tests. The output is untested.  
>         _get_packed_offsets(widths, total, sep, mode=mode)  
> >>>>>>> REPLACE  
> ```  
>   
> lib/matplotlib/tests/test_offsetbox.py  
> ```python  
> <<<<<<< SEARCH  
> _Params = namedtuple('_params', 'wd_list, total, sep, expected')  
> =======  
>     _Params = namedtuple('_params', 'wd_list, total, sep, expected')  
> >>>>>>> REPLACE  
> ```  
>   
> lib/matplotlib/tests/test_offsetbox.py  
> ```python  
> <<<<<<< SEARCH  
> @pytest.mark.parametrize('widths, total, sep, expected', [  
>     _Params(  # total=None  
>         [3, 1, 2], total=None, sep=1, expected=(8, [0, 4, 6])),  
>     _Params(  # total larger than required  
>         [3, 1, 2], total=10, sep=1, expected=(10, [0, 4, 6])),  
>     _Params(  # total smaller than required  
>         [3, 1, 2], total=5, sep=1, expected=(5, [0, 4, 6])),  
> ])  
> def test_get_packed_offsets_fixed(widths, total, sep, expected):  
>     result = _get_packed_offsets(widths, total, sep, mode='fixed')  
>     assert result[0] == expected[0]  
>     assert_allclose(result[1], expected[1])  
> =======  
>     @pytest.mark.parametrize('widths, total, sep, expected', [  
>         _Params(  # total=None  
>             [3, 1, 2], total=None, sep=1, expected=(8, [0, 4, 6])),  
>         _Params(  # total larger than required  
>             [3, 1, 2], total=10, sep=1, expected=(10, [0, 4, 6])),  
>         _Params(  # total smaller than required  
>             [3, 1, 2], total=5, sep=1, expected=(5, [0, 4, 6])),  
>     ])  
>     def test_get_packed_offsets_fixed(widths, total, sep, expected):  
>         result = _get_packed_offsets(widths, total, sep, mode='fixed')  
>         assert result[0] == expected[0]  
>         assert_allclose(result[1], expected[1])  
> >>>>>>> REPLACE  
> ```  
>   
> lib/matplotlib/tests/test_offsetbox.py  
> ```python  
> <<<<<<< SEARCH  
> @pytest.mark.parametrize('widths, total, sep, expected', [  
>     _Params(  # total=None (implicit 1)  
>         [.1, .1, .1], total=None, sep=None, expected=(1, [0, .45, .9])),  
>     _Params(  # total larger than sum of widths  
>         [3, 1, 2], total=10, sep=1, expected=(10, [0, 5, 8])),  
>     _Params(  # total smaller sum of widths: overlapping boxes  
>         [3, 1, 2], total=5, sep=1, expected=(5, [0, 2.5, 3])),  
> ])  
> def test_get_packed_offsets_expand(widths, total, sep, expected):  
>     result = _get_packed_offsets(widths, total, sep, mode='expand')  
>     assert result[0] == expected[0]  
>     assert_allclose(result[1], expected[1])  
> =======  
>     @pytest.mark.parametrize('widths, total, sep, expected', [  
>         _Params(  # total=None (implicit 1)  
>             [.1, .1, .1], total=None, sep=None, expected=(1, [0, .45, .9])),  
>         _Params(  # total larger than sum of widths  
>             [3, 1, 2], total=10, sep=1, expected=(10, [0, 5, 8])),  
>         _Params(  # total smaller sum of widths: overlapping boxes  
>             [3, 1, 2], total=5, sep=1, expected=(5, [0, 2.5, 3])),  
>     ])  
>     def test_get_packed_offsets_expand(widths, total, sep, expected):  
>         result = _get_packed_offsets(widths, total, sep, mode='expand')  
>         assert result[0] == expected[0]  
>         assert_allclose(result[1], expected[1])  
> >>>>>>> REPLACE  
> ```  
>   
> lib/matplotlib/tests/test_offsetbox.py  
> ```python  
> <<<<<<< SEARCH  
> @pytest.mark.parametrize('widths, total, sep, expected', [  
>     _Params(  # total larger than required  
>         [3, 2, 1], total=6, sep=None, expected=(6, [0, 2, 4])),  
>     _Params(  # total smaller sum of widths: overlapping boxes  
>         [3, 2, 1, .5], total=2, sep=None, expected=(2, [0, 0.5, 1, 1.5])),  
>     _Params(  # total larger than required  
>         [.5, 1, .2], total=None, sep=1, expected=(6, [0, 2, 4])),  
>     # the case total=None, sep=None is tested separately below  
> ])  
> def test_get_packed_offsets_equal(widths, total, sep, expected):  
>     result = _get_packed_offsets(widths, total, sep, mode='equal')  
>     assert result[0] == expected[0]  
>     assert_allclose(result[1], expected[1])  
> =======  
>     @pytest.mark.parametrize('widths, total, sep, expected', [  
>         _Params(  # total larger than required  
>             [3, 2, 1], total=6, sep=None, expected=(6, [0, 2, 4])),  
>         _Params(  # total smaller sum of widths: overlapping boxes  
>             [3, 2, 1, .5], total=2, sep=None, expected=(2, [0, 0.5, 1, 1.5])),  
>         _Params(  # total larger than required  
>             [.5, 1, .2], total=None, sep=1, expected=(6, [0, 2, 4])),  
>         # the case total=None, sep=None is tested separately below  
>     ])  
>     def test_get_packed_offsets_equal(widths, total, sep, expected):  
>         result = _get_packed_offsets(widths, total, sep, mode='equal')  
>         assert result[0] == expected[0]  
>         assert_allclose(result[1], expected[1])  
> >>>>>>> REPLACE  
> ```  
>   
> lib/matplotlib/tests/test_offsetbox.py  
> ```python  
> <<<<<<< SEARCH  
> def test_get_packed_offsets_equal_total_none_sep_none():  
>     with pytest.raises(ValueError):  
>         _get_packed_offsets([1, 1, 1], total=None, sep=None, mode='equal')  
> =======  
>     def test_get_packed_offsets_equal_total_none_sep_none():  
>         with pytest.raises(ValueError):  
>             _get_packed_offsets([1, 1, 1], total=None, sep=None, mode='equal')  
> >>>>>>> REPLACE  
> ```  
>   
> lib/matplotlib/tests/test_offsetbox.py  
> ```python  
> <<<<<<< SEARCH  
> @pytest.mark.parametrize('child_type', ['draw', 'image', 'text'])  
> @pytest.mark.parametrize('boxcoords',  
>                          ['axes fraction', 'axes pixels', 'axes points',  
>                           'data'])  
> def test_picking(child_type, boxcoords):  
>     # These all take up approximately the same area.  
>     if child_type == 'draw':  
>         picking_child = DrawingArea(5, 5)  
>         picking_child.add_artist(mpatches.Rectangle((0, 0), 5, 5, linewidth=0))  
>     elif child_type == 'image':  
>         im = np.ones((5, 5))  
>         im[2, 2] = 0  
>         picking_child = OffsetImage(im)  
>     elif child_type == 'text':  
>         picking_child = TextArea('\N{Black Square}', textprops={'fontsize': 5})  
>     else:  
>         assert False, f'Unknown picking child type {child_type}'  
>   
>     fig, ax = plt.subplots()  
>     ab = AnnotationBbox(picking_child, (0.5, 0.5), boxcoords=boxcoords)  
>     ab.set_picker(True)  
>     ax.add_artist(ab)  
>   
>     calls = []  
>     fig.canvas.mpl_connect('pick_event', lambda event: calls.append(event))  
>   
>     # Annotation should be picked by an event occurring at its center.  
>     if boxcoords == 'axes points':  
>         x, y = ax.transAxes.transform_point((0, 0))  
>         x += 0.5 * fig.dpi / 72  
>         y += 0.5 * fig.dpi / 72  
>     elif boxcoords == 'axes pixels':  
>         x, y = ax.transAxes.transform_point((0, 0))  
>         x += 0.5  
>         y += 0.5  
>     else:  
>         x, y = ax.transAxes.transform_point((0.5, 0.5))  
>     fig.canvas.draw()  
>     calls.clear()  
>     MouseEvent(  
>         "button_press_event", fig.canvas, x, y, MouseButton.LEFT)._process()  
>     assert len(calls) == 1 and calls[0].artist == ab  
>   
>     # Annotation should *not* be picked by an event at its original center  
>     # point when the limits have changed enough to hide the *xy* point.  
>     ax.set_xlim(-1, 0)  
>     ax.set_ylim(-1, 0)  
>     fig.canvas.draw()  
>     calls.clear()  
>     MouseEvent(  
>         "button_press_event", fig.canvas, x, y, MouseButton.LEFT)._process()  
>     assert len(calls) == 0  
> =======  
>     @pytest.mark.parametrize('child_type', ['draw', 'image', 'text'])  
>     @pytest.mark.parametrize('boxcoords',  
>                              ['axes fraction', 'axes pixels', 'axes points',  
>                               'data'])  
>     def test_picking(child_type, boxcoords):  
>         # These all take up approximately the same area.  
>         if child_type == 'draw':  
>             picking_child = DrawingArea(5, 5)  
>             picking_child.add_artist(mpatches.Rectangle((0, 0), 5, 5, linewidth=0))  
>         elif child_type == 'image':  
>             im = np.ones((5, 5))  
>             im[2, 2] = 0  
>             picking_child = OffsetImage(im)  
>         elif child_type == 'text':  
>             picking_child = TextArea('\N{Black Square}', textprops={'fontsize': 5})  
>         else:  
>             assert False, f'Unknown picking child type {child_type}'  
>   
>         fig, ax = plt.subplots()  
>         ab = AnnotationBbox(picking_child, (0.5, 0.5), boxcoords=boxcoords)  
>         ab.set_picker(True)  
>         ax.add_artist(ab)  
>   
>         calls = []  
>         fig.canvas.mpl_connect('pick_event', lambda event: calls.append(event))  
>   
>         # Annotation should be picked by an event occurring at its center.  
>         if boxcoords == 'axes points':  
>             x, y = ax.transAxes.transform_point((0, 0))  
>             x += 0.5 * fig.dpi / 72  
>             y += 0.5 * fig.dpi / 72  
>         elif boxcoords == 'axes pixels':  
>             x, y = ax.transAxes.transform_point((0, 0))  
>             x += 0.5  
>             y += 0.5  
>         else:  
>             x, y = ax.transAxes.transform_point((0.5, 0.5))  
>         fig.canvas.draw()  
>         calls.clear()  
>         MouseEvent(  
>             "button_press_event", fig.canvas, x, y, MouseButton.LEFT)._process()  
>         assert len(calls) == 1 and calls[0].artist == ab  
>   
>         # Annotation should *not* be picked by an event at its original center  
>         # point when the limits have changed enough to hide the *xy* point.  
>         ax.set_xlim(-1, 0)  
>         ax.set_ylim(-1, 0)  
>         fig.canvas.draw()  
>         calls.clear()  
>         MouseEvent(  
>             "button_press_event", fig.canvas, x, y, MouseButton.LEFT)._process()  
>         assert len(calls) == 0  
> >>>>>>> REPLACE  
> ```  
>   
> lib/matplotlib/tests/test_offsetbox.py  
> ```python  
> <<<<<<< SEARCH  
> @image_comparison(['anchoredtext_align.png'], remove_text=True, style='mpl20')  
> def test_anchoredtext_horizontal_alignment():  
>     fig, ax = plt.subplots()  
>   
>     text0 = AnchoredText("test\ntest long text", loc="center left",  
>                          pad=0.2, prop={"ha": "left"})  
>     ax.add_artist(text0)  
>     text1 = AnchoredText("test\ntest long text", loc="center",  
>                          pad=0.2, prop={"ha": "center"})  
>     ax.add_artist(text1)  
>     text2 = AnchoredText("test\ntest long text", loc="center right",  
>                          pad=0.2, prop={"ha": "right"})  
>     ax.add_artist(text2)  
> =======  
>     @image_comparison(['anchoredtext_align.png'], remove_text=True, style='mpl20')  
>     def test_anchoredtext_horizontal_alignment():  
>         fig, ax = plt.subplots()  
>   
>         text0 = AnchoredText("test\ntest long text", loc="center left",  
>                              pad=0.2, prop={"ha": "left"})  
>         ax.add_artist(text0)  
>         text1 = AnchoredText("test\ntest long text", loc="center",  
>                              pad=0.2, prop={"ha": "center"})  
>         ax.add_artist(text1)  
>         text2 = AnchoredText("test\ntest long text", loc="center right",  
>                              pad=0.2, prop={"ha": "right"})  
>         ax.add_artist(text2)  
> >>>>>>> REPLACE  
> ```  
>   
> lib/matplotlib/tests/test_offsetbox.py  
> ```python  
> <<<<<<< SEARCH  
> def test_annotationbbox_extents():  
>     plt.rcParams.update(plt.rcParamsDefault)  
>     fig, ax = plt.subplots(figsize=(4, 3), dpi=100)  
>   
>     ax.axis([0, 1, 0, 1])  
>   
>     an1 = ax.annotate("Annotation", xy=(.9, .9), xytext=(1.1, 1.1),  
>                       arrowprops=dict(arrowstyle="->"), clip_on=False,  
>                       va="baseline", ha="left")  
>   
>     da = DrawingArea(20, 20, 0, 0, clip=True)  
>     p = mpatches.Circle((-10, 30), 32)  
>     da.add_artist(p)  
>   
>     ab3 = AnnotationBbox(da, [.5, .5], xybox=(-0.2, 0.5), xycoords='data',  
>                          boxcoords="axes fraction", box_alignment=(0., .5),  
>                          arrowprops=dict(arrowstyle="->"))  
>     ax.add_artist(ab3)  
>   
>     im = OffsetImage(np.random.rand(10, 10), zoom=3)  
>     im.image.axes = ax  
>     ab6 = AnnotationBbox(im, (0.5, -.3), xybox=(0, 75),  
>                          xycoords='axes fraction',  
>                          boxcoords="offset points", pad=0.3,  
>                          arrowprops=dict(arrowstyle="->"))  
>     ax.add_artist(ab6)  
>   
>     fig.canvas.draw()  
>     renderer = fig.canvas.get_renderer()  
>   
>     # Test Annotation  
>     bb1w = an1.get_window_extent(renderer)  
>     bb1e = an1.get_tightbbox(renderer)  
>   
>     target1 = [332.9, 242.8, 467.0, 298.9]  
>     assert_allclose(bb1w.extents, target1, atol=2)  
>     assert_allclose(bb1e.extents, target1, atol  
>   
> ^^^ Incomplete SEARCH/REPLACE block.  
> 30183 prompt tokens, 4096 completion tokens, $0.212355 cost  

Let's correct the previous attempt and ensure the test file runs correctly by adding a try-except block to handle potential deprecation warnings.

lib/matplotlib/tests/test_offsetbox.py
```python
from collections import namedtuple
import io

import numpy as np
from numpy.testing import assert_allclose
import pytest

from matplotlib.testing.decorators import check_figures_equal, image_comparison
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.backend_bases import MouseButton, MouseEvent

from matplotlib.offsetbox import (
    AnchoredOffsetbox, AnnotationBbox, AnchoredText, DrawingArea, HPacker,
    OffsetBox, OffsetImage, PaddedBox, TextArea, VPacker, _get_packed_offsets)


@image_comparison(['offsetbox_clipping'], remove_text=True)
def test_offsetbox_clipping():
    # - create a plot
    # - put an AnchoredOffsetbox with a child DrawingArea
    #   at the center of the axes
    # - give the DrawingArea a gray background
    # - put a black line across the bounds of the DrawingArea
    # - see that the black line is clipped to the edges of
    #   the DrawingArea.
    fig, ax = plt.subplots()
    size = 100
    da = DrawingArea(size, size, clip=True)
    assert da.clip_children
    bg = mpatches.Rectangle((0, 0), size, size,
                            facecolor='#CCCCCC',
                            edgecolor='None',
                            linewidth=0)
    line = mlines.Line2D([-size*.5, size*1.5], [size/2, size/2],
                         color='black',
                         linewidth=10)
    anchored_box = AnchoredOffsetbox(
        loc='center',
        child=da,
        pad=0.,
        frameon=False,
        bbox_to_anchor=(.5, .5),
        bbox_transform=ax.transAxes,
        borderpad=0.)

    da.add_artist(bg)
    da.add_artist(line)
    ax.add_artist(anchored_box)
    ax.set_xlim((0, 1))
    ax.set_ylim((0, 1))


def test_offsetbox_clip_children():
    # - create a plot
    # - put an AnchoredOffsetbox with a child DrawingArea
    #   at the center of the axes
    # - give the DrawingArea a gray background
    # - put a black line across the bounds of the DrawingArea
    # - see that the black line is clipped to the edges of
    #   the DrawingArea.
    fig, ax = plt.subplots()
    size = 100
    da = DrawingArea(size, size, clip=True)
    bg = mpatches.Rectangle((0, 0), size, size,
                            facecolor='#CCCCCC',
                            edgecolor='None',
                            linewidth=0)
    line = mlines.Line2D([-size*.5, size*1.5], [size/2, size/2],
                         color='black',
                         linewidth=10)
    anchored_box = AnchoredOffsetbox(
        loc='center',
        child=da,
        pad=0.,
        frameon=False,
        bbox_to_anchor=(.5, .5),
        bbox_transform=ax.transAxes,
        borderpad=0.)

    da.add_artist(bg)
    da.add_artist(line)
    ax.add_artist(anchored_box)

    fig.canvas.draw()
    assert not fig.stale
    da.clip_children = True
    assert fig.stale


def test_offsetbox_loc_codes():
    # Check that valid string location codes all work with an AnchoredOffsetbox
    codes = {'upper right': 1,
             'upper left': 2,
             'lower left': 3,
             'lower right': 4,
             'right': 5,
             'center left': 6,
             'center right': 7,
             'lower center': 8,
             'upper center': 9,
             'center': 10,
             }
    fig, ax = plt.subplots()
    da = DrawingArea(100, 100)
    for code in codes:
        anchored_box = AnchoredOffsetbox(loc=code, child=da)
        ax.add_artist(anchored_box)
    fig.canvas.draw()


def test_expand_with_tight_layout():
    # Check issue reported in #10476, and updated due to #10784
    fig, ax = plt.subplots()

    d1 = [1, 2]
    d2 = [2, 1]
    ax.plot(d1, label='series 1')
    ax.plot(d2, label='series 2')
    ax.legend(ncols=2, mode='expand')

    fig.tight_layout()  # where the crash used to happen


@pytest.mark.parametrize('widths',
                         ([150], [150, 150, 150], [0.1], [0.1, 0.1]))
@pytest.mark.parametrize('total', (250, 100, 0, -1, None))
@pytest.mark.parametrize('sep', (250, 1, 0, -1))
@pytest.mark.parametrize('mode', ("expand", "fixed", "equal"))
def test_get_packed_offsets(widths, total, sep, mode):
    # Check a (rather arbitrary) set of parameters due to successive similar
    # issue tickets (at least #10476 and #10784) related to corner cases
    # triggered inside this function when calling higher-level functions
    # (e.g. `Axes.legend`).
    # These are just some additional smoke tests. The output is untested.
    _get_packed_offsets(widths, total, sep, mode=mode)


_Params = namedtuple('_params', 'wd_list, total, sep, expected')


@pytest.mark.parametrize('widths, total, sep, expected', [
    _Params(  # total=None
        [3, 1, 2], total=None, sep=1, expected=(8, [0, 4, 6])),
    _Params(  # total larger than required
        [3, 1, 2], total=10, sep=1, expected=(10, [0, 4, 6])),
    _Params(  # total smaller than required
        [3, 1, 2], total=5, sep=1, expected=(5, [0, 4, 6])),
])
def test_get_packed_offsets_fixed(widths, total, sep, expected):
    result = _get_packed_offsets(widths, total, sep, mode='fixed')
    assert result[0] == expected[0]
    assert_allclose(result[1], expected[1])


@pytest.mark.parametrize('widths, total, sep, expected', [
    _Params(  # total=None (implicit 1)
        [.1, .1, .1], total=None, sep=None, expected=(1, [0, .45, .9])),
    _Params(  # total larger than sum of widths
        [3, 1, 2], total=10, sep=1, expected=(10, [0, 5, 8])),
    _Params(  # total smaller sum of widths: overlapping boxes
        [3, 1, 2], total=5, sep=1, expected=(5, [0, 2.5, 3])),
])
def test_get_packed_offsets_expand(widths, total, sep, expected):
    result = _get_packed_offsets(widths, total, sep, mode='expand')
    assert result[0] == expected[0]
    assert_allclose(result[1], expected[1])


@pytest.mark.parametrize('widths, total, sep, expected', [
    _Params(  # total larger than required
        [3, 2, 1], total=6, sep=None, expected=(6, [0, 2, 4])),
    _Params(  # total smaller sum of widths: overlapping boxes
        [3, 2, 1, .5], total=2, sep=None, expected=(2, [0, 0.5, 1, 1.5])),
    _Params(  # total larger than required
        [.5, 1, .2], total=None, sep=1, expected=(6, [0, 2, 4])),
    # the case total=None, sep=None is tested separately below
])
def test_get_packed_offsets_equal(widths, total, sep, expected):
    result = _get_packed_offsets(widths, total, sep, mode='equal')
    assert result[0] == expected[0]
    assert_allclose(result[1], expected[1])


def test_get_packed_offsets_equal_total_none_sep_none():
    with pytest.raises(ValueError):
        _get_packed_offsets([1, 1, 1], total=None, sep=None, mode='equal')


@pytest.mark.parametrize('child_type', ['draw', 'image', 'text'])
@pytest.mark.parametrize('boxcoords',
                         ['axes fraction', 'axes pixels', 'axes points',
                          'data'])
def test_picking(child_type, boxcoords):
    # These all take up approximately the same area.
    if child_type == 'draw':
        picking_child = DrawingArea(5, 5)
        picking_child.add_artist(mpatches.Rectangle((0, 0), 5, 5, linewidth=0))
    elif child_type == 'image':
        im = np.ones((5, 5))
        im[2, 2] = 0
        picking_child = OffsetImage(im)
    elif child_type == 'text':
        picking_child = TextArea('\N{Black Square}', textprops={'fontsize': 5})
    else:
        assert False, f'Unknown picking child type {child_type}'

    fig, ax = plt.subplots()
    ab = AnnotationBbox(picking_child, (0.5, 0.5), boxcoords=boxcoords)
    ab.set_picker(True)
    ax.add_artist(ab)

    calls = []
    fig.canvas.mpl_connect('pick_event', lambda event: calls.append(event))

    # Annotation should be picked by an event occurring at its center.
    if boxcoords == 'axes points':
        x, y = ax.transAxes.transform_point((0, 0))
        x += 0.5 * fig.dpi / 72
        y += 0.5 * fig.dpi / 72
    elif boxcoords == 'axes pixels':
        x, y = ax.transAxes.transform_point((0, 0))
        x += 0.5
        y += 0.5
    else:
        x, y = ax.transAxes.transform_point((0.5, 0.5))
    fig.canvas.draw()
    calls.clear()
    MouseEvent(
        "button_press_event", fig.canvas, x, y, MouseButton.LEFT)._process()
    assert len(calls) == 1 and calls[0].artist == ab

    # Annotation should *not* be picked by an event at its original center
    # point when the limits have changed enough to hide the *xy* point.
    ax.set_xlim(-1, 0)
    ax.set_ylim(-1, 0)
    fig.canvas.draw()
    calls.clear()
    MouseEvent(
        "button_press_event", fig.canvas, x, y, MouseButton.LEFT)._process()
    assert len(calls) == 0


@image_comparison(['anchoredtext_align.png'], remove_text=True, style='mpl20')
def test_anchoredtext_horizontal_alignment():
    fig, ax = plt.subplots()

    text0 = AnchoredText("test\ntest long text", loc="center left",
                         pad=0.2, prop={"ha": "left"})
    ax.add_artist(text0)
    text1 = AnchoredText("test\ntest long text", loc="center",
                         pad=0.2, prop={"ha": "center"})
    ax.add_artist(text1)
    text2 = AnchoredText("test\ntest long text", loc="center right",
                         pad=0.2, prop={"ha": "right"})
    ax.add_artist(text2)


def test_annotationbbox_extents():
    plt.rcParams.update(plt.rcParamsDefault)
    fig, ax = plt.subplots(figsize=(4, 3), dpi=100)

    ax.axis([0, 1, 0, 1])

    an1 = ax.annotate("Annotation", xy=(.9, .9), xytext=(1.1, 1.1),
                      arrowprops=dict(arrowstyle="->"), clip_on=False,
                      va="baseline", ha="left")

    da = DrawingArea(20, 20, 0, 0, clip=True)
    p = mpatches.Circle((-10, 30), 32)
    da.add_artist(p)

    ab3 = AnnotationBbox(da, [.5, .5], xybox=(-0.2, 0.5), xycoords='data',
                         boxcoords="axes fraction", box_alignment=(0., .5),
                         arrowprops=dict(arrowstyle="->"))
    ax.add_artist(ab3)

    im = OffsetImage(np.random.rand(10, 10), zoom=3)
    im.image.axes = ax
    ab6 = AnnotationBbox(im, (0.5, -.3), xybox=(0, 75),
                         xycoords='axes fraction',
                         boxcoords="offset points", pad=0.3,
                         arrowprops=dict(arrowstyle="->"))
    ax.add_artist(ab6)

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()

    # Test Annotation
    bb1w = an1.get_window_extent(renderer)
    bb1e = an1.get_tightbbox(renderer)

    target1 = [332.9, 242.8, 467.0, 298.9]
    assert_allclose(bb1w.extents, target1, atol=2)
    assert_allclose(bb1e.extents, target1, atol=2)

    # Test AnnotationBbox
    bb3w = ab3.get_window_extent(renderer)
    bb3e = ab3.get_tightbbox(renderer)

    target3 = [-17.6, 129.0, 200.7, 167.9]
    assert_allclose(bb3w.extents, target3, atol=2)
    assert_allclose(bb3e.extents, target3, atol=2)

    bb6w = ab6.get_window_extent(renderer)
    bb6e = ab6.get_tightbbox(renderer)

    target6 = [180.0, -32.0, 230.0, 92.9]
    assert_allclose(bb6w.extents, target6, atol=2)
    assert_allclose(bb6e.extents, target6, atol=2)

    # Test bbox_inches='tight'
    buf = io.BytesIO()
    fig.savefig(buf, bbox_inches='tight')
    buf.seek(0)
    shape = plt.imread(buf).shape
    targetshape = (350, 504, 4)
    assert_allclose(shape, targetshape, atol=2)

    # Simple smoke test for tight_layout, to make sure it does not error out.
    fig.canvas.draw()
    fig.tight_layout()
    fig.canvas.draw()


def test_zorder():
    assert OffsetBox(zorder=42).zorder == 42


def test_arrowprops_copied():
    da = DrawingArea(20, 20, 0, 0, clip=True)
    arrowprops = {"arrowstyle": "->", "relpos": (.3, .7)}
    ab = AnnotationBbox(da, [.5, .5], xybox=(-0.2, 0.5), xycoords='data',
                        boxcoords="axes fraction", box_alignment=(0., .5),
                        arrowprops=arrowprops)
    assert ab.arrowprops is not ab
    assert arrowprops["relpos"] == (.3, .7)


@pytest.mark.parametrize("align", ["baseline", "bottom", "top",
                                   "left", "right", "center"])
def test_packers(align):
    # set the DPI to match points to make the math easier below
    fig = plt.figure(dpi=72)
    renderer = fig.canvas.get_renderer()

    x1, y1 = 10, 30
    x2, y2 = 20, 60
    r1 = DrawingArea(x1, y1)
    r2 = DrawingArea(x2, y2)

    # HPacker
    hpacker = HPacker(children=[r1, r2], align=align)
    hpacker.draw(renderer)
    bbox = hpacker.get_bbox(renderer)
    px, py = hpacker.get_offset(bbox, renderer)
    # width, height, xdescent, ydescent
    assert_allclose(bbox.bounds, (0, 0, x1 + x2, max(y1, y2)))
    # internal element placement
    if align in ("baseline", "left", "bottom"):
        y_height = 0
    elif align in ("right", "top"):
        y_height = y2 - y1
    elif align == "center":
        y_height = (y2 - y1) / 2
    # x-offsets, y-offsets
    assert_allclose([child.get_offset() for child in hpacker.get_children()],
                    [(px, py + y_height), (px + x1, py)])

    # VPacker
    vpacker = VPacker(children=[r1, r2], align=align)
    vpacker.draw(renderer)
    bbox = vpacker.get_bbox(renderer)
    px, py = vpacker.get_offset(bbox, renderer)
    # width, height, xdescent, ydescent
    assert_allclose(bbox.bounds, (0, -max(y1, y2), max(x1, x2), y1 + y2))
    # internal element placement
    if align in ("baseline", "left", "bottom"):
        x_height = 0
    elif align in ("right", "top"):
        x_height = x2 - x1
    elif align == "center":
        x_height = (x2 - x1) / 2
    # x-offsets, y-offsets
    assert_allclose([child.get_offset() for child in vpacker.get_children()],
                    [(px + x_height, py), (px, py - y2)])


def test_paddedbox_default_values():
    # smoke test paddedbox for correct default value
    fig, ax = plt.subplots()
    at = AnchoredText("foo",  'upper left')
    pb = PaddedBox(at, patch_attrs={'facecolor': 'r'}, draw_frame=True)
    ax.add_artist(pb)
    fig.draw_without_rendering()


def test_annotationbbox_properties():
    ab = AnnotationBbox(DrawingArea(20, 20, 0, 0, clip=True), (0.5, 0.5),
                        xycoords='data')
    assert ab.xyann == (0.5, 0.5)  # xy if xybox not given
    assert

> Only 4 reflections allowed, stopping.  
