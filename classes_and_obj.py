# to creat a class. use the keywords class
class Myclass:
    x = 5

# now lets create an object with our class
# create an objec name p1 and print the value of x
p1 = Myclass()
print(p1.x) # if I only put p1 in the parenthesis within the print fuction it onle print the instanciation <_main_.Myclass object at 0x74f2d5a577c0> insead of the value of x

## the __init__() function
# create a class namef person, use he init function to assign values for name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Insert a function that prints a greeting, and execute it on the p1 object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name + " and I'm " + str(self.age)) # this will work bcoz you can not concatenate string with integer
#        print("Hello my name is " + self.name + " and I'm " + self.age)
#        print("Hello my name is " + self.name) 

p1 = Person("John", 36)
p1.myfunc()

# the self parameter
# it is a reference to the current instance of the class and is used to access variables that belongs to the class.
# it doesn't have to be named self you can call it whaterver you like it to be
class olona:
    def __init__(izaho, name, age):
        izaho.name = name
        izaho.age = age

    def func(abd):
        print("Hello my name is " + abd.name + " and I'm " + str(abd.age))

p2 = olona("Haja", 31)
p2.func()

# Modifying the object properties
# lets set the age to 40
p1.age = 40
p1.myfunc()

# Deleting object properties 
# you can delete properties on objects by using the del keywords
#del p2.age
p2.func() # this will return as an error

# delete object too
#del p1
p1.myfunc() # this also will tun into an error

# the pass statement
class Person:
    pass

