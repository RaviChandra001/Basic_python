# Tuple are immutable in nature 
my_tuple = (1,1,2,3,4,5)
print(type(my_tuple))  # <class 'tuple'>

# Tuple operation 
print(5 in my_tuple)      # True
print(6 in my_tuple)      # False


# tuple methods in python
# count method in tuple 
x = my_tuple.count(1)
print(x)        #  2

# Another approach for tuple 
print(my_tuple.count(1))     # 2

# Tuple slicing as :
new_tuple = my_tuple[1:2]
print(new_tuple)    # (1,)

print(my_tuple.index(2))