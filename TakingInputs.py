#comments are made with a #
#it is essential you comment code.

#This program will take two integers
#And multiply them

#input
#the input function returns the string the user 
#all inputs start as strings
#to change the type of variable you "cast" it
#casting is the process of changing type
name = input ("Please input your name: ")
a = input ("Please input first number: ")
a = int (a) #self-refrencing assignment statement
b = input ("Please input second number: ")
b = int (b)

#procces
#what is process
product = (a * b)


#output
print ("Hi, " +name)
print ("The product of "+str(a)+" and "+str(b)+" is "+str(product)+".")