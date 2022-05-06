# Python has functions for creating, reading, updating, and deleting files.

myFile = open('myfile.txt', 'w')

# get info on the file

print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

#  write to file

myFile.write('I love Python')
myFile.write(' and Javascript')
myFile.close()

myFile = open('myfile.txt', 'a')
myFile.write('I also like Javascript')
myFile.close()


myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
