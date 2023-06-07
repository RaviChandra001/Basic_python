my_list = [1,2,3]
for item in my_list:
    print(item)
    break

i=0
while i<len(my_list):
    print(my_list[i])
    i += 1
    break

# output --> print 1 and 1 for both loops 

# Continue statement
my_list = [1,2,3,4]
for item in my_list:
    continue
    print(item)

i=0
while i < len(my_list):
    i = i+1
    continue
    print(my_list[i])

# Output --> Print nothing because continue statement skiping the part of print()

# Pass statement
my_list = [1,2,3,4]
for item in my_list:
    # Nothing inside the for loop that means error should be generate 
    pass

i = 0
while i < len(my_list):
    print(my_list[i])
    i = i+1
    pass

"""
It only print output of while loop 
1
2
3
4
"""

i = 0
while i < 50:
    reply = input("say something: ")
    if (reply == 'bye' or reply == "Bye"):
        print("loop is terminated using break ")
        break
    else:
        print(f"Your reply is : ",reply)

"""
Output --> 
say something: hello
Your reply is :  hello
say something: Bye
loop is terminated using break 
"""