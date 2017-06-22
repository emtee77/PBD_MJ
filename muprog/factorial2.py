#calculate the factorial of a number
def factorial(n):
	if n > 1:
		return n * factorial(n-1)
	
	if n < 0:
		return "inf"
	return 1

	
	
	
def add(first, second):
	return first + second

def subtract(first, second):
	return first - second
	
def divide(first, second):
	if first == 0:
		return 0
	elif second == 0:
		return "ERROR"
	else:
		return first/second

def exponent(first, second):
	if first == 0 and second == 0:
		return "ERROR"
	if first == 0:
		return 0
	if second == 0:
		return 1
	else:
		return first ** second	
		
		
def multiplication(first, second):
	return first * second
	
	
	
def squareroot(first):
	if first < 0:
		return "ERROR"
	else:
		return first ** 0.5
		
		
		
def cuberoot(first):
	if first > 0:
		return first ** (1/3.0)
	else:
		return -(-first) ** (1/3.0)	
			
			
			
def cube(first):
	return first ** 3
	
	

def square(first):
	return first ** 2
	
	

		
#print factorial(5)
#print factorial(6)
#print factorial(10)
#print factorial(0)
#print factorial(-3)


#import unittest
#test the factorial functionality
#class Testfactorial(unittest.TestCase):

#	def testfactorial(self):
#		self.assertEqual(120, factorial(5))
#		self.assertEqual(1, factorial(1))
#		self.assertEqual(1, factorial(0))
#		self.assertEqual(720, factorial(6))
#		self.assertEqual(3628800, factorial(10))
#		self.assertEqual("inf", factorial(-3))

#if __name__ =="__main__":
#	unittest.main()