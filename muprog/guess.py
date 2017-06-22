# guess.py
# Program to guess a number
# Pick a random number (call it thenumber)

#loop: 
	#let the user pick a number (call it guess)
	#if guess is higher than thenumber, print "Go lower"
	#if guess is lower than thenumber, print "Go higher"
	#if guess = thenumber, print "You got it" and exit
	
	
import random
thenumber=random.randint(1,100)
print "random number picked is", thenumber
guess=input("pls enter a number")

theygotit=0
guess=0

while theygotit==0:
	guess=input("pls enter a number")	
	if guess>thenumber:
		print "Go lower"
	if guess<thenumber:
		print "Go higher"
	if guess==thenumber:
		print "You got it"
		theygotit=1