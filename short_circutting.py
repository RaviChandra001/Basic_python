# Short circutting or Logical data type 
# Types --> and , or , not 
# EG : For and operator 
is_friend = True
is_user = True 

if is_friend and is_user:
    print("Friends forever")
else:
    print("Not good friends")

# Output --> Friends forever

# Eg : using or operator 
is_friend = True 
is_user = False

if is_friend or is_user:
    print("Yes,they are friends")
else:
    print("Not a friends")

#output -->  Yes,they are friends

# Eg: using not logical operator or short circutting
# not is work as invertor of the if condition 
is_friend = True 
is_user = True

if not(is_friend and is_user):
    print("friends")
else:
    print("Not a friends")

# output --> Not a friends