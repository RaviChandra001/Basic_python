class players:
	def __init__(self,name,age):
		self.age = age
		self.name = name

	def print_name(self):
		print("Name is : ",self.name)
		print("Age is : ",self.age)

play1 = players("Ravi",18)

# Calling a print_name Function 

play1.print_name()

# Updating value of name and age 
play1.name = "rahul"
play1.age = 20

print("<------- Details After change ---------->")
play1.print_name()