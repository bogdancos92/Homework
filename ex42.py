## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):

	##def good_boy(self):
		##print("Who's a good boy?\nI'm a good boy")
	pass

## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name
		
	def speak(self):
		print("Bark")

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name
		
	def speak(self):
		print("Meow")
		

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has a name and a pet ... hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## And also has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## HAlibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")
rover.speak()

## Satan is not a cat but ok xD
satan = Cat("Satan")
satan.speak()

## Mary is-a person
mary = Person("Mary")

## Mary's pet is satan...poor mary
mary.pet = satan

## frank is-a Employee wiht the name Frank and a salary of 120000
frank = Employee("Frank", 120000)

## franks pet is rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()

##satan.good_boy()
satan.speak()