
class animal:	# base - parent class
	def __init__(self,colour,legs):
		self.colour = colour
		self.legs = legs
	def show(self):
		print("your animal has",self.legs,"legs and colour of",self.colour)

class wild(animal): # derived - child
	def __init__(self,colour,legs,size):
		animal.__init__(self,colour,legs)
		#super().__init__(colour, legs)
		self.size = size

	def show(self):
		print("your animal has",self.legs,"legs and colour of",self.colour,"and size of",self.size)

animal_1 = animal('grey',2)
animal_1.show()

wild_animal_1 = wild('black',4,'small')
wild_animal_1.show()

wild_animal_2 = wild('white', 4, 'big')
wild_animal_2.show()






#baby = wild(12, 12)