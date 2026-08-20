## INTRODUCTION
# BASIC
# first thing first let's import NumPy, and put it in the alias np for more convenience
# creating an ndarray that numpy uses because it is an array object oriented
# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:
import numpy as np
arr = np.array([1, 2, 3, 4, 5]) # list into ndarray
print(arr)
print(type(arr))
# checking numpy version
print(np.__version__)

# using a tuple
arr_tuple = np.array((1, 2, 3, 4, 5))
print(arr_tuple)

## DIMENSION IN ARRAYS
## A dimension in arrays is one level of array depth (nested arrays).
# 0-D arrays
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
# Create a 0-D array with value 42
zero_D = np.array(42)
print(zero_D)

# 1-D arrays, the most common
# Create a 1-D array containing the values 1,2,3,4,5:
one_D = np.array([1, 2, 3, 4, 5])
print(one_D)

# 2-D arrays, nested one
# it has 1-D arrays as its elements is called a 2-D array.
# These are often used to represent matrix or 2nd order tensors.
# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
two_D = np.array([[1, 2, 3], [4, 5, 6]])
print(two_D)

# 3-D arrays
# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
three_D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(three_D)

## check the numbers of dimensions
# using the ndim function
# let's Check how many dimensions the arrays have:
print(zero_D.ndim)
print(one_D.ndim)
print(two_D.ndim)
print(three_D.ndim)

## Higher dimensional arrays
# when creating an array we can define the dimension by using the ndim argument
five_D = np.array([1, 2, 3, 4], ndmin=5)
print(five_D)
print('number of dimensions :', five_D.ndim)