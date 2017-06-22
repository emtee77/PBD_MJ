#Test Exception.py

invalid=1
while invalid==1:
	try:
		invalid=0
		instr=raw_input("Pls enter integer")
		inint=int(instr)
	except:
		print "Ooops...."
		invalid=1
	