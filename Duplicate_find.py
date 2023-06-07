my_list = ['a','b','c','d','b','m','n','n','a']
duplicate = []

for values in my_list:
    if my_list.count(values) > 1:
        if values not in duplicate:
         duplicate.append(values)
    else:
       continue

# printing a duplicate 
print(f"Duplicate from {my_list} is : ",duplicate)

# output = Duplicate from ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n', 'a'] is :  ['a', 'b', 'n']

