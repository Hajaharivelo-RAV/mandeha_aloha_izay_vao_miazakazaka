# creating and calling a function
def my_function():
    print("wassup bitch!")

my_function()

# arguments in function
def another_function(fname):
    print(fname + " U bitch!")

another_function("Alec")
another_function("Drake")
another_function("Kelly")

# numbers of arg in a function
# if a function is defined with 2 or 3 parameters, when it is call it has to have 2 or 3 arguments
def this_function(fname, lname):
    print(fname + " " + lname + " U bitches")

this_function("Drake", "Kelly")

# arbitrary argument *arg
def not_like_us(*bitch):
    print("the bichiest is " + bitch[2])

not_like_us("Joe Budden", "Akademiks", "Drake", "Kelly")

# keywords argument kind a lame
def not_like_anyone(bitch4, bitch3, bitch2, bitch1):
    print("the bichiest is " + bitch3)

not_like_anyone(bitch1 = "Joe Budden", bitch2 = "Akademiks", bitch3 = "Drake", bitch4 = "Kelly")

# keywords arbitrary argument **kwarg
def this_is_funny(**bitch):
    print("HI, my last name is " + bitch["lname"])

this_is_funny(fname = "Drake", lname = "Bichiest")

# default parameter function
def U_from(country ="Canada"):
    print("HI, I'm a bitch from " + country)

U_from()
U_from("Cleveland")
U_from("New Jersey")
U_from("Spanish town, Jamaica")

# datatype as argument
def unrelated(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
unrelated(fruits)

# return statement
# I'm not really sure that I get this one
def dunno(x):
    return 5 * x

print(dunno(9))
print(dunno(3))
print(dunno(4))

# pass statement
def tsimisyinin():
    pass
tsimisyinin()

# recursion of a function
# I think I get it but dunno exactly how and why used it
# recall the function in the function
def try_recursion(k):
    if k > 0:
        result = k + try_recursion(k - 1)
        print(result)
    else:
        result = 0
        print(result)
    return result

try_recursion(6)
try_recursion(1)