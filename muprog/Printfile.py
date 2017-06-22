# printfile.py
# print a file to the screen


fname = raw_input("Enter Filename:")
infile = open(fname, "r")
data = infile.read()
print data