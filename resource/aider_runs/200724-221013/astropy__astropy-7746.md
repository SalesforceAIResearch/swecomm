
# aider chat started at 2024-07-20 19:53:13

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp3gwn6xev/.git with 1,840 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Issue when passing empty lists/arrays to WCS transformations  
#### The following should not fail but instead should return empty lists/arrays:  
####   
#### ```  
#### In [1]: from astropy.wcs import WCS  
####   
#### In [2]: wcs = WCS('2MASS_h.fits')  
####   
#### In [3]: wcs.wcs_pix2world([], [], 0)  
#### ---------------------------------------------------------------------------  
#### InconsistentAxisTypesError                Traceback (most recent call last)  
#### <ipython-input-3-e2cc0e97941a> in <module>()  
#### ----> 1 wcs.wcs_pix2world([], [], 0)  
####   
#### ~/Dropbox/Code/Astropy/astropy/astropy/wcs/wcs.py in wcs_pix2world(self, *args, **kwargs)  
####    1352         return self._array_converter(  
####    1353             lambda xy, o: self.wcs.p2s(xy, o)['world'],  
#### -> 1354             'output', *args, **kwargs)  
####    1355     wcs_pix2world.__doc__ = """  
####    1356         Transforms pixel coordinates to world coordinates by doing  
####   
#### ~/Dropbox/Code/Astropy/astropy/astropy/wcs/wcs.py in _array_converter(self, func, sky, ra_dec_order, *args)  
####    1267                     "a 1-D array for each axis, followed by an origin.")  
####    1268   
#### -> 1269             return _return_list_of_arrays(axes, origin)  
####    1270   
####    1271         raise TypeError(  
####   
#### ~/Dropbox/Code/Astropy/astropy/astropy/wcs/wcs.py in _return_list_of_arrays(axes, origin)  
####    1223             if ra_dec_order and sky == 'input':  
####    1224                 xy = self._denormalize_sky(xy)  
#### -> 1225             output = func(xy, origin)  
####    1226             if ra_dec_order and sky == 'output':  
####    1227                 output = self._normalize_sky(output)  
####   
#### ~/Dropbox/Code/Astropy/astropy/astropy/wcs/wcs.py in <lambda>(xy, o)  
####    1351             raise ValueError("No basic WCS settings were created.")  
####    1352         return self._array_converter(  
#### -> 1353             lambda xy, o: self.wcs.p2s(xy, o)['world'],  
####    1354             'output', *args, **kwargs)  
####    1355     wcs_pix2world.__doc__ = """  
####   
#### InconsistentAxisTypesError: ERROR 4 in wcsp2s() at line 2646 of file cextern/wcslib/C/wcs.c:  
#### ncoord and/or nelem inconsistent with the wcsprm.  
#### ```  
> 34302 prompt tokens, 58 completion tokens, $0.172380 cost  

To address the issue with passing empty lists/arrays to WCS transformations, we will likely need to make changes to the following file:

- `astropy/wcs/wcs.py`

Please add this file to the chat so I can provide the necessary *SEARCH/REPLACE* blocks.

> astropy/wcs/wcs.py  
> Add these files to the chat? yes  
> 33227 prompt tokens, 231 completion tokens, $0.169600 cost  

To handle empty lists/arrays in WCS transformations, we need to modify the `_array_converter` method in `astropy/wcs/wcs.py` to check for empty inputs and return empty outputs accordingly.

Here are the *SEARCH/REPLACE* blocks:

astropy/wcs/wcs.py
```python
<<<<<<< SEARCH
        if len(args) == 2:
=======
        if len(args) == 2:
            if isinstance(args[0], (list, np.ndarray)) and len(args[0]) == 0:
                return np.array([]), np.array([])
>>>>>>> REPLACE
```

astropy/wcs/wcs.py
```python
<<<<<<< SEARCH
            axes = args[:-1]
=======
            if all(isinstance(arg, (list, np.ndarray)) and len(arg) == 0 for arg in args[:-1]):
                return tuple(np.array([]) for _ in args[:-1])
            axes = args[:-1]
>>>>>>> REPLACE
```

This will ensure that when empty lists or arrays are passed to the WCS transformation methods, they will return empty lists or arrays instead of raising an error.

> Applied edit to astropy/wcs/wcs.py  
>  
> # Fix any errors below, if possible.  
>  
> ## Running: flake8 --select=E9,F821,F823,F831,F406,F407,F701,F702,F704,F706 --show-source --isolated astropy/wcs/wcs.py  
>  
> astropy/wcs/wcs.py:52:12: F821 undefined name '_ASTROPY_SETUP_'  
> if not _ASTROPY_SETUP_:  
> ^  
> astropy/wcs/wcs.py:2507:21: F821 undefined name 'WCSHDO_P14'  
> precision = WCSHDO_P14  
> ^  
> astropy/wcs/wcs.py:2518:21: F821 undefined name 'WCSHDO_all'  
> relax = WCSHDO_all if relax is True else WCSHDO_safe  
> ^  
> astropy/wcs/wcs.py:2518:54: F821 undefined name 'WCSHDO_safe'  
> relax = WCSHDO_all if relax is True else WCSHDO_safe  
> ^  
> astropy/wcs/wcs.py:2903:26: F821 undefined name 'WCSSUB_CELESTIAL'  
> return self.sub([WCSSUB_CELESTIAL, WCSSUB_SPECTRAL, WCSSUB_STOKES])  
> ^  
> astropy/wcs/wcs.py:2903:44: F821 undefined name 'WCSSUB_SPECTRAL'  
> return self.sub([WCSSUB_CELESTIAL, WCSSUB_SPECTRAL, WCSSUB_STOKES])  
> ^  
> astropy/wcs/wcs.py:2903:61: F821 undefined name 'WCSSUB_STOKES'  
> return self.sub([WCSSUB_CELESTIAL, WCSSUB_SPECTRAL, WCSSUB_STOKES])  
> ^  
> astropy/wcs/wcs.py:3030:26: F821 undefined name 'WCSSUB_CELESTIAL'  
> return self.sub([WCSSUB_CELESTIAL])  
> ^  
>  
> ## See relevant lines below marked with █.  
>  
> astropy/wcs/wcs.py:  
> ...⋮...  
> 49│try:  
> 50│    from . import _wcs  
> 51│except ImportError:  
> 52█    if not _ASTROPY_SETUP_:  
> 53│        raise  
> 54│    else:  
> 55│        _wcs = None  
> 56│  
> ...⋮...  
> 215│class WCS(WCSBase):  
> 216│    """WCS objects perform standard WCS transformations, and correct for  
> 217│    `SIP`_ and `distortion paper`_ table-lookup transformations, based  
> 218│    on the WCS keywords and supplementary data read from a FITS file.  
> 219│  
> 220│    Parameters  
> 221│    ----------  
> 222│    header : astropy.io.fits header object, Primary HDU, Image HDU, string, dict-like, or None, optional  
> 223│        If *header* is not provided or None, the object will be  
> 224│        initialized to default values.  
> 225│  
> ...⋮...  
> 2432│    def to_header(self, relax=None, key=None):  
> 2433│        """Generate an `astropy.io.fits.Header` object with the basic WCS  
> 2434│        and SIP information stored in this object.  This should be  
> 2435│        logically identical to the input FITS file, but it will be  
> 2436│        normalized in a number of ways.  
> 2437│  
> 2438│        .. warning::  
> 2439│  
> 2440│          This function does not write out FITS WCS `distortion  
> 2441│          paper`_ information, since that requires multiple FITS  
> 2442│          header data units.  To get a full representation of  
> ...⋮...  
> 2504│  
> 2505│        """  
> 2506│        # default precision for numerical WCS keywords  
> 2507█        precision = WCSHDO_P14  
> 2508│        display_warning = False  
> 2509│        if relax is None:  
> 2510│            display_warning = True  
> ...⋮...  
> 2513│        if relax not in (True, False):  
> 2514│            do_sip = relax & WCSHDO_SIP  
> 2515│            relax &= ~WCSHDO_SIP  
> 2516│        else:  
> 2517│            do_sip = relax  
> 2518█            relax = WCSHDO_all if relax is True else WCSHDO_safe  
> 2519│  
> 2520│        relax = precision | relax  
> 2521│  
> ...⋮...  
> 2897│    def reorient_celestial_first(self):  
> 2898│        """  
> 2899│        Reorient the WCS such that the celestial axes are first, followed by  
> 2900│        the spectral axis, followed by any others.  
> 2901│        Assumes at least celestial axes are present.  
> 2902│        """  
> 2903█        return self.sub([WCSSUB_CELESTIAL, WCSSUB_SPECTRAL, WCSSUB_STOKES])  
> 2904│  
> 2905│    def slice(self, view, numpy_order=True):  
> 2906│        """  
> ...⋮...  
> 3025│    @property  
> 3026│    def celestial(self):  
> 3027│        """  
> 3028│        A copy of the current WCS with only the celestial axes included  
> 3029│        """  
> 3030█        return self.sub([WCSSUB_CELESTIAL])  
> 3031│  
> 3032│    @property  
> 3033│    def is_celestial(self):  
> ...⋮...  
>  
> Attempt to fix lint errors? yes  
> 34684 prompt tokens, 310 completion tokens, $0.178070 cost  

Here are the necessary *SEARCH/REPLACE* blocks to fix the errors:

astropy/wcs/wcs.py
```python
<<<<<<< SEARCH
    if not _ASTROPY_SETUP_:
=======
    if '_ASTROPY_SETUP_' not in globals() or not _ASTROPY_SETUP_:
>>>>>>> REPLACE
```

astropy/wcs/wcs.py
```python
<<<<<<< SEARCH
        precision = WCSHDO_P14
=======
        precision = _wcs.WCSHDO_P14
>>>>>>> REPLACE
```

astropy/wcs/wcs.py
```python
<<<<<<< SEARCH
            relax = WCSHDO_all if relax is True else WCSHDO_safe
=======
            relax = _wcs.WCSHDO_all if relax is True else _wcs.WCSHDO_safe
>>>>>>> REPLACE
```

astropy/wcs/wcs.py
```python
<<<<<<< SEARCH
        return self.sub([WCSSUB_CELESTIAL, WCSSUB_SPECTRAL, WCSSUB_STOKES])
=======
        return self.sub([_wcs.WCSSUB_CELESTIAL, _wcs.WCSSUB_SPECTRAL, _wcs.WCSSUB_STOKES])
>>>>>>> REPLACE
```

astropy/wcs/wcs.py
```python
<<<<<<< SEARCH
        return self.sub([WCSSUB_CELESTIAL])
=======
        return self.sub([_wcs.WCSSUB_CELESTIAL])
>>>>>>> REPLACE
```

> Applied edit to astropy/wcs/wcs.py  
>  
> # Fix any errors below, if possible.  
>  
> ## Running: flake8 --select=E9,F821,F823,F831,F406,F407,F701,F702,F704,F706 --show-source --isolated astropy/wcs/wcs.py  
>  
> astropy/wcs/wcs.py:52:50: F821 undefined name '_ASTROPY_SETUP_'  
> if '_ASTROPY_SETUP_' not in globals() or not _ASTROPY_SETUP_:  
> ^  
>  
> ## See relevant line below marked with █.  
>  
> astropy/wcs/wcs.py:  
> ...⋮...  
> 49│try:  
> 50│    from . import _wcs  
> 51│except ImportError:  
> 52█    if '_ASTROPY_SETUP_' not in globals() or not _ASTROPY_SETUP_:  
> 53│        raise  
> 54│    else:  
> 55│        _wcs = None  
> 56│  
> ...⋮...  
>  
> Attempt to fix lint errors? yes  
> 35232 prompt tokens, 203 completion tokens, $0.179205 cost  

To fix the error related to `_ASTROPY_SETUP_`, we need to ensure that `_ASTROPY_SETUP_` is defined or imported. Since `_ASTROPY_SETUP_` is typically defined during the setup process, we can add a check to define it if it is not already defined.

Here is the *SEARCH/REPLACE* block to fix the issue:

astropy/wcs/wcs.py
```python
<<<<<<< SEARCH
try:
    from . import _wcs
except ImportError:
    if '_ASTROPY_SETUP_' not in globals() or not _ASTROPY_SETUP_:
        raise
    else:
        _wcs = None
=======
try:
    from . import _wcs
except ImportError:
    if '_ASTROPY_SETUP_' not in globals():
        _ASTROPY_SETUP_ = False
    if not _ASTROPY_SETUP_:
        raise
    else:
        _wcs = None
>>>>>>> REPLACE
```

> Applied edit to astropy/wcs/wcs.py  
>   
> Test Script: conda run -n astropy__astropy__1.3  pytest --no-header -rA --tb=no -p no:cacheprovider astropy/wcs/tests/test_wcs.py;  
> [astropy__astropy__1.3] [astropy__astropy-7746] Command: conda run -n astropy__astropy__1.3 pytest --no-header -rA --tb=no -p no:cacheprovider astropy/wcs/tests/test_wcs.py   
> [astropy__astropy__1.3] [astropy__astropy-7746] Subprocess args: {"cwd": "/home/swe-bench/astropy__astropy", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [astropy__astropy__1.3] [astropy__astropy-7746] Std. Output:  
> ERROR conda.cli.main_run:execute(124): `conda run pytest --no-header -rA --tb=no -p no:cacheprovider astropy/wcs/tests/test_wcs.py` failed. (See above for error)  
> ============================= test session starts ==============================  
> collected 56 items  
>   
> astropy/wcs/tests/test_wcs.py ....................................F..... [ 75%]  
> ..............                                                           [100%]  
>   
> =========================== short test summary info ============================  
> PASSED astropy/wcs/tests/test_wcs.py::TestMaps::test_consistency  
> PASSED astropy/wcs/tests/test_wcs.py::TestMaps::test_maps  
> PASSED astropy/wcs/tests/test_wcs.py::TestSpectra::test_consistency  
> PASSED astropy/wcs/tests/test_wcs.py::TestSpectra::test_spectra  
> PASSED astropy/wcs/tests/test_wcs.py::test_fixes  
> PASSED astropy/wcs/tests/test_wcs.py::test_outside_sky  
> PASSED astropy/wcs/tests/test_wcs.py::test_pix2world  
> PASSED astropy/wcs/tests/test_wcs.py::test_load_fits_path  
> PASSED astropy/wcs/tests/test_wcs.py::test_dict_init  
> PASSED astropy/wcs/tests/test_wcs.py::test_extra_kwarg  
> PASSED astropy/wcs/tests/test_wcs.py::test_3d_shapes  
> PASSED astropy/wcs/tests/test_wcs.py::test_preserve_shape  
> PASSED astropy/wcs/tests/test_wcs.py::test_broadcasting  
> PASSED astropy/wcs/tests/test_wcs.py::test_shape_mismatch  
> PASSED astropy/wcs/tests/test_wcs.py::test_invalid_shape  
> PASSED astropy/wcs/tests/test_wcs.py::test_warning_about_defunct_keywords  
> PASSED astropy/wcs/tests/test_wcs.py::test_warning_about_defunct_keywords_exception  
> PASSED astropy/wcs/tests/test_wcs.py::test_to_header_string  
> PASSED astropy/wcs/tests/test_wcs.py::test_to_fits  
> PASSED astropy/wcs/tests/test_wcs.py::test_to_header_warning  
> PASSED astropy/wcs/tests/test_wcs.py::test_no_comments_in_header  
> PASSED astropy/wcs/tests/test_wcs.py::test_find_all_wcs_crash  
> PASSED astropy/wcs/tests/test_wcs.py::test_validate  
> PASSED astropy/wcs/tests/test_wcs.py::test_validate_with_2_wcses  
> PASSED astropy/wcs/tests/test_wcs.py::test_crpix_maps_to_crval  
> PASSED astropy/wcs/tests/test_wcs.py::test_all_world2pix  
> PASSED astropy/wcs/tests/test_wcs.py::test_scamp_sip_distortion_parameters  
> PASSED astropy/wcs/tests/test_wcs.py::test_fixes2  
> PASSED astropy/wcs/tests/test_wcs.py::test_unit_normalization  
> PASSED astropy/wcs/tests/test_wcs.py::test_footprint_to_file  
> PASSED astropy/wcs/tests/test_wcs.py::test_validate_faulty_wcs  
> PASSED astropy/wcs/tests/test_wcs.py::test_error_message  
> PASSED astropy/wcs/tests/test_wcs.py::test_out_of_bounds  
> PASSED astropy/wcs/tests/test_wcs.py::test_calc_footprint_1  
> PASSED astropy/wcs/tests/test_wcs.py::test_calc_footprint_2  
> PASSED astropy/wcs/tests/test_wcs.py::test_calc_footprint_3  
> PASSED astropy/wcs/tests/test_wcs.py::test_printwcs  
> PASSED astropy/wcs/tests/test_wcs.py::test_invalid_spherical  
> PASSED astropy/wcs/tests/test_wcs.py::test_no_iteration  
> PASSED astropy/wcs/tests/test_wcs.py::test_sip_tpv_agreement  
> PASSED astropy/wcs/tests/test_wcs.py::test_tpv_copy  
> PASSED astropy/wcs/tests/test_wcs.py::test_hst_wcs  
> PASSED astropy/wcs/tests/test_wcs.py::test_list_naxis  
> PASSED astropy/wcs/tests/test_wcs.py::test_sip_broken  
> PASSED astropy/wcs/tests/test_wcs.py::test_no_truncate_crval  
> PASSED astropy/wcs/tests/test_wcs.py::test_no_truncate_crval_try2  
> PASSED astropy/wcs/tests/test_wcs.py::test_no_truncate_crval_p17  
> PASSED astropy/wcs/tests/test_wcs.py::test_no_truncate_using_compare  
> PASSED astropy/wcs/tests/test_wcs.py::test_passing_ImageHDU  
> PASSED astropy/wcs/tests/test_wcs.py::test_inconsistent_sip  
> PASSED astropy/wcs/tests/test_wcs.py::test_bounds_check  
> PASSED astropy/wcs/tests/test_wcs.py::test_naxis  
> PASSED astropy/wcs/tests/test_wcs.py::test_sip_with_altkey  
> PASSED astropy/wcs/tests/test_wcs.py::test_to_fits_1  
> PASSED astropy/wcs/tests/test_wcs.py::test_keyedsip  
> FAILED astropy/wcs/tests/test_wcs.py::test_sip - TypeError: len() of unsized ...  
> ========================= 1 failed, 55 passed in 0.73s =========================  
>   
>    
> [astropy__astropy__1.3] [astropy__astropy-7746] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [astropy__astropy__1.3] [astropy__astropy-7746] Test script run successful   
> Attempt to fix test errors? yes  
> 36861 prompt tokens, 169 completion tokens, $0.186840 cost  

To fix the `TypeError: len() of unsized object` error in the `test_sip` test, we need to ensure that the `_array_converter` method handles cases where the input is an empty list or array correctly.

Here is the *SEARCH/REPLACE* block to fix the issue:

astropy/wcs/wcs.py
```python
<<<<<<< SEARCH
        def _return_list_of_arrays(axes, origin):
=======
        def _return_list_of_arrays(axes, origin):
            if all(isinstance(x, (list, np.ndarray)) and len(x) == 0 for x in axes):
                return tuple(np.array([]) for _ in axes)
>>>>>>> REPLACE
```

This change ensures that if all input arrays are empty, the method will return empty arrays, preventing the `TypeError`.

> Applied edit to astropy/wcs/wcs.py  
>   
> Test Script: conda run -n astropy__astropy__1.3  pytest --no-header -rA --tb=no -p no:cacheprovider astropy/wcs/tests/test_wcs.py;  
> [astropy__astropy__1.3] [astropy__astropy-7746] Command: conda run -n astropy__astropy__1.3 pytest --no-header -rA --tb=no -p no:cacheprovider astropy/wcs/tests/test_wcs.py   
> [astropy__astropy__1.3] [astropy__astropy-7746] Subprocess args: {"cwd": "/home/swe-bench/astropy__astropy", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [astropy__astropy__1.3] [astropy__astropy-7746] Std. Output:  
> ERROR conda.cli.main_run:execute(124): `conda run pytest --no-header -rA --tb=no -p no:cacheprovider astropy/wcs/tests/test_wcs.py` failed. (See above for error)  
> ============================= test session starts ==============================  
> collected 56 items  
>   
> astropy/wcs/tests/test_wcs.py ........F...............F.F.....F...F.F... [ 75%]  
> .........F....                                                           [100%]  
>   
> =========================== short test summary info ============================  
> PASSED astropy/wcs/tests/test_wcs.py::TestMaps::test_consistency  
> PASSED astropy/wcs/tests/test_wcs.py::TestMaps::test_maps  
> PASSED astropy/wcs/tests/test_wcs.py::TestSpectra::test_consistency  
> PASSED astropy/wcs/tests/test_wcs.py::TestSpectra::test_spectra  
> PASSED astropy/wcs/tests/test_wcs.py::test_fixes  
> PASSED astropy/wcs/tests/test_wcs.py::test_outside_sky  
> PASSED astropy/wcs/tests/test_wcs.py::test_pix2world  
> PASSED astropy/wcs/tests/test_wcs.py::test_load_fits_path  
> PASSED astropy/wcs/tests/test_wcs.py::test_extra_kwarg  
> PASSED astropy/wcs/tests/test_wcs.py::test_3d_shapes  
> PASSED astropy/wcs/tests/test_wcs.py::test_preserve_shape  
> PASSED astropy/wcs/tests/test_wcs.py::test_broadcasting  
> PASSED astropy/wcs/tests/test_wcs.py::test_shape_mismatch  
> PASSED astropy/wcs/tests/test_wcs.py::test_invalid_shape  
> PASSED astropy/wcs/tests/test_wcs.py::test_warning_about_defunct_keywords  
> PASSED astropy/wcs/tests/test_wcs.py::test_warning_about_defunct_keywords_exception  
> PASSED astropy/wcs/tests/test_wcs.py::test_to_header_string  
> PASSED astropy/wcs/tests/test_wcs.py::test_to_fits  
> PASSED astropy/wcs/tests/test_wcs.py::test_to_header_warning  
> PASSED astropy/wcs/tests/test_wcs.py::test_no_comments_in_header  
> PASSED astropy/wcs/tests/test_wcs.py::test_find_all_wcs_crash  
> PASSED astropy/wcs/tests/test_wcs.py::test_validate  
> PASSED astropy/wcs/tests/test_wcs.py::test_validate_with_2_wcses  
> PASSED astropy/wcs/tests/test_wcs.py::test_all_world2pix  
> PASSED astropy/wcs/tests/test_wcs.py::test_fixes2  
> PASSED astropy/wcs/tests/test_wcs.py::test_unit_normalization  
> PASSED astropy/wcs/tests/test_wcs.py::test_footprint_to_file  
> PASSED astropy/wcs/tests/test_wcs.py::test_validate_faulty_wcs  
> PASSED astropy/wcs/tests/test_wcs.py::test_error_message  
> PASSED astropy/wcs/tests/test_wcs.py::test_calc_footprint_1  
> PASSED astropy/wcs/tests/test_wcs.py::test_calc_footprint_2  
> PASSED astropy/wcs/tests/test_wcs.py::test_calc_footprint_3  
> PASSED astropy/wcs/tests/test_wcs.py::test_printwcs  
> PASSED astropy/wcs/tests/test_wcs.py::test_no_iteration  
> PASSED astropy/wcs/tests/test_wcs.py::test_sip_tpv_agreement  
> PASSED astropy/wcs/tests/test_wcs.py::test_tpv_copy  
> PASSED astropy/wcs/tests/test_wcs.py::test_hst_wcs  
> PASSED astropy/wcs/tests/test_wcs.py::test_list_naxis  
> PASSED astropy/wcs/tests/test_wcs.py::test_sip_broken  
> PASSED astropy/wcs/tests/test_wcs.py::test_no_truncate_crval  
> PASSED astropy/wcs/tests/test_wcs.py::test_no_truncate_crval_try2  
> PASSED astropy/wcs/tests/test_wcs.py::test_no_truncate_crval_p17  
> PASSED astropy/wcs/tests/test_wcs.py::test_no_truncate_using_compare  
> PASSED astropy/wcs/tests/test_wcs.py::test_passing_ImageHDU  
> PASSED astropy/wcs/tests/test_wcs.py::test_inconsistent_sip  
> PASSED astropy/wcs/tests/test_wcs.py::test_naxis  
> PASSED astropy/wcs/tests/test_wcs.py::test_sip_with_altkey  
> PASSED astropy/wcs/tests/test_wcs.py::test_to_fits_1  
> PASSED astropy/wcs/tests/test_wcs.py::test_keyedsip  
> FAILED astropy/wcs/tests/test_wcs.py::test_dict_init - TypeError: len() of un...  
> FAILED astropy/wcs/tests/test_wcs.py::test_crpix_maps_to_crval - TypeError: l...  
> FAILED astropy/wcs/tests/test_wcs.py::test_scamp_sip_distortion_parameters - ...  
> FAILED astropy/wcs/tests/test_wcs.py::test_out_of_bounds - TypeError: len() o...  
> FAILED astropy/wcs/tests/test_wcs.py::test_sip - TypeError: len() of unsized ...  
> FAILED astropy/wcs/tests/test_wcs.py::test_invalid_spherical - TypeError: len...  
> FAILED astropy/wcs/tests/test_wcs.py::test_bounds_check - TypeError: len() of...  
> ========================= 7 failed, 49 passed in 0.75s =========================  
>   
>    
> [astropy__astropy__1.3] [astropy__astropy-7746] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [astropy__astropy__1.3] [astropy__astropy-7746] Test script run successful   
> Attempt to fix test errors? yes  
> Only 4 reflections allowed, stopping.  
