#Formatting program

my_name=raw_input("Enter a name :")
my_age=raw_input("Enter age :")
my_height=raw_input("Enter height (in cm) :")
my_weight=raw_input("Enter weight in kilos :")
my_eyes=raw_input("Enter eyes colour :")
my_teeth=raw_input("Enter teeth colours :")
my_hair=raw_input("Enter hair colours :")

Total=int(my_age)+int(my_weight)+int(my_height)

print "Let's talk about %s." % my_name
print "He's %s, years old." % my_age
print "He's %s, tall." % my_height
print "He's %s, kilos heavy." %my_weight
print "Actually thats a normal weight."
#print "He's got %s %s eyes and hair." %my_eyes, my_hair
print "He's got %s, eyes." %my_eyes
print "His teeth is %s," %my_teeth

print "if i add his age, weight and height, I get", Total 
