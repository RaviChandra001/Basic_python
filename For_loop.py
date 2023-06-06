  # Loop are the powerfull feature of the programming which allows you to repeat those expressions which you need to repeat with each iteration.

for i in 'Ravichandra':
    print(i,end=" ")
# Output --> R a v i c h a n d r a 


# List with for loop
list1 = [1,2,3,4,5]
for i in list1:
    print(i,end=" ")

# Output --> 1,2,3,4,5

# Dictionary 
my_dict = {
    "year":"1002",
    "name":"ravi",
    "Friend":"rahul"
}

# First on dictinory keys 
for d in my_dict.keys():
    print(d)

"""
Output --> year , name , Friend
"""

# Another on values of the dictinoary
for d in my_dict.values():
    print(d)

"""
Output --> 1002 , ravi , rahul
"""

# Om items
for i in my_dict.items():
    print(i)

"""
('year', '1002')
('name', 'ravi')
('Friend', 'rahul')
"""

# Multiple times printing the statements
for item in (1,2,3,4):
    print(item,end=" ")
    print(item,end=" ")
    print(item,end=" ")

# Output --> 1 1 1 2 2 2 3 3 3 4 4 4


# Muliple loops --> Loop inside the loop
for item in (1,2,3,4):
    for x in ['a','b','c']:
        # for y in [1]:
            print(item,x)

"""
Output --> 
1 a
1 b
1 c
2 a
2 b
2 c
3 a
3 b
3 c
4 a
4 b
4 c
"""