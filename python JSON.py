# python JSON
# it is a syntax for storing and exchanging data
# it is a text written in JavaScript object notation
# built-in package called json used to work with json data

import json

## parse JSON - convert from JSON to python
# if we have a JSON string we can parse it by using json.loads() method
# it will be converted in py dictionary
# some json data

x = '{"name": "John", "age": 30, "city": "New York"}'

y = json.loads(x) # parse x

print(y["age"])

## we can do the opposite operation
# convert py to JSON
# using the json.dumps() method
# a python dict
z = {
	"name": "John",
	"age": 30,
	"city": "New York"
}

a = json.dumps(z)
print(a) # print in JSON string type object

# convert python objects into JSON string
print(json.dumps(["apple", "banana"])) # type array
print(json.dumps(("cherry", "strawberry"))) # type array
print(json.dumps("hello")) # type string
print(json.dumps(42)) # type number
print(json.dumps(31.76)) # type number
print(json.dumps(True)) # type true
print(json.dumps(False)) # type false
print(json.dumps(None)) # type null

# let's convert a python dictionary that contain all the data type
profile = {
	"name": "John",
	"age": 30,
	"married": True,
	"divorced": False,
	"children": ("Annie", "Billy"),
	"pets": None,
	"cars": [
		{"model": "BMW 230", "mpg": 27.5},
		{"model": "Ford Edge", "mpg": 24.1}
	]
}

print(json.dumps(profile))


## format the result
# the JSON string is not very convenient to read
# json.dumps() parameters
# the indent parameter
print(json.dumps(profile, indent=4))

# using separators parameter, defaults are (", " ; ": ") they mean comma and space for separates each object. colon and a space to separates keys from value
print(json.dumps(profile, indent=4, separators=(". ", " = ")))


## order the result
# the sort_keys parameter to specify if the result should be sorted or not
print(json.dumps(profile, indent=4, sort_keys=True))


## challenge JSON

# instruction
'''
1 import json module
2 create a variable j_son that contains a JSON string Emil aged 30
3 convert it to a python object in a variable p_y
4 print the age from p_y 
'''

import json
j_son = '{"name": "Emil", "age": 30}'
p_y = json.loads(j_son)
print(p_y["age"])
print(dir(json.dumps))