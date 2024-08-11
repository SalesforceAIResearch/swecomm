
# aider chat started at 2024-07-20 08:37:41

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmpt2ay0rfq/.git with 4,366 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### Add easily comparable version info to toplevel  
#### <!--  
#### Welcome! Thanks for thinking of a way to improve Matplotlib.  
####   
####   
#### Before creating a new feature request please search the issues for relevant feature requests.  
#### -->  
####   
#### ### Problem  
####   
#### Currently matplotlib only exposes `__version__`.  For quick version checks, exposing either a `version_info` tuple (which can be compared with other tuples) or a `LooseVersion` instance (which can be properly compared with other strings) would be a small usability improvement.  
####   
#### (In practice I guess boring string comparisons will work just fine until we hit mpl 3.10 or 4.10 which is unlikely to happen soon, but that feels quite dirty :))  
#### <!--  
#### Provide a clear and concise description of the problem this feature will solve.   
####   
#### For example:  
#### * I'm always frustrated when [...] because [...]  
#### * I would like it if [...] happened when I [...] because [...]  
#### * Here is a sample image of what I am asking for [...]  
#### -->  
####   
#### ### Proposed Solution  
####   
#### I guess I slightly prefer `LooseVersion`, but exposing just a `version_info` tuple is much more common in other packages (and perhaps simpler to understand).  The hardest(?) part is probably just bikeshedding this point :-)  
#### <!-- Provide a clear and concise description of a way to accomplish what you want. For example:  
####   
#### * Add an option so that when [...]  [...] will happen  
####  -->  
####   
#### ### Additional context and prior art  
####   
#### `version_info` is a pretty common thing (citation needed).  
#### <!-- Add any other context or screenshots about the feature request here. You can also include links to examples of other programs that have something similar to your request. For example:  
####   
#### * Another project [...] solved this by [...]  
#### -->  
####  
> 34082 prompt tokens, 89 completion tokens, $0.171745 cost  

To add easily comparable version info to the top level, we will likely need to edit the following files:

1. `lib/matplotlib/__init__.py` - This is where the `__version__` is currently defined, and where we should add the new `version_info` tuple or `LooseVersion` instance.

Please add `lib/matplotlib/__init__.py` to the chat so I can proceed with the changes.

> lib/matplotlib/__init__.py  
> Add these files to the chat? yes  
> 15347 prompt tokens, 268 completion tokens, $0.080755 cost  

To add easily comparable version info to the top level, we will:

1. Import `LooseVersion` from `distutils.version`.
2. Define `version_info` as a tuple.
3. Define `LooseVersion` instance for the version.

Here are the *SEARCH/REPLACE* blocks:

lib/matplotlib/__init__.py
```python
<<<<<<< SEARCH
from packaging.version import parse as parse_version
=======
from packaging.version import parse as parse_version
from distutils.version import LooseVersion
>>>>>>> REPLACE
```

lib/matplotlib/__init__.py
```python
<<<<<<< SEARCH
        return __version__
=======
        global version_info, loose_version
        version_info = tuple(map(int, __version__.split('.')[:3]))
        loose_version = LooseVersion(__version__)
        return __version__

>>>>>>> REPLACE
```

lib/matplotlib/__init__.py
```python
<<<<<<< SEARCH
def _check_versions():
=======
def _check_versions():
    global version_info, loose_version
    version_info = tuple(map(int, _version.version.split('.')[:3]))
    loose_version = LooseVersion(_version.version)
>>>>>>> REPLACE
```

This will add `version_info` and `loose_version` to the top level of the module, making it easier to compare versions.

> Applied edit to lib/matplotlib/__init__.py  