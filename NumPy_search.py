# searching an item within an array is possible by using the function where()
# if we print the result will display a tuple with the indexe position of the item

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr2 = np.array([6, 7, 8, 9])
arr3 = np.array([1, 3, 5, 7])

# searching for a specific item value (well actualy it's position)
x = np.where(arr == 4)
print(x)
#print(x.shape)

# Find the indexes where the values are even
y = np.where(arr1%2 == 0)
print(y)
#print(x.shape)

# Find the indexes where the values are odd
z = np.where(arr1%2 == 1)
print(z)
#print(x.shape)

## Sorted search
# using the searchsorted() method
# The searchsorted() method is assumed to be used on sorted arrays, which mean will return as an error if we using it with the arr
# Find the indexes where the values are 7
a = np.searchsorted(arr2, 7)
print(a)

# search from the right side
# By default the left most index is returned, but we can give side='right' to return the right most index instead
b = np.searchsorted(arr2, 7, side= 'right')
print(b)

# Multiple value search
# Find the indexes where the values 2, 4, and 6 should be inserted
c = np.searchsorted(arr3, [2, 4, 6])
print(c)

