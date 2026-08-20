# Module is a set of code that had been store in python file and we can use it as it
# it is like a code library (like pandas ect) that you ceated
# we can use it alongside the main code of your application
# lets create a module and then save the code with the extension .py
#def greeting(name):
#    print("hello my name is " + name)  
# this will be created afterwards 
# to use this newly module (even it is kinda lame) we can import it using the, very hard guest import statement in another file
import lay_module

lay_module.greeting("Jonathan")
# Note: When using a function from a module, use the syntax: module_name.function_name

a = lay_module.person1["age"]
print(a)

# we can name the module like we wanted to, it must be have the .py extension
# we can re-name our module when we import it by giving it an alias using the as statement 
import lay_module as lm

b = lm.person1["country"]
print(b)

# built-in modules, there are plenty of them and we can import it whenever we wanted 
# using the module platform and the system() function to see operating system
import platform

c = platform.system()
print(c)

# using the dir() function to List all the defined names belonging to the platform module
d = dir(platform)
print(d)
# Note: The dir() function can be used on all modules, also the ones you create yourself
e = dir(lay_module)
print(e)

# import from module, mean that you can import only one defined name belonging to the module, I mean somtetimr you do not need all the shi** i mean things inside the module
from lay_module import person2

print(person2["rating"])
# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]
