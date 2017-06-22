import random
thenumber=random.randint(1,100)
print "random number picked is", thenumber
guess=input("pls enter a number")

	
if guess>thenumber:
	print "Go lower"
else:
	if guess<thenumber:
			print "Go higher"
	else:	
		print "You got it"