# formatted string in python

name = 'Johnny'
age = 55
age = str(age)
print('hi ' + name + '. You are'+age+'year old')

# # Another way by using f.This is python3 feature
print(f"hi {name} . You are {age} year old")

# # Now using .format feature of python3 then
print("Hii {} you are {} years old ".format(name, age))

print("hii {new_name} .You are {age} years old ".format(
    new_name="Ravi", age=20))


# Another some examples of foramtted strings
age = 10
name = 'ram'
print(f" You name is : {name} and age is {age}")

print("Name is {} and age is {}".format(name, age))


# Outputs --> 
# hi Johnny. You are55year old
# hi Johnny . You are 55 year old
# Hii Johnny you are 55 years old 
# hii Ravi .You are 20 years old 
#  You name is : ram and age is 10
# Name is ram and age is 10