# Zn equivalence classes operation table generator

Package to obtain Zn's equivalence classes sum or product operation tables.

The build_table method takes an positive integer (n) and 'sum' or 'prod' as first and second arguments.
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

## build_table function

build_table(n, operation, bool:headers(opt), bool:inversibles(opt))

n: positive integer.  
operation: 'sum' for class sum and 'prod' for class product.  
headers: for row and column headers.  
inversibles: for using the given set's inversibles for the given operation.
