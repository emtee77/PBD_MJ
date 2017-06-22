#RockPaperScissors.py


player1=input("pls enter your choice (rock, paper or scissors):")
player2=input("pls enter your choice (rock, paper or scissors):")

print "player1 chose", player1
print "player2 chose", player2

if player1==player2:
	print "its a draw"
	
elif player1=="rock":
	if player2=="scissors":
		print "player2 loses! rock beats scissors"
	else:
		print "player2 wins! paper covers rock"

elif player1=="paper":
	if player2=="rock":
		print "player2 loses! paper covers rock"
	else:
		print "player2 wins! rock beats scissors"
		
else:
	if player2=="paper":
		print "player2 loses! scissors cut paper"
	else:
		print "player2 wins! rock blunts scissors"

#if player1=="rock"  player2=="paper":
#print "player2 wins"
#else:
#print "player1 wins"
		

#if player1=="scissors" and player2=="rock":
	print "player2 wins"
#else:
#print "player1 wins"
	
#if player1=="paper" and player2=="scissors":
#print "player2 wins"
#else:
#print "player1 wins"
	
		

