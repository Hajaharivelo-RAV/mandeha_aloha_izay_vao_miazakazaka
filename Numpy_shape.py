# shape of an array
# it's the number of  an element of each dimension
# using the shape attribute to display the number of element 
# the result is a tuple that display the dimension of the array on index 0 and the number of each element inside the array on index 1
import numpy as np
arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(arr.shape)

# using the ndim method to create an array
arr_5 = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr_5)
print(" the shape of array: " , arr_5.shape)

