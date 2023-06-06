# Iterable --> Dictinory, set , tuple are iterable 
user = {
    'name':'golem',
    'age':100,
    'can_dance': False
}

# Iterating the dictionary 
for key,value in user.items():
    print(key,value)

"""
Output -->
name golem
age 100
can_dance False
"""

# Iterating with values 
for values in user.values():
    print(values)

"""
Output -->
golem
100
False
"""

# Iterative on keys of the dictionary
for keys in user.keys():
    print(keys)
"""
Output --> 
name
age
can_dance
"""

# Iteration on set and tuple
set1 = {1,2,3,4,5,6}
print(type(set1))  # Output : <class 'set'>

