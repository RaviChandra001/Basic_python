class practice:
	name = ""
	age = 0
	l_name = ""

	def __init__(self,name,age,l_name):
		self.name = name 
		self.age = age
		self.l_name = l_name

	def Details(self):
		print(self.name,self.l_name,"Age is : ",self.age)

prac1 = practice("Ravi",18,"Chandra's ")
prac1.Details()