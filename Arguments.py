# Here name and l_name is parameters 
"""
Arguments is used to call a function and parameters is defines to create a function 
"""
def hello(name,l_name):
    print(f"Hello {name} {l_name}")

hello('Ravi',"Chandra")

# Default parameters 
def add(a=10,b=12):
    print(f"Addition of {a} and {b} is : ",a+b)

add()

# Retuen Function in python 
def sum(a,b):
    c = a+b
    return c

sum_is = sum(10,12)
print(f'Sum : ', sum_is)



