#Filereader.py

import string

infile=open("testdata.csv", "r")

outfile=open("testoutput.csv", "w")

country=raw_input("Pls Enter Country: ")
counter=0
for line in infile:
	counter=counter+1
	if counter % 10 == 0:
		print "processed" ,counter, "records"
	lfield=string.split(line, ",")
	if lfield[3]=="japan":
		outfile.write(line+"\n")
		

outfile.close()
infile.close()