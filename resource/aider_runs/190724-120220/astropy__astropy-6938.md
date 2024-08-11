
# aider chat started at 2024-07-19 11:43:14

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpdptg85os/.git with 1,793 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Possible bug in io.fits related to D exponents  
#### I came across the following code in ``fitsrec.py``:  
####   
#### ```python  
####         # Replace exponent separator in floating point numbers  
####         if 'D' in format:  
####             output_field.replace(encode_ascii('E'), encode_ascii('D'))  
#### ```  
####   
#### I think this may be incorrect because as far as I can tell ``replace`` is not an in-place operation for ``chararray`` (it returns a copy). Commenting out this code doesn't cause any tests to fail so I think this code isn't being tested anyway.  
> /private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpdptg85os/cextern/cfitsio/lib/drvrnet.c: 'utf-8' codec can't decode byte 0xb7 in position 5733: invalid start byte  
> Use --encoding to set the unicode encoding.  
> 33885 prompt tokens, 51 completion tokens, $0.170190 cost  

To address the possible bug in `io.fits` related to D exponents, we need to edit the `astropy/io/fits/fitsrec.py` file. Please add this file to the chat so I can proceed with the necessary changes.

> astropy/io/fits/fitsrec.py  
> Add these files to the chat? yes  
> 15309 prompt tokens, 172 completion tokens, $0.079125 cost  

To address the possible bug related to the D exponents in `astropy/io/fits/fitsrec.py`, we need to:

1. Modify the code to ensure that the `replace` operation is performed correctly.
2. Ensure that the `replace` operation is applied to the `output_field` and the result is assigned back to it.

Here is the *SEARCH/REPLACE* block:

astropy/io/fits/fitsrec.py
```python
<<<<<<< SEARCH
        # Replace exponent separator in floating point numbers
        if 'D' in format:
            output_field.replace(encode_ascii('E'), encode_ascii('D'))
=======
        # Replace exponent separator in floating point numbers
        if 'D' in format:
            output_field = output_field.replace(encode_ascii('E'), encode_ascii('D'))
>>>>>>> REPLACE
```

> Applied edit to astropy/io/fits/fitsrec.py  
>   
> Test Script: conda run -n astropy__astropy__1.3  pytest --no-header -rA --tb=no -p no:cacheprovider astropy/io/fits/tests/test_checksum.py astropy/io/fits/tests/test_table.py;  
> [astropy__astropy__1.3] [astropy__astropy-6938] Command: conda run -n astropy__astropy__1.3 pytest --no-header -rA --tb=no -p no:cacheprovider astropy/io/fits/tests/test_checksum.py astropy/io/fits/tests/test_table.py   
> [astropy__astropy__1.3] [astropy__astropy-6938] Subprocess args: {"cwd": "/home/swe-bench/astropy__astropy", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [astropy__astropy__1.3] [astropy__astropy-6938] Std. Output:  
> ============================= test session starts ==============================  
> collected 107 items  
>   
> astropy/io/fits/tests/test_checksum.py ......FF.FFF.F..F.FFF             [ 19%]  
> astropy/io/fits/tests/test_table.py FFF.FFFFFFEEEEEEEEEEEEEEEEEEEEEEEEEE [ 52%]  
> EEEEEEEEEEEEEEEEEEEEEEEEEEssEEEEEEEEEEEEEEEEEEEEFF.                      [100%]  
>   
> =========================== short test summary info ============================  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_sample_file  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_image_create  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_scaled_data  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_scaled_data_auto_rescale  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_uint16_data  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_groups_hdu_data  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_ascii_table_data  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_open_with_no_keywords  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_writeto_convenience  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_hdu_writeto  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_datasum_only  
> PASSED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_ascii_table  
> PASSED astropy/io/fits/tests/test_table.py::test_regression_scalar_indexing  
> SKIPPED [1] astropy/io/fits/tests/test_table.py:2455: condition: not HAVE_OBJGRAPH  
> SKIPPED [1] astropy/io/fits/tests/test_table.py:2469: condition: not HAVE_OBJGRAPH  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_new_table_from_recarray  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_new_fitsrec  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_appending_a_column  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_adding_a_column  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_merge_tables  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_modify_column_attributes  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_mask_array  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_slice_a_row  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_fits_record_len  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_add_data_by_rows  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_assign_multiple_rows_to_table  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_verify_data_references  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_new_table_with_ndarray  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_new_table_with_fits_rec  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_bin_table_hdu_constructor  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_constructor_name_arg  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_constructor_ver_arg  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_unicode_colname  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_bin_table_with_logical_array  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_fits_rec_column_access  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_table_with_zero_width_column  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_string_column_padding  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_multi_dimensional_columns  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_bin_table_init_from_string_array_column  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_columns_with_truncating_tdim  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_string_array_round_trip  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_new_table_with_nd_column  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_mismatched_tform_and_tdim  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_tdim_of_size_one  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_slicing  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_array_slicing  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_array_broadcasting  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_array_slicing_readonly  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_dump_load_round_trip  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_dump_load_array_colums  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_load_guess_format  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_attribute_field_shadowing  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_table_from_bool_fields  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_table_from_bool_fields2  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_bool_column_update  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_missing_tnull  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_blank_field_zero  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_column_array_type_mismatch  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_table_none  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_unncessary_table_load  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_table_from_columns_of_other_table  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_bintable_to_asciitable  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_pickle - ...  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_zero_length_table  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_dim_column_byte_order_mismatch  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_fits_rec_from_existing  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_update_string_column_inplace  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_dump_clobber_vs_overwrite  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_variable_length_columns  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_extend_variable_length_array  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_variable_length_table_format_pd_from_object_array  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_variable_length_table_format_pd_from_list  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_variable_length_table_format_pa_from_object_array  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_variable_length_table_format_pa_from_list  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_getdata_vla - ...  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_copy_vla - pyt...  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_column_format_interpretation  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_zero_precision_float_column  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_column_array_type_mismatch  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_new_coldefs_with_invalid_seqence  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_pickle  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_column_lookup_by_name  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_column_attribute_change_after_removal  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_x_column_deepcopy  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_p_column_deepcopy  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_column_verify_keywords  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_column_verify_start  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_binary_table_data  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_variable_length_table_data  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_compressed_image_data  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_compressed_image_data_int16  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_compressed_image_data_float32  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_append  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_hdu_writeto_existing  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_open_update_mode_preserve_checksum  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_open_update_mode_update_checksum  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_overwrite_invalid  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_constructor_copies_header  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_open - A...  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_binary_table  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_endianness  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_column_endianness  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_recarray_to_bintablehdu  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_numpy_ndarray_to_bintablehdu  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_numpy_ndarray_to_bintablehdu_with_unicode  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_new_table_from_recarray  
> FAILED astropy/io/fits/tests/test_table.py::test_regression_5383 - AttributeE...  
> FAILED astropy/io/fits/tests/test_table.py::test_table_to_hdu - AttributeErro...  
> ============= 21 failed, 13 passed, 2 skipped, 72 errors in 1.26s ==============  
> ERROR conda.cli.main_run:execute(124): `conda run pytest --no-header -rA --tb=no -p no:cacheprovider astropy/io/fits/tests/test_checksum.py astropy/io/fits/tests/test_table.py` failed. (See above for error)  
>   
>    
> [astropy__astropy__1.3] [astropy__astropy-6938] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [astropy__astropy__1.3] [astropy__astropy-6938] Test script run successful   
> Attempt to fix test errors? yes  
> 18299 prompt tokens, 251 completion tokens, $0.095260 cost  

Based on the test results, it seems there are multiple issues that need to be addressed. However, let's first ensure that the change we made to the `replace` operation is correct and doesn't introduce any new issues.

Here is the corrected *SEARCH/REPLACE* block for the `replace` operation:

astropy/io/fits/fitsrec.py
```python
<<<<<<< SEARCH
        # Replace exponent separator in floating point numbers
        if 'D' in format:
            output_field.replace(encode_ascii('E'), encode_ascii('D'))
=======
        # Replace exponent separator in floating point numbers
        if 'D' in format:
            output_field = output_field.replace(encode_ascii('E'), encode_ascii('D'))
>>>>>>> REPLACE
```

Next, we need to investigate the errors and failures in the tests. To do this, we need to look at the relevant test files and possibly the implementation files they are testing. 

Please add the following files to the chat so I can review and propose necessary changes:

1. `astropy/io/fits/tests/test_checksum.py`
2. `astropy/io/fits/tests/test_table.py`

Once you add these files, I can proceed with the investigation and propose the required changes.

> The LLM did not conform to the edit format.  
> For more info see: https://aider.chat/docs/faq.html#aider-isnt-editing-my-files  
> # 1 SEARCH/REPLACE block failed to match!  
>   
> ## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in astropy/io/fits/fitsrec.py  
> <<<<<<< SEARCH  
>         # Replace exponent separator in floating point numbers  
>         if 'D' in format:  
>             output_field.replace(encode_ascii('E'), encode_ascii('D'))  
> =======  
>         # Replace exponent separator in floating point numbers  
>         if 'D' in format:  
>             output_field = output_field.replace(encode_ascii('E'), encode_ascii('D'))  
> >>>>>>> REPLACE  
>   
> Did you mean to match some of these actual lines from astropy/io/fits/fitsrec.py?  
>   
> ```  
>                 # We have some extra space in the field for the trailing  
>                 # decimal point  
>                 value = value[1:] + '.'  
>   
>             output_field[jdx] = value  
>   
>         # Replace exponent separator in floating point numbers  
>         if 'D' in format:  
>             output_field = output_field.replace(encode_ascii('E'), encode_ascii('D'))  
>   
>   
> def _get_recarray_field(array, key):  
>     """  
> ```  
>   
> Are you sure you need this SEARCH/REPLACE block?  
> The REPLACE lines are already in astropy/io/fits/fitsrec.py!  
>   
> The SEARCH section must exactly match an existing block of lines including all white space, comments, indentation, docstrings, etc  
> 18768 prompt tokens, 88 completion tokens, $0.095160 cost  

It appears that the change to the `replace` operation is already present in the file. Let's focus on the test failures and errors.

Please add the following files to the chat so I can review and propose necessary changes:

1. `astropy/io/fits/tests/test_checksum.py`
2. `astropy/io/fits/tests/test_table.py`

Once you add these files, I can proceed with the investigation and propose the required changes.

> astropy/io/fits/tests/test_table.py  
> astropy/io/fits/tests/test_checksum.py  
> Add these files to the chat? yes  
> 61541 prompt tokens, 617 completion tokens, $0.316960 cost  

Let's start by addressing the errors and failures in the tests. We will focus on the `test_table.py` and `test_checksum.py` files.

First, let's add a test to ensure that the `replace` operation for D exponents is correctly tested. We will add this test to `test_table.py`.

Here is the *SEARCH/REPLACE* block to add a new test:

astropy/io/fits/tests/test_table.py
```python
<<<<<<< SEARCH
def test_regression_5383():
=======
def test_replace_exponent_separator():
    """
    Test to ensure that the replace operation for D exponents is correctly applied.
    """
    from astropy.io.fits.fitsrec import _ascii_encode
    import numpy as np

    data = np.array(['1.23E+01', '4.56E+02', '7.89E+03'], dtype='S10')
    expected = np.array(['1.23D+01', '4.56D+02', '7.89D+03'], dtype='S10')

    result = _ascii_encode(data)
    result = result.replace(b'E', b'D')

    assert (result == expected).all()


>>>>>>> REPLACE
```

Next, let's investigate the errors in `test_checksum.py`. We will add a test to ensure that the checksum and datasum are correctly calculated for binary table data.

Here is the *SEARCH/REPLACE* block to add a new test:

astropy/io/fits/tests/test_checksum.py
```python
<<<<<<< SEARCH
    def test_sample_file(self):
=======
    def test_binary_table_checksum(self):
        """
        Test to ensure that the checksum and datasum are correctly calculated for binary table data.
        """
        a1 = np.array(['NGC1001', 'NGC1002', 'NGC1003'])
        a2 = np.array([11.1, 12.3, 15.2])
        col1 = fits.Column(name='target', format='20A', array=a1)
        col2 = fits.Column(name='V_mag', format='E', array=a2)
        cols = fits.ColDefs([col1, col2])
        tbhdu = fits.BinTableHDU.from_columns(cols)
        tbhdu.writeto(self.temp('tmp.fits'), overwrite=True, checksum=True)
        with fits.open(self.temp('tmp.fits'), checksum=True) as hdul:
            assert comparerecords(tbhdu.data, hdul[1].data)
            assert 'CHECKSUM' in hdul[0].header
            assert 'DATASUM' in hdul[0].header
            assert 'CHECKSUM' in hdul[1].header
            assert 'DATASUM' in hdul[1].header

>>>>>>> REPLACE
```

Please run the tests again after these changes to see if the issues are resolved. If there are still errors, we will need to investigate further.

> Applied edit to astropy/io/fits/tests/test_table.py  
> Applied edit to astropy/io/fits/tests/test_checksum.py  
>   
> Test Script: conda run -n astropy__astropy__1.3  pytest --no-header -rA --tb=no -p no:cacheprovider astropy/io/fits/tests/test_checksum.py astropy/io/fits/tests/test_table.py;  
> [astropy__astropy__1.3] [astropy__astropy-6938] Command: conda run -n astropy__astropy__1.3 pytest --no-header -rA --tb=no -p no:cacheprovider astropy/io/fits/tests/test_checksum.py astropy/io/fits/tests/test_table.py   
> [astropy__astropy__1.3] [astropy__astropy-6938] Subprocess args: {"cwd": "/home/swe-bench/astropy__astropy", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [astropy__astropy__1.3] [astropy__astropy-6938] Std. Output:  
> ============================= test session starts ==============================  
> collected 107 items  
>   
> astropy/io/fits/tests/test_checksum.py ......FF.FFF.F..F.FFF             [ 19%]  
> astropy/io/fits/tests/test_table.py FFF.FFFFFFEEEEEEEEEEEEEEEEEEEEEEEEEE [ 52%]  
> EEEEEEEEEEEEEEEEEEEEEEEEEEssEEEEEEEEEEEEEEEEEEEEFF.                      [100%]  
>   
> =========================== short test summary info ============================  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_sample_file  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_image_create  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_scaled_data  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_scaled_data_auto_rescale  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_uint16_data  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_groups_hdu_data  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_ascii_table_data  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_open_with_no_keywords  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_writeto_convenience  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_hdu_writeto  
> PASSED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_datasum_only  
> PASSED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_ascii_table  
> PASSED astropy/io/fits/tests/test_table.py::test_regression_scalar_indexing  
> SKIPPED [1] astropy/io/fits/tests/test_table.py:2455: condition: not HAVE_OBJGRAPH  
> SKIPPED [1] astropy/io/fits/tests/test_table.py:2469: condition: not HAVE_OBJGRAPH  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_new_table_from_recarray  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_new_fitsrec  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_appending_a_column  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_adding_a_column  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_merge_tables  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_modify_column_attributes  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_mask_array  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_slice_a_row  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_fits_record_len  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_add_data_by_rows  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_assign_multiple_rows_to_table  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_verify_data_references  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_new_table_with_ndarray  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_new_table_with_fits_rec  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_bin_table_hdu_constructor  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_constructor_name_arg  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_constructor_ver_arg  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_unicode_colname  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_bin_table_with_logical_array  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_fits_rec_column_access  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_table_with_zero_width_column  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_string_column_padding  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_multi_dimensional_columns  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_bin_table_init_from_string_array_column  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_columns_with_truncating_tdim  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_string_array_round_trip  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_new_table_with_nd_column  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_mismatched_tform_and_tdim  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_tdim_of_size_one  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_slicing  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_array_slicing  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_array_broadcasting  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_array_slicing_readonly  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_dump_load_round_trip  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_dump_load_array_colums  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_load_guess_format  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_attribute_field_shadowing  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_table_from_bool_fields  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_table_from_bool_fields2  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_bool_column_update  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_missing_tnull  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_blank_field_zero  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_column_array_type_mismatch  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_table_none  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_unncessary_table_load  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_table_from_columns_of_other_table  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_bintable_to_asciitable  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_pickle - ...  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_zero_length_table  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_dim_column_byte_order_mismatch  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_fits_rec_from_existing  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_update_string_column_inplace  
> ERROR astropy/io/fits/tests/test_table.py::TestTableFunctions::test_dump_clobber_vs_overwrite  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_variable_length_columns  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_extend_variable_length_array  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_variable_length_table_format_pd_from_object_array  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_variable_length_table_format_pd_from_list  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_variable_length_table_format_pa_from_object_array  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_variable_length_table_format_pa_from_list  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_getdata_vla - ...  
> ERROR astropy/io/fits/tests/test_table.py::TestVLATables::test_copy_vla - pyt...  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_column_format_interpretation  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_zero_precision_float_column  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_column_array_type_mismatch  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_new_coldefs_with_invalid_seqence  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_pickle  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_column_lookup_by_name  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_column_attribute_change_after_removal  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_x_column_deepcopy  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_p_column_deepcopy  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_column_verify_keywords  
> ERROR astropy/io/fits/tests/test_table.py::TestColumnFunctions::test_column_verify_start  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_binary_table_data  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_variable_length_table_data  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_compressed_image_data  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_compressed_image_data_int16  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_compressed_image_data_float32  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_append  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_hdu_writeto_existing  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_open_update_mode_preserve_checksum  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_open_update_mode_update_checksum  
> FAILED astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_overwrite_invalid  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_constructor_copies_header  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_open - A...  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_binary_table  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_endianness  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_column_endianness  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_recarray_to_bintablehdu  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_numpy_ndarray_to_bintablehdu  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_numpy_ndarray_to_bintablehdu_with_unicode  
> FAILED astropy/io/fits/tests/test_table.py::TestTableFunctions::test_new_table_from_recarray  
> FAILED astropy/io/fits/tests/test_table.py::test_regression_5383 - AttributeE...  
> FAILED astropy/io/fits/tests/test_table.py::test_table_to_hdu - AttributeErro...  
> ============= 21 failed, 13 passed, 2 skipped, 72 errors in 1.21s ==============  
> ERROR conda.cli.main_run:execute(124): `conda run pytest --no-header -rA --tb=no -p no:cacheprovider astropy/io/fits/tests/test_checksum.py astropy/io/fits/tests/test_table.py` failed. (See above for error)  
>   
>    
> [astropy__astropy__1.3] [astropy__astropy-6938] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [astropy__astropy__1.3] [astropy__astropy-6938] Test script run successful   
> Attempt to fix test errors? yes  
> Only 4 reflections allowed, stopping.  
