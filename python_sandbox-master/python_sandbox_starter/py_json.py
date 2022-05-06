# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json 

# Sample JSON getting from API
userJSON = '{"first_name":"John", "last_name": "Doe", "age": 20}'

#  parse to dictionnary

user = json.loads(userJSON)

# print(user)
# print(user['first_name'])

#  does the opposite, to transform to JSON format 
car = {'make': 'Ford', 'model':'Mustang'}
carJSON = json.dumps(car)
print(carJSON)