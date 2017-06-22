# this program calculates factorial of a number
def main():
	n = int(raw_input("pls enter a number"))

	fact = 1
	for factor in range(1,n+1):
		fact = fact*factor
	print "factorial of", n, "is:", fact
main()