class Dairy:
	def __init__(self):
		self.one_liter = 40
		self.amount = 0
		self.liters = 0
	def mul(self, liters):
		self.amount = self.amount + (self.one_liter * liters)
		self.liters = liters
	def add(self, days, bonus):
		self.amount = (self.amount * days)
		self.liters = self.liters * days
		self.amount = self.amount + (self.liters * bonus)

	def display(self):
		return self.amount
a = Dairy()
print a.mul(5)
print a.display()
print a.add(30, 1)
print a.display()



