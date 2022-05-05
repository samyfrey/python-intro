# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#  similar to an object literal in JS and JSON
person = {
    'first_name': 'John', 
    'last_name': 'Doe',
    'age': 20
}

#  use a constructor

person2 = dict(first_name='Sara', last_name='Williams' )
# print(person2, type(person2))

#  get value (2 ways)
print(person['first_name']) # in JS we would do person.name)
print(person.get('last_name'))

#Add key/value
person['phone'] = '555-555-5555'

#  get dict keys
print(person.keys())
#  returns: dict_keys(['first_name', 'last_name', 'age', 'phone'])

# get items
print(person.items())
#  returns: dict_items([('first_name', 'John'), ('last_name', 'Doe'), ('age', 20), ('phone', '555-555-5555')])

# copy dict
#  similar to spread operator (get all values of object and add to it) in JS
person2 = person.copy()
person2['city'] = 'Boston'



#  remove an item
del(person['age'])
person.pop('phone')

#  clear 
person.clear()

# get length
print(len(person2))
print(person)

#  same way we can have an array of objects in JS, here a list of dictionnaries 

people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people)
# access the second dictionnary
print(people[1]['name'])