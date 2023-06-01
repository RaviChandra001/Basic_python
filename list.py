# List is collection of different data types inside a single varible is known as a list

list1 = [1,2,3,'hey','123']
print(list1) # [1, 2, 3, 'hey', '123']

list2 = [4,5,6,7]
# list concatination 
list3 = []
list3 = list1 + list2
print(list3)

# using append function 
list2.append(list1)
print(list2)

# Accessing list using indexing
print(list2[0])
print(list2[1])

# Itrative approach 
for i in list2:
    print(i)

# List updating 
list2[0] = 100
print(list2) # [100, 5, 6, 7, [1, 2, 3, 'hey', '123']

# using insert method
list2.insert(0,"Ravi")  #['Ravi', 100, 5, 6, 7, [1, 2, 3, 'hey', '123']]
print(list2)

# Deletion of list in python
list2.pop(0)
list2.pop(1)
list2.pop(2)
print(list2) # [100, 6, [1, 2, 3, 'hey', '123']

