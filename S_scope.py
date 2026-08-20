# A VARIABLE IS ONLY AVAILABLE FROM INSIDE THE REGION IT IS CREATED. THIS IS CALLED SCOPE
## local scope
# a variable created inside a function belongs to the local scope of that function, and can only be used inside that function
# let's create a variable inside a function yayy
def this_function():
    x = 300
    print(x)

this_function()

# a function inside a function can use the variable inside the function, well pretty obvious
def another_function():
    x = 400
    def my_inner_function():
        print(x)
    my_inner_function()

another_function()

## global scope
# a variable created in the main py file, and is available for anyone
# global variables are available from within any scope, global or local
# let us create a variable outside of a function
o = 500
def that_function():
    print(o)
that_function()

print(o)

## so naming variables can tricky, well not very much, at least for python point of view
# if you create two variable that share the same name, but one is global (outside the function) and the other is local (inside the function)
# python will treat them both as local and global, and it will output some twice which can be odd

# GLOBAL KEYWORDS
# use it to render a local variable into a global variable
def global_function():
    global g
    g = 600

global_function() # this will do nothing because the variable is now global and not inside (even it is) the function
print(g)

# this way you can also change the value of a global variable like so
l = 600
def oops_function():
    global l
    l = 700

oops_function()
print(l)
