import re

#Basic example 1
"""
str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:                      
    print('found') ## 'found word:cat'
    print (match.group())
else:
    print('did not find')   """

#Basic example 2
## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere
## On success, match.group() is matched text
match = re.search(r'iii', 'piiig') 
if match:                      
    print('found')
    print (match.group() == 'iii')
else:
    print('did not find') 
match = re.search(r'igs', 'piiig') 
if match:                      
    print('found') 
    print (match.group() == 'igs')
else:
    print('did not find')

## . = any char but \n
match = re.search(r'..g', 'piiig')
if match:                      
    print('found') 
    print (match.group() == 'iig')
else:
    print('did not find')

    
## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g')   # found "123"
match = re.search(r'\w\w\w', '@@abcd!!') # found "abc"

##Repetition examples
## i+ = one or more i's, as many as possible
match = re.search(r'pi+', 'piiig') # found "piii"

## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest')
## In this example, note that it does not get to the second set of i's
match = re.search(r'i+', 'piigiiii') # found "ii"

## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace
match = re.search(r'\d\s*\d\s*\d', 'xx1 2  3xx') # found "1 2  3"
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # found "12  3"
match = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found "123"

## ^ = matches the start of string, so this fails:
match = re.search(r'^b\w+', 'foobar') # not found
## but without the ^ it succeeds:
match = re.search(r'b\w+', 'foobar') # found "bar"


## find exmail address inside a string
word = "purple alice-b@google.com monkey dishwasher"
match = re.search(r'\w+@\w+', word)
if match:
    print (match.group())



## find exmail address inside a string using square brackets
word = "purple alice-b@google.com monkey dishwasher"
match = re.search(r'[\w.-]+@[\w.-]+', word)
if match:
    print (match.group())



## find exmail address inside a string using square brackets and perform group extraction
word = "purple alice-b@google.com monkey dishwasher"
match = re.search(r'([\w.-]+)@([\w.-]+)', word)
if match:
    print (match.group())
    print (match.group(1))
    print (match.group(2))


## Suppose we have a text with many mail addresses
word = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.finall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', word)
for email in emails:
    # do something with each found email string
    print (email)


## findall With Files
"""
# Open file
f = open('text.txt', 'r')
# Feed the file text into findall(); it return a list of all the found strings
strings = re.findall(r'some pattern', f.read())
f.close()  """

## findall and groups
word = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', word)
print(tuples)
for email in tuples:
    # do something with each found email string
    print (email[0])  ## username
    print (email[1])  ## host




## Example substitution

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print (re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher

















































    
