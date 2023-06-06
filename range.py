# Range function in python 
for number in range(0,10):
    print(number)

for _ in range(0,10,1):
    print(_,end="\n")

for _ in range(0,10,2):
    print(_)

for i in range(0,10,-1):
    print(i)  # Does not print anything

for j in range(10,0,-1):
    print(j)  # print the number in reverse order

for ij in range(10,0,-2):
    print(ij) # Print number in reverse with -2 step_over

for i in range(10,0,1):
    print(i,end=" ")  # Does not print anything 

# Converting the elements in list 
for _ in range(5):
    print(list(range(10)))

"""
output --> 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
