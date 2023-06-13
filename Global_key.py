# Without Global keyword
total = 0

def count():
    total = 0
    total += 1
    return total

#  On each function calling the value of total is start from initially because here we using a local varible 

count()
count()
count()
print(count())

# GLOBAL varible

def count1():
    global total
    total += 1
    return total 
 
count1()
count1()
count1()
print(count1())

# output --> 4
