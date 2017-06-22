#get users first and last names

first=raw_input("pls enter your first name (all lower cases):")
last=raw_input("pls enter your last name (all lower cases):")

#Concatenete first initial with 7 chars of last name

uname=first[0] + last[:7]
#uname=last[:6]+first[:2]

print "uname is", uname