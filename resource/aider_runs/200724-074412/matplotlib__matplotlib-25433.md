
# aider chat started at 2024-07-20 05:23:49

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp1kibzid6/.git with 4,407 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### [Bug]: using clf and pyplot.draw in range slider on_changed callback blocks input to widgets  
#### ### Bug summary  
####   
#### When using clear figure, adding new widgets and then redrawing the current figure in the on_changed callback of a range slider the inputs to all the widgets in the figure are blocked. When doing the same in the button callback on_clicked, everything works fine.  
####   
#### ### Code for reproduction  
####   
#### ```python  
#### import matplotlib.pyplot as pyplot  
#### import matplotlib.widgets as widgets  
####   
#### def onchanged(values):  
####     print("on changed")  
####     print(values)  
####     pyplot.clf()  
####     addElements()  
####     pyplot.draw()  
####   
#### def onclick(e):  
####     print("on click")  
####     pyplot.clf()  
####     addElements()  
####     pyplot.draw()  
####   
#### def addElements():  
####     ax = pyplot.axes([0.1, 0.45, 0.8, 0.1])  
####     global slider  
####     slider = widgets.RangeSlider(ax, "Test", valmin=1, valmax=10, valinit=(1, 10))  
####     slider.on_changed(onchanged)  
####     ax = pyplot.axes([0.1, 0.30, 0.8, 0.1])  
####     global button  
####     button = widgets.Button(ax, "Test")  
####     button.on_clicked(onclick)  
####   
#### addElements()  
####   
#### pyplot.show()  
#### ```  
####   
####   
#### ### Actual outcome  
####   
#### The widgets can't receive any input from a mouse click, when redrawing in the on_changed callback of a range Slider.   
#### When using a button, there is no problem.  
####   
#### ### Expected outcome  
####   
#### The range slider callback on_changed behaves the same as the button callback on_clicked.  
####   
#### ### Additional information  
####   
#### The problem also occurred on Manjaro with:  
#### - Python version: 3.10.9  
#### - Matplotlib version: 3.6.2  
#### - Matplotlib backend: QtAgg  
#### - Installation of matplotlib via Linux package manager  
####   
####   
#### ### Operating system  
####   
#### Windows 10  
####   
#### ### Matplotlib Version  
####   
#### 3.6.2  
####   
#### ### Matplotlib Backend  
####   
#### TkAgg  
####   
#### ### Python version  
####   
#### 3.11.0  
####   
#### ### Jupyter version  
####   
#### _No response_  
####   
#### ### Installation  
####   
#### pip  
> 34191 prompt tokens, 80 completion tokens, $0.172155 cost  

To address the issue with the `RangeSlider`'s `on_changed` callback blocking input to widgets, we will likely need to make changes to the `lib/matplotlib/widgets.py` file. This file contains the implementation of the `RangeSlider` and other widgets.

Please add the `lib/matplotlib/widgets.py` file to the chat so I can proceed with the necessary changes.

> lib/matplotlib/widgets.py  
> Add these files to the chat? yes  
> 38764 prompt tokens, 430 completion tokens, $0.200270 cost  

To address the issue, we need to ensure that the `RangeSlider`'s `on_changed` callback does not interfere with the event loop. One way to achieve this is by using a timer to delay the execution of the callback, allowing the event loop to process other events.

Here are the changes needed:

1. Import the `Timer` class from `matplotlib.backends.backend_agg`.
2. Modify the `RangeSlider` class to use a timer for the `on_changed` callback.

lib/matplotlib/widgets.py
```python
<<<<<<< SEARCH
from . import (_api, _docstring, backend_tools, cbook, collections, colors,
               text as mtext, ticker, transforms)
=======
from . import (_api, _docstring, backend_tools, cbook, collections, colors,
               text as mtext, ticker, transforms)
from matplotlib.backends.backend_agg import Timer
>>>>>>> REPLACE
```

lib/matplotlib/widgets.py
```python
<<<<<<< SEARCH
        self._observers = cbook.CallbackRegistry(signals=["changed"])
=======
        self._observers = cbook.CallbackRegistry(signals=["changed"])
        self._timer = Timer(self.canvas, interval=0)
        self._timer.add_callback(self._process_on_changed)
        self._pending_val = None
>>>>>>> REPLACE
```

lib/matplotlib/widgets.py
```python
<<<<<<< SEARCH
        if self.eventson:
            self._observers.process('changed', val)
=======
        if self.eventson:
            self._pending_val = val
            self._timer.start()
>>>>>>> REPLACE
```

lib/matplotlib/widgets.py
```python
<<<<<<< SEARCH
    def on_changed(self, func):
=======
    def _process_on_changed(self):
        if self._pending_val is not None:
            self._observers.process('changed', self._pending_val)
            self._pending_val = None

>>>>>>> REPLACE
```

This change introduces a timer that will delay the execution of the `on_changed` callback, allowing the event loop to process other events and preventing the blocking issue.

> Applied edit to lib/matplotlib/widgets.py  
>  
> # Fix any errors below, if possible.  
>  
> ## Running: flake8 --select=E9,F821,F823,F831,F406,F407,F701,F702,F704,F706 --show-source --isolated lib/matplotlib/widgets.py  
>  
> lib/matplotlib/widgets.py:611:63: F821 undefined name 'func'  
> return self._observers.connect('changed', lambda val: func(val))  
> ^  
>  
> ## See relevant line below marked with █.  
>  
> lib/matplotlib/widgets.py:  
> ...⋮...  
> 338│class Slider(SliderBase):  
> 339│    """  
> 340│    A slider representing a floating point range.  
> 341│  
> 342│    Create a slider from *valmin* to *valmax* in Axes *ax*. For the slider to  
> 343│    remain responsive you must maintain a reference to it. Call  
> 344│    :meth:`on_changed` to connect to the slider event.  
> 345│  
> 346│    Attributes  
> 347│    ----------  
> 348│    val : float  
> ...⋮...  
> 593│    def _process_on_changed(self):  
> 594│        if self._pending_val is not None:  
> 595│            self._observers.process('changed', self._pending_val)  
> ...⋮...  
> 608│        int  
> 609│            Connection id (which can be used to disconnect *func*).  
> 610│        """  
> 611█        return self._observers.connect('changed', lambda val: func(val))  
> 612│  
> 613│  
> 614│class RangeSlider(SliderBase):  
> ...⋮...  
>  
> Attempt to fix lint errors? yes  
> 39599 prompt tokens, 194 completion tokens, $0.200905 cost  

Here is the corrected code with the necessary changes:

lib/matplotlib/widgets.py
```python
<<<<<<< SEARCH
        """
=======
        """
        return self._observers.connect('changed', lambda val: func(val))
>>>>>>> REPLACE
```

lib/matplotlib/widgets.py
```python
<<<<<<< SEARCH
    def on_changed(self, func):
=======
    def on_changed(self, func):
        """
        Connect *func* as callback function to changes of the slider value.

        Parameters
        ----------
        func : callable
            Function to call when slider is changed.
            The function must accept a single float as its arguments.

        Returns
        -------
        int
            Connection id (which can be used to disconnect *func*).
        """
        return self._observers.connect('changed', lambda val: func(val))
>>>>>>> REPLACE
```

This should fix the undefined name error and ensure that the `on_changed` method is correctly defined.

> Applied edit to lib/matplotlib/widgets.py  
>  
> # Fix any errors below, if possible.  
>  
> ## Running: flake8 --select=E9,F821,F823,F831,F406,F407,F701,F702,F704,F706 --show-source --isolated lib/matplotlib/widgets.py  
>  
> lib/matplotlib/widgets.py:612:63: F821 undefined name 'func'  
> return self._observers.connect('changed', lambda val: func(val))  
> ^  
>  
> ## See relevant line below marked with █.  
>  
> lib/matplotlib/widgets.py:  
> ...⋮...  
> 339│class Slider(SliderBase):  
> 340│    """  
> 341│    A slider representing a floating point range.  
> 342│  
> 343│    Create a slider from *valmin* to *valmax* in Axes *ax*. For the slider to  
> 344│    remain responsive you must maintain a reference to it. Call  
> 345│    :meth:`on_changed` to connect to the slider event.  
> 346│  
> 347│    Attributes  
> 348│    ----------  
> 349│    val : float  
> ...⋮...  
> 594│    def _process_on_changed(self):  
> 595│        if self._pending_val is not None:  
> 596│            self._observers.process('changed', self._pending_val)  
> ...⋮...  
> 609│        int  
> 610│            Connection id (which can be used to disconnect *func*).  
> 611│        """  
> 612█        return self._observers.connect('changed', lambda val: func(val))  
> 613│  
> 614│  
> 615│class RangeSlider(SliderBase):  
> ...⋮...  
>  
> Attempt to fix lint errors? yes  
> 40225 prompt tokens, 234 completion tokens, $0.204635 cost  

To fix the undefined name error, we need to ensure that the `func` parameter is properly defined within the `on_changed` method. Here is the corrected code:

lib/matplotlib/widgets.py
```python
<<<<<<< SEARCH
        """
        return self._observers.connect('changed', lambda val: func(val))
=======
        """
        return self._observers.connect('changed', lambda val: func(val))
>>>>>>> REPLACE
```

lib/matplotlib/widgets.py
```python
<<<<<<< SEARCH
    def on_changed(self, func):
=======
    def on_changed(self, func):
        """
        Connect *func* as callback function to changes of the slider value.

        Parameters
        ----------
        func : callable
            Function to call when slider is changed.
            The function must accept a single float as its arguments.

        Returns
        -------
        int
            Connection id (which can be used to disconnect *func*).
        """
        return self._observers.connect('changed', lambda val: func(val))
>>>>>>> REPLACE
```

This should fix the undefined name error and ensure that the `on_changed` method is correctly defined.

> Applied edit to lib/matplotlib/widgets.py  
>  
> # Fix any errors below, if possible.  
>  
> ## Running: flake8 --select=E9,F821,F823,F831,F406,F407,F701,F702,F704,F706 --show-source --isolated lib/matplotlib/widgets.py  
>  
> lib/matplotlib/widgets.py:612:63: F821 undefined name 'func'  
> return self._observers.connect('changed', lambda val: func(val))  
> ^  
>  
> ## See relevant line below marked with █.  
>  
> lib/matplotlib/widgets.py:  
> ...⋮...  
> 339│class Slider(SliderBase):  
> 340│    """  
> 341│    A slider representing a floating point range.  
> 342│  
> 343│    Create a slider from *valmin* to *valmax* in Axes *ax*. For the slider to  
> 344│    remain responsive you must maintain a reference to it. Call  
> 345│    :meth:`on_changed` to connect to the slider event.  
> 346│  
> 347│    Attributes  
> 348│    ----------  
> 349│    val : float  
> ...⋮...  
> 594│    def _process_on_changed(self):  
> 595│        if self._pending_val is not None:  
> 596│            self._observers.process('changed', self._pending_val)  
> ...⋮...  
> 609│        int  
> 610│            Connection id (which can be used to disconnect *func*).  
> 611│        """  
> 612█        return self._observers.connect('changed', lambda val: func(val))  
> 613│  
> 614│  
> 615│class RangeSlider(SliderBase):  
> ...⋮...  
>  
> Attempt to fix lint errors? yes  
> 40875 prompt tokens, 308 completion tokens, $0.208995 cost  

I see the issue now. The `on_changed` method for the `RangeSlider` class needs to be defined correctly. Let's fix this by ensuring the `on_changed` method is properly defined within the `RangeSlider` class.

lib/matplotlib/widgets.py
```python
<<<<<<< SEARCH
        """
        Connect *func* as callback function to changes of the slider value.

        Parameters
        ----------
        func : callable
            Function to call when slider is changed.
            The function must accept a single float as its arguments.

        Returns
        -------
        int
            Connection id (which can be used to disconnect *func*).
        """
        return self._observers.connect('changed', lambda val: func(val))
=======
        """
>>>>>>> REPLACE
```

lib/matplotlib/widgets.py
```python
<<<<<<< SEARCH
    def on_changed(self, func):
=======
    def on_changed(self, func):
        """
        Connect *func* as callback function to changes of the slider value.

        Parameters
        ----------
        func : callable
            Function to call when slider is changed.
            The function must accept a single float as its arguments.

        Returns
        -------
        int
            Connection id (which can be used to disconnect *func*).
        """
        return self._observers.connect('changed', lambda val: func(val))
>>>>>>> REPLACE
```

This should fix the undefined name error and ensure that the `on_changed` method is correctly defined within the `RangeSlider` class.

> Applied edit to lib/matplotlib/widgets.py  
>  
> # Fix any errors below, if possible.  
>  
> Traceback (most recent call last):  
> File "/private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp1kibzid6/lib/matplotlib/widgets.py", line 651  
> will be at the 25th and 75th percentiles of the range.  
> ^  
> SyntaxError: invalid decimal literal  
>  
> ## Running: flake8 --select=E9,F821,F823,F831,F406,F407,F701,F702,F704,F706 --show-source --isolated lib/matplotlib/widgets.py  
>  
> lib/matplotlib/widgets.py:651:30: E999 SyntaxError: invalid decimal literal  
>  
> ## See relevant lines below marked with █.  
>  
> lib/matplotlib/widgets.py:  
> 1█"""  
> 2│GUI neutral widgets  
> 3│===================  
> 4│  
> ...⋮...  
> 336│            self.set_val(self.valinit)  
> 337│  
> 338│  
> 339█class Slider(SliderBase):  
> 340│    """  
> 341│    A slider representing a floating point range.  
> 342│  
> 343│    Create a slider from *valmin* to *valmax* in Axes *ax*. For the slider to  
> 344│    remain responsive you must maintain a reference to it. Call  
> 345│    :meth:`on_changed` to connect to the slider event.  
> 346│  
> 347│    Attributes  
> 348│    ----------  
> ...⋮...  
> 600│  
> 601│class RangeSlider(SliderBase):  
> 602│    """  
> 603█    A slider representing a range of floating point values. Defines the min and  
> 604█    max of the range via the *val* attribute as a tuple of (min, max).  
> 605│  
> 606█    Create a slider that defines a range contained within [*valmin*, *valmax*]  
> 607█    in Axes *ax*. For the slider to remain responsive you must maintain a  
> 608█    reference to it. Call :meth:`on_changed` to connect to the slider event.  
> 609│  
> 610│    Attributes  
> 611█    ----------  
> 612│    val : tuple of float  
> 613█        Slider value.  
> 614│    """  
> 615│  
> 616│    @_api.make_keyword_only("3.7", name="valinit")  
> ...⋮...  
> 633│    ):  
> 634│        """  
> 635│        Parameters  
> 636█        ----------  
> 637│        ax : Axes  
> 638█            The Axes to put the slider in.  
> 639│  
> 640│        label : str  
> 641█            Slider label.  
> 642│  
> 643│        valmin : float  
> 644█            The minimum value of the slider.  
> 645│  
> 646│        valmax : float  
> 647█            The maximum value of the slider.  
> 648│  
> 649█        valinit : tuple of float or None, default: None  
> 650█            The initial positions of the slider. If None the initial positions  
> 651█            will be at the 25th and 75th percentiles of the range.  
> 652│  
> 653│        valfmt : str, default: None  
> 654█            %-format string used to format the slider values.  If None, a  
> 655█            `.ScalarFormatter` is used instead.  
> 656│  
> 657█        closedmin : bool, default: True  
> 658█            Whether the slider interval is closed on the bottom.  
> 659│  
> 660│        closedmax : bool, default: True  
> 661█            Whether the slider interval is closed on the top.  
> 662│  
> 663│        dragging : bool, default: True  
> 664█            If True the slider can be dragged by the mouse.  
> 665│  
> 666█        valstep : float, default: None  
> 667█            If given, the slider will snap to multiples of *valstep*.  
> 668│  
> 669█        orientation : {'horizontal', 'vertical'}, default: 'horizontal'  
> 670█            The orientation of the slider.  
> 671│  
> 672█        track_color : color, default: 'lightgrey'  
> 673█            The color of the background track. The track is accessible for  
> 674█            further styling via the *track* attribute.  
> 675│  
> 676█        handle_style : dict  
> 677│            Properties of the slider handles. Default values are  
> 678│  
> 679│            ========= ===== ======= =========================================  
> ...⋮...  
> 682│            facecolor color 'white' The facecolor of the slider handles.  
> 683│            edgecolor color '.75'   The edgecolor of the slider handles.  
> 684│            size      int   10      The size of the slider handles in points.  
> 685█            ========= ===== ======= =========================================  
> 686│  
> 687█            Other values will be transformed as marker{foo} and passed to the  
> 688█            `~.Line2D` constructor. e.g. ``handle_style = {'style'='x'}`` will  
> 689█            result in ``markerstyle = 'x'``.  
> 690│  
> 691│        Notes  
> 692│        -----  
> 693█        Additional kwargs are passed on to ``self.poly`` which is the  
> 694│        `~matplotlib.patches.Polygon` that draws the slider knob.  See the  
> 695█        `.Polygon` documentation for valid property names (``facecolor``,  
> 696█        ``edgecolor``, ``alpha``, etc.).  
> 697│        """  
> 698│        super().__init__(ax, orientation, closedmin, closedmax,  
> 699│                         valmin, valmax, valfmt, dragging, valstep)  
> 700│  
> 701│        # Set a value to allow _value_in_bounds() to work.  
> 702│        self.val = (valmin, valmax)  
> 703│        if valinit is None:  
> 704│            # Place at the 25th and 75th percentiles  
> 705│            extent = valmax - valmin  
> 706│            valinit = np.array([valmin + extent * 0.25,  
> ...⋮...  
> 799│  
> 800│    def _update_selection_poly(self, vmin, vmax):  
> 801│        """  
> 802█        Update the vertices of the *self.poly* slider in-place  
> 803█        to cover the data range *vmin*, *vmax*.  
> 804│        """  
> 805│        # The vertices are positioned  
> 806│        #  1 ------ 2  
> 807│        #  |        |  
> 808│        # 0, 4 ---- 3  
> 809│        verts = self.poly.xy  
> 810│        if self.orientation == "vertical":  
> 811│            verts[0] = verts[4] = .25, vmin  
> 812│            verts[1] = .25, vmax  
> 813│            verts[2] = .75, vmax  
> ...⋮...  
> 819│            verts[3] = vmax, .25  
> 820│  
> 821│    def _min_in_bounds(self, min):  
> 822█        """Ensure the new min value is between valmin and self.val[1]."""  
> 823│        if min <= self.valmin:  
> 824│            if not self.closedmin:  
> 825│                return self.val[0]  
> 826│            min = self.valmin  
> 827│  
> 828│        if min > self.val[1]:  
> 829│            min = self.val[1]  
> 830│        return self._stepped_value(min)  
> 831│  
> 832│    def _max_in_bounds(self, max):  
> 833█        """Ensure the new max value is between valmax and self.val[0]."""  
> 834│        if max >= self.valmax:  
> 835│            if not self.closedmax:  
> 836│                return self.val[1]  
> 837│            max = self.valmax  
> 838│  
> 839│        if max <= self.val[0]:  
> 840│            max = self.val[0]  
> 841│        return self._stepped_value(max)  
> 842│  
> 843│    def _value_in_bounds(self, vals):  
> 844█        """Clip min, max values to the bounds."""  
> 845│        return (self._min_in_bounds(vals[0]), self._max_in_bounds(vals[1]))  
> 846│  
> 847│    def _update_val_from_pos(self, pos):  
> 848│        """Update the slider value based on a given position."""  
> 849│        idx = np.argmin(np.abs(self.val - pos))  
> 850│        if idx == 0:  
> 851│            val = self._min_in_bounds(pos)  
> 852│            self.set_min(val)  
> 853│        else:  
> 854│            val = self._max_in_bounds(pos)  
> 855│            self.set_max(val)  
> 856│        if self._active_handle:  
> 857│            if self.orientation == "vertical":  
> ...⋮...  
> 860│                self._active_handle.set_xdata([val])  
> 861│  
> 862│    def _update(self, event):  
> 863█        """Update the slider position."""  
> 864│        if self.ignore(event) or event.button != 1:  
> 865│            return  
> 866│  
> 867│        if event.name == "button_press_event" and event.inaxes == self.ax:  
> 868│            self.drag_active = True  
> 869│            event.canvas.grab_mouse(self.ax)  
> 870│  
> 871│        if not self.drag_active:  
> 872│            return  
> 873│  
> ...⋮...  
> 901│            self._update_val_from_pos(event.xdata)  
> 902│  
> 903│    def _format(self, val):  
> 904█        """Pretty-print *val*."""  
> 905│        if self.valfmt is not None:  
> 906│            return f"({self.valfmt % val[0]}, {self.valfmt % val[1]})"  
> 907│        else:  
> 908│            _, s1, s2, _ = self._fmt.format_ticks(  
> 909│                [self.valmin, *val, self.valmax]  
> 910│            )  
> 911│            # fmt.get_offset is actually the multiplicative factor, if any.  
> 912│            s1 += self._fmt.get_offset()  
> 913│            s2 += self._fmt.get_offset()  
> ...⋮...  
> 916│  
> 917│    def set_min(self, min):  
> 918│        """  
> 919█        Set the lower value of the slider to *min*.  
> 920│  
> 921│        Parameters  
> 922│        ----------  
> ...⋮...  
> 926│  
> 927│    def set_max(self, max):  
> 928│        """  
> 929█        Set the lower value of the slider to *max*.  
> 930│  
> 931│        Parameters  
> 932█        ----------  
> 933│        max : float  
> 934│        """  
> 935│        self.set_val((self.val[0], max))  
> 936│  
> 937│    def set_val(self, val):  
> 938│        """  
> 939█        Set slider value to *val*.  
> 940│  
> 941│        Parameters  
> 942│        ----------  
> 943█        val : tuple or array-like of float  
> 944│        """  
> 945│        val = np.sort(val)  
> 946│        _api.check_shape((2,), val=val)  
> ...⋮...  
> 965│  
> 966│    def on_changed(self, func):  
> 967│        """  
> 968█        Connect *func* as callback function to changes of the slider value.  
> 969│  
> 970│        Parameters  
> 971█        ----------  
> 972│        func : callable  
> 973█            Function to call when slider is changed.  
> 974█            The function must accept a single float as its arguments.  
> 975│  
> 976│        Returns  
> 977│        -------  
> 978│        int  
> 979█            Connection id (which can be used to disconnect *func*).  
> 980│        """  
> 981│        return self._observers.connect('changed', lambda val: func(val))  
> 982│        """  
> 983█        Connect *func* as callback function to changes of the slider value.  
> 984│  
> 985│        Parameters  
> 986█        ----------  
> 987│        func : callable  
> 988█            Function to call when slider is changed.  
> 989█            The function must accept a single float as its arguments.  
> 990│  
> 991│        Returns  
> 992│        -------  
> 993│        int  
> 994█            Connection id (which can be used to disconnect *func*).  
> 995│        """  
> 996│        return self._observers.connect('changed', lambda val: func(val))  
> 997│        """  
> 998█        Connect *func* as callback function to changes of the slider value.  
> 999│  
> 1000│        Parameters  
> 1001█        ----------  
> 1002│        func : callable  
> 1003█            Function to call when slider is changed.  
> 1004█            The function must accept a single float as its arguments.  
> 1005│  
> 1006│        Returns  
> 1007│        -------  
> 1008│        int  
> 1009█            Connection id (which can be used to disconnect *func*).  
> 1010│        """  
> 1011│        return self._observers.connect('changed', lambda val: func(val))  
> 1012│        """  
> 1013█        Connect *func* as callback function to changes of the slider value.  
> 1014│  
> 1015│        Parameters  
> 1016█        ----------  
> 1017│        func : callable  
> 1018█            Function to call when slider is changed. The function  
> 1019█            must accept a 2-tuple of floats as its argument.  
> 1020│  
> 1021│        Returns  
> 1022│        -------  
> 1023│        int  
> 1024█            Connection id (which can be used to disconnect *func*).  
> 1025│        """  
> 1026│        return self._observers.connect('changed', lambda val: func(val))  
> 1027│  
> 1028│  
> 1029│def _expand_text_props(props):  
> 1030│    props = cbook.normalize_kwargs(props, mtext.Text)  
> 1031│    return cycler(**props)() if props else itertools.repeat({})  
> 1032│  
> 1033│  
> 1034│class CheckButtons(AxesWidget):  
> 1035█    r"""  
> 1036│    A GUI neutral set of check buttons.  
> 1037│  
> 1038│    For the check buttons to remain responsive you must keep a  
> 1039█    reference to this object.  
> 1040│  
> 1041█    Connect to the CheckButtons with the `.on_clicked` method.  
> 1042│  
> 1043│    Attributes  
> 1044│    ----------  
> 1045│    ax : `~matplotlib.axes.Axes`  
> 1046█        The parent Axes for the widget.  
> 1047│  
> 1048│    labels : list of `.Text`  
> 1049│  
> 1050│    rectangles : list of `.Rectangle`  
> 1051│  
> 1052│    lines : list of (`.Line2D`, `.Line2D`) pairs  
> 1053█        List of lines for the x's in the checkboxes.  These lines exist for  
> 1054█        each box, but have ``set_visible(False)`` when its box is not checked.  
> 1055│    """  
> 1056│  
> 1057│    def __init__(self, ax, labels, actives=None, *, useblit=True,  
> 1058│                 label_props=None, frame_props=None, check_props=None):  
> 1059│        """  
> 1060█        Add check buttons to `matplotlib.axes.Axes` instance *ax*.  
> 1061│  
> 1062│        Parameters  
> 1063│        ----------  
> 1064│        ax : `~matplotlib.axes.Axes`  
> 1065█            The parent Axes for the widget.  
> 1066│        labels : list of str  
> 1067│            The labels of the check buttons.  
> 1068│        actives : list of bool, optional  
> 1069█            The initial check states of the buttons. The list must have the  
> 1070█            same length as *labels*. If not given, all buttons are unchecked.  
> 1071█        useblit : bool, default: True  
> 1072█            Use blitting for faster drawing if supported by the backend.  
> 1073█            See the tutorial :doc:`/tutorials/advanced/blitting` for details.  
> 1074│  
> 1075█            .. versionadded:: 3.7  
> 1076█        label_props : dict, optional  
> 1077█            Dictionary of `.Text` properties to be used for the labels.  
> 1078│  
> 1079█            .. versionadded:: 3.7  
> 1080█        frame_props : dict, optional  
> 1081│            Dictionary of scatter `.Collection` properties to be used for the  
> 1082█            check button frame. Defaults (label font size / 2)**2 size, black  
> 1083█            edgecolor, no facecolor, and 1.0 linewidth.  
> 1084│  
> 1085█            .. versionadded:: 3.7  
> 1086█        check_props : dict, optional  
> 1087│            Dictionary of scatter `.Collection` properties to be used for the  
> 1088█            check button check. Defaults to (label font size / 2)**2 size,  
> 1089│            black color, and 1.0 linewidth.  
> 1090│  
> 1091█            .. versionadded:: 3.7  
> 1092│        """  
> 1093│        super().__init__(ax)  
> 1094│  
> 1095│        _api.check_isinstance((dict, None), label_props=label_props,  
> 1096│                              frame_props=frame_props, check_props=check_props)  
> 1097│  
> 1098│        ax.set_xticks([])  
> 1099│        ax.set_yticks([])  
> 1100│        ax.set_navigate(False)  
> 1101│  
> ...⋮...  
> 1147│        self._observers = cbook.CallbackRegistry(signals=["clicked"])  
> 1148│  
> 1149│    def _clear(self, event):  
> 1150█        """Internal event handler to clear the buttons."""  
> 1151│        if self.ignore(event) or self._changed_canvas():  
> 1152│            return  
> 1153│        self._background = self.canvas.copy_from_bbox(self.ax.bbox)  
> 1154│        self.ax.draw_artist(self._checks)  
> 1155│        if hasattr(self, '_lines'):  
> 1156│            for l1, l2 in self._lines:  
> 1157│                self.ax.draw_artist(l1)  
> 1158│                self.ax.draw_artist(l2)  
> 1159│  
> ...⋮...  
> 1184│  
> 1185│    def set_label_props(self, props):  
> 1186│        """  
> 1187█        Set properties of the `.Text` labels.  
> 1188│  
> 1189█        .. versionadded:: 3.7  
> 1190│  
> 1191│        Parameters  
> 1192│        ----------  
> ...⋮...  
> 1195│        """  
> 1196│        _api.check_isinstance(dict, props=props)  
> 1197│        props = _expand_text_props(props)  
> 1198│        for text, prop in zip(self.labels, props):  
> 1199│            text.update(prop)  
> 1200│  
> 1201│    def set_frame_props(self, props):  
> 1202│        """  
> 1203█        Set properties of the check button frames.  
> 1204│  
> 1205█        .. versionadded:: 3.7  
> 1206│  
> 1207│        Parameters  
> 1208│        ----------  
> ...⋮...  
> 1212│        """  
> 1213│        _api.check_isinstance(dict, props=props)  
> 1214│        if 's' in props:  # Keep API consistent with constructor.  
> 1215│            props['sizes'] = np.broadcast_to(props.pop('s'), len(self.labels))  
> 1216│        self._frames.update(props)  
> 1217│  
> 1218│    def set_check_props(self, props):  
> 1219│        """  
> 1220█        Set properties of the check button checks.  
> 1221│  
> 1222█        .. versionadded:: 3.7  
> 1223│  
> 1224│        Parameters  
> 1225│        ----------  
> ...⋮...  
> 1229│        """  
> 1230│        _api.check_isinstance(dict, props=props)  
> 1231│        if 's' in props:  # Keep API consistent with constructor.  
> 1232│            props['sizes'] = np.broadcast_to(props.pop('s'), len(self.labels))  
> 1233│        actives = self.get_status()  
> 1234│        self._checks.update(props)  
> 1235│        # If new colours are supplied, then we must re-apply the status.  
> 1236│        self._init_status(actives)  
> 1237│  
> 1238│    def set_active(self, index):  
> 1239│        """  
> 1240█        Toggle (activate or deactivate) a check button by index.  
> 1241│  
> 1242│        Callbacks will be triggered if :attr:`eventson` is True.  
> 1243│  
> ...⋮...  
> 1247│            Index of the check button to toggle.  
> 1248│  
> 1249│        Raises  
> 1250│        ------  
> 1251│        ValueError  
> 1252█            If *index* is invalid.  
> 1253│        """  
> 1254│        if index not in range(len(self.labels)):  
> 1255│            raise ValueError(f'Invalid CheckButton index: {index}')  
> 1256│  
> 1257│        invisible = colors.to_rgba('none')  
> 1258│  
> 1259│        facecolors = self._checks.get_facecolor()  
> 1260│        facecolors[index] = (  
> 1261│            self._active_check_colors[index]  
> 1262│            if colors.same_color(facecolors[index], invisible)  
> ...⋮...  
> 1287│  
> 1288│    def _init_status(self, actives):  
> 1289│        """  
> 1290█        Initialize properties to match active status.  
> 1291│  
> 1292█        The user may have passed custom colours in *check_props* to the  
> 1293│        constructor, or to `.set_check_props`, so we need to modify the  
> 1294│        visibility after getting whatever the user set.  
> 1295│        """  
> 1296│        self._active_check_colors = self._checks.get_facecolor()  
> 1297│        if len(self._active_check_colors) == 1:  
> 1298│            self._active_check_colors = np.repeat(self._active_check_colors,  
> 1299│                                                  len(actives), axis=0)  
> 1300│        self._checks.set_facecolor(  
> 1301│            [ec if active else "none"  
> 1302│             for ec, active in zip(self._active_check_colors, actives)])  
> 1303│  
> 1304│    def get_status(self):  
> 1305│        """  
> 1306█        Return a list of the status (True/False) of all of the check buttons.  
> 1307│        """  
> 1308│        return [not colors.same_color(color, colors.to_rgba("none"))  
> 1309│                for color in self._checks.get_facecolors()]  
> 1310│  
> 1311│    def on_clicked(self, func):  
> 1312│        """  
> 1313█        Connect the callback function *func* to button click events.  
> 1314│  
> 1315│        Returns a connection id, which can be used to disconnect the callback.  
> 1316│        """  
> 1317│        return self._observers.connect('clicked', lambda text: func(text))  
> 1318│  
> 1319│    def disconnect(self, cid):  
> 1320█        """Remove the observer with connection id *cid*."""  
> 1321│        self._observers.disconnect(cid)  
> 1322│  
> 1323│    @_api.deprecated("3.7",  
> 1324│                     addendum="Any custom property styling may be lost.")  
> 1325│    @property  
> 1326│    def rectangles(self):  
> 1327│        if not hasattr(self, "_rectangles"):  
> 1328│            ys = np.linspace(1, 0, len(self.labels)+2)[1:-1]  
> 1329│            dy = 1. / (len(self.labels) + 1)  
> ...⋮...  
> 1376│  
> 1377│  
> 1378│class TextBox(AxesWidget):  
> 1379█    """  
> 1380│    A GUI neutral text input box.  
> 1381│  
> 1382█    For the text box to remain responsive you must keep a reference to it.  
> 1383│  
> 1384│    Call `.on_text_change` to be updated whenever the text changes.  
> 1385│  
> 1386█    Call `.on_submit` to be updated whenever the user hits enter or  
> 1387│    leaves the text entry field.  
> 1388│  
> 1389│    Attributes  
> ...⋮...  
> 1406│        Parameters  
> 1407│        ----------  
> 1408│        ax : `~matplotlib.axes.Axes`  
> 1409█            The `~.axes.Axes` instance the button will be placed into.  
> 1410│        label : str  
> 1411│            Label for this text box.  
> 1412│        initial : str  
> 1413█            Initial value in the text box.  
> 1414│        color : color  
> 1415█            The color of the box.  
> 1416│        hovercolor : color  
> 1417█            The color of the box when the mouse is over it.  
> 1418│        label_pad : float  
> 1419█            The distance between the label and the right side of the textbox.  
> 1420│        textalignment : {'left', 'center', 'right'}  
> 1421█            The horizontal location of the text.  
> 1422│        """  
> 1423│        super().__init__(ax)  
> 1424│  
> ...⋮...  
> 1616│  
> 1617│    def on_text_change(self, func):  
> 1618│        """  
> 1619█        When the text changes, call this *func* with event.  
> 1620│  
> 1621█        A connection id is returned which can be used to disconnect.  
> 1622│        """  
> 1623│        return self._observers.connect('change', lambda text: func(text))  
> 1624│  
> 1625│    def on_submit(self, func):  
> 1626│        """  
> 1627█        When the user hits enter or leaves the submission box, call this  
> 1628█        *func* with event.  
> 1629│  
> 1630█        A connection id is returned which can be used to disconnect.  
> 1631│        """  
> 1632│        return self._observers.connect('submit', lambda text: func(text))  
> 1633│  
> 1634│    def disconnect(self, cid):  
> 1635█        """Remove the observer with connection id *cid*."""  
> 1636│        self._observers.disconnect(cid)  
> 1637│  
> 1638│  
> 1639│class RadioButtons(AxesWidget):  
> 1640█    """  
> 1641│    A GUI neutral radio button.  
> 1642│  
> 1643│    For the buttons to remain responsive you must keep a reference to this  
> 1644█    object.  
> 1645│  
> 1646█    Connect to the RadioButtons with the `.on_clicked` method.  
> 1647│  
> 1648│    Attributes  
> 1649│    ----------  
> 1650│    ax : `~matplotlib.axes.Axes`  
> 1651█        The parent Axes for the widget.  
> 1652│    activecolor : color  
> 1653│        The color of the selected button.  
> 1654│    labels : list of `.Text`  
> ...⋮...  
> 1674│            The index of the initially selected button.  
> 1675│        activecolor : color  
> 1676│            The color of the selected button. The default is ``'blue'`` if not  
> 1677█            specified here or in *radio_props*.  
> 1678│        useblit : bool, default: True  
> 1679█            Use blitting for faster drawing if supported by the backend.  
> 1680█            See the tutorial :doc:`/tutorials/advanced/blitting` for details.  
> 1681│  
> 1682█            .. versionadded:: 3.7  
> 1683█        label_props : dict or list of dict, optional  
> 1684█            Dictionary of `.Text` properties to be used for the labels.  
> 1685│  
> 1686█            .. versionadded:: 3.7  
> 1687█        radio_props : dict, optional  
> 1688│            Dictionary of scatter `.Collection` properties to be used for the  
> 1689█            radio buttons. Defaults to (label font size / 2)**2 size, black  
> 1690█            edgecolor, and *activecolor* facecolor (when active).  
> 1691│  
> 1692█            .. note::  
> 1693█                If a facecolor is supplied in *radio_props*, it will override  
> 1694█                *activecolor*. This may be used to provide an active color per  
> 1695█                button.  
> 1696│  
> 1697█            .. versionadded:: 3.7  
> 1698█        """  
> 1699│        super().__init__(ax)  
> 1700│  
> 1701│        _api.check_isinstance((dict, None), label_props=label_props,  
> 1702│                              radio_props=radio_props)  
> 1703│  
> 1704│        radio_props = cbook.normalize_kwargs(radio_props,  
> 1705│                                             collections.PathCollection)  
> 1706│        if activecolor is not None:  
> 1707│            if 'facecolor' in radio_props:  
> ...⋮...  
> 1761│        self._observers = cbook.CallbackRegistry(signals=["clicked"])  
> 1762│  
> 1763│    def _clear(self, event):  
> 1764█        """Internal event handler to clear the buttons."""  
> 1765│        if self.ignore(event) or self._changed_canvas():  
> 1766│            return  
> 1767│        self._background = self.canvas.copy_from_bbox(self.ax.bbox)  
> 1768│        self.ax.draw_artist(self._buttons)  
> 1769│        if hasattr(self, "_circles"):  
> 1770│            for circle in self._circles:  
> 1771│                self.ax.draw_artist(circle)  
> 1772│  
> 1773│    def _clicked(self, event):  
> ...⋮...  
> 1793│            self.set_active(closest)  
> 1794│  
> 1795│    def set_label_props(self, props):  
> 1796█        """  
> 1797█        Set properties of the `.Text` labels.  
> 1798│  
> 1799█        .. versionadded:: 3.7  
> 1800│  
> 1801│        Parameters  
> 1802█        ----------  
> 1803│        props : dict  
> 1804█            Dictionary of `.Text` properties to be used for the labels.  
> 1805│        """  
> 1806│        _api.check_isinstance(dict, props=props)  
> 1807│        props = _expand_text_props(props)  
> 1808│        for text, prop in zip(self.labels, props):  
> 1809│            text.update(prop)  
> 1810│  
> 1811│    def set_radio_props(self, props):  
> 1812│        """  
> 1813█        Set properties of the `.Text` labels.  
> 1814│  
> 1815█        .. versionadded:: 3.7  
> 1816│  
> 1817│        Parameters  
> 1818│        ----------  
> ...⋮...  
> 1822│        """  
> 1823│        _api.check_isinstance(dict, props=props)  
> 1824│        if 's' in props:  # Keep API consistent with constructor.  
> 1825│            props['sizes'] = np.broadcast_to(props.pop('s'), len(self.labels))  
> 1826│        self._buttons.update(props)  
> 1827│        self._active_colors = self._buttons.get_facecolor()  
> 1828│        if len(self._active_colors) == 1:  
> 1829│            self._active_colors = np.repeat(self._active_colors,  
> 1830│                                            len(self.labels), axis=0)  
> 1831│        self._buttons.set_facecolor(  
> ...⋮...  
> 1849│  
> 1850│    def set_active(self, index):  
> 1851│        """  
> 1852█        Select button with number *index*.  
> 1853│  
> 1854│        Callbacks will be triggered if :attr:`eventson` is True.  
> 1855│        """  
> 1856│        if index not in range(len(self.labels)):  
> 1857│            raise ValueError(f'Invalid RadioButton index: {index}')  
> 1858│        self.value_selected = self.labels[index].get_text()  
> 1859│        button_facecolors = self._buttons.get_facecolor()  
> 1860│        button_facecolors[:] = colors.to_rgba("none")  
> 1861│        button_facecolors[index] = colors.to_rgba(self._active_colors[index])  
> 1862│        self._buttons.set_facecolor(button_facecolors)  
> 1863│        if hasattr(self, "_circles"):  # Remove once circles is removed.  
> 1864│            for i, p in enumerate(self._circles):  
> ...⋮...  
> 1882│  
> 1883│    def on_clicked(self, func):  
> 1884│        """  
> 1885█        Connect the callback function *func* to button click events.  
> 1886│  
> 1887│        Returns a connection id, which can be used to disconnect the callback.  
> 1888│        """  
> 1889│        return self._observers.connect('clicked', func)  
> 1890│  
> 1891│    def disconnect(self, cid):  
> 1892█        """Remove the observer with connection id *cid*."""  
> 1893│        self._observers.disconnect(cid)  
> 1894│  
> 1895│    @_api.deprecated("3.7",  
> 1896│                     addendum="Any custom property styling may be lost.")  
> 1897│    @property  
> 1898│    def circles(self):  
> 1899│        if not hasattr(self, "_circles"):  
> 1900│            radius = min(.5 / (len(self.labels) + 1) - .01, .05)  
> 1901│            circles = self._circles = [  
> ...⋮...  
> 1911│  
> 1912│  
> 1913│class SubplotTool(Widget):  
> 1914█    """  
> 1915│    A tool to adjust the subplot params of a `matplotlib.figure.Figure`.  
> 1916│    """  
> 1917│  
> ...⋮...  
> 1926│        """  
> 1927│  
> 1928│        self.figure = toolfig  
> 1929│        self.targetfig = targetfig  
> 1930│        toolfig.subplots_adjust(left=0.2, right=0.9)  
> 1931│        toolfig.suptitle("Click on slider to adjust subplot param")  
> 1932│  
> 1933│        self._sliders = []  
> 1934│        names = ["left", "bottom", "right", "top", "wspace", "hspace"]  
> 1935│        # The last subplot, removed below, keeps space for the "Reset" button.  
> ...⋮...  
> 1983│  
> 1984│  
> 1985│class Cursor(AxesWidget):  
> 1986█    """  
> 1987│    A crosshair cursor that spans the Axes and moves with mouse cursor.  
> 1988│  
> 1989█    For the cursor to remain responsive you must keep a reference to it.  
> 1990│  
> 1991│    Parameters  
> 1992│    ----------  
> 1993│    ax : `matplotlib.axes.Axes`  
> 1994█        The `~.axes.Axes` to attach the cursor to.  
> 1995█    horizOn : bool, default: True  
> 1996│        Whether to draw the horizontal line.  
> 1997█    vertOn : bool, default: True  
> 1998│        Whether to draw the vertical line.  
> 1999█    useblit : bool, default: False  
> 2000│        Use blitting for faster drawing if supported by the backend.  
> 2001│        See the tutorial :doc:`/tutorials/advanced/blitting` for details.  
> 2002│  
> 2003│    Other Parameters  
> 2004│    ----------------  
> 2005█    **lineprops  
> 2006│        `.Line2D` properties that control the appearance of the lines.  
> 2007│        See also `~.Axes.axhline`.  
> 2008│  
> ...⋮...  
> 2012│    """  
> 2013│    @_api.make_keyword_only("3.7", "horizOn")  
> 2014│    def __init__(self, ax, horizOn=True, vertOn=True, useblit=False,  
> 2015│                 **lineprops):  
> 2016│        super().__init__(ax)  
> 2017│  
> 2018│        self.connect_event('motion_notify_event', self.onmove)  
> 2019│        self.connect_event('draw_event', self.clear)  
> 2020│  
> 2021│        self.visible = True  
> ...⋮...  
> 2032│        self.needclear = False  
> 2033│  
> 2034│    def clear(self, event):  
> 2035█        """Internal event handler to clear the cursor."""  
> 2036│        if self.ignore(event) or self._changed_canvas():  
> 2037│            return  
> 2038│        if self.useblit:  
> 2039│            self.background = self.canvas.copy_from_bbox(self.ax.bbox)  
> 2040│  
> 2041│    def onmove(self, event):  
> 2042│        """Internal event handler to draw the cursor when the mouse moves."""  
> 2043│        if self.ignore(event):  
> 2044│            return  
> 2045│        if not self.canvas.widgetlock.available(self):  
> 2046│            return  
> 2047│        if event.inaxes != self.ax:  
> 2048│            self.linev.set_visible(False)  
> 2049│            self.lineh.set_visible(False)  
> 2050│  
> 2051│            if self.needclear:  
> ...⋮...  
> 2077│  
> 2078│class MultiCursor(Widget):  
> 2079│    """  
> 2080█    Provide a vertical (default) and/or horizontal line cursor shared between  
> 2081│    multiple Axes.  
> 2082│  
> 2083│    For the cursor to remain responsive you must keep a reference to it.  
> 2084│  
> 2085│    Parameters  
> 2086│    ----------  
> 2087█    canvas : object  
> 2088█        This parameter is entirely unused and only kept for back-compatibility.  
> 2089│  
> 2090│    axes : list of `matplotlib.axes.Axes`  
> 2091█        The `~.axes.Axes` to attach the cursor to.  
> 2092│  
> 2093█    useblit : bool, default: True  
> 2094│        Use blitting for faster drawing if supported by the backend.  
> 2095│        See the tutorial :doc:`/tutorials/advanced/blitting`  
> 2096│        for details.  
> 2097│  
> 2098█    horizOn : bool, default: False  
> 2099│        Whether to draw the horizontal line.  
> 2100│  
> 2101█    vertOn : bool, default: True  
> 2102│        Whether to draw the vertical line.  
> 2103│  
> 2104│    Other Parameters  
> 2105│    ----------------  
> 2106█    **lineprops  
> 2107│        `.Line2D` properties that control the appearance of the lines.  
> 2108│        See also `~.Axes.axhline`.  
> 2109│  
> ...⋮...  
> 2113│    """  
> 2114│  
> 2115│    @_api.make_keyword_only("3.6", "useblit")  
> 2116│    def __init__(self, canvas, axes, useblit=True, horizOn=False, vertOn=True,  
> 2117│                 **lineprops):  
> 2118│        # canvas is stored only to provide the deprecated .canvas attribute;  
> 2119│        # once it goes away the unused argument won't need to be stored at all.  
> 2120│        self._canvas = canvas  
> 2121│  
> 2122│        self.axes = axes  
> ...⋮...  
> 2152│    needclear = _api.deprecated("3.7")(lambda self: False)  
> 2153│  
> 2154│    def connect(self):  
> 2155█        """Connect events."""  
> 2156│        for canvas, info in self._canvas_infos.items():  
> 2157│            info["cids"] = [  
> 2158│                canvas.mpl_connect('motion_notify_event', self.onmove),  
> 2159│                canvas.mpl_connect('draw_event', self.clear),  
> 2160│            ]  
> 2161│  
> 2162│    def disconnect(self):  
> 2163█        """Disconnect events."""  
> 2164│        for canvas, info in self._canvas_infos.items():  
> 2165│            for cid in info["cids"]:  
> 2166│                canvas.mpl_disconnect(cid)  
> 2167│            info["cids"].clear()  
> 2168│  
> 2169│    def clear(self, event):  
> ...⋮...  
> 2257│        """  
> 2258│        Convenience method to get all animated artists of the figure containing  
> 2259│        this widget, excluding those already present in self.artists.  
> 2260█        The returned tuple is not sorted by 'z_order': z_order sorting is  
> 2261█        valid only when considering all artists and not only a subset of all  
> 2262█        artists.  
> 2263│        """  
> 2264│        return tuple(a for ax_ in self.ax.get_figure().get_axes()  
> 2265│                     for a in ax_.get_children()  
> ...⋮...  
> 2269│        """Force an update of the background."""  
> 2270│        # If you add a call to `ignore` here, you'll want to check edge case:  
> 2271│        # `release` can call a draw event even when `ignore` is True.  
> 2272│        if not self.useblit:  
> 2273│            return  
> 2274│        # Make sure that widget artists don't get accidentally included in the  
> 2275│        # background, by re-rendering the background if needed (and then  
> 2276│        # re-re-rendering the canvas with the visible widget artists).  
> 2277│        # We need to remove all artists which will be drawn when updating  
> 2278│        # the selector: if we have animated artists in the figure, it is safer  
> ...⋮...  
> 2292│                self.ax.draw_artist(artist)  
> 2293│  
> 2294│    def connect_default_events(self):  
> 2295█        """Connect the major canvas events to methods."""  
> 2296│        self.connect_event('motion_notify_event', self.onmove)  
> 2297│        self.connect_event('button_press_event', self.press)  
> 2298│        self.connect_event('button_release_event', self.release)  
> 2299│        self.connect_event('draw_event', self.update_background)  
> 2300│        self.connect_event('key_press_event', self.on_key_press)  
> 2301│        self.connect_event('key_release_event', self.on_key_release)  
> 2302│        self.connect_event('scroll_event', self.on_scroll)  
> 2303│  
> 2304│    def ignore(self, event):  
> ...⋮...  
> 2327│                event.button != self._eventpress.button)  
> 2328│  
> 2329│    def update(self):  
> 2330█        """Draw using blit() or draw_idle(), depending on ``self.useblit``."""  
> 2331│        if (not self.ax.get_visible() or  
> 2332│                self.ax.figure._get_renderer() is None):  
> 2333│            return  
> 2334│        if self.useblit:  
> 2335│            if self.background is not None:  
> 2336│                self.canvas.restore_region(self.background)  
> 2337│            else:  
> 2338│                self.update_background(None)  
> 2339│            # We need to draw all artists, which are not included in the  
> ...⋮...  
> 2348│            self.canvas.draw_idle()  
> 2349│  
> 2350│    def _get_data(self, event):  
> 2351█        """Get the xdata and ydata for event, with limits."""  
> 2352│        if event.xdata is None:  
> 2353│            return None, None  
> 2354│        xdata = np.clip(event.xdata, *self.ax.get_xbound())  
> 2355│        ydata = np.clip(event.ydata, *self.ax.get_ybound())  
> 2356│        return xdata, ydata  
> 2357│  
> 2358│    def _clean_event(self, event):  
> 2359│        """  
> 2360█        Preprocess an event:  
> 2361│  
> 2362█        - Replace *event* by the previous event if *event* has no ``xdata``.  
> 2363█        - Clip ``xdata`` and ``ydata`` to the axes limits.  
> 2364█        - Update the previous event.  
> 2365│        """  
> 2366│        if event.xdata is None:  
> 2367│            event = self._prev_event  
> 2368│        else:  
> 2369│            event = copy.copy(event)  
> 2370│        event.xdata, event.ydata = self._get_data(event)  
> 2371│        self._prev_event = event  
> 2372│        return event  
> 2373│  
> 2374│    def press(self, event):  
> 2375█        """Button press handler and validator."""  
> 2376│        if not self.ignore(event):  
> 2377│            event = self._clean_event(event)  
> 2378│            self._eventpress = event  
> 2379│            self._prev_event = event  
> 2380│            key = event.key or ''  
> 2381│            key = key.replace('ctrl', 'control')  
> 2382│            # move state is locked in on a button press  
> 2383│            if key == self._state_modifier_keys['move']:  
> 2384│                self._state.add('move')  
> ...⋮...  
> 2387│        return False  
> 2388│  
> 2389│    def _press(self, event):  
> 2390█        """Button press event handler."""  
> 2391│  
> 2392│    def release(self, event):  
> 2393█        """Button release event handler and validator."""  
> 2394│        if not self.ignore(event) and self._eventpress:  
> 2395│            event = self._clean_event(event)  
> 2396│            self._eventrelease = event  
> 2397│            self._release(event)  
> 2398│            self._eventpress = None  
> 2399│            self._eventrelease = None  
> 2400│            self._state.discard('move')  
> 2401│            return True  
> 2402│        return False  
> 2403│  
> 2404│    def _release(self, event):  
> 2405█        """Button release event handler."""  
> 2406│  
> 2407│    def onmove(self, event):  
> 2408█        """Cursor move event handler and validator."""  
> 2409│        if not self.ignore(event) and self._eventpress:  
> 2410│            event = self._clean_event(event)  
> 2411│            self._onmove(event)  
> 2412│            return True  
> 2413│        return False  
> 2414│  
> 2415│    def _onmove(self, event):  
> 2416│        """Cursor move event handler."""  
> 2417│  
> 2418│    def on_scroll(self, event):  
> 2419█        """Mouse scroll event handler and validator."""  
> 2420│        if not self.ignore(event):  
> 2421│            self._on_scroll(event)  
> 2422│  
> 2423│    def _on_scroll(self, event):  
> 2424│        """Mouse scroll event handler."""  
> 2425│  
> 2426│    def on_key_press(self, event):  
> 2427█        """Key press event handler and validator for all selection widgets."""  
> 2428│        if self.active:  
> 2429│            key = event.key or ''  
> 2430│            key = key.replace('ctrl', 'control')  
> 2431│            if key == self._state_modifier_keys['clear']:  
> 2432│                self.clear()  
> 2433│                return  
> 2434│            for (state, modifier) in self._state_modifier_keys.items():  
> 2435│                if modifier in key.split('+'):  
> 2436│                    # 'rotate' is changing _state on press and is not removed  
> ...⋮...  
> 2445│            self._on_key_press(event)  
> 2446│  
> 2447│    def _on_key_press(self, event):  
> 2448█        """Key press event handler - for widget-specific key press actions."""  
> 2449│  
> 2450│    def on_key_release(self, event):  
> 2451█        """Key release event handler and validator."""  
> 2452│        if self.active:  
> 2453│            key = event.key or ''  
> 2454│            for (state, modifier) in self._state_modifier_keys.items():  
> 2455│                # 'rotate' is changing _state on press and is not removed  
> 2456│                # from _state when releasing  
> 2457│                if modifier in key.split('+') and state != 'rotate':  
> 2458│                    self._state.discard(state)  
> 2459│            self._on_key_release(event)  
> 2460│  
> 2461│    def _on_key_release(self, event):  
> 2462█        """Key release event handler."""  
> 2463│  
> 2464│    def set_visible(self, visible):  
> 2465│        """Set the visibility of the selector artists."""  
> ...⋮...  
> 2471│        """Get the visibility of the selector artists."""  
> 2472│        return self._visible  
> 2473│  
> 2474│    @property  
> 2475│    def visible(self):  
> 2476│        return self.get_visible()  
> 2477│  
> 2478│    @visible.setter  
> 2479│    def visible(self, visible):  
> 2480│        _api.warn_deprecated("3.6", alternative="set_visible")  
> 2481│        self.set_visible(visible)  
> 2482│  
> 2483│    def clear(self):  
> 2484█        """Clear the selection and set the selector ready to make a new one."""  
> 2485│        self._clear_without_update()  
> 2486│        self.update()  
> 2487│  
> 2488│    def _clear_without_update(self):  
> 2489│        self._selection_completed = False  
> 2490│        self.set_visible(False)  
> 2491│  
> 2492│    @property  
> 2493│    def artists(self):  
> 2494█        """Tuple of the artists of the selector."""  
> 2495│        handles_artists = getattr(self, '_handles_artists', ())  
> 2496│        return (self._selection_artist,) + handles_artists  
> 2497│  
> 2498│    def set_props(self, **props):  
> 2499│        """  
> 2500│        Set the properties of the selector artist. See the `props` argument  
> 2501█        in the selector docstring to know which properties are supported.  
> 2502│        """  
> 2503│        artist = self._selection_artist  
> 2504│        props = cbook.normalize_kwargs(props, artist)  
> 2505│        artist.set(**props)  
> 2506│        if self.useblit:  
> 2507│            self.update()  
> 2508│        self._props.update(props)  
> 2509│  
> 2510│    def set_handle_props(self, **handle_props):  
> 2511│        """  
> 2512█        Set the properties of the handles selector artist. See the  
> 2513█        `handle_props` argument in the selector docstring to know which  
> 2514│        properties are supported.  
> 2515│        """  
> 2516│        if not hasattr(self, '_handles_artists'):  
> 2517│            raise NotImplementedError("This selector doesn't have handles.")  
> 2518│  
> 2519│        artist = self._handles_artists[0]  
> 2520│        handle_props = cbook.normalize_kwargs(handle_props, artist)  
> 2521│        for handle in self._handles_artists:  
> 2522│            handle.set(**handle_props)  
> 2523│        if self.useblit:  
> 2524│            self.update()  
> ...⋮...  
> 2533│  
> 2534│    def add_state(self, state):  
> 2535│        """  
> 2536█        Add a state to define the widget's behavior. See the  
> 2537│        `state_modifier_keys` parameters for details.  
> 2538│  
> 2539│        Parameters  
> ...⋮...  
> 2545│        Raises  
> 2546│        ------  
> 2547│        ValueError  
> 2548█            When the state is not supported by the selector.  
> 2549│  
> 2550│        """  
> 2551│        self._validate_state(state)  
> ...⋮...  
> 2565│        Raises  
> 2566│        ------  
> 2567│        ValueError  
> 2568█            When the state is not supported by the selector.  
> 2569│  
> 2570│        """  
> 2571│        self._validate_state(state)  
> ...⋮...  
> 2574│  
> 2575│class SpanSelector(_SelectorWidget):  
> 2576│    """  
> 2577█    Visually select a min/max range on a single axis and call a function with  
> 2578│    those values.  
> 2579│  
> 2580│    To guarantee that the selector remains responsive, keep a reference to it.  
> 2581│  
> 2582│    In order to turn off the SpanSelector, set ``span_selector.active`` to  
> 2583│    False.  To turn it back on, set it to True.  
> 2584│  
> 2585█    Press and release events triggered at the same coordinates outside the  
> 2586│    selection will clear the selector, except when  
> 2587│    ``ignore_event_outside=True``.  
> 2588│  
> ...⋮...  
> 2591│    ax : `matplotlib.axes.Axes`  
> 2592│  
> 2593│    onselect : callable  
> 2594█        A callback function that is called after a release event and the  
> 2595█        selection is created, changed or removed.  
> 2596│        It must have the signature::  
> 2597│  
> 2598█            def on_select(min: float, max: float) -> Any  
> 2599│  
> 2600│    direction : {"horizontal", "vertical"}  
> 2601│        The direction along which to draw the span selector.  
> 2602│  
> 2603│    minspan : float, default: 0  
> 2604█        If selection is less than or equal to *minspan*, the selection is  
> 2605█        removed (when already existing) or cancelled.  
> 2606│  
> 2607│    useblit : bool, default: False  
> 2608█        If True, use the backend-dependent blitting features for faster  
> 2609│        canvas updates. See the tutorial :doc:`/tutorials/advanced/blitting`  
> 2610│        for details.  
> 2611│  
> ...⋮...  
> 2615│  
> 2616│            ``dict(facecolor='red', alpha=0.5)``  
> 2617│  
> 2618█    onmove_callback : func(min, max), min/max are floats, default: None  
> 2619█        Called on mouse move while the span is being selected.  
> 2620│  
> 2621│    span_stays : bool, default: False  
> 2622│        If True, the span stays visible after the mouse is released.  
> ...⋮...  
> 2626│        Whether to draw a set of handles that allow interaction with the  
> 2627│        widget after it is drawn.  
> 2628│  
> 2629█    button : `.MouseButton` or list of `.MouseButton`, default: all buttons  
> 2630│        The mouse buttons which activate the span selector.  
> 2631│  
> 2632│    handle_props : dict, default: None  
> 2633│        Properties of the handle lines at the edges of the span. Only used  
> 2634█        when *interactive* is True. See `matplotlib.lines.Line2D` for valid  
> 2635│        properties.  
> 2636│  
> 2637│    grab_range : float, default: 10  
> 2638█        Distance in pixels within which the interactive tool handles can be  
> 2639│        activated.  
> 2640│  
> 2641│    state_modifier_keys : dict, optional  
> 2642│        Keyboard modifiers which affect the widget's behavior.  Values  
> 2643█        amend the defaults, which are:  
> 2644│  
> 2645│        - "clear": Clear the current shape, default: "escape".  
> 2646│  
> ...⋮...  
> 2656│        Snap the selector edges to the given values.  
> 2657│  
> 2658│    Examples  
> 2659│    --------  
> 2660█    >>> import matplotlib.pyplot as plt  
> 2661█    >>> import matplotlib.widgets as mwidgets  
> 2662█    >>> fig, ax = plt.subplots()  
> 2663█    >>> ax.plot([1, 2, 3], [10, 50, 100])  
> 2664█    >>> def onselect(vmin, vmax):  
> 2665│    ...     print(vmin, vmax)  
> 2666█    >>> span = mwidgets.SpanSelector(ax, onselect, 'horizontal',  
> 2667█    ...                              props=dict(facecolor='blue', alpha=0.5))  
> 2668█    >>> fig.show()  
> 2669│  
> 2670│    See also: :doc:`/gallery/widgets/span_selector`  
> 2671│    """  
> 2672│  
> 2673│    @_api.make_keyword_only("3.7", name="minspan")  
> 2674│    def __init__(self, ax, onselect, direction, minspan=0, useblit=False,  
> 2675│                 props=None, onmove_callback=None, interactive=False,  
> 2676│                 button=None, handle_props=None, grab_range=10,  
> 2677│                 state_modifier_keys=None, drag_from_anywhere=False,  
> 2678│                 ignore_event_outside=False, snap_values=None):  
> 2679│  
> 2680│        if state_modifier_keys is None:  
> ...⋮...  
> 2727│        self._prev = (0, 0)  
> 2728│  
> 2729│    def new_axes(self, ax):  
> 2730█        """Set SpanSelector to operate on a new Axes."""  
> 2731│        self.ax = ax  
> 2732│        if self.canvas is not ax.figure.canvas:  
> 2733│            if self.canvas is not None:  
> 2734│                self.disconnect_events()  
> 2735│  
> 2736│            self.canvas = ax.figure.canvas  
> 2737│            self.connect_default_events()  
> 2738│  
> 2739│        # Reset  
> ...⋮...  
> 2772│            return ()  
> 2773│  
> 2774│    def _set_cursor(self, enabled):  
> 2775█        """Update the canvas cursor based on direction of the selector."""  
> 2776│        if enabled:  
> 2777│            cursor = (backend_tools.Cursors.RESIZE_HORIZONTAL  
> 2778│                      if self.direction == 'horizontal' else  
> 2779│                      backend_tools.Cursors.RESIZE_VERTICAL)  
> 2780│        else:  
> 2781│            cursor = backend_tools.Cursors.POINTER  
> 2782│  
> 2783│        self.ax.figure.canvas.set_cursor(cursor)  
> 2784│  
> ...⋮...  
> 2789│            self.connect_event('motion_notify_event', self._hover)  
> 2790│  
> 2791│    def _press(self, event):  
> 2792█        """Button press event handler."""  
> 2793│        self._set_cursor(True)  
> 2794│        if self._interactive and self._selection_artist.get_visible():  
> 2795│            self._set_active_handle(event)  
> 2796│        else:  
> 2797│            self._active_handle = None  
> 2798│  
> 2799│        if self._active_handle is None or not self._interactive:  
> 2800│            # Clear previous rectangle before drawing new rectangle.  
> 2801│            self.update()  
> 2802│  
> ...⋮...  
> 2822│  
> 2823│    @property  
> 2824│    def direction(self):  
> 2825█        """Direction of the span selector: 'vertical' or 'horizontal'."""  
> 2826│        return self._direction  
> 2827│  
> 2828│    @direction.setter  
> 2829│    def direction(self, direction):  
> 2830│        """Set the direction of the span selector."""  
> 2831│        _api.check_in_list(['horizontal', 'vertical'], direction=direction)  
> 2832│        if hasattr(self, '_direction') and direction != self._direction:  
> 2833│            # remove previous artists  
> 2834│            self._selection_artist.remove()  
> 2835│            if self._interactive:  
> 2836│                self._edge_handles.remove()  
> 2837│            self._direction = direction  
> 2838│            self.new_axes(self.ax)  
> 2839│            if self._interactive:  
> ...⋮...  
> 2842│            self._direction = direction  
> 2843│  
> 2844│    def _release(self, event):  
> 2845█        """Button release event handler."""  
> 2846│        self._set_cursor(False)  
> 2847│        # self._pressv is deprecated but we still need to maintain it  
> 2848│        self._pressv = None  
> 2849│  
> 2850│        if not self._interactive:  
> 2851│            self._selection_artist.set_visible(False)  
> 2852│  
> 2853│        if (self._active_handle is None and self._selection_completed and  
> 2854│                self.ignore_event_outside):  
> ...⋮...  
> 2875│        return False  
> 2876│  
> 2877│    def _hover(self, event):  
> 2878█        """Update the canvas cursor if it's over a handle."""  
> 2879│        if self.ignore(event):  
> 2880│            return  
> 2881│  
> 2882│        if self._active_handle is not None or not self._selection_completed:  
> 2883│            # Do nothing if button is pressed and a handle is active, which may  
> 2884│            # occur with drag_from_anywhere=True.  
> 2885│            # Do nothing if selection is not completed, which occurs when  
> 2886│            # a selector has been cleared  
> 2887│            return  
> 2888│  
> ...⋮...  
> 2890│        self._set_cursor(e_dist <= self.grab_range)  
> 2891│  
> 2892│    def _onmove(self, event):  
> 2893█        """Motion notify event handler."""  
> 2894│  
> 2895│        # self._prev are deprecated but we still need to maintain it  
> 2896│        self._prev = self._get_data(event)  
> 2897│  
> 2898│        v = event.xdata if self.direction == 'horizontal' else event.ydata  
> 2899│        if self.direction == 'horizontal':  
> 2900│            vpress = self._eventpress.xdata  
> 2901│        else:  
> 2902│            vpress = self._eventpress.ydata  
> 2903│  
> ...⋮...  
> 2945│            self._selection_artist.set_height(vmax - vmin)  
> 2946│  
> 2947│    def _set_active_handle(self, event):  
> 2948█        """Set active handle based on the location of the mouse event."""  
> 2949│        # Note: event.xdata/ydata in data coordinates, event.x/y in pixels  
> 2950│        e_idx, e_dist = self._edge_handles.closest(event.x, event.y)  
> 2951│  
> 2952│        # Prioritise center handle over other handles  
> 2953│        # Use 'C' to match the notation used in the RectangleSelector  
> 2954│        if 'move' in self._state:  
> 2955│            self._active_handle = 'C'  
> 2956│        elif e_dist > self.grab_range:  
> 2957│            # Not close to any handles  
> ...⋮...  
> 2971│        self._extents_on_press = self.extents  
> 2972│  
> 2973│    def _contains(self, event):  
> 2974█        """Return True if event is within the patch."""  
> 2975│        return self._selection_artist.contains(event, radius=0)[0]  
> 2976│  
> 2977│    @staticmethod  
> 2978│    def _snap(values, snap_values):  
> 2979│        """Snap values to a given array values (snap_values)."""  
> 2980│        # take into account machine precision  
> 2981│        eps = np.min(np.abs(np.diff(snap_values))) * 1e-12  
> 2982│        return tuple(  
> 2983│            snap_values[np.abs(snap_values - v + np.sign(v) * eps).argmin()]  
> 2984│            for v in values)  
> 2985│  
> 2986│    @property  
> 2987│    def extents(self):  
> 2988█        """Return extents of the span selector."""  
> 2989│        if self.direction == 'horizontal':  
> 2990│            vmin = self._selection_artist.get_x()  
> 2991│            vmax = vmin + self._selection_artist.get_width()  
> 2992│        else:  
> 2993│            vmin = self._selection_artist.get_y()  
> 2994│            vmax = vmin + self._selection_artist.get_height()  
> 2995│        return vmin, vmax  
> 2996│  
> 2997│    @extents.setter  
> ...⋮...  
> 3009│  
> 3010│class ToolLineHandles:  
> 3011│    """  
> 3012█    Control handles for canvas tools.  
> 3013│  
> 3014│    Parameters  
> 3015│    ----------  
> 3016│    ax : `matplotlib.axes.Axes`  
> 3017│        Matplotlib Axes where tool handles are displayed.  
> 3018│    positions : 1D array  
> 3019█        Positions of handles in data coordinates.  
> 3020│    direction : {"horizontal", "vertical"}  
> 3021█        Direction of handles, either 'vertical' or 'horizontal'  
> 3022│    line_props : dict, optional  
> 3023│        Additional line properties. See `matplotlib.lines.Line2D`.  
> 3024│    useblit : bool, default: True  
> 3025█        Whether to use blitting for faster drawing (if supported by the  
> 3026│        backend). See the tutorial :doc:`/tutorials/advanced/blitting`  
> 3027│        for details.  
> 3028│    """  
> 3029│  
> 3030│    @_api.make_keyword_only("3.7", "line_props")  
> 3031│    def __init__(self, ax, positions, direction, line_props=None,  
> 3032│                 useblit=True):  
> 3033│        self.ax = ax  
> 3034│  
> 3035│        _api.check_in_list(['horizontal', 'vertical'], direction=direction)  
> 3036│        self._direction = direction  
> 3037│  
> ...⋮...  
> 3051│  
> 3052│    @property  
> 3053│    def positions(self):  
> 3054█        """Positions of the handle in data coordinates."""  
> 3055│        method = 'get_xdata' if self.direction == 'horizontal' else 'get_ydata'  
> 3056│        return [getattr(line, method)()[0] for line in self.artists]  
> 3057│  
> 3058│    @property  
> 3059│    def direction(self):  
> 3060█        """Direction of the handle: 'vertical' or 'horizontal'."""  
> 3061│        return self._direction  
> 3062│  
> 3063│    def set_data(self, positions):  
> 3064│        """  
> 3065█        Set x- or y-positions of handles, depending on if the lines are  
> 3066│        vertical or horizontal.  
> 3067│  
> 3068│        Parameters  
> 3069│        ----------  
> 3070│        positions : tuple of length 2  
> 3071█            Set the positions of the handle in data coordinates  
> 3072│        """  
> 3073│        method = 'set_xdata' if self.direction == 'horizontal' else 'set_ydata'  
> 3074│        for line, p in zip(self.artists, positions):  
> 3075│            getattr(line, method)([p, p])  
> 3076│  
> 3077│    def set_visible(self, value):  
> 3078│        """Set the visibility state of the handles artist."""  
> 3079│        for artist in self.artists:  
> 3080│            artist.set_visible(value)  
> 3081│  
> ...⋮...  
> 3091│  
> 3092│    def closest(self, x, y):  
> 3093│        """  
> 3094█        Return index and pixel distance to closest handle.  
> 3095│  
> 3096│        Parameters  
> 3097│        ----------  
> 3098█        x, y : float  
> 3099│            x, y position from which the distance will be calculated to  
> 3100│            determinate the closest handle  
> 3101│  
> 3102│        Returns  
> 3103│        -------  
> 3104█        index, distance : index of the handle and its distance from  
> 3105│            position x, y  
> 3106│        """  
> 3107│        if self.direction == 'horizontal':  
> 3108│            p_pts = np.array([  
> 3109│                self.ax.transData.transform((p, 0))[0] for p in self.positions  
> 3110│                ])  
> 3111│            dist = abs(p_pts - x)  
> 3112│        else:  
> 3113│            p_pts = np.array([  
> 3114│                self.ax.transData.transform((0, p))[1] for p in self.positions  
> 3115│                ])  
> ...⋮...  
> 3119│  
> 3120│  
> 3121│class ToolHandles:  
> 3122█    """  
> 3123│    Control handles for canvas tools.  
> 3124│  
> 3125│    Parameters  
> ...⋮...  
> 3133│    marker_props : dict, optional  
> 3134│        Additional marker properties. See `matplotlib.lines.Line2D`.  
> 3135│    useblit : bool, default: True  
> 3136█        Whether to use blitting for faster drawing (if supported by the  
> 3137│        backend). See the tutorial :doc:`/tutorials/advanced/blitting`  
> 3138│        for details.  
> 3139│    """  
> 3140│  
> 3141│    @_api.make_keyword_only("3.7", "marker")  
> 3142│    def __init__(self, ax, x, y, marker='o', marker_props=None, useblit=True):  
> 3143│        self.ax = ax  
> 3144│        props = {'marker': marker, 'markersize': 7, 'markerfacecolor': 'w',  
> 3145│                 'linestyle': 'none', 'alpha': 0.5, 'visible': False,  
> 3146│                 'label': '_nolegend_',  
> 3147│                 **cbook.normalize_kwargs(marker_props, Line2D._alias_map)}  
> 3148│        self._markers = Line2D(x, y, animated=useblit, **props)  
> ...⋮...  
> 3161│        return (self._markers, )  
> 3162│  
> 3163│    def set_data(self, pts, y=None):  
> 3164█        """Set x and y positions of handles."""  
> 3165│        if y is not None:  
> 3166│            x = pts  
> 3167│            pts = np.array([x, y])  
> 3168│        self._markers.set_data(pts)  
> 3169│  
> 3170│    def set_visible(self, val):  
> 3171│        self._markers.set_visible(val)  
> 3172│  
> 3173│    def set_animated(self, val):  
> 3174│        self._markers.set_animated(val)  
> 3175│  
> 3176│    def closest(self, x, y):  
> 3177█        """Return index and pixel distance to closest index."""  
> 3178│        pts = np.column_stack([self.x, self.y])  
> 3179│        # Transform data coordinates to pixel coordinates.  
> 3180│        pts = self.ax.transData.transform(pts)  
> 3181│        diff = pts - [x, y]  
> 3182│        dist = np.hypot(*diff.T)  
> 3183│        min_index = np.argmin(dist)  
> 3184│        return min_index, dist[min_index]  
> 3185│  
> 3186│  
> 3187│_RECTANGLESELECTOR_PARAMETERS_DOCSTRING = \  
> 3188│    r"""  
> 3189█    Parameters  
> 3190│    ----------  
> 3191│    ax : `~matplotlib.axes.Axes`  
> 3192│        The parent axes for the widget.  
> 3193│  
> 3194│    onselect : function  
> 3195█        A callback function that is called after a release event and the  
> 3196█        selection is created, changed or removed.  
> 3197│        It must have the signature::  
> 3198│  
> 3199█            def onselect(eclick: MouseEvent, erelease: MouseEvent)  
> 3200│  
> 3201█        where *eclick* and *erelease* are the mouse click and release  
> 3202█        `.MouseEvent`\s that start and complete the selection.  
> 3203│  
> 3204│    minspanx : float, default: 0  
> 3205█        Selections with an x-span less than or equal to *minspanx* are removed  
> 3206█        (when already existing) or cancelled.  
> 3207│  
> 3208│    minspany : float, default: 0  
> 3209█        Selections with an y-span less than or equal to *minspanx* are removed  
> 3210█        (when already existing) or cancelled.  
> 3211│  
> 3212│    useblit : bool, default: False  
> 3213█        Whether to use blitting for faster drawing (if supported by the  
> 3214│        backend). See the tutorial :doc:`/tutorials/advanced/blitting`  
> 3215│        for details.  
> 3216│  
> 3217│    props : dict, optional  
> 3218█        Properties with which the __ARTIST_NAME__ is drawn. See  
> 3219│        `matplotlib.patches.Patch` for valid properties.  
> 3220│        Default:  
> 3221│  
> 3222│        ``dict(facecolor='red', edgecolor='black', alpha=0.2, fill=True)``  
> 3223│  
> 3224│    spancoords : {"data", "pixels"}, default: "data"  
> 3225█        Whether to interpret *minspanx* and *minspany* in data or in pixel  
> 3226│        coordinates.  
> 3227│  
> 3228│    button : `.MouseButton`, list of `.MouseButton`, default: all buttons  
> 3229│        Button(s) that trigger rectangle selection.  
> 3230│  
> 3231│    grab_range : float, default: 10  
> 3232█        Distance in pixels within which the interactive tool handles can be  
> 3233│        activated.  
> 3234│  
> 3235│    handle_props : dict, optional  
> 3236█        Properties with which the interactive handles (marker artists) are  
> 3237█        drawn. See the marker arguments in `matplotlib.lines.Line2D` for valid  
> 3238█        properties.  Default values are defined in ``mpl.rcParams`` except for  
> 3239█        the default value of ``markeredgecolor`` which will be the same as the  
> 3240█        ``edgecolor`` property in *props*.  
> 3241│  
> 3242│    interactive : bool, default: False  
> 3243│        Whether to draw a set of handles that allow interaction with the  
> 3244│        widget after it is drawn.  
> 3245│  
> 3246│    state_modifier_keys : dict, optional  
> 3247│        Keyboard modifiers which affect the widget's behavior.  Values  
> 3248█        amend the defaults, which are:  
> 3249│  
> 3250│        - "move": Move the existing shape, default: no modifier.  
> 3251│        - "clear": Clear the current shape, default: "escape".  
> 3252│        - "square": Make the shape square, default: "shift".  
> 3253│        - "center": change the shape around its center, default: "ctrl".  
> 3254█        - "rotate": Rotate the shape around its center between -45° and 45°,  
> 3255│          default: "r".  
> 3256│  
> 3257█        "square" and "center" can be combined. The square shape can be defined  
> 3258█        in data or display coordinates as determined by the  
> 3259█        ``use_data_coordinates`` argument specified when creating the selector.  
> 3260│  
> 3261│    drag_from_anywhere : bool, default: False  
> 3262│        If `True`, the widget can be moved by clicking anywhere within  
> ...⋮...  
> 3268│  
> 3269│    use_data_coordinates : bool, default: False  
> 3270│        If `True`, the "square" shape of the selector is defined in  
> 3271█        data coordinates instead of display coordinates.  
> 3272│    """  
> 3273│  
> 3274│  
> 3275│@_docstring.Substitution(_RECTANGLESELECTOR_PARAMETERS_DOCSTRING.replace(  
> 3276│    '__ARTIST_NAME__', 'rectangle'))  
> 3277│class RectangleSelector(_SelectorWidget):  
> 3278│    """  
> 3279│    Select a rectangular region of an Axes.  
> 3280│  
> 3281│    For the cursor to remain responsive you must keep a reference to it.  
> 3282│  
> 3283█    Press and release events triggered at the same coordinates outside the  
> 3284│    selection will clear the selector, except when  
> 3285│    ``ignore_event_outside=True``.  
> 3286│  
> 3287█    %s  
> 3288│  
> 3289│    Examples  
> 3290│    --------  
> 3291█    >>> import matplotlib.pyplot as plt  
> 3292█    >>> import matplotlib.widgets as mwidgets  
> 3293█    >>> fig, ax = plt.subplots()  
> 3294│    >>> ax.plot([1, 2, 3], [10, 50, 100])  
> 3295█    >>> def onselect(eclick, erelease):  
> 3296│    ...     print(eclick.xdata, eclick.ydata)  
> 3297█    ...     print(erelease.xdata, erelease.ydata)  
> 3298█    >>> props = dict(facecolor='blue', alpha=0.5)  
> 3299█    >>> rect = mwidgets.RectangleSelector(ax, onselect, interactive=True,  
> 3300█    ...                                   props=props)  
> 3301█    >>> fig.show()  
> 3302█    >>> rect.add_state('square')  
> 3303│  
> 3304│    See also: :doc:`/gallery/widgets/rectangle_selector`  
> 3305│    """  
> 3306│  
> 3307│    def __init__(self, ax, onselect, *, minspanx=0, minspany=0, useblit=False,  
> 3308│                 props=None, spancoords='data', button=None, grab_range=10,  
> 3309│                 handle_props=None, interactive=False,  
> 3310│                 state_modifier_keys=None, drag_from_anywhere=False,  
> 3311│                 ignore_event_outside=False, use_data_coordinates=False):  
> 3312│        super().__init__(ax, onselect, useblit=useblit, button=button,  
> 3313│                         state_modifier_keys=state_modifier_keys,  
> 3314│                         use_data_coordinates=use_data_coordinates)  
> 3315│  
> ...⋮...  
> 3380│                         rotation_point='center', **props)  
> 3381│  
> 3382│    def _press(self, event):  
> 3383█        """Button press event handler."""  
> 3384│        # make the drawn box/line visible get the click-coordinates,  
> 3385│        # button, ...  
> 3386│        if self._interactive and self._selection_artist.get_visible():  
> 3387│            self._set_active_handle(event)  
> 3388│        else:  
> 3389│            self._active_handle = None  
> 3390│  
> 3391│        if ((self._active_handle is None or not self._interactive) and  
> 3392│                self._allow_creation):  
> ...⋮...  
> 3410│        return False  
> 3411│  
> 3412│    def _release(self, event):  
> 3413█        """Button release event handler."""  
> 3414│        if not self._interactive:  
> 3415│            self._selection_artist.set_visible(False)  
> 3416│  
> 3417│        if (self._active_handle is None and self._selection_completed and  
> 3418│                self.ignore_event_outside):  
> 3419│            return  
> 3420│  
> 3421│        # update the eventpress and eventrelease with the resulting extents  
> 3422│        x0, x1, y0, y1 = self.extents  
> ...⋮...  
> 3459│  
> 3460│    def _onmove(self, event):  
> 3461│        """  
> 3462█        Motion notify event handler.  
> 3463│  
> 3464█        This can do one of four things:  
> 3465│        - Translate  
> 3466│        - Rotate  
> 3467│        - Re-size  
> 3468█        - Continue the creation of a new shape  
> 3469│        """  
> 3470│        eventpress = self._eventpress  
> 3471│        # The calculations are done for rotation at zero: we apply inverse  
> ...⋮...  
> 3627│    @property  
> 3628│    def corners(self):  
> 3629│        """  
> 3630█        Corners of rectangle in data coordinates from lower left,  
> 3631│        moving clockwise.  
> 3632│        """  
> 3633│        x0, y0, width, height = self._rect_bbox  
> ...⋮...  
> 3640│    @property  
> 3641│    def edge_centers(self):  
> 3642│        """  
> 3643█        Midpoint of rectangle edges in data coordinates from left,  
> 3644█        moving anti-clockwise.  
> 3645│        """  
> 3646│        x0, y0, width, height = self._rect_bbox  
> 3647│        w = width / 2.  
> 3648│        h = height / 2.  
> 3649│        xe = x0, x0 + w, x0 + width, x0 + w  
> 3650│        ye = y0 + h, y0, y0 + h, y0 + height  
> 3651│        transform = self._get_rotation_transform()  
> 3652│        coords = transform.transform(np.array([xe, ye]).T).T  
> 3653│        return coords[0], coords[1]  
> 3654│  
> 3655│    @property  
> 3656│    def center(self):  
> 3657█        """Center of rectangle in data coordinates."""  
> 3658│        x0, y0, width, height = self._rect_bbox  
> 3659│        return x0 + width / 2., y0 + height / 2.  
> 3660│  
> 3661│    @property  
> 3662│    def extents(self):  
> 3663│        """  
> 3664█        Return (xmin, xmax, ymin, ymax) in data coordinates as defined by the  
> 3665│        bounding box before rotation.  
> 3666│        """  
> 3667│        x0, y0, width, height = self._rect_bbox  
> 3668│        xmin, xmax = sorted([x0, x0 + width])  
> 3669│        ymin, ymax = sorted([y0, y0 + height])  
> 3670│        return xmin, xmax, ymin, ymax  
> 3671│  
> 3672│    @extents.setter  
> 3673│    def extents(self, extents):  
> 3674│        # Update displayed shape  
> 3675│        self._draw_shape(extents)  
> ...⋮...  
> 3685│    @property  
> 3686│    def rotation(self):  
> 3687│        """  
> 3688█        Rotation in degree in interval [-45°, 45°]. The rotation is limited in  
> 3689█        range to keep the implementation simple.  
> 3690│        """  
> 3691│        return np.rad2deg(self._rotation)  
> 3692│  
> 3693│    @rotation.setter  
> 3694│    def rotation(self, value):  
> 3695│        # Restrict to a limited range of rotation [-45°, 45°] to avoid changing  
> 3696│        # order of handles  
> 3697│        if -45 <= value and value <= 45:  
> 3698│            self._rotation = np.deg2rad(value)  
> 3699│            # call extents setter to draw shape and update handles positions  
> ...⋮...  
> 3718│        self._selection_artist.set_angle(self.rotation)  
> 3719│  
> 3720│    def _set_active_handle(self, event):  
> 3721█        """Set active handle based on the location of the mouse event."""  
> 3722│        # Note: event.xdata/ydata in data coordinates, event.x/y in pixels  
> 3723│        c_idx, c_dist = self._corner_handles.closest(event.x, event.y)  
> 3724│        e_idx, e_dist = self._edge_handles.closest(event.x, event.y)  
> 3725│        m_idx, m_dist = self._center_handle.closest(event.x, event.y)  
> 3726│  
> 3727│        if 'move' in self._state:  
> 3728│            self._active_handle = 'C'  
> 3729│        # Set active handle as closest handle, if mouse click is close enough.  
> 3730│        elif m_dist < self.grab_range * 2:  
> ...⋮...  
> 3746│            self._active_handle = self._edge_order[e_idx]  
> 3747│  
> 3748│    def _contains(self, event):  
> 3749█        """Return True if event is within the patch."""  
> 3750│        return self._selection_artist.contains(event, radius=0)[0]  
> 3751│  
> 3752│    @property  
> 3753│    def geometry(self):  
> 3754│        """  
> 3755│        Return an array of shape (2, 5) containing the  
> 3756█        x (``RectangleSelector.geometry[1, :]``) and  
> 3757█        y (``RectangleSelector.geometry[0, :]``) data coordinates of the four  
> 3758█        corners of the rectangle starting and ending in the top left corner.  
> 3759│        """  
> 3760│        if hasattr(self._selection_artist, 'get_verts'):  
> 3761│            xfm = self.ax.transData.inverted()  
> 3762│            y, x = xfm.transform(self._selection_artist.get_verts()).T  
> 3763│            return np.array([x, y])  
> 3764│        else:  
> 3765│            return np.array(self._selection_artist.get_data())  
> 3766│  
> 3767│  
> 3768│@_docstring.Substitution(_RECTANGLESELECTOR_PARAMETERS_DOCSTRING.replace(  
> 3769│    '__ARTIST_NAME__', 'ellipse'))  
> 3770│class EllipseSelector(RectangleSelector):  
> 3771█    """  
> 3772│    Select an elliptical region of an Axes.  
> 3773│  
> 3774█    For the cursor to remain responsive you must keep a reference to it.  
> 3775│  
> 3776█    Press and release events triggered at the same coordinates outside the  
> 3777│    selection will clear the selector, except when  
> 3778│    ``ignore_event_outside=True``.  
> 3779│  
> 3780█    %s  
> 3781│  
> 3782│    Examples  
> 3783│    --------  
> 3784█    :doc:`/gallery/widgets/rectangle_selector`  
> 3785│    """  
> 3786│    def _init_shape(self, **props):  
> 3787│        return Ellipse((0, 0), 0, 1, visible=False, **props)  
> 3788│  
> 3789│    def _draw_shape(self, extents):  
> 3790│        x0, x1, y0, y1 = extents  
> 3791│        xmin, xmax = sorted([x0, x1])  
> 3792│        ymin, ymax = sorted([y0, y1])  
> 3793│        center = [x0 + (x1 - x0) / 2., y0 + (y1 - y0) / 2.]  
> ...⋮...  
> 3809│  
> 3810│class LassoSelector(_SelectorWidget):  
> 3811│    """  
> 3812█    Selection curve of an arbitrary shape.  
> 3813│  
> 3814█    For the selector to remain responsive you must keep a reference to it.  
> 3815│  
> 3816█    The selected path can be used in conjunction with `~.Path.contains_point`  
> 3817│    to select data points from an image.  
> 3818│  
> 3819█    In contrast to `Lasso`, `LassoSelector` is written with an interface  
> 3820█    similar to `RectangleSelector` and `SpanSelector`, and will continue to  
> 3821│    interact with the Axes until disconnected.  
> 3822│  
> 3823│    Example usage::  
> 3824│  
> ...⋮...  
> 3835│        The parent Axes for the widget.  
> 3836│    onselect : function  
> 3837│        Whenever the lasso is released, the *onselect* function is called and  
> 3838█        passed the vertices of the selected path.  
> 3839│    useblit : bool, default: True  
> 3840█        Whether to use blitting for faster drawing (if supported by the  
> 3841│        backend). See the tutorial :doc:`/tutorials/advanced/blitting`  
> 3842│        for details.  
> 3843│    props : dict, optional  
> 3844│        Properties with which the line is drawn, see `matplotlib.lines.Line2D`  
> 3845█        for valid properties. Default values are defined in ``mpl.rcParams``.  
> 3846█    button : `.MouseButton` or list of `.MouseButton`, optional  
> 3847█        The mouse buttons used for rectangle selection.  Default is ``None``,  
> 3848│        which corresponds to all buttons.  
> 3849│    """  
> 3850│  
> 3851│    @_api.make_keyword_only("3.7", name="useblit")  
> 3852│    def __init__(self, ax, onselect, useblit=True, props=None, button=None):  
> 3853│        super().__init__(ax, onselect, useblit=useblit, button=button)  
> 3854│        self.verts = None  
> 3855│        props = {  
> 3856│            **(props if props is not None else {}),  
> 3857│            # Note that self.useblit may be != useblit, if the canvas doesn't  
> 3858│            # support blitting.  
> ...⋮...  
> 3885│  
> 3886│class PolygonSelector(_SelectorWidget):  
> 3887│    """  
> 3888█    Select a polygon region of an Axes.  
> 3889│  
> 3890█    Place vertices with each mouse click, and make the selection by completing  
> 3891█    the polygon (clicking on the first vertex). Once drawn individual vertices  
> 3892█    can be moved by clicking and dragging with the left mouse button, or  
> 3893█    removed by clicking the right mouse button.  
> 3894│  
> 3895█    In addition, the following modifier keys can be used:  
> 3896│  
> 3897█    - Hold *ctrl* and click and drag a vertex to reposition it before the  
> 3898│      polygon has been completed.  
> 3899█    - Hold the *shift* key and click and drag anywhere in the Axes to move  
> 3900│      all vertices.  
> 3901█    - Press the *esc* key to start a new polygon.  
> 3902│  
> 3903│    For the selector to remain responsive you must keep a reference to it.  
> 3904│  
> ...⋮...  
> 3908│        The parent Axes for the widget.  
> 3909│  
> 3910│    onselect : function  
> 3911█        When a polygon is completed or modified after completion,  
> 3912█        the *onselect* function is called and passed a list of the vertices as  
> 3913█        ``(xdata, ydata)`` tuples.  
> 3914│  
> 3915│    useblit : bool, default: False  
> 3916█        Whether to use blitting for faster drawing (if supported by the  
> 3917│        backend). See the tutorial :doc:`/tutorials/advanced/blitting`  
> 3918│        for details.  
> 3919│  
> ...⋮...  
> 3926│  
> 3927│    handle_props : dict, optional  
> 3928│        Artist properties for the markers drawn at the vertices of the polygon.  
> 3929█        See the marker arguments in `matplotlib.lines.Line2D` for valid  
> 3930█        properties.  Default values are defined in ``mpl.rcParams`` except for  
> 3931█        the default value of ``markeredgecolor`` which will be the same as the  
> 3932█        ``color`` property in *props*.  
> 3933│  
> 3934│    grab_range : float, default: 10  
> 3935█        A vertex is selected (to complete the polygon or to move a vertex) if  
> 3936█        the mouse click is within *grab_range* pixels of the vertex.  
> 3937│  
> 3938│    draw_bounding_box : bool, optional  
> 3939│        If `True`, a bounding box will be drawn around the polygon selector  
> 3940█        once it is complete. This box can be used to move and resize the  
> 3941│        selector.  
> 3942│  
> 3943│    box_handle_props : dict, optional  
> 3944│        Properties to set for the box handles. See the documentation for the  
> 3945█        *handle_props* argument to `RectangleSelector` for more info.  
> 3946│  
> 3947│    box_props : dict, optional  
> 3948│        Properties to set for the box. See the documentation for the *props*  
> 3949█        argument to `RectangleSelector` for more info.  
> 3950│  
> 3951│    Examples  
> 3952│    --------  
> 3953█    :doc:`/gallery/widgets/polygon_selector_simple`  
> 3954│    :doc:`/gallery/widgets/polygon_selector_demo`  
> 3955│  
> 3956│    Notes  
> 3957│    -----  
> 3958█    If only one point remains after removing points, the selector reverts to an  
> 3959█    incomplete state and you can start drawing a new polygon from the existing  
> 3960│    point.  
> 3961│    """  
> 3962│  
> 3963│    @_api.make_keyword_only("3.7", name="useblit")  
> 3964│    def __init__(self, ax, onselect, useblit=False,  
> 3965│                 props=None, handle_props=None, grab_range=10, *,  
> 3966│                 draw_bounding_box=False, box_handle_props=None,  
> 3967│                 box_props=None):  
> 3968│        # The state modifiers 'move', 'square', and 'center' are expected by  
> 3969│        # _SelectorWidget but are not supported by PolygonSelector  
> 3970│        # Note: could not use the existing 'move' state modifier in-place of  
> ...⋮...  
> 4041│  
> 4042│    def _scale_polygon(self, event):  
> 4043│        """  
> 4044█        Scale the polygon selector points when the bounding box is moved or  
> 4045│        scaled.  
> 4046│  
> 4047█        This is set as a callback on the bounding box RectangleSelector.  
> 4048│        """  
> 4049│        if not self._selection_completed:  
> 4050│            return  
> 4051│  
> 4052│        if self._old_box_extents == self._box.extents:  
> 4053│            return  
> 4054│  
> 4055│        # Create transform from old box to new box  
> 4056│        x1, y1, w1, h1 = self._box._rect_bbox  
> 4057│        old_bbox = self._get_bbox()  
> ...⋮...  
> 4072│        return self._polygon_handles.artists  
> 4073│  
> 4074│    def _remove_vertex(self, i):  
> 4075█        """Remove vertex with index i."""  
> 4076│        if (len(self._xys) > 2 and  
> 4077│                self._selection_completed and  
> 4078│                i in (0, len(self._xys) - 1)):  
> 4079│            # If selecting the first or final vertex, remove both first and  
> 4080│            # last vertex as they are the same for a closed polygon  
> 4081│            self._xys.pop(0)  
> 4082│            self._xys.pop(-1)  
> 4083│            # Close the polygon again by appending the new first vertex to the  
> 4084│            # end  
> ...⋮...  
> 4092│            self._remove_box()  
> 4093│  
> 4094│    def _press(self, event):  
> 4095█        """Button press event handler."""  
> 4096│        # Check for selection of a tool handle.  
> 4097│        if ((self._selection_completed or 'move_vertex' in self._state)  
> 4098│                and len(self._xys) > 0):  
> 4099│            h_idx, h_dist = self._polygon_handles.closest(event.x, event.y)  
> 4100│            if h_dist < self.grab_range:  
> 4101│                self._active_handle_idx = h_idx  
> 4102│        # Save the vertex positions at the time of the press event (needed to  
> 4103│        # support the 'move_all' state modifier).  
> 4104│        self._xys_at_press = self._xys.copy()  
> 4105│  
> 4106│    def _release(self, event):  
> 4107█        """Button release event handler."""  
> 4108│        # Release active tool handle.  
> 4109│        if self._active_handle_idx >= 0:  
> 4110│            if event.button == 3:  
> 4111│                self._remove_vertex(self._active_handle_idx)  
> 4112│                self._draw_polygon()  
> 4113│            self._active_handle_idx = -1  
> 4114│  
> 4115│        # Complete the polygon.  
> 4116│        elif len(self._xys) > 3 and self._xys[-1] == self._xys[0]:  
> ...⋮...  
> 4128│            self.onselect(self.verts)  
> 4129│  
> 4130│    def onmove(self, event):  
> 4131█        """Cursor move event handler and validator."""  
> 4132│        # Method overrides _SelectorWidget.onmove because the polygon selector  
> 4133│        # needs to process the move callback even if there is no button press.  
> 4134│        # _SelectorWidget.onmove include logic to ignore move event if  
> 4135│        # _eventpress is None.  
> 4136│        if not self.ignore(event):  
> 4137│            event = self._clean_event(event)  
> 4138│            self._onmove(event)  
> 4139│            return True  
> 4140│        return False  
> 4141│  
> 4142│    def _onmove(self, event):  
> 4143█        """Cursor move event handler."""  
> 4144│        # Move the active vertex (ToolHandle).  
> 4145│        if self._active_handle_idx >= 0:  
> 4146│            idx = self._active_handle_idx  
> 4147│            self._xys[idx] = event.xdata, event.ydata  
> 4148│            # Also update the end of the polygon line if the first vertex is  
> 4149│            # the active handle and the polygon is completed.  
> 4150│            if idx == 0 and self._selection_completed:  
> 4151│                self._xys[-1] = event.xdata, event.ydata  
> 4152│  
> ...⋮...  
> 4178│        self._draw_polygon()  
> 4179│  
> 4180│    def _on_key_press(self, event):  
> 4181█        """Key press event handler."""  
> 4182│        # Remove the pending vertex if entering the 'move_vertex' or  
> 4183│        # 'move_all' mode  
> 4184│        if (not self._selection_completed  
> 4185│                and ('move_vertex' in self._state or  
> 4186│                     'move_all' in self._state)):  
> 4187│            self._xys.pop()  
> 4188│            self._draw_polygon()  
> 4189│  
> 4190│    def _on_key_release(self, event):  
> 4191█        """Key release event handler."""  
> 4192│        # Add back the pending vertex if leaving the 'move_vertex' or  
> 4193│        # 'move_all' mode (by checking the released key)  
> 4194│        if (not self._selection_completed  
> 4195│                and  
> 4196│                (event.key == self._state_modifier_keys.get('move_vertex')  
> 4197│                 or event.key == self._state_modifier_keys.get('move_all'))):  
> 4198│            self._xys.append((event.xdata, event.ydata))  
> 4199│            self._draw_polygon()  
> 4200│        # Reset the polygon if the released key is the 'clear' key.  
> ...⋮...  
> 4206│            self.set_visible(True)  
> 4207│  
> 4208│    def _draw_polygon(self):  
> 4209█        """Redraw the polygon based on the new vertex positions."""  
> 4210│        xs, ys = zip(*self._xys) if self._xys else ([], [])  
> 4211│        self._selection_artist.set_data(xs, ys)  
> 4212│        self._update_box()  
> 4213│        # Only show one tool handle at the start and end vertex of the polygon  
> 4214│        # if the polygon is completed or the user is locked on to the start  
> 4215│        # vertex.  
> 4216│        if (self._selection_completed  
> 4217│                or (len(self._xys) > 3  
> 4218│                    and self._xys[-1] == self._xys[0])):  
> ...⋮...  
> 4223│  
> 4224│    @property  
> 4225│    def verts(self):  
> 4226█        """The polygon vertices, as a list of ``(x, y)`` pairs."""  
> 4227│        return self._xys[:-1]  
> 4228│  
> 4229│    @verts.setter  
> 4230│    def verts(self, xys):  
> ...⋮...  
> 4236│        """  
> 4237│        self._xys = [*xys, xys[0]]  
> 4238│        self._selection_completed = True  
> 4239│        self.set_visible(True)  
> 4240│        if self._draw_box and self._box is None:  
> 4241│            self._add_box()  
> 4242│        self._draw_polygon()  
> 4243│  
> 4244│  
> 4245│class Lasso(AxesWidget):  
> 4246█    """  
> 4247│    Selection curve of an arbitrary shape.  
> 4248│  
> 4249█    The selected path can be used in conjunction with  
> 4250│    `~matplotlib.path.Path.contains_point` to select data points from an image.  
> 4251│  
> 4252█    Unlike `LassoSelector`, this must be initialized with a starting  
> 4253█    point *xy*, and the `Lasso` events are destroyed upon release.  
> 4254│  
> 4255│    Parameters  
> 4256│    ----------  
> ...⋮...  
> 4260│        Coordinates of the start of the lasso.  
> 4261│    callback : callable  
> 4262│        Whenever the lasso is released, the *callback* function is called and  
> 4263█        passed the vertices of the selected path.  
> 4264│    useblit : bool, default: True  
> 4265█        Whether to use blitting for faster drawing (if supported by the  
> 4266│        backend). See the tutorial :doc:`/tutorials/advanced/blitting`  
> 4267│        for details.  
> 4268│    """  
> 4269│  
> ...⋮...  
>  
> Attempt to fix lint errors? yes  
> Only 4 reflections allowed, stopping.  
