# Zn equivalence classes operation table generator

Simple package to obtain Zn's equivalence classes sum or product operation tables.

The build_table method takes an integer (n) and 'sum' or 'prod' as first and second arguments.
It will return a nxn matrix with the result of operating every item with each other.

## Installation:

``
    pip install zn_operation_table
``

## Example

``
    build_table(3, 'sum')
``

Will return:

``
    [[0,1,2], [1,2,0], [2,0,1]]
``
