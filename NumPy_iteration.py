## Iterate through arrays using for loop
# well it is quite straight forward
# 1-D
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
for x in arr:
  print(x)
# 2-D
arr_2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
## iterate each arrays
for x in arr_2D:
    print(x)
## iterate each element in each arrays
for a in arr_2D:
    for b in a:
        print(b)

# 3-D
arr_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
## iterate each arrays
for x in arr_3D:
    print(x)
## iterate each element in each arrays
for a in arr_3D:
    for b in a:
        for c in b:
            print(c)

## Iterate using nditer, more useful, powerful and convenient
for x in np.nditer(arr_3D):
    print(x)

"""
Iterating Array With Different Data Types

We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].
"""
for x in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
    print(x)

# iterating with different step size
# Iterate through every scalar element of the 2D array skipping 1 element:
for x in np.nditer(arr_2D [:, ::2]):
    print(x)

# iterate by enumerate the steps using the enumerate function
for idx, x in enumerate(arr):
    print(idx, x)
for idy, y in enumerate(arr_2D):
    print(idy, y)