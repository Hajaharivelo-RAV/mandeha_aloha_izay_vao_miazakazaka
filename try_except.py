"""
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""
# exception handling
# usually when error occur python will output an error message, using the try block will handle that error
# very useful for debugging
# the try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print(" an exception occur")

## Many exception
# we can define as many exception as we want for a special error messages
# Print one message if the try block raises a NameError and another for other errors:
try:
    print(x)
except NameError:
    print(" the variable x is not defined")
except:
    print(" some other shit happened")

## Else
# this one is used if there is no error but Hey you still need to put the except block so that you have a double standard of output
# no error on the try block
try:
    print("Wassup")
except:
    print(" there is something wrong")
else:
    print(" Everything is ok ")

## Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(y)
except:
    print("something went wrong")
finally:
    print("the try except is finished")

## These can be useful to close objects and clean up resources:
# Try to open and write to a file that is not writable:

try:
    f = open("demo_file.txt")
    try:
        f.write("wassup bitch")
    except:
        print("shit happened when writing to file")
    finally:
        f.close()
except:
    print("shit happened when opening the file")

## raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.
## To throw (or raise) an exception, use the raise keyword.
# Raise an error and stop the program if x is lower than 0:

z = -1

if z < 0:
    raise Exception("sorry bitch, not below zero")

# The raise keyword is used to raise an exception.
## You can define what kind of error to raise, and the text to print to the user.
a = "Hello"

if not type(a) is int:
    raise TypeError("only integer are allowed")

