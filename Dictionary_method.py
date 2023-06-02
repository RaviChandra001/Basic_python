
mydict = {
    'name':'ravi',
    'age': 20,
    'company':'REGex',
    'salary':10000
}

print(mydict)

# dictionary methods
mydict.update({'name':'rishabh'})
print(mydict)

print(mydict['name'])   # rishabh

# Accesing the elements
x = mydict['company']
print(x)   # REGex

# Using get method
y = mydict.get('salary')
print(y)   # 10000

# Removing elements from dictionary
mydict.pop('age')
mydict.pop('salary')
for i in mydict.items():
    print(i)

# output -->
# ('name', 'rishabh')
# ('company', 'REGex')

# Using popitem() 
mydict.clear()
print(mydict)
 # It will clear all the content of the dictionary

# Now my dictionary is totaly cleared so putting some values ,
mydict={
    'name':'ravi',
    'age':20
}

# Now copying this dictionary to another using copy command
new_dict = { }
new_dict = mydict.copy()
print(new_dict)

# {'name': 'ravi', 'age': 20}
