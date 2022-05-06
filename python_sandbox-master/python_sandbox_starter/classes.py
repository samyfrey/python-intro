# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create a class

class User:
    #constructor (function that runs when you instiate an object from a class)
    # this (in JS) is similar to self
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    def has_birthday(self):
        self.age += 1
    
    # init user object
samy = User('Samy Frey', 'hello@gmail.com', 27)
samy.has_birthday()
print(samy.greeting())

# Extend class 
# in JS ES6 class Customer extends User
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
            return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'



#  Init a customer object
janet = Customer('Janet Johnson', 'janet@gmail.com', 25)
janet.set_balance(500)

# print(samy.greeting())
# print(type(samy))



print(janet.greeting())
