# ( == ) and is differences using some examples 
print(True == 1) # True
print(False == 1) # False
print(False == 0) # True
print([]==[])    # True
print([1,2,3]==[1,2,3])  # True

# Using is we can address the memory locations of the varible of given expression 

print(True is True )  # True
print('1' is 1)  # False
print(10 is 10.0)  #False
print([1,2,3] is [1,2,3]) # False 

"""
False because of when we create first list [1,2,3] it has different memory address , and when we create [1,2,3] another list then it has different memory location.  So it retuens false here.....
"""

print([] is [])
# Also print false 

# EG :- 
a = [1,2,3,4]
b = [1,2,3,4]
print(a==b)  # True 
print(a is b ) # false
