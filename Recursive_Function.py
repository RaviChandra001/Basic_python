"""
Recursion is a process of calling a function itself again and again till condition is True.
"""

def factorial(num):
    if num==1:
        return num
    else:
        return num* factorial(num-1)

num = 5
result = factorial (num)
print("Factorial is : ",result)