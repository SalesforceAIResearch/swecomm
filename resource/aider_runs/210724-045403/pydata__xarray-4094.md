
# aider chat started at 2024-07-20 23:09:09

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpbwzw7tf8/.git with 258 files  
> Repo-map: using 2048 tokens  

#### to_unstacked_dataset broken for single-dim variables  
#### <!-- A short summary of the issue, if appropriate -->  
####   
####   
#### #### MCVE Code Sample  
####   
#### ```python  
#### arr = xr.DataArray(  
####      np.arange(3),  
####      coords=[("x", [0, 1, 2])],  
####  )  
#### data = xr.Dataset({"a": arr, "b": arr})  
#### stacked = data.to_stacked_array('y', sample_dims=['x'])  
#### unstacked = stacked.to_unstacked_dataset('y')  
#### # MergeError: conflicting values for variable 'y' on objects to be combined. You can skip this check by specifying compat='override'.  
#### ```  
####   
#### #### Expected Output  
#### A working roundtrip.  
####   
#### #### Problem Description  
#### I need to stack a bunch of variables and later unstack them again, however this doesn't work if the variables only have a single dimension.  
####   
#### #### Versions  
####   
#### <details><summary>Output of <tt>xr.show_versions()</tt></summary>  
####   
#### INSTALLED VERSIONS  
#### ------------------  
#### commit: None  
#### python: 3.7.3 (default, Mar 27 2019, 22:11:17)   
#### [GCC 7.3.0]  
#### python-bits: 64  
#### OS: Linux  
#### OS-release: 4.15.0-96-generic  
#### machine: x86_64  
#### processor: x86_64  
#### byteorder: little  
#### LC_ALL: None  
#### LANG: en_GB.UTF-8  
#### LOCALE: en_GB.UTF-8  
#### libhdf5: 1.10.4  
#### libnetcdf: 4.6.2  
####   
#### xarray: 0.15.1  
#### pandas: 1.0.3  
#### numpy: 1.17.3  
#### scipy: 1.3.1  
#### netCDF4: 1.4.2  
#### pydap: None  
#### h5netcdf: None  
#### h5py: 2.10.0  
#### Nio: None  
#### zarr: None  
#### cftime: 1.0.4.2  
#### nc_time_axis: None  
#### PseudoNetCDF: None  
#### rasterio: None  
#### cfgrib: None  
#### iris: None  
#### bottleneck: None  
#### dask: 2.10.1  
#### distributed: 2.10.0  
#### matplotlib: 3.1.1  
#### cartopy: None  
#### seaborn: 0.10.0  
#### numbagg: None  
#### setuptools: 41.0.0  
#### pip: 19.0.3  
#### conda: 4.8.3  
#### pytest: 5.3.5  
#### IPython: 7.9.0  
#### sphinx: None  
####   
####   
#### </details>  
####  
> 33862 prompt tokens, 91 completion tokens, $0.170675 cost  

To address the issue with `to_unstacked_dataset` for single-dimension variables, we will likely need to make changes to the following files:

1. `xarray/core/dataset.py`: This file contains the `to_stacked_array` and `to_unstacked_dataset` methods, which are directly related to the issue described.

Please add `xarray/core/dataset.py` to the chat so I can proceed with the necessary changes.

> xarray/core/dataset.py  
> Add these files to the chat? yes  
> 57235 prompt tokens, 1262 completion tokens, $0.305105 cost  

To fix the issue with `to_unstacked_dataset` for single-dimension variables, we need to modify the `to_stacked_array` and `to_unstacked_dataset` methods in `xarray/core/dataset.py`.

Here are the necessary changes:

xarray/core/dataset.py
```python
<<<<<<< SEARCH
        stacking_dims = tuple(dim for dim in self.dims if dim not in sample_dims)

        for variable in self:
            dims = self[variable].dims
            dims_include_sample_dims = set(sample_dims) <= set(dims)
            if not dims_include_sample_dims:
                raise ValueError(
                    "All variables in the dataset must contain the "
                    "dimensions {}.".format(dims)
                )

        def ensure_stackable(val):
            assign_coords = {variable_dim: val.name}
            for dim in stacking_dims:
                if dim not in val.dims:
                    assign_coords[dim] = None

            expand_dims = set(stacking_dims).difference(set(val.dims))
            expand_dims.add(variable_dim)
            # must be list for .expand_dims
            expand_dims = list(expand_dims)

            return (
                val.assign_coords(**assign_coords)
                .expand_dims(expand_dims)
                .stack({new_dim: (variable_dim,) + stacking_dims})
            )

        # concatenate the arrays
        stackable_vars = [ensure_stackable(self[key]) for key in self.data_vars]
        data_array = xr.concat(stackable_vars, dim=new_dim)

        # coerce the levels of the MultiIndex to have the same type as the
        # input dimensions. This code is messy, so it might be better to just
        # input a dummy value for the singleton dimension.
        idx = data_array.indexes[new_dim]
        levels = [idx.levels[0]] + [
            level.astype(self[level.name].dtype) for level in idx.levels[1:]
        ]
        new_idx = idx.set_levels(levels)
        data_array[new_dim] = IndexVariable(new_dim, new_idx)

        if name is not None:
            data_array.name = name

        return data_array
=======
        stacking_dims = tuple(dim for dim in self.dims if dim not in sample_dims)

        for variable in self:
            dims = self[variable].dims
            dims_include_sample_dims = set(sample_dims) <= set(dims)
            if not dims_include_sample_dims:
                raise ValueError(
                    "All variables in the dataset must contain the "
                    "dimensions {}.".format(dims)
                )

        def ensure_stackable(val):
            assign_coords = {variable_dim: val.name}
            for dim in stacking_dims:
                if dim not in val.dims:
                    assign_coords[dim] = None

            expand_dims = set(stacking_dims).difference(set(val.dims))
            expand_dims.add(variable_dim)
            # must be list for .expand_dims
            expand_dims = list(expand_dims)

            stacked = val.assign_coords(**assign_coords).expand_dims(expand_dims)
            if stacking_dims:
                stacked = stacked.stack({new_dim: (variable_dim,) + stacking_dims})
            else:
                stacked = stacked.rename({variable_dim: new_dim})
            return stacked

        # concatenate the arrays
        stackable_vars = [ensure_stackable(self[key]) for key in self.data_vars]
        data_array = xr.concat(stackable_vars, dim=new_dim)

        # coerce the levels of the MultiIndex to have the same type as the
        # input dimensions. This code is messy, so it might be better to just
        # input a dummy value for the singleton dimension.
        idx = data_array.indexes[new_dim]
        levels = [idx.levels[0]] + [
            level.astype(self[level.name].dtype) for level in idx.levels[1:]
        ]
        new_idx = idx.set_levels(levels)
        data_array[new_dim] = IndexVariable(new_dim, new_idx)

        if name is not None:
            data_array.name = name

        return data_array
>>>>>>> REPLACE
```

xarray/core/dataset.py
```python
<<<<<<< SEARCH
    def to_unstacked_dataset(self, dim: Hashable) -> "Dataset":
        """Unstack a DataArray with a MultiIndex dimension into a Dataset.

        This is the inverse operation of Dataset.to_stacked_array.

        Parameters
        ----------
        dim : Hashable
            Name of the existing dimension to unstack.

        Returns
        -------
        unstacked : Dataset
        """
        idx = self.indexes[dim]
        if not isinstance(idx, pd.MultiIndex):
            raise ValueError(f"{dim} is not a MultiIndex")

        variables = {}
        for name, var in self.variables.items():
            if dim in var.dims:
                unstacked = var.unstack(dim)
                for level in idx.names:
                    variables[f"{name}_{level}"] = unstacked[level]
            else:
                variables[name] = var

        return self._replace(variables)
=======
    def to_unstacked_dataset(self, dim: Hashable) -> "Dataset":
        """Unstack a DataArray with a MultiIndex dimension into a Dataset.

        This is the inverse operation of Dataset.to_stacked_array.

        Parameters
        ----------
        dim : Hashable
            Name of the existing dimension to unstack.

        Returns
        -------
        unstacked : Dataset
        """
        idx = self.indexes[dim]
        if not isinstance(idx, pd.MultiIndex):
            raise ValueError(f"{dim} is not a MultiIndex")

        variables = {}
        for name, var in self.variables.items():
            if dim in var.dims:
                unstacked = var.unstack(dim)
                if unstacked.ndim == 1:
                    variables[name] = unstacked
                else:
                    for level in idx.names:
                        variables[f"{name}_{level}"] = unstacked[level]
            else:
                variables[name] = var

        return self._replace(variables)
>>>>>>> REPLACE
```

> The LLM did not conform to the edit format.  
> For more info see: https://aider.chat/docs/faq.html#aider-isnt-editing-my-files  
> # 1 SEARCH/REPLACE block failed to match!  
>   
> ## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in xarray/core/dataset.py  
> <<<<<<< SEARCH  
>     def to_unstacked_dataset(self, dim: Hashable) -> "Dataset":  
>         """Unstack a DataArray with a MultiIndex dimension into a Dataset.  
>   
>         This is the inverse operation of Dataset.to_stacked_array.  
>   
>         Parameters  
>         ----------  
>         dim : Hashable  
>             Name of the existing dimension to unstack.  
>   
>         Returns  
>         -------  
>         unstacked : Dataset  
>         """  
>         idx = self.indexes[dim]  
>         if not isinstance(idx, pd.MultiIndex):  
>             raise ValueError(f"{dim} is not a MultiIndex")  
>   
>         variables = {}  
>         for name, var in self.variables.items():  
>             if dim in var.dims:  
>                 unstacked = var.unstack(dim)  
>                 for level in idx.names:  
>                     variables[f"{name}_{level}"] = unstacked[level]  
>             else:  
>                 variables[name] = var  
>   
>         return self._replace(variables)  
> =======  
>     def to_unstacked_dataset(self, dim: Hashable) -> "Dataset":  
>         """Unstack a DataArray with a MultiIndex dimension into a Dataset.  
>   
>         This is the inverse operation of Dataset.to_stacked_array.  
>   
>         Parameters  
>         ----------  
>         dim : Hashable  
>             Name of the existing dimension to unstack.  
>   
>         Returns  
>         -------  
>         unstacked : Dataset  
>         """  
>         idx = self.indexes[dim]  
>         if not isinstance(idx, pd.MultiIndex):  
>             raise ValueError(f"{dim} is not a MultiIndex")  
>   
>         variables = {}  
>         for name, var in self.variables.items():  
>             if dim in var.dims:  
>                 unstacked = var.unstack(dim)  
>                 if unstacked.ndim == 1:  
>                     variables[name] = unstacked  
>                 else:  
>                     for level in idx.names:  
>                         variables[f"{name}_{level}"] = unstacked[level]  
>             else:  
>                 variables[name] = var  
>   
>         return self._replace(variables)  
> >>>>>>> REPLACE  
>   
> The SEARCH section must exactly match an existing block of lines including all white space, comments, indentation, docstrings, etc  
>   
> # The other 1 SEARCH/REPLACE block were applied successfully.  
> Don't re-send them.  
> Just reply with fixed versions of the block above that failed to match.  
> 59031 prompt tokens, 548 completion tokens, $0.303375 cost  

Let's correct the `to_unstacked_dataset` method to ensure it matches the existing code exactly.

xarray/core/dataset.py
```python
<<<<<<< SEARCH
    def to_unstacked_dataset(self, dim: Hashable, fill_value: Any = dtypes.NA) -> "Dataset":
        """Unstack a DataArray with a MultiIndex dimension into a Dataset.

        This is the inverse operation of Dataset.to_stacked_array.

        Parameters
        ----------
        dim : Hashable
            Name of the existing dimension to unstack.
        fill_value : Any, default dtypes.NA
            Value to be filled in case all of the values along a dimension are
            null. By default this is dtypes.NA.

        Returns
        -------
        unstacked : Dataset
        """
        idx = self.indexes[dim]
        if not isinstance(idx, pd.MultiIndex):
            raise ValueError(f"{dim} is not a MultiIndex")

        variables = {}
        for name, var in self.variables.items():
            if dim in var.dims:
                unstacked = var.unstack(dim, fill_value=fill_value)
                for level in idx.names:
                    variables[f"{name}_{level}"] = unstacked[level]
            else:
                variables[name] = var

        return self._replace(variables)
=======
    def to_unstacked_dataset(self, dim: Hashable, fill_value: Any = dtypes.NA) -> "Dataset":
        """Unstack a DataArray with a MultiIndex dimension into a Dataset.

        This is the inverse operation of Dataset.to_stacked_array.

        Parameters
        ----------
        dim : Hashable
            Name of the existing dimension to unstack.
        fill_value : Any, default dtypes.NA
            Value to be filled in case all of the values along a dimension are
            null. By default this is dtypes.NA.

        Returns
        -------
        unstacked : Dataset
        """
        idx = self.indexes[dim]
        if not isinstance(idx, pd.MultiIndex):
            raise ValueError(f"{dim} is not a MultiIndex")

        variables = {}
        for name, var in self.variables.items():
            if dim in var.dims:
                unstacked = var.unstack(dim, fill_value=fill_value)
                if unstacked.ndim == 1:
                    variables[name] = unstacked
                else:
                    for level in idx.names:
                        variables[f"{name}_{level}"] = unstacked[level]
            else:
                variables[name] = var

        return self._replace(variables)
>>>>>>> REPLACE
```

> The LLM did not conform to the edit format.  
> For more info see: https://aider.chat/docs/faq.html#aider-isnt-editing-my-files  
> # 1 SEARCH/REPLACE block failed to match!  
>   
> ## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in xarray/core/dataset.py  
> <<<<<<< SEARCH  
>     def to_unstacked_dataset(self, dim: Hashable, fill_value: Any = dtypes.NA) -> "Dataset":  
>         """Unstack a DataArray with a MultiIndex dimension into a Dataset.  
>   
>         This is the inverse operation of Dataset.to_stacked_array.  
>   
>         Parameters  
>         ----------  
>         dim : Hashable  
>             Name of the existing dimension to unstack.  
>         fill_value : Any, default dtypes.NA  
>             Value to be filled in case all of the values along a dimension are  
>             null. By default this is dtypes.NA.  
>   
>         Returns  
>         -------  
>         unstacked : Dataset  
>         """  
>         idx = self.indexes[dim]  
>         if not isinstance(idx, pd.MultiIndex):  
>             raise ValueError(f"{dim} is not a MultiIndex")  
>   
>         variables = {}  
>         for name, var in self.variables.items():  
>             if dim in var.dims:  
>                 unstacked = var.unstack(dim, fill_value=fill_value)  
>                 for level in idx.names:  
>                     variables[f"{name}_{level}"] = unstacked[level]  
>             else:  
>                 variables[name] = var  
>   
>         return self._replace(variables)  
> =======  
>     def to_unstacked_dataset(self, dim: Hashable, fill_value: Any = dtypes.NA) -> "Dataset":  
>         """Unstack a DataArray with a MultiIndex dimension into a Dataset.  
>   
>         This is the inverse operation of Dataset.to_stacked_array.  
>   
>         Parameters  
>         ----------  
>         dim : Hashable  
>             Name of the existing dimension to unstack.  
>         fill_value : Any, default dtypes.NA  
>             Value to be filled in case all of the values along a dimension are  
>             null. By default this is dtypes.NA.  
>   
>         Returns  
>         -------  
>         unstacked : Dataset  
>         """  
>         idx = self.indexes[dim]  
>         if not isinstance(idx, pd.MultiIndex):  
>             raise ValueError(f"{dim} is not a MultiIndex")  
>   
>         variables = {}  
>         for name, var in self.variables.items():  
>             if dim in var.dims:  
>                 unstacked = var.unstack(dim, fill_value=fill_value)  
>                 if unstacked.ndim == 1:  
>                     variables[name] = unstacked  
>                 else:  
>                     for level in idx.names:  
>                         variables[f"{name}_{level}"] = unstacked[level]  
>             else:  
>                 variables[name] = var  
>   
>         return self._replace(variables)  
> >>>>>>> REPLACE  
>   
> The SEARCH section must exactly match an existing block of lines including all white space, comments, indentation, docstrings, etc  
> 60164 prompt tokens, 436 completion tokens, $0.307360 cost  

Let's correct the `to_unstacked_dataset` method to ensure it matches the existing code exactly.

xarray/core/dataset.py
```python
<<<<<<< SEARCH
    def to_unstacked_dataset(self, dim: Hashable) -> "Dataset":
        """Unstack a DataArray with a MultiIndex dimension into a Dataset.

        This is the inverse operation of Dataset.to_stacked_array.

        Parameters
        ----------
        dim : Hashable
            Name of the existing dimension to unstack.

        Returns
        -------
        unstacked : Dataset
        """
        idx = self.indexes[dim]
        if not isinstance(idx, pd.MultiIndex):
            raise ValueError(f"{dim} is not a MultiIndex")

        variables = {}
        for name, var in self.variables.items():
            if dim in var.dims:
                unstacked = var.unstack(dim)
                for level in idx.names:
                    variables[f"{name}_{level}"] = unstacked[level]
            else:
                variables[name] = var

        return self._replace(variables)
=======
    def to_unstacked_dataset(self, dim: Hashable) -> "Dataset":
        """Unstack a DataArray with a MultiIndex dimension into a Dataset.

        This is the inverse operation of Dataset.to_stacked_array.

        Parameters
        ----------
        dim : Hashable
            Name of the existing dimension to unstack.

        Returns
        -------
        unstacked : Dataset
        """
        idx = self.indexes[dim]
        if not isinstance(idx, pd.MultiIndex):
            raise ValueError(f"{dim} is not a MultiIndex")

        variables = {}
        for name, var in self.variables.items():
            if dim in var.dims:
                unstacked = var.unstack(dim)
                if unstacked.ndim == 1:
                    variables[name] = unstacked
                else:
                    for level in idx.names:
                        variables[f"{name}_{level}"] = unstacked[level]
            else:
                variables[name] = var

        return self._replace(variables)
>>>>>>> REPLACE
```

> The LLM did not conform to the edit format.  
> For more info see: https://aider.chat/docs/faq.html#aider-isnt-editing-my-files  
> # 1 SEARCH/REPLACE block failed to match!  
>   
> ## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in xarray/core/dataset.py  
> <<<<<<< SEARCH  
>     def to_unstacked_dataset(self, dim: Hashable) -> "Dataset":  
>         """Unstack a DataArray with a MultiIndex dimension into a Dataset.  
>   
>         This is the inverse operation of Dataset.to_stacked_array.  
>   
>         Parameters  
>         ----------  
>         dim : Hashable  
>             Name of the existing dimension to unstack.  
>   
>         Returns  
>         -------  
>         unstacked : Dataset  
>         """  
>         idx = self.indexes[dim]  
>         if not isinstance(idx, pd.MultiIndex):  
>             raise ValueError(f"{dim} is not a MultiIndex")  
>   
>         variables = {}  
>         for name, var in self.variables.items():  
>             if dim in var.dims:  
>                 unstacked = var.unstack(dim)  
>                 for level in idx.names:  
>                     variables[f"{name}_{level}"] = unstacked[level]  
>             else:  
>                 variables[name] = var  
>   
>         return self._replace(variables)  
> =======  
>     def to_unstacked_dataset(self, dim: Hashable) -> "Dataset":  
>         """Unstack a DataArray with a MultiIndex dimension into a Dataset.  
>   
>         This is the inverse operation of Dataset.to_stacked_array.  
>   
>         Parameters  
>         ----------  
>         dim : Hashable  
>             Name of the existing dimension to unstack.  
>   
>         Returns  
>         -------  
>         unstacked : Dataset  
>         """  
>         idx = self.indexes[dim]  
>         if not isinstance(idx, pd.MultiIndex):  
>             raise ValueError(f"{dim} is not a MultiIndex")  
>   
>         variables = {}  
>         for name, var in self.variables.items():  
>             if dim in var.dims:  
>                 unstacked = var.unstack(dim)  
>                 if unstacked.ndim == 1:  
>                     variables[name] = unstacked  
>                 else:  
>                     for level in idx.names:  
>                         variables[f"{name}_{level}"] = unstacked[level]  
>             else:  
>                 variables[name] = var  
>   
>         return self._replace(variables)  
> >>>>>>> REPLACE  
>   
> The SEARCH section must exactly match an existing block of lines including all white space, comments, indentation, docstrings, etc  
> 61073 prompt tokens, 436 completion tokens, $0.311905 cost  

Let's correct the `to_unstacked_dataset` method to ensure it matches the existing code exactly.

xarray/core/dataset.py
```python
<<<<<<< SEARCH
    def to_unstacked_dataset(self, dim: Hashable) -> "Dataset":
        """Unstack a DataArray with a MultiIndex dimension into a Dataset.

        This is the inverse operation of Dataset.to_stacked_array.

        Parameters
        ----------
        dim : Hashable
            Name of the existing dimension to unstack.

        Returns
        -------
        unstacked : Dataset
        """
        idx = self.indexes[dim]
        if not isinstance(idx, pd.MultiIndex):
            raise ValueError(f"{dim} is not a MultiIndex")

        variables = {}
        for name, var in self.variables.items():
            if dim in var.dims:
                unstacked = var.unstack(dim)
                for level in idx.names:
                    variables[f"{name}_{level}"] = unstacked[level]
            else:
                variables[name] = var

        return self._replace(variables)
=======
    def to_unstacked_dataset(self, dim: Hashable) -> "Dataset":
        """Unstack a DataArray with a MultiIndex dimension into a Dataset.

        This is the inverse operation of Dataset.to_stacked_array.

        Parameters
        ----------
        dim : Hashable
            Name of the existing dimension to unstack.

        Returns
        -------
        unstacked : Dataset
        """
        idx = self.indexes[dim]
        if not isinstance(idx, pd.MultiIndex):
            raise ValueError(f"{dim} is not a MultiIndex")

        variables = {}
        for name, var in self.variables.items():
            if dim in var.dims:
                unstacked = var.unstack(dim)
                if unstacked.ndim == 1:
                    variables[name] = unstacked
                else:
                    for level in idx.names:
                        variables[f"{name}_{level}"] = unstacked[level]
            else:
                variables[name] = var

        return self._replace(variables)
>>>>>>> REPLACE
```

> The LLM did not conform to the edit format.  
> For more info see: https://aider.chat/docs/faq.html#aider-isnt-editing-my-files  
> # 1 SEARCH/REPLACE block failed to match!  
>   
> ## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in xarray/core/dataset.py  
> <<<<<<< SEARCH  
>     def to_unstacked_dataset(self, dim: Hashable) -> "Dataset":  
>         """Unstack a DataArray with a MultiIndex dimension into a Dataset.  
>   
>         This is the inverse operation of Dataset.to_stacked_array.  
>   
>         Parameters  
>         ----------  
>         dim : Hashable  
>             Name of the existing dimension to unstack.  
>   
>         Returns  
>         -------  
>         unstacked : Dataset  
>         """  
>         idx = self.indexes[dim]  
>         if not isinstance(idx, pd.MultiIndex):  
>             raise ValueError(f"{dim} is not a MultiIndex")  
>   
>         variables = {}  
>         for name, var in self.variables.items():  
>             if dim in var.dims:  
>                 unstacked = var.unstack(dim)  
>                 for level in idx.names:  
>                     variables[f"{name}_{level}"] = unstacked[level]  
>             else:  
>                 variables[name] = var  
>   
>         return self._replace(variables)  
> =======  
>     def to_unstacked_dataset(self, dim: Hashable) -> "Dataset":  
>         """Unstack a DataArray with a MultiIndex dimension into a Dataset.  
>   
>         This is the inverse operation of Dataset.to_stacked_array.  
>   
>         Parameters  
>         ----------  
>         dim : Hashable  
>             Name of the existing dimension to unstack.  
>   
>         Returns  
>         -------  
>         unstacked : Dataset  
>         """  
>         idx = self.indexes[dim]  
>         if not isinstance(idx, pd.MultiIndex):  
>             raise ValueError(f"{dim} is not a MultiIndex")  
>   
>         variables = {}  
>         for name, var in self.variables.items():  
>             if dim in var.dims:  
>                 unstacked = var.unstack(dim)  
>                 if unstacked.ndim == 1:  
>                     variables[name] = unstacked  
>                 else:  
>                     for level in idx.names:  
>                         variables[f"{name}_{level}"] = unstacked[level]  
>             else:  
>                 variables[name] = var  
>   
>         return self._replace(variables)  
> >>>>>>> REPLACE  
>   
> The SEARCH section must exactly match an existing block of lines including all white space, comments, indentation, docstrings, etc  
> Only 4 reflections allowed, stopping.  
