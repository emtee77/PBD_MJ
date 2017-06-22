myfile = open('cities.txt', 'w')	#This is used to open a file, w-writes to the file 
myfile.write("Dublin\n")
myfile.write("Paris\n")
myfile.write("London\n")

myfile.close()	#it is good to always close the file when you are done with it


myfile = open("cities.txt", "r")	#This is used to open a file, r-reads the file
s1 = myfile.readline()
print s1
s2 = myfile.readline()
print s2
s3 = myfile.readline()
print s3

myfile.close()


myfile = open("cities.txt", "r")
lines = myfile.readlines()
myfile.close()
print lines
for line in lines:
	print line
	

myfile = open("cities.txt", "r")
for line in myfile:
	print line
myfile.close()