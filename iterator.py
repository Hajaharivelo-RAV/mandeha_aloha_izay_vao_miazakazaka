# create a tuple and iterate through it
my_tuple = ("banana", "apple", "cherry")
my_it = iter(my_tuple)

print(next(my_it))
print(next(my_it))
print(next(my_it))
# print(next(my_it)) this will generate an error message because it will run out of object to iterate. 3 iterator for 3 objects, no more maybe less. this is not a loop

# strings are also iterable bcoz they contain iterable sequences
str = "banana"
itit = iter(str)

print(next(itit))
print(next(itit))
print(next(itit))
print(next(itit))
print(next(itit))
print(next(itit))

# looping through an iterator
# let's use for loop tor iterate into a tuple
t = ("banana", "apple", "cherry")

for x in t:
    print(x)
# we can do the same thing with strings
s = "banana"
for x in s:
    print(x) # minions will love this

# NB: The for loop actually creates an iterator object and executes the next() method for each loop.

## creating iterators
# class object methode
# the __iter__() and __next__() function
# creat an iterator that return numbers starting with 1, and each sequence will increase one by one

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

my_class = MyNumber()
my_iter = iter(my_class)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# stop iteration statement
# put a stop condition in the __next__() object definition
# creat an iterator that display numbers till 20

class MyNumberToo:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_class = MyNumberToo()
my_iter = iter(my_class)

for x in my_iter:
    print(x)





