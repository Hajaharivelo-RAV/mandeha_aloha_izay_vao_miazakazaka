# syntax lambda function
# lambda arg: expression

# Add 10 to argument a and return the result:
x = lambda a: a + 10
print(x(5))

# it can take more than one argument
x = lambda a, b: a * b
print(x(5, 6))

y = lambda a, b, c: a + b + c
print(y(5, 6, 3))

# an anonymous function in a function
def myfunc(n):
    return lambda a: a * n
my_doubler = myfunc(2)
print(my_doubler(11))
my_triple = myfunc(3)
print(my_triple(5))