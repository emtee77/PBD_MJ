# This program checks the largest of 3 numbers

print "this program checks the biggest of 3 numbers"

A=input("pls enter a number A")
B=input("pls enter a number B")
C=input("pls enter a number c")

print "A is", A, "B is", B and "C is", C

if A>B and A>C:
	print "A is the largest"
	
if B>A and B>C:
	print "B is the largest"
	
if C>A and C>B:
	print "C is the largest"
	
else:
	print "catch yah"