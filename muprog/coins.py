#This program shows how many coins is reqd to make up given amt

print "this prog cal reqd coins to make up a given amt"


print
amt=input("pls enter an amt")
intamount=int(amt*100)

#for E2
coins=intamount/200
intamount=intamount % 200

print"the number of E2 is", coins, 

#for E1
coins=intamount/100
intamount=intamount % 100

print"the number of E1 is", coins

#for 50c
coins=intamount/50
intamount=intamount % 50

print"the number of 50c is", coins

#for 20c
coins=intamount/20
intamount=intamount % 20

print"the number of 20c is", coins

#for 10c
coins=intamount/10
intamount=intamount % 10

print"the number of 10c is", coins

#for 5c
coins=intamount/5
intamount=intamount % 5

print"the number of 5c is", coins

#for 2c
coins=intamount/2
intamount=intamount % 2

print"the number of 2c is", coins

#for 1c
coins=intamount/1
intamount=intamount % 1

print"the number of 1c is", coins