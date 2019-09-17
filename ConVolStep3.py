import math
print("Volume of a Cylinder Formula: ")
#input
name = input ("What is your name: ") #takes users name
radius = input("\n\tInput radius(cm): ") #input
radius = (int)(radius) #cast to int

height = input ("Input height(cm): ") #input
height = (int)(height) #input
#what imputs are needed to calculate the volume of a cylinder?

#process
volume = math.pi*radius*radius*height
volume = round(volume, 2)
#what formula is used to calculate the volume of a cylinder?

#output
print("Hi "+name+"!")
print("Give a cylinder with:")
print("Radius = "+str(radius))
print("Height = "+str(height))
print("The volume is: "+str(volume)) 
#what is important about the output?