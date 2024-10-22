**Title**: Add support for header rows in RestructuredText output

**Problem**: The `RST` writer in the `astropy.io.ascii` module does not currently support specifying additional header rows when formatting output. Attempting to specify `header_rows` results in a `TypeError` due to the `__init__()` method of the `RST` class not accepting this argument. 

**Analysis**: The issue arises because the `RST` writer class does not handle the `header_rows` argument. To resolve this, the `RST` class needs to be updated to accept and process the `header_rows` keyword argument, allowing users to customize the header rows in the output. Additionally, the core writer logic needs to be adjusted to incorporate the specified header rows in the final output.

The approach to resolve the issue involves making the following changes:

1. Modify the `RST` class to accept the `header_rows` argument in its initializer.
2. Update the `write` method of the `RST` class to process and include the specified header rows when generating the output.

**Proposed Changes**: 

1. **File**: `astropy/io/ascii/rst.py`
   - **Modification**: Update the `RST` class to include the `header_rows` argument in the initializer.
   - **Details**:
      - Modify the `__init__` method of the `RST` class to accept `header_rows` as an optional argument.
      - Store the `header_rows` value within the instance for later use in the `write` method.

2. **File**: `astropy/io/ascii/rst.py`
   - **Modification**: Update the `write` method of the `RST` class to process the `header_rows` argument.
   - **Details**:
      - Adjust the `write` method to include the additional header rows from `header_rows`.
      - If `header_rows` is provided, prepend these rows to the table headers in the output.

These modifications enable the `RST` writer to accept and process the `header_rows` argument, thus providing the desired functionality.

Make sure to thoroughly test the changes against various scenarios, especially with different combinations of headers, to ensure compatibility and correctness.