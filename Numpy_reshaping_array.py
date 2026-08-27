# re-shaping array
# modifying by adding or removing the element of arrays in each dimension

# converting using reshape attribute
## reshaping from 1-D to 2-D
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

new_arr = arr.reshape(4, 3) # the outermost dimension will have 4 arrays with 3 elements each
print(new_arr)

## reshaping from 1-D to 3-D
new_other_arr = arr.reshape(2, 3, 2) # the outermost dimension will have 2 arrays that contains 3 arrays each with two elements
print(new_other_arr)

# any reshaping is possible as long as the number of element in each dimension are equal
# check if its copy of views base
print(arr.reshape(2, 6).base)

## unknow dimension
# it is allowed to have one unknown dimension, by not specifying the exact number of one dimension in the reshape method
# pass -1 as value and NumPy will calculate the number itself
print(arr.reshape(2, 2, -1))

# flattening the arrays
# this is the reverse operation from multidimensional to 1-D
flat_arr = new_arr.reshape(-1)
print(flat_arr)
