import unittest

from factorial2 import add, subtract, divide, exponent, multiplication, squareroot, cuberoot, cube, square, factorial
#test the calculator functionality
class Testcalculator(unittest.TestCase):
	def testadd(self):
		self.assertEqual(4, add(2,2))
		self.assertEqual(6, add(2,4))
		self.assertEqual(4, add(4,0))
		self.assertEqual(6, add(4,2))
		self.assertEqual(3, add(4,-1))
		self.assertEqual(0, add(-2,2))
		self.assertEqual(round(5/6.0,4), round(add(2/4.0,2/6.0),4))
		
	def testsubtract(self):
		self.assertEqual(6, subtract(8,2))
		self.assertEqual(-2, subtract(4,6))
		self.assertEqual(0, subtract(-3,-3))
		self.assertEqual(-16, subtract(-9,7))
		self.assertEqual(1/4.0, subtract(1/2.0,1/4.0))
		
	def testdivision(self):
		self.assertEqual(4, divide(8,2))
		self.assertEqual("ERROR", divide(2,0))
		self.assertEqual(0, divide(0,2))
		self.assertEqual(0.25, divide(2/4.0, 4/2.0))
		self.assertEqual(1, divide(-3,-3))
		self.assertEqual(-3, divide(-3,1))
		
	def testexponent(self):
		self.assertEqual(8, exponent(2,3))
		self.assertEqual(0, exponent(0,3))
		self.assertEqual(1, exponent(2,0))
		self.assertEqual('ERROR', exponent(0,0))
		self.assertEqual(1/8.0, exponent(2,-3))
		
	def testmulplication(self):
		self.assertEqual(2, multiplication(1,2))
		self.assertEqual(0, multiplication(0,2))
		self.assertEqual(4, multiplication(-2,-2))
		self.assertEqual(-2, multiplication(-1,2))
		self.assertEqual(0, multiplication(0,0))
		
	def testfactorial(self):
		self.assertEqual(120, factorial(5))
		self.assertEqual(1, factorial(1))
		self.assertEqual(1, factorial(0))
		self.assertEqual(720, factorial(6))
		self.assertEqual(3628800, factorial(10))
		self.assertEqual("inf", factorial(-3))
		
		
		
	def testsquareroot(self):
		self.assertEqual(3, squareroot(9))
		self.assertEqual("ERROR", squareroot(-16))
		self.assertEqual(4, squareroot(16))
		self.assertEqual(0.5, squareroot(1/4.0))
		self.assertEqual(4, squareroot(16))
		
		
	def testcuberoot(self):
		self.assertEqual(round(-2.08, 2), round(cuberoot(-9.0), 2))
		self.assertEqual(3, cuberoot(27))
		self.assertEqual(round(2.5198, 4), round(cuberoot(16), 4))
		self.assertEqual(4, round(cuberoot(64)))
		self.assertEqual(1/3, cuberoot(1/27))
		
		
	def testcube(self):
		self.assertEqual(27, cube(3))
		self.assertEqual((-27), cube(-3))
		self.assertEqual(1/27, cube(1/3))
		self.assertEqual(1000, cube(10))
		self.assertEqual(0.125, cube(0.5))
		
		
	def square(self):
		self.assertEqual(4, square(2))
		self.assertEqual(9, square(-3))
		self.assertEqual(1/9.0, square(1/3.0))
		self.assertEqual(0, square(0))
		self.assertEqual(144, square(12))
	
			

if __name__ =="__main__":
	unittest.main()