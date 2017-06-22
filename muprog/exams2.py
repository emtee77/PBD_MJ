

#This program calculate postage cost for a company
#


weight=raw_input("What is the weight of this package: ")
where=raw_input("where is this package to be sent (domestic or overseas): ")
ExNorm=raw_input("Is this package to be sent by (Express post or Normal post): ")
recorded=raw_input("Is recorded delivery required (Y/N): ")
new=("Are you a new customer (Y/N): ")

weight=int(weight)		#to convert weight to an integer
Normaldomestic=5.0
normaloversea=7.50
expressdomestic=15.00
expressoverseas=20.00
Weighsurcharge=0.05*weight
Recorded=10.00
#to calculate total due for normal post domestic, recorded and new customer

if ExNorm == "Normal post":
	
	Totalbill=Normaldomestic+Recorded+Weighsurcharge
	Discount=0.10*Totalbill
	Totaldue=Totalbill-Discount
	
print "total bill equals:", Totaldue


#for normal post overseas

Totalbill=Normaloverseas+Recorded+Weighsurcharge
Discount=0.10*Totalbill
Totaldue=Totalbill-Discount

#for expresspost domestic


Totalbill=expressdomestic+Recorded+Weighsurcharge
Discount=0.10*Totalbill
Totaldue=Totalbill-Discount

for expresspost overseas

Totalbill=expressoverseas+Recorded+Weighsurcharge
Discount=0.10*Totalbill
Totaldue=Totalbill-Discount


#print Normal postage rate is:, normaldomestic
#print weight surcharge is:, weighsurcharge
#print recorded delivery is:, Recorded
#print subtototal is:, Totalbill
#print discount for new customer is:, Discount

#print"total bill is", Totaldue

