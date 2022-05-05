# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 

# Create a tuple
#  needs parenthesis as opposed to brackets for lists

fruits = ('Apples', 'Oranges', 'Grapes')
# constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

#  single value needs trailing comma to become a tuple
# fruits2 = ('Apples') type returns string
fruits2 = ('Apples',) # type returns tuple

#  Get value 
print(fruits[1])

# Cannot change value - this wont work
# fruits[0] = 'Pears'

# delete tuple
del fruits2

print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set 
fruits_set = {'Apples', 'Oranges', 'Mango'}
print('Apples' in fruits_set)

# Add to set 
fruits_set.add('Grapes')

#  when theres a duplicate, doesnt do anything 
fruits_set.add('Apples')

# Remove from set

fruits_set.remove('Grapes')

# Clear set (set remains but empty)
# fruits_set.clear()

# delete completely removes
# del fruits_set

print(fruits_set)