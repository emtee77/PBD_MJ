# This progra calculates the compound interest

#ask for principal
#ask for rate
#ask for years

#for each year: 
#	interest=principal*rate
#	principal=principal+interest
#	print out interest and year earned e.g "year x, earned y interest"

#	at the end print out the total amount e.g "total amount including interest is z"

principal=input("pls enter principal")
time=input("pls enter number of years")
rate=input("pls enter rate")



for i in range (time):
	Interest=principal*rate
	principal=principal+Interest
	
	print"the interest for year", i+1, "is", principal


