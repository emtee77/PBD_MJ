# Define a class for a car

class car(object):
	#implementation follows
	#Note: use of indentation to define code block associated with the class
	
	def __init__(self):
		self.__make = "Ferrari"
		self.__colour = "Red"
		self.__mileage = 10
		self.engineSize = "5.4l "   #this can be seen by the public, bcos it has no 2 underscore @ d beginning
		
		
	def getmake(self):
			return self.__make
			
			
	def getcolour(self):
			return self.__colour
			
			
	def getmileage(self):
			return self.__mileage		
	
	def setmake(self, make):	#setmake is to update the make of the car
		self.__make = make
		
	def setcolour(self, colour):	#setcolour - to update the colour
		self. __colour = colour
		
	def setmileage(self, mileage):	#setmileage - to update the mileage
		self.__mileage = mileage
		
	def move(self, distance):
		print ("Moved" + str(distance) + "kms. ")
		self. __mileage = self. __mileage + distance
	
	def paint(self, colour):
		print ("Getting a paint job - new colour is: " + colour)
		self. __colour = colour
	

class Electriccar(car):
	def __init__(self):
		car.__init__(self)
		self.__numberFuelCells = 1
		
	def getnumberFuelCells(self):
		return self.__numberFuelCells
	
	def setnumberFuelCells(self, value):
		self.__numberFuelCells = value
		
