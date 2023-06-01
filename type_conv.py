# Type conversion 
# Note --> In python dafault input has string data type even you taking integer 

num1 = input("Enter a number ")

print(type(num1))

# output--> Enter a number:  3 AND <class 'str'>

# To change data type we use the type casting method
num2 = int(num1)
print(type(num2))  #output --> <class 'int'>

num3 = float(num2)
print(type(num3)) # output --> <class 'float'>

# num4 = chr(num3)
# print(type(num4)) # output --> Error because can't possible

# chr convertion is ::--> Using Assci value 
A = 65

value = chr(A)
print(value)
print(type(value)) # output --> <class 'str'>
