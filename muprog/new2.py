def salutation(name):
	salutation = "Hello" + name
	print (salutation)
	return salutation
	
def average (number1, number2):
	averageValue = (number1 + number2)/2.0
	return averageValue
	
print salutation("Mutiu")

print(average(5,6))	

print [1,2,3]

print list([1,2,3])

print []

print list()

print range (1,10)

mylist = [1,2,3,4,5]
mylistlength = len(mylist)
print mylistlength

print max(mylist)
print min(mylist)
print sum(mylist)

mylist = range(1,11)
print mylist
print mylist [5:10] #first parameter to slice is index and second parameter is element number

import random
random.shuffle(mylist)
print mylist
print mylist[5:]

mylist1 = [1,2,3]
mylist2 = [4,5,6]
print mylist1 + mylist2
print 3 * mylist1
print 10 in mylist1
print 1 in mylist1
print 3 in mylist1
print 3 not in mylist1


mylist1.append(4)
print mylist1
mylist1.insert(1,50)
print mylist1
mylist1.remove(50)
print mylist1
print mylist1.pop()
print mylist1.index(3)
mylist1.count(2)
mylist1.reverse()
print mylist1
mylist1.sort()
print mylist1

from array import *
myarray = array("i", [1,2,3,4,5])	#i stands for integers-telling python to only store integers in myarray
for i in myarray:
	print i

myarray.append(6)
print myarray
#myarray.append('hi')	#This makes the prog cratch because 'hi' is of a different data type

