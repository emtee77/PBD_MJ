
import string
months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
inputdate=raw_input("pls enter date in format mm/dd/yyyy")

mm,dd,yyyy=string.split(inputdate, "/")

print "the date is", dd, months[int(mm)-1], yyyy, "."

#replace(s, s, n)