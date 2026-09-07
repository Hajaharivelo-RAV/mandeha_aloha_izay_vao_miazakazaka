# splitting arrays
# using array_split() function 
# 1-D
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
new_arr = np.array_split(arr, 3)

print(new_arr)
print(new_arr[0])
print(new_arr[1])
print(new_arr[2])

# 2-D
two_D = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
new_tD = np.array_split(two_D, 3)

print(new_tD)

# 2-D with 3 elements
two_D2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_tD2 = np.array_split(two_D2, 3)

print(new_tD2)

new_tD2c = np.array_split(two_D2, 3, axis=1) # split arrays along the column

print(new_tD2c)

new_tD2h = np.hsplit(two_D2, 3) # alternatively we can use hsplit to split along the column 

print(new_tD2h)

# similar alternate for row and height are available as vsplit and dsplit
