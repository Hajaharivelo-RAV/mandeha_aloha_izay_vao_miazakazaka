# it is basically concatenating two arrays into one by the axes
import numpy as np

# using the concatenate function 
# we will precise the axis if not it will by default 0
# 1-D
ar1 = np.array([1, 2])
ar2 = np.array([3, 4])
arr = np.concatenate((ar1, ar2))
print(arr)

# 2-D
twod1 = np.array([[1, 2], [3, 4]])
twod2 = np.array([[5, 6], [7, 8]])
arrd = np.concatenate((twod1, twod2), axis=1)

print(arrd)

# joining by stacking. this time we concatenating the arrays in a new axe
# using the stack function
# 1-D
arrs = np.stack((ar1, ar2), axis=1)
print(arrs)

# stacking along rows using hstack()
arrh = np.hstack((ar1, ar2))

print(arrh)

# stacking along column using vstack()
arrv= np.vstack((ar1, ar2))
print(arrv)


# stacking along height (depth) using dstack()
arrd= np.dstack((ar1, ar2))
print(arrd)

