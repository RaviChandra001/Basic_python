 # Index method in python

list1 = ['a','b','c','d','e']

print(list1.index('a'))    
print(list1.index('b'))
print(list1.index('c'))
print(list1.index('d'))
print(list1.index('e'))

# Syntax of list => index(value,start,stop/end)

print(list1.index('c',0,4)) # 2
print(list1.index('e',1,5)) # 4

# IN  method apply on list

print('d' in list1 ) # True
print('x' in list1)  # False
print('i' in "hello hi")  # True


# Count of word 

list1[4] = 'd'
print(list1.count('d'))  # 2 times 'd' are there in list1
print(list1.count('a'))  # 1 times 'a' are there in list1


# Sort method in list
list2 = [1,4,2,3,6,5,8,7]
print(f"Before sort function ", list2)

list2.sort()
print("After sort list is : ",list2)

# Before sort function  [1, 4, 2, 3, 6, 5, 8, 7]
# After sort list is :  [1, 2, 3, 4, 5, 6, 7, 8]

# Sorted function --> sort the list by making its copy and put it into the newly created array by making sort them

list3 = [10,9,8,7,6,5,4,3,2,1]
print(sorted(list3))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list3) 
#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1] It means original list can't change , new array creats


# reverse list function
list5 = [10,9,8]
list5.reverse()
print(list5)  # [8, 9, 10]

