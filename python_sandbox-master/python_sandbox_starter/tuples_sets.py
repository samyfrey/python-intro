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
