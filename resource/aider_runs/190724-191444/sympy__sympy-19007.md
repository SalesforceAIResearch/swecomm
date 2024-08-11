
# aider chat started at 2024-07-19 18:20:26

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp4p8otj55/.git with 1,760 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Wrong matrix element fetched from BlockMatrix  
#### Given this code:  
#### ```  
#### from sympy import *  
#### n, i = symbols('n, i', integer=True)  
#### A = MatrixSymbol('A', 1, 1)  
#### B = MatrixSymbol('B', n, 1)  
#### C = BlockMatrix([[A], [B]])  
#### print('C is')  
#### pprint(C)  
#### print('C[i, 0] is')  
#### pprint(C[i, 0])  
#### ```  
#### I get this output:  
#### ```  
#### C is  
#### ⎡A⎤  
#### ⎢ ⎥  
#### ⎣B⎦  
#### C[i, 0] is  
#### (A)[i, 0]  
#### ```  
#### `(A)[i, 0]` is the wrong here. `C[i, 0]` should not be simplified as that element may come from either `A` or `B`.  
> 33512 prompt tokens, 53 completion tokens, $0.168355 cost  

To address the issue with fetching the wrong matrix element from `BlockMatrix`, the most likely file that needs changes is:

- `sympy/matrices/expressions/blockmatrix.py`

Please add this file to the chat so I can proceed with the necessary modifications.

> sympy/matrices/expressions/blockmatrix.py  
> Add these files to the chat? yes  
> 8445 prompt tokens, 302 completion tokens, $0.046755 cost  

To fix the issue with fetching the wrong matrix element from `BlockMatrix`, we need to modify the `_entry` method in `sympy/matrices/expressions/blockmatrix.py`. The current implementation incorrectly simplifies the element access, which can lead to incorrect results.

Here are the necessary changes:

sympy/matrices/expressions/blockmatrix.py
```python
<<<<<<< SEARCH
        # Find row entry
        for row_block, numrows in enumerate(self.rowblocksizes):
            if (i < numrows) != False:
                break
            else:
                i -= numrows
        for col_block, numcols in enumerate(self.colblocksizes):
            if (j < numcols) != False:
                break
            else:
                j -= numcols
        return self.blocks[row_block, col_block][i, j]
=======
        # Find row entry
        row_block = 0
        for numrows in self.rowblocksizes:
            if i < numrows:
                break
            i -= numrows
            row_block += 1

        # Find column entry
        col_block = 0
        for numcols in self.colblocksizes:
            if j < numcols:
                break
            j -= numcols
            col_block += 1

        return self.blocks[row_block, col_block]._entry(i, j, **kwargs)
>>>>>>> REPLACE
```

This change ensures that the correct matrix element is fetched without incorrect simplification.

> Applied edit to sympy/matrices/expressions/blockmatrix.py  
>   
> Test Script: conda run -n sympy__sympy__1.6  bin/test -C --verbose sympy/matrices/expressions/tests/test_blockmatrix.py sympy/matrices/expressions/tests/test_indexing.py;  
> [sympy__sympy__1.6] [sympy__sympy-19007] Command: conda run -n sympy__sympy__1.6 bin/test -C --verbose sympy/matrices/expressions/tests/test_blockmatrix.py sympy/matrices/expressions/tests/test_indexing.py   
> [sympy__sympy__1.6] [sympy__sympy-19007] Subprocess args: {"cwd": "/home/swe-bench/sympy__sympy", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [sympy__sympy__1.6] [sympy__sympy-19007] Std. Output:  
> ERROR conda.cli.main_run:execute(124): `conda run bin/test -C --verbose sympy/matrices/expressions/tests/test_blockmatrix.py sympy/matrices/expressions/tests/test_indexing.py` failed. (See above for error)  
> ============================= test process starts ==============================  
> executable:         /home/swe-bench/miniconda3/envs/sympy__sympy__1.6/bin/python  (3.9.19-final-0) [CPython]  
> architecture:       64-bit  
> cache:              no  
> ground types:       python   
> numpy:              None  
> random seed:        6286546  
> hash randomization: on (PYTHONHASHSEED=2462964372)  
>   
> sympy/matrices/expressions/tests/test_blockmatrix.py[17]   
> test_bc_matmul ok  
> test_bc_matadd ok  
> test_bc_transpose ok  
> test_bc_dist_diag ok  
> test_block_plus_ident ok  
> test_BlockMatrix ok  
> test_block_collapse_explicit_matrices ok  
> test_issue_17624 ok  
> test_issue_18618 ok  
> test_BlockMatrix_trace ok  
> test_BlockMatrix_Determinant ok  
> test_squareBlockMatrix ok  
> test_BlockDiagMatrix ok  
> test_blockcut E  
> test_reblock_2x2 ok  
> test_deblock ok  
> test_block_collapse_type ok                                               [FAIL]  
>   
> sympy/matrices/expressions/tests/test_indexing.py[11]   
> test_symbolic_indexing ok  
> test_add_index ok  
> test_mul_index ok  
> test_pow_index ok  
> test_transpose_index ok  
> test_Identity_index ok  
> test_block_index ok  
> test_slicing ok  
> test_errors ok  
> test_matrix_expression_to_indices ok  
> test_matrix_expression_from_index_summation ok                              [OK]  
>   
>   
> ________________________________________________________________________________  
> ______ sympy/matrices/expressions/tests/test_blockmatrix.py:test_blockcut ______  
> Traceback (most recent call last):  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/tests/test_blockmatrix.py", line 195, in test_blockcut  
>     assert A[i, j] == B[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 296, in __getitem__  
>     return self._entry(i, j)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/blockmatrix.py", line 239, in _entry  
>     if i < numrows:  
>   File "/home/swe-bench/sympy__sympy/sympy/core/relational.py", line 391, in __nonzero__  
>     raise TypeError("cannot determine truth value of Relational")  
> TypeError: cannot determine truth value of Relational  
>   
> =========== tests finished: 27 passed, 1 exceptions, in 0.66 seconds ===========  
> DO *NOT* COMMIT!  
>   
>    
> [sympy__sympy__1.6] [sympy__sympy-19007] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [sympy__sympy__1.6] [sympy__sympy-19007] Test script run successful   
> Attempt to fix test errors? yes  
> 9667 prompt tokens, 360 completion tokens, $0.053735 cost  

The error indicates that the comparison `if i < numrows:` is causing a `TypeError` because `i` can be a symbolic expression, and symbolic expressions cannot be directly compared using standard comparison operators.

To fix this, we need to use SymPy's relational operators for symbolic comparisons. Here are the necessary changes:

sympy/matrices/expressions/blockmatrix.py
```python
<<<<<<< SEARCH
        # Find row entry
        row_block = 0
        for numrows in self.rowblocksizes:
            if i < numrows:
                break
            i -= numrows
            row_block += 1

        # Find column entry
        col_block = 0
        for numcols in self.colblocksizes:
            if j < numcols:
                break
            j -= numcols
            col_block += 1

        return self.blocks[row_block, col_block]._entry(i, j, **kwargs)
=======
        from sympy import Ge

        # Find row entry
        row_block = 0
        for numrows in self.rowblocksizes:
            if not Ge(i, numrows):
                break
            i -= numrows
            row_block += 1

        # Find column entry
        col_block = 0
        for numcols in self.colblocksizes:
            if not Ge(j, numcols):
                break
            j -= numcols
            col_block += 1

        return self.blocks[row_block, col_block]._entry(i, j, **kwargs)
>>>>>>> REPLACE
```

This change uses SymPy's `Ge` (greater than or equal) function to handle symbolic comparisons properly. This should resolve the `TypeError` and ensure that the correct matrix element is fetched.

> Applied edit to sympy/matrices/expressions/blockmatrix.py  
>   
> Test Script: conda run -n sympy__sympy__1.6  bin/test -C --verbose sympy/matrices/expressions/tests/test_blockmatrix.py sympy/matrices/expressions/tests/test_indexing.py;  
> [sympy__sympy__1.6] [sympy__sympy-19007] Command: conda run -n sympy__sympy__1.6 bin/test -C --verbose sympy/matrices/expressions/tests/test_blockmatrix.py sympy/matrices/expressions/tests/test_indexing.py   
> [sympy__sympy__1.6] [sympy__sympy-19007] Subprocess args: {"cwd": "/home/swe-bench/sympy__sympy", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [sympy__sympy__1.6] [sympy__sympy-19007] Std. Output:  
> ERROR conda.cli.main_run:execute(124): `conda run bin/test -C --verbose sympy/matrices/expressions/tests/test_blockmatrix.py sympy/matrices/expressions/tests/test_indexing.py` failed. (See above for error)  
> ============================= test process starts ==============================  
> executable:         /home/swe-bench/miniconda3/envs/sympy__sympy__1.6/bin/python  (3.9.19-final-0) [CPython]  
> architecture:       64-bit  
> cache:              no  
> ground types:       python   
> numpy:              None  
> random seed:        6585161  
> hash randomization: on (PYTHONHASHSEED=2866811566)  
>   
> sympy/matrices/expressions/tests/test_blockmatrix.py[17]   
> test_bc_matmul ok  
> test_bc_matadd ok  
> test_bc_transpose ok  
> test_bc_dist_diag ok  
> test_block_plus_ident ok  
> test_BlockMatrix ok  
> test_block_collapse_explicit_matrices ok  
> test_issue_17624 ok  
> test_issue_18618 ok  
> test_BlockMatrix_trace ok  
> test_BlockMatrix_Determinant ok  
> test_squareBlockMatrix ok  
> test_BlockDiagMatrix ok  
> test_blockcut E  
> test_reblock_2x2 ok  
> test_deblock ok  
> test_block_collapse_type ok                                               [FAIL]  
>   
> sympy/matrices/expressions/tests/test_indexing.py[11]   
> test_symbolic_indexing ok  
> test_add_index ok  
> test_mul_index ok  
> test_pow_index ok  
> test_transpose_index ok  
> test_Identity_index ok  
> test_block_index ok  
> test_slicing ok  
> test_errors ok  
> test_matrix_expression_to_indices ok  
> test_matrix_expression_from_index_summation ok                              [OK]  
>   
>   
> ________________________________________________________________________________  
> ______ sympy/matrices/expressions/tests/test_blockmatrix.py:test_blockcut ______  
> Traceback (most recent call last):  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/tests/test_blockmatrix.py", line 195, in test_blockcut  
>     assert A[i, j] == B[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 296, in __getitem__  
>     return self._entry(i, j)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/blockmatrix.py", line 241, in _entry  
>     if not Ge(i, numrows):  
>   File "/home/swe-bench/sympy__sympy/sympy/core/relational.py", line 391, in __nonzero__  
>     raise TypeError("cannot determine truth value of Relational")  
> TypeError: cannot determine truth value of Relational  
>   
> =========== tests finished: 27 passed, 1 exceptions, in 0.65 seconds ===========  
> DO *NOT* COMMIT!  
>   
>    
> [sympy__sympy__1.6] [sympy__sympy-19007] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [sympy__sympy__1.6] [sympy__sympy-19007] Test script run successful   
> Attempt to fix test errors? yes  
> 10944 prompt tokens, 376 completion tokens, $0.060360 cost  

The error indicates that the comparison `if not Ge(i, numrows):` is causing a `TypeError` because `Ge` returns a relational object, and relational objects cannot be directly used in boolean contexts.

To fix this, we need to use SymPy's `is_true` function to evaluate the relational object. Here are the necessary changes:

sympy/matrices/expressions/blockmatrix.py
```python
<<<<<<< SEARCH
        from sympy import Ge

        # Find row entry
        row_block = 0
        for numrows in self.rowblocksizes:
            if not Ge(i, numrows):
                break
            i -= numrows
            row_block += 1

        # Find column entry
        col_block = 0
        for numcols in self.colblocksizes:
            if not Ge(j, numcols):
                break
            j -= numcols
            col_block += 1

        return self.blocks[row_block, col_block]._entry(i, j, **kwargs)
=======
        from sympy import Ge, is_true

        # Find row entry
        row_block = 0
        for numrows in self.rowblocksizes:
            if is_true(i < numrows):
                break
            i -= numrows
            row_block += 1

        # Find column entry
        col_block = 0
        for numcols in self.colblocksizes:
            if is_true(j < numcols):
                break
            j -= numcols
            col_block += 1

        return self.blocks[row_block, col_block]._entry(i, j, **kwargs)
>>>>>>> REPLACE
```

This change uses SymPy's `is_true` function to evaluate the relational object properly. This should resolve the `TypeError` and ensure that the correct matrix element is fetched.

> Applied edit to sympy/matrices/expressions/blockmatrix.py  
>   
> Test Script: conda run -n sympy__sympy__1.6  bin/test -C --verbose sympy/matrices/expressions/tests/test_blockmatrix.py sympy/matrices/expressions/tests/test_indexing.py;  
> [sympy__sympy__1.6] [sympy__sympy-19007] Command: conda run -n sympy__sympy__1.6 bin/test -C --verbose sympy/matrices/expressions/tests/test_blockmatrix.py sympy/matrices/expressions/tests/test_indexing.py   
> [sympy__sympy__1.6] [sympy__sympy-19007] Subprocess args: {"cwd": "/home/swe-bench/sympy__sympy", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [sympy__sympy__1.6] [sympy__sympy-19007] Std. Output:  
> ERROR conda.cli.main_run:execute(124): `conda run bin/test -C --verbose sympy/matrices/expressions/tests/test_blockmatrix.py sympy/matrices/expressions/tests/test_indexing.py` failed. (See above for error)  
> ============================= test process starts ==============================  
> executable:         /home/swe-bench/miniconda3/envs/sympy__sympy__1.6/bin/python  (3.9.19-final-0) [CPython]  
> architecture:       64-bit  
> cache:              no  
> ground types:       python   
> numpy:              None  
> random seed:        44930191  
> hash randomization: on (PYTHONHASHSEED=1843373204)  
>   
> sympy/matrices/expressions/tests/test_blockmatrix.py[17]   
> test_bc_matmul ok  
> test_bc_matadd ok  
> test_bc_transpose ok  
> test_bc_dist_diag ok  
> test_block_plus_ident ok  
> test_BlockMatrix ok  
> test_block_collapse_explicit_matrices ok  
> test_issue_17624 ok  
> test_issue_18618 E  
> test_BlockMatrix_trace ok  
> test_BlockMatrix_Determinant ok  
> test_squareBlockMatrix ok  
> test_BlockDiagMatrix ok  
> test_blockcut E  
> test_reblock_2x2 E  
> test_deblock ok  
> test_block_collapse_type ok                                               [FAIL]  
>   
> sympy/matrices/expressions/tests/test_indexing.py[11]   
> test_symbolic_indexing ok  
> test_add_index ok  
> test_mul_index ok  
> test_pow_index ok  
> test_transpose_index ok  
> test_Identity_index ok  
> test_block_index E  
> test_slicing ok  
> test_errors ok  
> test_matrix_expression_to_indices ok  
> test_matrix_expression_from_index_summation ok                            [FAIL]  
>   
>   
> ________________________________________________________________________________  
> ____ sympy/matrices/expressions/tests/test_blockmatrix.py:test_issue_18618 _____  
> Traceback (most recent call last):  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/tests/test_blockmatrix.py", line 115, in test_issue_18618  
>     assert A == Matrix(BlockDiagMatrix(A))  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/dense.py", line 296, in __new__  
>     return cls._new(*args, **kwargs)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/dense.py", line 308, in _new  
>     rows, cols, flat_list = cls._handle_creation_inputs(*args, **kwargs)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 974, in _handle_creation_inputs  
>     return args[0].rows, args[0].cols, args[0].as_explicit()._mat  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 345, in as_explicit  
>     return ImmutableDenseMatrix([[    self[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 345, in <listcomp>  
>     return ImmutableDenseMatrix([[    self[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 345, in <listcomp>  
>     return ImmutableDenseMatrix([[    self[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 296, in __getitem__  
>     return self._entry(i, j)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/blockmatrix.py", line 236, in _entry  
>     from sympy import Ge, is_true  
> ImportError: cannot import name 'is_true' from 'sympy' (/home/swe-bench/sympy__sympy/sympy/__init__.py)  
> ________________________________________________________________________________  
> ______ sympy/matrices/expressions/tests/test_blockmatrix.py:test_blockcut ______  
> Traceback (most recent call last):  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/tests/test_blockmatrix.py", line 195, in test_blockcut  
>     assert A[i, j] == B[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 296, in __getitem__  
>     return self._entry(i, j)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/blockmatrix.py", line 236, in _entry  
>     from sympy import Ge, is_true  
> ImportError: cannot import name 'is_true' from 'sympy' (/home/swe-bench/sympy__sympy/sympy/__init__.py)  
> ________________________________________________________________________________  
> ____ sympy/matrices/expressions/tests/test_blockmatrix.py:test_reblock_2x2 _____  
> Traceback (most recent call last):  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/tests/test_blockmatrix.py", line 216, in test_reblock_2x2  
>     assert B.as_explicit() == BB.as_explicit()  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 345, in as_explicit  
>     return ImmutableDenseMatrix([[    self[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 345, in <listcomp>  
>     return ImmutableDenseMatrix([[    self[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 345, in <listcomp>  
>     return ImmutableDenseMatrix([[    self[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 296, in __getitem__  
>     return self._entry(i, j)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/blockmatrix.py", line 236, in _entry  
>     from sympy import Ge, is_true  
> ImportError: cannot import name 'is_true' from 'sympy' (/home/swe-bench/sympy__sympy/sympy/__init__.py)  
> ________________________________________________________________________________  
> ______ sympy/matrices/expressions/tests/test_indexing.py:test_block_index ______  
> Traceback (most recent call last):  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/tests/test_indexing.py", line 75, in test_block_index  
>     assert B[0, 0] == B[3, 0] == B[0, 3] == B[3, 3] == 1  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 296, in __getitem__  
>     return self._entry(i, j)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/blockmatrix.py", line 236, in _entry  
>     from sympy import Ge, is_true  
> ImportError: cannot import name 'is_true' from 'sympy' (/home/swe-bench/sympy__sympy/sympy/__init__.py)  
>   
> =========== tests finished: 24 passed, 4 exceptions, in 0.66 seconds ===========  
> DO *NOT* COMMIT!  
>   
>    
> [sympy__sympy__1.6] [sympy__sympy-19007] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [sympy__sympy__1.6] [sympy__sympy-19007] Test script run successful   
> Attempt to fix test errors? yes  
> 13405 prompt tokens, 128 completion tokens, $0.068945 cost  

The error indicates that the `is_true` function is not available in the `sympy` module. Instead, we should use `sympy.core.logic` to import `is_true`.

Here are the necessary changes:

sympy/matrices/expressions/blockmatrix.py
```python
<<<<<<< SEARCH
        from sympy import Ge, is_true
=======
        from sympy import Ge
        from sympy.core.logic import is_true
>>>>>>> REPLACE
```

This change ensures that `is_true` is correctly imported from `sympy.core.logic`. This should resolve the `ImportError` and allow the tests to pass.

> Applied edit to sympy/matrices/expressions/blockmatrix.py  
>   
> Test Script: conda run -n sympy__sympy__1.6  bin/test -C --verbose sympy/matrices/expressions/tests/test_blockmatrix.py sympy/matrices/expressions/tests/test_indexing.py;  
> [sympy__sympy__1.6] [sympy__sympy-19007] Command: conda run -n sympy__sympy__1.6 bin/test -C --verbose sympy/matrices/expressions/tests/test_blockmatrix.py sympy/matrices/expressions/tests/test_indexing.py   
> [sympy__sympy__1.6] [sympy__sympy-19007] Subprocess args: {"cwd": "/home/swe-bench/sympy__sympy", "check": false, "shell": false, "universal_newlines": true, "stdout": -1, "stderr": -2, "timeout": 60}   
> [sympy__sympy__1.6] [sympy__sympy-19007] Std. Output:  
> ERROR conda.cli.main_run:execute(124): `conda run bin/test -C --verbose sympy/matrices/expressions/tests/test_blockmatrix.py sympy/matrices/expressions/tests/test_indexing.py` failed. (See above for error)  
> ============================= test process starts ==============================  
> executable:         /home/swe-bench/miniconda3/envs/sympy__sympy__1.6/bin/python  (3.9.19-final-0) [CPython]  
> architecture:       64-bit  
> cache:              no  
> ground types:       python   
> numpy:              None  
> random seed:        2016721  
> hash randomization: on (PYTHONHASHSEED=846635122)  
>   
> sympy/matrices/expressions/tests/test_blockmatrix.py[17]   
> test_bc_matmul ok  
> test_bc_matadd ok  
> test_bc_transpose ok  
> test_bc_dist_diag ok  
> test_block_plus_ident ok  
> test_BlockMatrix ok  
> test_block_collapse_explicit_matrices ok  
> test_issue_17624 ok  
> test_issue_18618 E  
> test_BlockMatrix_trace ok  
> test_BlockMatrix_Determinant ok  
> test_squareBlockMatrix ok  
> test_BlockDiagMatrix ok  
> test_blockcut E  
> test_reblock_2x2 E  
> test_deblock ok  
> test_block_collapse_type ok                                               [FAIL]  
>   
> sympy/matrices/expressions/tests/test_indexing.py[11]   
> test_symbolic_indexing ok  
> test_add_index ok  
> test_mul_index ok  
> test_pow_index ok  
> test_transpose_index ok  
> test_Identity_index ok  
> test_block_index E  
> test_slicing ok  
> test_errors ok  
> test_matrix_expression_to_indices ok  
> test_matrix_expression_from_index_summation ok                            [FAIL]  
>   
>   
> ________________________________________________________________________________  
> ____ sympy/matrices/expressions/tests/test_blockmatrix.py:test_issue_18618 _____  
> Traceback (most recent call last):  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/tests/test_blockmatrix.py", line 115, in test_issue_18618  
>     assert A == Matrix(BlockDiagMatrix(A))  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/dense.py", line 296, in __new__  
>     return cls._new(*args, **kwargs)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/dense.py", line 308, in _new  
>     rows, cols, flat_list = cls._handle_creation_inputs(*args, **kwargs)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/matrices.py", line 974, in _handle_creation_inputs  
>     return args[0].rows, args[0].cols, args[0].as_explicit()._mat  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 345, in as_explicit  
>     return ImmutableDenseMatrix([[    self[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 345, in <listcomp>  
>     return ImmutableDenseMatrix([[    self[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 345, in <listcomp>  
>     return ImmutableDenseMatrix([[    self[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 296, in __getitem__  
>     return self._entry(i, j)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/blockmatrix.py", line 237, in _entry  
>     from sympy.core.logic import is_true  
> ImportError: cannot import name 'is_true' from 'sympy.core.logic' (/home/swe-bench/sympy__sympy/sympy/core/logic.py)  
> ________________________________________________________________________________  
> ______ sympy/matrices/expressions/tests/test_blockmatrix.py:test_blockcut ______  
> Traceback (most recent call last):  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/tests/test_blockmatrix.py", line 195, in test_blockcut  
>     assert A[i, j] == B[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 296, in __getitem__  
>     return self._entry(i, j)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/blockmatrix.py", line 237, in _entry  
>     from sympy.core.logic import is_true  
> ImportError: cannot import name 'is_true' from 'sympy.core.logic' (/home/swe-bench/sympy__sympy/sympy/core/logic.py)  
> ________________________________________________________________________________  
> ____ sympy/matrices/expressions/tests/test_blockmatrix.py:test_reblock_2x2 _____  
> Traceback (most recent call last):  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/tests/test_blockmatrix.py", line 216, in test_reblock_2x2  
>     assert B.as_explicit() == BB.as_explicit()  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 345, in as_explicit  
>     return ImmutableDenseMatrix([[    self[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 345, in <listcomp>  
>     return ImmutableDenseMatrix([[    self[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 345, in <listcomp>  
>     return ImmutableDenseMatrix([[    self[i, j]  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 296, in __getitem__  
>     return self._entry(i, j)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/blockmatrix.py", line 237, in _entry  
>     from sympy.core.logic import is_true  
> ImportError: cannot import name 'is_true' from 'sympy.core.logic' (/home/swe-bench/sympy__sympy/sympy/core/logic.py)  
> ________________________________________________________________________________  
> ______ sympy/matrices/expressions/tests/test_indexing.py:test_block_index ______  
> Traceback (most recent call last):  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/tests/test_indexing.py", line 75, in test_block_index  
>     assert B[0, 0] == B[3, 0] == B[0, 3] == B[3, 3] == 1  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/matexpr.py", line 296, in __getitem__  
>     return self._entry(i, j)  
>   File "/home/swe-bench/sympy__sympy/sympy/matrices/expressions/blockmatrix.py", line 237, in _entry  
>     from sympy.core.logic import is_true  
> ImportError: cannot import name 'is_true' from 'sympy.core.logic' (/home/swe-bench/sympy__sympy/sympy/core/logic.py)  
>   
> =========== tests finished: 24 passed, 4 exceptions, in 0.63 seconds ===========  
> DO *NOT* COMMIT!  
>   
>    
> [sympy__sympy__1.6] [sympy__sympy-19007] Return Code: 1   
>   
> >>>>> Some Tests Failed  
> [sympy__sympy__1.6] [sympy__sympy-19007] Test script run successful   
> Attempt to fix test errors? yes  
> Only 4 reflections allowed, stopping.  
