class Fibonacci(object):
	
	def __init__(self, max):
		self.a = 0
		self.b = 1
		self.max = max
		
	def __iter__(self):
		print(self.a, end=" ")
		return self
		
	def __next__(self):
		if self.b >= self.max:
			raise StopIteration
		aux = self.b
		self.b = self.b+self.a			
		self.a = aux
		# sau asa self.a, self.b = self.b, self.a + self.b
		return self.a
		
for num in Fibonacci(900):
	print(num, end=" ")
print("")