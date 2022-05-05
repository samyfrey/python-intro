# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

# all strings have methods attached to it 

name = 'Samy'
age = 30

# Concatenate 
# print('Hello, my name is ' + name)

# this wouldnt work as we can only concatenate strings and age is an int 
# print('Hello, my name is ' + name + ' and I am ' + age)
# hence 
# method #1
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# method #2
# Arguments by position / positional arguments
# whats in the curly braces are placeholders and defined later 

# print('My name is {name} and I am {age}'.format(name=name, age=age))

# method #3

# F-strings
# similar to JS template literals but here not using backticks and money sign 
# print(f'Hello, my name is {name} and I am {age}')




# String Methods

s = 'hello world'

#capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with (boolean)
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list (returns each word in an array)
# ['hello', 'world']
print(s.split())

# Find position (position number)
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# s = 'hello world' is false
# s = 'helloworld' is true

# Is all numeric
print(s.isnumeric())
