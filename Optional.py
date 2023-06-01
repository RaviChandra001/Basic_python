
"""
complex and bin()  data type

bin() --> This function are used to write any given number to binary repersentaion 

syntax --> bin(Number_to_be_passed)
Eg :- bin(5)
output --> 0b101
"""

print(bin(5))

# converting binary to integer then then we get 5
print(int('0b101',2))

# Here --> 2 is base of number type


        # <----complex------->

x = complex(2,1)
y = complex(3,1)

z=x+y
print(f"{x} and {y} sum is : ",z)
