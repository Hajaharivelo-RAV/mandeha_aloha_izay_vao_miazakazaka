# Datatype in NumPy
"""
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )


"""
# checking the datatype in a NumPy array
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array(["banana", "apple", "pineapple"])

print(arr.dtype)
print(arr2.dtype)

# creating an array with defined datatype using the argument dtype()
arr3 = np.array([1, 2, 3], dtype="S")

print(arr3.dtype)
