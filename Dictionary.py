# Dictionary is collection of pair of key and value in which keys are unique and value can be duplicates
# It is unorderd key valur pair 

mydict = {
 'age' : 19,
 'name' : 'ravi',
 'company' : 'Regex',
 'Id' : '123DHI',
 'Department' : 'CSE'
}

print(mydict)

# output --> {'age': 19, 'name': 'ravi', 'company': 'Regex', 'Id': '123DHI', 'Department': 'CSE'}

# Accesing a dictionary
for i in mydict.values():
    print(i)

# output 
# 19
# ravi
# Regex
# 123DHI
# CSE


# Manully accesing the values 
print(mydict.values())
# dict_values([19, 'ravi', 'Regex', '123DHI', 'CSE'])

# Item function and key function of dictionary
for keys in mydict.keys():
    print(keys)
# It will retuen all the keys elements of dictionary

for items in mydict.items():
    print(items)

# Item will retunr key and value individually 
# ('age', 19)
# ('name', 'ravi')
# ('company', 'Regex')
# ('Id', '123DHI')
# ('Department', 'CSE')

