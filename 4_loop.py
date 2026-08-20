# for loop
fruit = ["apple", "banana", "cherry"]
for x in fruit:
    print(x)
# iterate through strings
for x in "banana":
    print(x)
# the break statement
for x in fruit:
    print(x)
    if x == "banana":
        break
# the break statement comes before the print function
for x in fruit:
    if x == "banana":
        break
    print(x)
# the continue statement
# do not print banana
for x in fruit:
    if x == "banana":
        continue
    print(x)
# loop through the range() function
for x in range(6):
    print(x)
# loop through the range() function but specify the starting point instead of zero by default
for x in range(2, 6):
    print(x)
# loop through the range() function but specify the starting point instead of zero by default and specify the incrementing value instead of one by default
for x in range(2, 30, 3):
    print(x)
# else in for loop
for y in range(7):
    print(y)
else:
    print("Finally finished")
# a side, else won't be executed if there is a break statement before it
for y in range(7):
    print(y)
    if y == 4:
        break
else:
    print("Finally finished")
# nested loop
adj = ["red", "big", "juicy"]
for x in adj:
    for y in fruit:
        print(x, y)

# the pass statement
for x in [0, 1, 2]:
    pass
