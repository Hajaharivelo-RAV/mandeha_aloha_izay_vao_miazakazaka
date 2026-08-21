# the copy function creates a new array and onw its data. any changes into the new data will not affect the original one
# the view function do not onw the data, any changes in the original source will be displayed in the view function
import numpy as np
arr = np.array([1, 2, 3, 4])
x = arr.copy()
y = arr.view()
x[0] = 42
print(x)
print(y)
print(arr)
# any changes in the original array will affect the view methode but not the copy
arr[3] = 31
print(x)
print(y)
print(arr)
# if we make any change withing the view methode it will affect the original
z = arr.view()
z[1] = 56
print(z)
print(x)
print(y)
print(arr)

# to check if an array onw his data we can use the base methode, it will return none if it does own the data
print(x.base)
print(y.base)
print(z.base)