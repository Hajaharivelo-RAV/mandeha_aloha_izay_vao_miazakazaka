## Slicing, or cutting arrays
# this we use the operator ":" for slicing
# of course we use the index to access the element that where we want to slice
# this is the syntax [start:end] or [start:end:step]
# if we do not specify the start by default it will use the 0 index
# if we do not specify the end by default it will use the length of the array
# if we do not specify the step by default it will be 1

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[:5])
print(arr[2:])

# Negative slicing
# Use the minus operator to refer to an index from the end:
# Slice from the index 3 from the end to index 1 from the end:
print(arr[-3: -1])

# STEP
# Use the step value to determine the step of the slicing:
# Return every other element from index 1 to index 5:
print(arr[1:6:2])
print(arr[::2]) # Return every other element from the entire array

## Slicing 2-D Arrays
#From the second element, slice elements from index 1 to index 4 (not included):
two_D = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(two_D[1, 1:4])
# From both elements, return index 2
print(two_D[0:2, 2])
# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array
print(two_D[0:2, 1:4])


