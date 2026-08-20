## the format() method
# to control the display of a string input we can use the format() methode with a curly brace placeholder within the format
price = 49
txt = "the price is  {} dollars"
print(txt.format(price))

# You can add parameters inside the curly brackets to specify how to convert the value
# Format the price to be displayed as a number with two decimals:
txt2 = "the price is  {:.2f} dollars"
print(txt2.format(price))

## Multiple value
# format() can handle multiple value
quantity = 3
itemno = 536
price = 50
myorder = "I would like {} unity of the item number {} for {:.2f} dollars, Please thank you"
p = myorder.format(quantity, itemno, price)
print(p)

# Index number
# using index number inside the placeholder for more precision
myorder2 = "I would like {0} unity of the item number {1} for {2:.2f} dollars, Please thank you"
p2 = myorder2.format(quantity, itemno, price)
print(p2)

# another example is we can display the same argument twice using the index number
age = 35
name = "John"
introducing = "this is {1}, {1} is {0} year old "
f = introducing.format(age, name)
print(f)

## Named Indexes

# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

myorder3 = "I have a {carname}, it is a {model}."
print(myorder3.format(carname = "Ford", model = "Mustang"))