# creates an arrays containing car names
cars = ["volvo", "toyota", "mercedes"]
# so basically it is says that an arrays is a special variable which can hold mora than on value at a time
# well it kind looks like a list for me

# now let's get the first car of the "array" by call it by the index 
x = cars[0]
print(x)

# modifying the value of the first array
y = cars[0] = "Ford"
print(y)

# the length of an array
z = len(cars)
print(z)
# adding element in arrays usind append() function
cars.append("honda")
print(cars)
# removing arrays elements using the pop() function
cars.pop(0)
print(cars)
# using remove() funtion to delete one element im the array
cars.remove("mercedes")
print(cars)
