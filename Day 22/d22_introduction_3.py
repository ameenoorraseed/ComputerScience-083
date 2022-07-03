
class animal:	# base - parent class
	def __init__(self,colour,legs):
		self.colour = colour
		self.legs = legs
	def show(self):
		print("your animal has",self.legs,"legs and colour of",self.colour)

class wild(animal): # derived - child
	def __init__(self,colour,legs,size):
		animal.__init__(self,colour,legs)
		self.size = size

	def show(self):
		print(self.legs,"legs and colour of",self.colour,"size of",self.size)

a1 = animal('black',4)
a1.show()

wa1= wild('black',4,'medium')
wa1.show()

wa2= wild('pink',6,'big')
wa2.show()