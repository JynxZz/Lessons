import random

class OrangeTree:
	def __init__(self, age=0, height=0, fruits=0, dead=False):
		self.age = age
		self.height = height
		self.fruits = fruits
		self.dead = dead

	def one_year_passes(self):
		self.age += 1 
		if not self.dead :
			self.grows()
			self.make_fruits()
			self.dies()

	def grows(self):
		if self.age < 11 : self.height += 1 
		
	def make_fruits(self):
		self.fruits = 0 
		if self.age >= 15 : self.fruits = 0
		elif self.age >= 10 : self.fruits += 200
		elif self.age > 5 : self.fruits += 100


	def dies(self):
		if self.age < 50:
			self.dead = False
		else : 
			self.dead = random.randint(self.age, 100) == 100

	def pick_a_fruit(self):
		if self.fruits : self.fruits -= 1