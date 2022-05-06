# A List is a collection which is ordered and changeable. Allows duplicate members.
# similar to JS arrays

# create a list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
# use a constructor (similar to JS) but less common 
# numbers2 = list((1, 2, 3, 4, 5))

# print(numbers, numbers2)

# Get a value from a list
print(fruits[1])

# Get length
print(len(fruits))

# append, add to the end
fruits.append('Mangos')

#  remote from list passing in the value
fruits.remove('Grapes')

# insert into position (position first and value then)
fruits.insert(2, 'Strawberry')

#  remove from list with pop
fruits.pop(2)

# reverse list
fruits.reverse()

# sort alphabetically

fruits.sort()

# reverse sort 
fruits.sort(reverse=True)

# Change a value 
fruits[0] = 'Blueberries'

print(fruits)