
# aider chat started at 2024-07-19 18:01:55

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp15wa5oqd/.git with 1,427 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### is_upper() raises IndexError for tall matrices  
#### The function Matrix.is_upper raises an IndexError for a 4x2 matrix of zeros.  
#### ```  
#### >>> sympy.zeros(4,2).is_upper  
#### Traceback (most recent call last):  
####   File "<stdin>", line 1, in <module>  
####   File "sympy/matrices/matrices.py", line 1112, in is_upper  
####     for i in range(1, self.rows)  
####   File "sympy/matrices/matrices.py", line 1113, in <genexpr>  
####     for j in range(i))  
####   File "sympy/matrices/dense.py", line 119, in __getitem__  
####     return self.extract(i, j)  
####   File "sympy/matrices/matrices.py", line 352, in extract  
####     colsList = [a2idx(k, self.cols) for k in colsList]  
####   File "sympy/matrices/matrices.py", line 5261, in a2idx  
####     raise IndexError("Index out of range: a[%s]" % (j,))  
#### IndexError: Index out of range: a[2]  
#### ```  
#### The code for is_upper() is  
#### ```  
####         return all(self[i, j].is_zero  
####                    for i in range(1, self.rows)  
####                    for j in range(i))  
#### ```  
#### For a 4x2 matrix, is_upper iterates over the indices:  
#### ```  
#### >>> A = sympy.zeros(4, 2)  
#### >>> print tuple([i, j] for i in range(1, A.rows) for j in range(i))  
#### ([1, 0], [2, 0], [2, 1], [3, 0], [3, 1], [3, 2])  
#### ```  
#### The attempt to index the (3,2) entry appears to be the source of the error.  
> 33667 prompt tokens, 83 completion tokens, $0.169580 cost  

To fix the `is_upper` method so that it doesn't raise an `IndexError` for tall matrices, we need to modify the logic to ensure that it doesn't attempt to access out-of-bounds indices.

The file that needs to be edited is:
- `sympy/matrices/matrices.py`

Please add `sympy/matrices/matrices.py` to the chat so I can provide the necessary changes.

> sympy/matrices/matrices.py  
> Add these files to the chat? yes  
> 47763 prompt tokens, 104 completion tokens, $0.240375 cost  

Here is the fix for the `is_upper` method in `sympy/matrices/matrices.py`:

sympy/matrices/matrices.py
```python
<<<<<<< SEARCH
        return all(self[i, j].is_zero
                   for i in range(1, self.rows)
                   for j in range(i))
=======
        return all(self[i, j].is_zero
                   for i in range(1, self.rows)
                   for j in range(min(i, self.cols)))
>>>>>>> REPLACE
```

> Applied edit to sympy/matrices/matrices.py  
>   
> Test Script: conda run -n sympy__sympy__1.0  bin/test -C --verbose sympy/matrices/tests/test_matrices.py;  
> [sympy__sympy__1.0] [sympy__sympy-12454] Command: conda run -n sympy__sympy__1.0 bin/test -C --verbose sympy/matrices/tests/test_matrices.py   
> [sympy__sympy__1.0] [sympy__sympy-12454] Subprocess args: {"cwd": "/home/swe-bench/sympy__sympy", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [sympy__sympy__1.0] [sympy__sympy-12454] Std. Output:  
> ============================= test process starts ==============================  
> executable:         /home/swe-bench/miniconda3/envs/sympy__sympy__1.0/bin/python  (3.7.16-final-0) [CPython]  
> architecture:       64-bit  
> cache:              no  
> ground types:       python   
> random seed:        35256047  
> hash randomization: on (PYTHONHASHSEED=2453774058)  
>   
> sympy/matrices/tests/test_matrices.py[152]   
> test_args ok  
> test_division ok  
> test_sum ok  
> test_addition ok  
> test_fancy_index_matrix ok  
> test_multiplication ok  
> test_power ok  
> test_creation ok  
> test_tolist ok  
> test_as_mutable ok  
> test_determinant ok  
> test_det_LU_decomposition ok  
> test_berkowitz_minors ok  
> test_slicing ok  
> test_submatrix_assignment ok  
> test_extract ok  
> test_reshape ok  
> test_applyfunc ok  
> test_expand ok  
> test_refine E  
> test_random ok  
> test_LUdecomp ok  
> test_LUsolve ok  
> test_QRsolve ok  
> test_inverse ok  
> test_matrix_inverse_mod ok  
> test_util ok  
> test_jacobian_hessian ok  
> test_QR ok  
> test_QR_non_square ok  
> test_nullspace ok  
> test_columnspace ok  
> test_wronskian ok  
> test_eigen E  
> test_subs ok  
> test_xreplace ok  
> test_simplify E  
> test_transpose ok  
> test_conjugate ok  
> test_conj_dirac ok  
> test_trace ok  
> test_shape ok  
> test_col_row_op ok  
> test_zip_row_op ok  
> test_issue_3950 ok  
> test_issue_3981 ok  
> test_evalf ok  
> test_is_symbolic ok  
> test_is_upper ok  
> test_is_lower ok  
> test_is_nilpotent ok  
> test_zeros_ones_fill ok  
> test_empty_zeros ok  
> test_issue_3749 E  
> test_inv_iszerofunc ok  
> test_jacobian_metrics ok  
> test_jacobian2 ok  
> test_issue_4564 ok  
> test_nonvectorJacobian ok  
> test_vec ok  
> test_vech ok  
> test_vech_errors ok  
> test_diag ok  
> test_get_diag_blocks1 ok  
> test_get_diag_blocks2 ok  
> test_inv_block ok  
> test_creation_args ok  
> test_diagonal_symmetrical ok  
> test_diagonalization ok  
> test_eigen_vects f  
> test_jordan_form ok  
> test_jordan_form_complex_issue_9274 ok  
> test_issue_10220 ok  
> test_Matrix_berkowitz_charpoly ok  
> test_exp ok  
> test_has ok  
> test_errors ok  
> test_len ok  
> test_integrate ok  
> test_limit E  
> test_diff ok  
> test_getattr ok  
> test_hessenberg ok  
> test_cholesky ok  
> test_LDLdecomposition ok  
> test_cholesky_solve ok  
> test_LDLsolve ok  
> test_lower_triangular_solve ok  
> test_upper_triangular_solve ok  
> test_diagonal_solve ok  
> test_matrix_norm E  
> test_singular_values ok  
> test_condition_number ok  
> test_equality ok  
> test_col_join ok  
> test_row_insert ok  
> test_col_insert ok  
> test_normalized ok  
> test_print_nonzero ok  
> test_zeros_eye ok  
> test_is_zero ok  
> test_rotation_matrices ok  
> test_DeferredVector ok  
> test_DeferredVector_not_iterable ok  
> test_DeferredVector_Matrix ok  
> test_GramSchmidt ok  
> test_casoratian ok  
> test_zero_dimension_multiply ok  
> test_slice_issue_2884 ok  
> test_slice_issue_3401 ok  
> test_copyin ok  
> test_invertible_check ok  
> test_issue_3959 f  
> test_issue_5964 ok  
> test_issue_7604 ok  
> test_is_Identity ok  
> test_dot ok  
> test_dual ok  
> test_anti_symmetric ok  
> test_normalize_sort_diogonalization ok  
> test_issue_5321 ok  
> test_issue_5320 ok  
> test_issue_11944 ok  
> test_cross ok  
> test_hash ok  
> test_issue_3979 f  
> test_adjoint ok  
> test_simplify_immutable ok  
> test_rank ok  
> test_issue_11434 ok  
> test_rank_regression_from_so ok  
> test_replace ok  
> test_replace_map ok  
> test_atoms ok  
> test_pinv Slow w  
> test_pinv_solve ok  
> test_pinv_rank_deficient f  
> test_gauss_jordan_solve ok  
> test_issue_7201 ok  
> test_free_symbols ok  
> test_from_ndarray NumPy must be available to test creating matrices from ndarrays   
> s  
> test_hermitian ok  
> test_doit ok  
> test_issue_9457_9467_9876 ok  
> test_issue_9422 ok  
> test_issue_10770 ok  
> test_issue_10658 ok  
> test_opportunistic_simplification E  
> test_partial_pivoting ok  
> test_iszero_substitution ok  
> test_issue_11238 Slow w  
> test_as_real_imag E                                                       [FAIL]  
>   
>   
> ________________________________ slowest tests _________________________________  
> test_inv_block - Took 12.298 seconds  
> ________________________________________________________________________________  
> ______________ sympy/matrices/tests/test_matrices.py:test_refine _______________  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/tests/test_matrices.py", line 559, in test_refine  
>     m0 = Matrix([[Abs(x)**2, sqrt(x**2)],  
>   File "/home/swe-bench/sympy__sympy/sympy/functions/elementary/miscellaneous.py", line 115, in sqrt  
>     return Pow(arg, S.Half)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 227, in __new__  
>     obj = b._eval_power(e)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 314, in _eval_power  
>     S.Half - e*arg(b)/(2*S.Pi)))  
>   File "/home/swe-bench/sympy__sympy/sympy/core/function.py", line 427, in __new__  
>     result = super(Function, cls).__new__(cls, *args, **options)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/function.py", line 250, in __new__  
>     evaluated = cls.eval(*args)  
>   File "/home/swe-bench/sympy__sympy/sympy/functions/elementary/integers.py", line 23, in eval  
>     if arg.is_integer:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 458, in <lambda>  
>     (a.is_integer for a in self.args), quick_exit=True)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/logic.py", line 78, in _fuzzy_group  
>     for a in args:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 458, in <genexpr>  
>     (a.is_integer for a in self.args), quick_exit=True)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1097, in _eval_is_integer  
>     is_rational = self.is_rational  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1260, in _eval_is_negative  
>     return (-self).is_positive  # remove -1  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1313, in _eval_is_prime  
>     if self.is_integer and self.is_positive:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1097, in _eval_is_integer  
>     is_rational = self.is_rational  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   [Previous line repeated 2 more times]  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1073, in _eval_is_algebraic  
>     r = _fuzzy_group((a.is_algebraic for a in self.args), quick_exit=True)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/logic.py", line 78, in _fuzzy_group  
>     for a in args:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1073, in <genexpr>  
>     r = _fuzzy_group((a.is_algebraic for a in self.args), quick_exit=True)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 1059, in _eval_is_algebraic  
>     if self.base.is_zero or (self.base - 1).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/operations.py", line 41, in __new__  
>     c_part, nc_part, order_symbols = cls.flatten(args)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 135, in flatten  
>     coeff += o  
>   File "/home/swe-bench/sympy__sympy/sympy/core/numbers.py", line 1875, in __add__  
>     return Integer(self.p + other.p)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/numbers.py", line 1800, in __new__  
>     if isinstance(i, string_types):  
> RecursionError: maximum recursion depth exceeded in __instancecheck__  
> ________________________________________________________________________________  
> _______________ sympy/matrices/tests/test_matrices.py:test_eigen _______________  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/tests/test_matrices.py", line 950, in test_eigen  
>     (a - b/2, 1, [Matrix([(12 + 24/(c - b/2))/((c - b/2)*e) + 3/(c - b/2),  
>   File "/home/swe-bench/sympy__sympy/sympy/core/decorators.py", line 78, in __sympifyit_wrapper  
>     return func(a, b)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/decorators.py", line 119, in binary_op_wrapper  
>     return func(self, other)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/expr.py", line 140, in __mul__  
>     return Mul(self, other)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/operations.py", line 41, in __new__  
>     c_part, nc_part, order_symbols = cls.flatten(args)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 182, in flatten  
>     if not a.is_zero and a.is_Rational:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/operations.py", line 30, in __new__  
>     args = list(map(_sympify, args))  
>   File "/home/swe-bench/sympy__sympy/sympy/core/sympify.py", line 379, in _sympify  
>     return sympify(a, strict=True)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/sympify.py", line 238, in sympify  
>     if global_evaluate[0] is False:  
> RecursionError: maximum recursion depth exceeded while calling a Python object  
> ________________________________________________________________________________  
> _____________ sympy/matrices/tests/test_matrices.py:test_simplify ______________  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/tests/test_matrices.py", line 1040, in test_simplify  
>     M.simplify()  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/dense.py", line 684, in simplify  
>     measure=measure)  
>   File "/home/swe-bench/sympy__sympy/sympy/simplify/simplify.py", line 543, in simplify  
>     expr = bottom_up(expr, lambda w: w.normal())  
>   File "/home/swe-bench/sympy__sympy/sympy/simplify/simplify.py", line 998, in bottom_up  
>     rv = F(rv)  
>   File "/home/swe-bench/sympy__sympy/sympy/simplify/simplify.py", line 543, in <lambda>  
>     expr = bottom_up(expr, lambda w: w.normal())  
>   File "/home/swe-bench/sympy__sympy/sympy/core/expr.py", line 1917, in normal  
>     return n/d  
>   File "/home/swe-bench/sympy__sympy/sympy/core/decorators.py", line 78, in __sympifyit_wrapper  
>     return func(a, b)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/decorators.py", line 119, in binary_op_wrapper  
>     return func(self, other)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/expr.py", line 160, in __div__  
>     return Mul(self, Pow(other, S.NegativeOne))  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 227, in __new__  
>     obj = b._eval_power(e)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 627, in _eval_power  
>     Pow(Mul._from_args(nc), e, evaluate=False)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/decorators.py", line 78, in __sympifyit_wrapper  
>     return func(a, b)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/decorators.py", line 119, in binary_op_wrapper  
>     return func(self, other)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/expr.py", line 140, in __mul__  
>     return Mul(self, other)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/operations.py", line 41, in __new__  
>     c_part, nc_part, order_symbols = cls.flatten(args)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 182, in flatten  
>     if not a.is_zero and a.is_Rational:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1200, in _eval_is_irrational  
>     a = t.is_irrational  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 548, in _eval_is_prime  
>     return self.doit().is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/basic.py", line 1555, in doit  
>     return self.func(*terms)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 191, in __new__  
>     from sympy.functions.elementary.exponential import exp_polar  
>   File "<frozen importlib._bootstrap>", line 1019, in _handle_fromlist  
> RecursionError: maximum recursion depth exceeded while calling a Python object  
> ________________________________________________________________________________  
> ____________ sympy/matrices/tests/test_matrices.py:test_issue_3749 _____________  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/tests/test_matrices.py", line 1280, in test_issue_3749  
>     [exp(x), 1/x - exp(-x), x + 1/x]]).limit(x, oo) == \  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 4213, in limit  
>     lambda i, j: self[i, j].limit(*args))  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/dense.py", line 363, in _new  
>     rows, cols, flat_list = cls._handle_creation_inputs(*args, **kwargs)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 2276, in _handle_creation_inputs  
>     for j in range(cols)])  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 2276, in <listcomp>  
>     for j in range(cols)])  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 4213, in <lambda>  
>     lambda i, j: self[i, j].limit(*args))  
>   File "/home/swe-bench/sympy__sympy/sympy/core/expr.py", line 2788, in limit  
>     return limit(self, x, xlim, dir)  
>   File "/home/swe-bench/sympy__sympy/sympy/series/limits.py", line 49, in limit  
>     return Limit(e, z, z0, dir).doit(deep=False)  
>   File "/home/swe-bench/sympy__sympy/sympy/series/limits.py", line 178, in doit  
>     r = gruntz(e, z, z0, dir)  
>   File "/home/swe-bench/sympy__sympy/sympy/series/gruntz.py", line 648, in gruntz  
>     r = limitinf(e, z)  
>   File "/home/swe-bench/sympy__sympy/sympy/series/gruntz.py", line 428, in limitinf  
>     c0, e0 = mrv_leadterm(e, x)  
>   File "/home/swe-bench/sympy__sympy/sympy/series/gruntz.py", line 513, in mrv_leadterm  
>     series = calculate_series(f, w, logx=logw)  
>   File "/home/swe-bench/sympy__sympy/sympy/series/gruntz.py", line 466, in calculate_series  
>     for t in e.lseries(x, logx=logx):  
>   File "/home/swe-bench/sympy__sympy/sympy/core/expr.py", line 2613, in yield_lseries  
>     for si in s:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/expr.py", line 2678, in _eval_lseries  
>     series = self._eval_nseries(x, n=n, logx=logx)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1595, in _eval_nseries  
>     res = powsimp(self.func(*terms).expand(), combine='exp', deep=True)  
>   File "/home/swe-bench/sympy__sympy/sympy/simplify/powsimp.py", line 118, in powsimp  
>     expr = expr.func(*[recurse(w) for w in expr.args])  
>   File "/home/swe-bench/sympy__sympy/sympy/simplify/powsimp.py", line 118, in <listcomp>  
>     expr = expr.func(*[recurse(w) for w in expr.args])  
>   File "/home/swe-bench/sympy__sympy/sympy/simplify/powsimp.py", line 109, in recurse  
>     return powsimp(arg, _deep, _combine, _force, _measure)  
>   File "/home/swe-bench/sympy__sympy/sympy/simplify/powsimp.py", line 121, in powsimp  
>     return recurse(expr*_y, deep=False)/_y  
>   File "/home/swe-bench/sympy__sympy/sympy/core/decorators.py", line 78, in __sympifyit_wrapper  
>     return func(a, b)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/decorators.py", line 119, in binary_op_wrapper  
>     return func(self, other)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/expr.py", line 160, in __div__  
>     return Mul(self, Pow(other, S.NegativeOne))  
>   File "/home/swe-bench/sympy__sympy/sympy/core/operations.py", line 41, in __new__  
>     c_part, nc_part, order_symbols = cls.flatten(args)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 182, in flatten  
>     if not a.is_zero and a.is_Rational:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1066, in _eval_is_rational  
>     r = _fuzzy_group((a.is_rational for a in self.args), quick_exit=True)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/logic.py", line 78, in _fuzzy_group  
>     for a in args:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1066, in <genexpr>  
>     r = _fuzzy_group((a.is_rational for a in self.args), quick_exit=True)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   [Previous line repeated 1 more time]  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 1059, in _eval_is_algebraic  
>     if self.base.is_zero or (self.base - 1).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/operations.py", line 30, in __new__  
>     args = list(map(_sympify, args))  
>   File "/home/swe-bench/sympy__sympy/sympy/core/sympify.py", line 379, in _sympify  
>     return sympify(a, strict=True)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/sympify.py", line 243, in sympify  
>     if a in sympy_classes:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/numbers.py", line 1996, in __hash__  
>     return hash(self.p)  
> RecursionError: maximum recursion depth exceeded while calling a Python object  
> ________________________________________________________________________________  
> _______________ sympy/matrices/tests/test_matrices.py:test_limit _______________  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/tests/test_matrices.py", line 1847, in test_limit  
>     assert A.limit(x, 0) == Matrix(((1, 4, 1), (y, 2, 4), (10, 5, 1)))  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 4213, in limit  
>     lambda i, j: self[i, j].limit(*args))  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/dense.py", line 363, in _new  
>     rows, cols, flat_list = cls._handle_creation_inputs(*args, **kwargs)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 2276, in _handle_creation_inputs  
>     for j in range(cols)])  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 2276, in <listcomp>  
>     for j in range(cols)])  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 4213, in <lambda>  
>     lambda i, j: self[i, j].limit(*args))  
>   File "/home/swe-bench/sympy__sympy/sympy/core/expr.py", line 2788, in limit  
>     return limit(self, x, xlim, dir)  
>   File "/home/swe-bench/sympy__sympy/sympy/series/limits.py", line 49, in limit  
>     return Limit(e, z, z0, dir).doit(deep=False)  
>   File "/home/swe-bench/sympy__sympy/sympy/series/limits.py", line 178, in doit  
>     r = gruntz(e, z, z0, dir)  
>   File "/home/swe-bench/sympy__sympy/sympy/series/gruntz.py", line 658, in gruntz  
>     r = limitinf(e0, z)  
>   File "/home/swe-bench/sympy__sympy/sympy/series/gruntz.py", line 428, in limitinf  
>     c0, e0 = mrv_leadterm(e, x)  
>   File "/home/swe-bench/sympy__sympy/sympy/series/gruntz.py", line 487, in mrv_leadterm  
>     Omega, exps = mrv(e, x)  
>   File "/home/swe-bench/sympy__sympy/sympy/series/gruntz.py", line 246, in mrv  
>     e = powsimp(e, deep=True, combine='exp')  
>   File "/home/swe-bench/sympy__sympy/sympy/simplify/powsimp.py", line 118, in powsimp  
>     expr = expr.func(*[recurse(w) for w in expr.args])  
>   File "/home/swe-bench/sympy__sympy/sympy/simplify/powsimp.py", line 118, in <listcomp>  
>     expr = expr.func(*[recurse(w) for w in expr.args])  
>   File "/home/swe-bench/sympy__sympy/sympy/simplify/powsimp.py", line 109, in recurse  
>     return powsimp(arg, _deep, _combine, _force, _measure)  
>   File "/home/swe-bench/sympy__sympy/sympy/simplify/powsimp.py", line 118, in powsimp  
>     expr = expr.func(*[recurse(w) for w in expr.args])  
>   File "/home/swe-bench/sympy__sympy/sympy/simplify/powsimp.py", line 118, in <listcomp>  
>     expr = expr.func(*[recurse(w) for w in expr.args])  
>   File "/home/swe-bench/sympy__sympy/sympy/simplify/powsimp.py", line 109, in recurse  
>     return powsimp(arg, _deep, _combine, _force, _measure)  
>   File "/home/swe-bench/sympy__sympy/sympy/simplify/powsimp.py", line 121, in powsimp  
>     return recurse(expr*_y, deep=False)/_y  
>   File "/home/swe-bench/sympy__sympy/sympy/core/decorators.py", line 78, in __sympifyit_wrapper  
>     return func(a, b)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/decorators.py", line 119, in binary_op_wrapper  
>     return func(self, other)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/expr.py", line 160, in __div__  
>     return Mul(self, Pow(other, S.NegativeOne))  
>   File "/home/swe-bench/sympy__sympy/sympy/core/operations.py", line 41, in __new__  
>     c_part, nc_part, order_symbols = cls.flatten(args)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 182, in flatten  
>     if not a.is_zero and a.is_Rational:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1097, in _eval_is_integer  
>     is_rational = self.is_rational  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1066, in _eval_is_rational  
>     r = _fuzzy_group((a.is_rational for a in self.args), quick_exit=True)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/logic.py", line 78, in _fuzzy_group  
>     for a in args:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1066, in <genexpr>  
>     r = _fuzzy_group((a.is_rational for a in self.args), quick_exit=True)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 550, in _eval_is_prime  
>     if self.is_integer and self.is_positive:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 1059, in _eval_is_algebraic  
>     if self.base.is_zero or (self.base - 1).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/operations.py", line 30, in __new__  
>     args = list(map(_sympify, args))  
>   File "/home/swe-bench/sympy__sympy/sympy/core/sympify.py", line 379, in _sympify  
>     return sympify(a, strict=True)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/sympify.py", line 238, in sympify  
>     if global_evaluate[0] is False:  
> RecursionError: maximum recursion depth exceeded while calling a Python object  
> ________________________________________________________________________________  
> ____________ sympy/matrices/tests/test_matrices.py:test_matrix_norm ____________  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/tests/test_matrices.py", line 2011, in test_matrix_norm  
>     assert A.norm(2) == sqrt(S(389)/8 + sqrt(78665)/8)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 4515, in norm  
>     return Max(*self.singular_values())  
>   File "/home/swe-bench/sympy__sympy/sympy/functions/elementary/miscellaneous.py", line 334, in __new__  
>     _args = frozenset(cls._new_args_filter(args))  
>   File "/home/swe-bench/sympy__sympy/sympy/functions/elementary/miscellaneous.py", line 369, in _new_args_filter  
>     if (not isinstance(arg, Expr)) or (arg.is_real is False) or (arg is S.ComplexInfinity):  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/power.py", line 433, in _eval_is_real  
>     if self.base.is_positive:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 544, in _eval_is_positive  
>     return super(Add, self)._eval_is_positive()  
>   File "/home/swe-bench/sympy__sympy/sympy/core/expr.py", line 710, in _eval_is_positive  
>     n2 = self._eval_evalf(2)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/operations.py", line 312, in _eval_evalf  
>     x, tail = self.as_independent(Symbol, AppliedUndef)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/expr.py", line 1622, in as_independent  
>     if self.is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/operations.py", line 30, in __new__  
>     args = list(map(_sympify, args))  
>   File "/home/swe-bench/sympy__sympy/sympy/core/sympify.py", line 379, in _sympify  
>     return sympify(a, strict=True)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/sympify.py", line 243, in sympify  
>     if a in sympy_classes:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/numbers.py", line 1654, in __hash__  
>     return super(Rational, self).__hash__()  
> RecursionError: maximum recursion depth exceeded while calling a Python object  
> ________________________________________________________________________________  
> ___ sympy/matrices/tests/test_matrices.py:test_opportunistic_simplification ____  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/tests/test_matrices.py", line 2821, in test_opportunistic_simplification  
>     assert m.rank() == 1  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 4952, in rank  
>     row_reduced = self.rref(iszerofunc=iszerofunc, simplify=simplify)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 4994, in rref  
>     r[pivot:, i], iszerofunc, simpfunc)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 5392, in _find_reasonable_pivot  
>     is_zero = iszerofunc(x)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 34, in _iszero  
>     return x.is_zero  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/add.py", line 513, in _eval_is_zero  
>     if self.func(*nz).is_zero:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/operations.py", line 30, in __new__  
>     args = list(map(_sympify, args))  
>   File "/home/swe-bench/sympy__sympy/sympy/core/sympify.py", line 379, in _sympify  
>     return sympify(a, strict=True)  
> RecursionError: maximum recursion depth exceeded  
> ________________________________________________________________________________  
> ___________ sympy/matrices/tests/test_matrices.py:test_as_real_imag ____________  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/tests/test_matrices.py", line 2883, in test_as_real_imag  
>     a,b = kls(m3).as_real_imag()  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 1207, in as_real_imag  
>     return self._eval_as_real_imag()  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 1167, in _eval_as_real_imag  
>     return (self.applyfunc(re), self.applyfunc(im))  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 1203, in applyfunc  
>     return self._eval_applyfunc(f)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 1161, in _eval_applyfunc  
>     out = self._new(self.rows, self.cols, [f(x) for x in self])  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 1161, in <listcomp>  
>     out = self._new(self.rows, self.cols, [f(x) for x in self])  
>   File "/home/swe-bench/sympy__sympy/sympy/core/function.py", line 427, in __new__  
>     result = super(Function, cls).__new__(cls, *args, **options)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/function.py", line 250, in __new__  
>     evaluated = cls.eval(*args)  
>   File "/home/swe-bench/sympy__sympy/sympy/functions/elementary/complexes.py", line 59, in eval  
>     elif arg.is_imaginary or (S.ImaginaryUnit*arg).is_real:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1288, in _eval_is_even  
>     is_integer = self.is_integer  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 302, in _ask  
>     _ask(pk, obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1311, in _eval_is_prime  
>     return r.is_prime  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 247, in getit  
>     return _ask(fact, self)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/assumptions.py", line 290, in _ask  
>     a = evaluate(obj)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 1310, in _eval_is_prime  
>     r *= arg  
>   File "/home/swe-bench/sympy__sympy/sympy/core/decorators.py", line 78, in __sympifyit_wrapper  
>     return func(a, b)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/decorators.py", line 119, in binary_op_wrapper  
>     return func(self, other)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/expr.py", line 140, in __mul__  
>     return Mul(self, other)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/operations.py", line 41, in __new__  
>     c_part, nc_part, order_symbols = cls.flatten(args)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/mul.py", line 287, in flatten  
>     neg1e += S.Half  
>   File "/home/swe-bench/sympy__sympy/sympy/core/numbers.py", line 1877, in __add__  
>     return Rational(self.p*other.q + other.p, other.q, 1)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/numbers.py", line 1331, in __new__  
>     p = Rational(p)  
>   File "/home/swe-bench/sympy__sympy/sympy/core/numbers.py", line 1318, in __new__  
>     if isinstance(p, fractions.Fraction):  
>   File "/home/swe-bench/miniconda3/envs/sympy__sympy__1.0/lib/python3.7/abc.py", line 139, in __instancecheck__  
>     return _abc_instancecheck(cls, instance)  
> RecursionError: maximum recursion depth exceeded in comparison  
>   
>  tests finished: 137 passed, 3 skipped, 4 expected to fail, 8 exceptions,   
> in 30.35 seconds   
> DO *NOT* COMMIT!  
> /home/swe-bench/sympy__sympy/sympy/core/basic.py:3: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3,and in 3.9 it will stop working  
>   from collections import Mapping  
> /home/swe-bench/sympy__sympy/sympy/plotting/plot.py:28: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3,and in 3.9 it will stop working  
>   from collections import Callable  
> /home/swe-bench/sympy__sympy/sympy/core/basic.py:3: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3,and in 3.9 it will stop working  
>   from collections import Mapping  
> /home/swe-bench/sympy__sympy/sympy/plotting/plot.py:28: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3,and in 3.9 it will stop working  
>   from collections import Callable  
>   
> ERROR conda.cli.main_run:execute(124): `conda run bin/test -C --verbose sympy/matrices/tests/test_matrices.py` failed. (See above for error)  
>   
>    
> [sympy__sympy__1.0] [sympy__sympy-12454] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [sympy__sympy__1.0] [sympy__sympy-12454] Test script run successful   
> Attempt to fix test errors? yes  
> BadRequestError: OpenAIException - Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 366675 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}  
