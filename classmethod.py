class player:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def shout(self):
		print(f'my name is {self.name}')
		print(f'my age is {self.age}')

	@classmethod
	def adding(cls,num1,num2):
		return num1+num2

	@staticmethod
	def adding1(num1,num2):
		return (num1+num2)

player2 = player.adding(2,6)
print(player2)

"""
Another way :-   print(player.adding(1,2))

"""
player3 = player.adding1(4,3)
print(player3)
