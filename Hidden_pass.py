# In this we enscrypt the password
name = input("Enter name of user : ")
password = input("Enter password : ")

length = len(password)
hidden_pass = '*' * length

print(f"{name} , your password is {hidden_pass}")

# output --> 
# Enter name of user : ravi
# Enter password : ravi1234
# ravi , your password is ********