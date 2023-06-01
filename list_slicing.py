# creating a list
list1 = [
    "ravi",
    "rahul",
    "richeek",
    "rishabh",
    "khyati"
]

# now applying list slicing on list1

print(list1[1:3])  #['rahul', 'richeek']
print(list1[:])  # ['ravi', 'rahul', 'richeek', 'rishabh', 'khyati']
print(list1[3::-1])  # ['rishabh', 'richeek', 'rahul', 'ravi']

# updating value of list
list1[0] = "Ram"

# slicing the list1 
print(list1[:])  # ['Ram', 'rahul', 'richeek', 'rishabh', 'khyati']


