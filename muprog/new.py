n = 100
sum = 0
i = 1
while i <= n:
  sum = sum + i
  i = i + 1
print "Sum of 1 until %d: %d" % (n,sum)



n = 10
mult = 1
i = 1
while i <= n:
  mult = mult * i
  i = i + 1
print "Multiplication of 1 until %d: %d" % (n,mult)



amount = float(raw_input("Please enter an amount"))
cent_amount = amount * 100
print(cent_amount)


amount = float(raw_input("Please enter an amount?"))
cent_amount = amount * 100
print("The number of euro in cents is : %d" %(cent_amount))
