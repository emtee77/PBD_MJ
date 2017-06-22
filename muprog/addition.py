# To add 2 numbers together

print "this program add two numbers together"
print
A=input("please enter a number")
B=input("please enter a second number")

C=A+B
print "the value of c", "is", C

if A>B:
	print "A is more than B"
	print "And the line executes too"
	print "As does this"
if C<10:
	print "C is less than 10"
	
if C>=20:
	print "C is greater than 20"
	
if (A<B) and (C>10):
	print "A is less than B AND C is greater than 10"
	
if C<=10:
	print "C is less than or equal to 10"
	
else:
	print "C is greater than 10"