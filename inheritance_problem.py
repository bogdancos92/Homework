# Animal is-a object
class Animal(object):
	pass
	
# Cat is-a Animal	
class Cat(Animal):

	def __init__(self, name):
		self.name=name
	
	def speak(self):
		print("Meow")
		
class Dog(Animal):

	def __init__(self, name):
		self.name=name
		
	def speak(self):
		print("Bark")
		
tom = Cat("Tom")
tom.speak()

rover = Dog("Rover")
rover.speak()