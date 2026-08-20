# regular expression is a module that can find a specific pattern in a string
# RegEx can be used to check if a string contains the specified search pattern
# import the re module
import re
print(dir(re))
# search a pattern that begin with "the" and end with "Spain"
txt = "The rain falls with 73 degree Fahrenheit temperature in Spain"
teny = " The rain falls! with seventy 3 degree Fahrenheit temperature in Spain."
x = re.search("^The.*Spain$", txt)
print(x)

'''
RegEx Functions

The re module offers a set of functions that allows us to search a string for a match:
Function 	Description
findall() 	Returns a list containing all matches
search()    Returns a Match object if there is a match anywhere in the string
split()	    Returns a list where the string has been split at each match
sub() 	    Replaces one or many matches with a string

'''
## Metacharacters
# [] set of character
# Find all lower case characters alphabetically between "a" and "m":
m = re.findall("[a-m]", txt)
print(m)

# \ Signals a special sequence (can also be used to escape special characters)
# Find all digit characters:
digit = re.findall("\d", txt)
print(digit)

# . Any character (except newline character)
# Search for a sequence that starts with "fa", followed by two (any) characters, and an "s":
dot = re.findall("fa..s", txt)
print(dot)

# ^ Starts with
# Check if the string starts with "the":
start = re.findall("^The", txt)
if start:
    print("Yes, there is a match")
else:
    print("No match")

# $ Ends with
# Check if the string ends with "Spain":
end = re.findall("Spain$", txt)
if end:
    print("Yes, there is a match")
else:
    print("No match")

# * Zero or more occurrences
# Search for a sequence that starts with "fa", followed by 0 or more  (any) characters, and an "s"
star = re.findall("fa.*s", txt)
print(star)

# + One or more occurrences
# Search for a sequence that starts with "fa", followed by 1 or more  (any) characters, and an "s":
plus = re.findall("fa.+s", txt)
print(plus)

# ? Zero or one occurrences
# Search for a sequence that starts with "ra", followed by 0 or 1  (any) character, and an "n":
q_mark = re.findall("ra.?n", txt)
print(q_mark)

# {} Exactly the specified number of occurrences
# Search for a sequence that starts with "fa", followed exactly 2 (any) characters, and an "s":
curly = re.findall("fa.{2}s", txt)
print(curly)

# | Either or
# Check if the string contains either "falls" or "stays":
pipe = re.findall("falls|stays", txt)
if pipe:
    print("Yes, at least there is one match")
else:
    print("No match")

## Special character "\"
# \A 	Returns a match if the specified characters are at the beginning of the string
# Check if the string starts with "The":
start_2 = re.findall("\AThe", txt)
print(start_2)
if start_2:
    print("Yes, there is a match")
else:
    print("No match")

# \b 	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")
# Check if "ain" is present at the beginning of a WORD:
start_3 = re.findall(r"\bain", txt)
print(start_3)
if start_3:
    print("Yes, there is a match")
else:
    print("No match")
#Check if "ain" is present at the end of a WORD:
end_2 = re.findall(r"ain\b", txt)
print(end_2)
if end_2:
    print("Yes, there is a match")
else:
    print("No match")

# \B 	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")
# Check if "ain" is NOT present at the beginning of a WORD:
start_4 = re.findall(r"\Bain", txt)
print(start_4)
if start_4:
    print("Yes, there is a match")
else:
    print("No match")
#Check if "ain" is NOT present at the end of a WORD:
end_3 = re.findall(r"ain\B", txt)
print(end_3)
if end_3:
    print("Yes, there is a match")
else:
    print("No match")

# \d 	Returns a match where the string contains digits (numbers from 0-9)
# Check if the string contains any digits (numbers from 0-9):
digit_2 = re.findall("\d", txt)
print(digit_2)
if digit_2:
    print("Yes, there is a match")
else:
    print("No match")

# \D 	Returns a match where the string DOES NOT contain digits
# Return a match at every no-digit character:
digit_3 = re.findall("\D", teny)
print(digit_3)
if digit_3:
    print("Yes, at least one match")
else:
    print("No match")

# \s 	Returns a match where the string contains a white space character
# Return a match at every white-space character:
w_space = re.findall("\s", txt)
print(w_space)
if w_space:
    print("Yes, there is a match")
else:
    print("No match")

# \S Returns a match where the string DOES NOT contain a white space character
# Return a match if there is no white space:
no_w_space = re.findall("\S", teny)
print(no_w_space)
if no_w_space:
    print("Yes, there is at least one a match")
else:
    print("No match")

# \w 	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
rht = re.findall("\w", txt)
print(rht)
if rht:
    print("Yes, there is a match")
else:
    print("No match")

# \W 	Returns a match where the string DOES NOT contain any word characters
# Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
rht_2 = re.findall("\W", teny)
print(rht_2)
if rht_2:
    print("Yes, there is a match")
else:
    print("No match")

# \Z 	Returns a match if the specified characters are at the end of the string
# Check if the string ends with "Spain":
end_4 = re.findall("Spain\Z", txt)
print(end_4)
if end_4:
    print("Yes, there is a match")
else:
    print("No match")

end_5 = re.findall("Spain\Z", teny)
print(end_5)
if end_5:
    print("Yes, there is a match")
else:
    print("No match")

## Sets
'''
A set is a set of characters inside a pair of square brackets [] with a special meaning:
Set 	Description 	Try it
[arn] 	Returns a match where one of the specified characters (a, r, or n) is present 	
[a-n] 	Returns a match for any lower case character, alphabetically between a and n 	
[^arn] 	Returns a match for any character EXCEPT a, r, and n 	
[0123] 	Returns a match where any of the specified digits (0, 1, 2, or 3) are present 	
[0-9] 	Returns a match for any digit between 0 and 9 	
[0-5][0-9] 	Returns a match for any two-digit numbers from 00 and 59 	
[a-zA-Z] 	Returns a match for any character alphabetically between a and z, lower case OR upper case 	
[+] 	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
'''

## the split() function
# return a list where string have been split at each match
# return a match on white space split
# Split at each white-space character:
spl = re.split("\s", txt)
print(spl)

# You can control the number of occurrences by specifying the maxsplit parameter:
# Split the string only at the first occurrence:
spl_2 = re.split("\s", txt, 1)
print(spl_2)

## the sub() function
# this function replaces the matches by character by your choice
# relace every white space with 9
rplc = re.sub("\s", "9", txt)
print(rplc)

# You can control the number of replacements by specifying the count parameter:
# replace the first 2 occurrences
rplc_2 = re.sub("\s", "9", txt, 2)
print(rplc_2)

## Match object
'''
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
'''

# The regular expression looks for any words that starts with an upper case "S":
var_ult = re.search(r"\bS\w+", txt)
# Print the position (start- and end-position) of the first match occurrence.
print(var_ult.span())

# Print the string passed into the function:
print(var_ult.string)

# Print the part of the string where there was a match.
print(var_ult.group())
