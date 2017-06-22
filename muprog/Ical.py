#This program calculates simple interest

print "This program calculates simple interest"
print

principal=input("pls enter principal")
rate=input("pls enter rate")
years=input("pls enter no of years")

simpleinterest=principal*float(rate)/100*years



total=simpleinterest+principal

print "the principal is", principal, "the Interest is", simpleinterest, "the total is", total