#month.py
#A prog to print the month name, given its number
#This version uses a list as a look up table

#Months is a list used as a look up table

months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

n=input("Enter a month number (1-12):")
print "The month abbreviation is", months[n-1]