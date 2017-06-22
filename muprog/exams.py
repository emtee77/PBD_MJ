#studentname 	- Jimoh-Akindele Mutiu
#student number - 10276658

#This program converts degree celcius to degree fahrenheit and degree Kelvin

#The user will be presented with options available to them
#The user must be able to convert from celcius to fahrenheit and kelvin
#The user will be asked to input degree in celcius
#


print "This program converts from degree celcius to degree fahrenheit and degree kelvin"
user = raw_input("please state what you will like to convert to (fahrenheit or kelvin): ")
c 	 = raw_input("please enter your temperature in celcius: ")
c 	 = int(c)


if user == fahrenheit:
	fah = (c * 9/5) + 32	#to calculate degrees in fahrenheit
print" Your degree is: ", fah,"degrees" 

else:
	kelvin = c + 273.15		#to calculate degrees in kelvin
	
print"Your degree is: ", kelvin, "degrees", "."



	
