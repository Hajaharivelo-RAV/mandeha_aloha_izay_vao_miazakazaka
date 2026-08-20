# while loop
i = 1
while i < 6:
#    i += 1 # this works too but will exclude 1 and include 6, as opposition to the icrementation after the print function
    print(i)
    i += 1 # I dunno if this is the reason but I think the icrementation is still in the while section

# break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# continue statement
i = 1
while i < 6:
    i += 1     # iteration first
    if i == 3: # stop the iteration and continue to the loop
        continue
    print(i)

# else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

