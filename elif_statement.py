a = 41
b = 200

if a < b:
    print('b is greater than a')

if a == b:
    print('a is equal to b')
elif a < b:
    print('b is greater than a')

if a == b:
    print('a is equal to b')
elif a > b:
    print('a is greater than b')
else:
    print('brupp')

if a == b:
    print('a is equal to b')
else:
    print('b greater than a')

if b > a: print('b greater than a')

print('A') if a > b else print('B')

print('A') if a > b else print('E') if a == b else print('B')

c = 500

if a < b and c > b:
    print('both condition are true')

if a > b or c > a:
    print('at least one condition is true')

if a > 10:
    print('above ten,')
    if a > 20:
        print('also above twenty,')
else:
    print('but not above 20')

if b > a:
    pass
