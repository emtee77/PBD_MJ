infile = open(somefile, "r")
for i in range(3):
	line=infile.readline()
	print line[:-1]