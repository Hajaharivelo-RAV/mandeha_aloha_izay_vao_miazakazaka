# access arrays elements
# using the index number
# indexes start with 0

import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0]) # this will print the first element in the array 

# since we have access to the elements in the array we can also do the math
print(arr[2] + arr[3]) # it is basically 3 + 4 = 7

#to access element in an 2-D arrays we have to use a separators "," for the syntax
# as we already know the print function can take 3 argument
two_D = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])

print("the 4th element of the 2nd row is: ", two_D[1, 3]) #this will print 8 

# access element of an 3-D array, same operation with 3 argument in the square brace
three_D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9],[10, 11, 12]]])

print("the 3rd element of the 1st row of the 1st column is: ", three_D[0, 0, 2])


# negative indexing to access element from the end
print("last element from 2nd dim: ", two_D[1, -1])
