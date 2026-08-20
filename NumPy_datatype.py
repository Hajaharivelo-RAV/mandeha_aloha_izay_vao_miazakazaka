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

# For i, u, f, S and U we can define size as well.
# Create an array with data type 4 bytes integer
arr4 = np.array([1, 2, 3, 4], dtype="i4") # unspecified size will rise an value error
print(arr4.dtype)
# A non integer string like 'a' can not be converted to integer (will raise an error):
# arr_fa_tsy_mety = np.array(['a', '2', '3'], dtype="i4") # ValueError: invalid literal for int() with base 10: 'a'

## converting data type on existing array using astype() method
arr5 = np.array([1.1, 2.1, 0.0, 3.1])
new_arr = arr5.astype("i") # converting float to integer
arr_new = arr5.astype(int) # converting float to integer same same but not really
a_new_arr = arr5.astype(bool) # converting float to boolean
print(new_arr)  # 32 bit
print(new_arr.dtype) # checking the datatype of new array
print(arr_new) # 64 bit
print(arr_new.dtype) # checking the datatype of new array
print(a_new_arr) 
print(a_new_arr.dtype) # checking the datatype of new array
