# built-in math function
# min() and max() to find the lowest and the highest value
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# the abs() function returns the absolute value 
z = abs(-7.25)
print(z)

# the pow(x, y) function return the value of x power of y
a = pow(4, 3)
print(a)

## the math module
# the built-in math module
# let's import it
import math
d = dir(math) # still useful to know what's in here
print(d)

# let's use the math.sqrt() that return the square root of the value
b = math.sqrt(64)

print(b)

# math.ceil() and math.floor() function to rounds number upwards and downwards to its nearest value
r_up = math.ceil(1.4)
r_dwn = math.floor(1.4)

print(r_up)
print(r_dwn)

# the math.pi() returns the value of pi
p = math.pi

print(p)

# math challenge
# instructions 
'''
1 print the lowest value of 5 and 10
2 print the highest value of 5 and 10 
3 print the absolute value of -7.25
4 print the value of 4 power 3

'''

print(min(5, 10))
print(max(5, 10))
print(abs(-7.25))
print(pow(4, 3))