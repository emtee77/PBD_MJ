from car import car, Electriccar

my_car = car()
print my_car.engineSize

#print my_car.make		#make is private instance and will not print, it gives error

print my_car.getmake()	#to be able to print make, add another function called def getmake

print my_car.getcolour()

print my_car.getmileage()

my_car.engineSize = "2.4l" #there is no need for setengineSize as it is public and could be updated with this code
print my_car.engineSize

my_car.setmake("BMW")
print my_car.getmake()

my_car.setcolour("Black")
print my_car.getcolour()

my_car.setmileage(5000)
print my_car.getmileage()

my_car.move(10)
print my_car.getmileage()

my_car.paint("black")
print my_car.getcolour()
#my_car.engineSize = "3.6l" #updating engineSize needs no set function as it is public, otherwise there will be a need for setengineSize function

#print my_car.engineSize

electric_car = Electriccar()
print electric_car.getnumberFuelCells()

electric_car.move(20)
print electric_car.getmileage()