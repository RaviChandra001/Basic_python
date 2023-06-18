class person:
	def __init__(self,name = "Dafault",age = 0):
		if (age > 18):
			self.name = name
			self.age  = age 
		elif (age<18):
			print("Name and age not passed")

	def Details(self):
		print(self.name)
		print(self.age)
		pass

per1 = person('Ravi',10)
print(per1.Details())