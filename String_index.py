# Strings are imutable in nature which means by updating indexily not possible only we can assigning new value make changes into the string

name = "0123456"

# Iterable approach to print the string words
for i in name:
    print(i),name[0]

# standard approach

print(name[0])
print(name[1])
print(name[2])
print(name[3])

# [start : stop : stepover ]
# Default stap over is 1 and default stop size is full as
print(name[0:]) # Output-->0123456
print(name[0:3:]) #output-->012

print(name[:5]) #output-->01234
print(name[::1]) #output --> 0123456

# Negative index in python (which means if here we writing  [-1] that denote the last element of the sting )

print(name[-1]) #output-->6
print(name[6:0:-1]) #output --> 654321

# Note --> why it note consider 0 in negative indexing
print(name[::-1]) #output --> 6543210

# By default negative indexing start from last and goes to the very first element

