# list unpacking in python 

a,b,c=[1,2,3]
print(a)
print(b)
print(c)


# Applying list unpacking then it is 

a,b,c, *others = [1,2,3,4,5,6,7]
print(a)
print(b)
print(c)
print(others)

# If we have another one data  along the other 

a,b,*other,d=[1,2,3,4,5,6,7]
print(a)
print(b)
print(*other)
print(d)



