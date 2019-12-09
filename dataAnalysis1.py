print("DATA ANALYSIS 1")
#Big Skill: Reading from text file.
data = open("randomDataExtract1.txt","r"); 
dataString = data.read()
dataList = dataString.split("\n")
#Beyond the Coding:  
#	The order of the data could be important
#	if any of the analysis requires changing 
#	the order you need to make a copy of the 
#	information
print(dataList)
#Big Skill: Looping through a list using counted loop.  
for i in range(0, len(dataList),1):
	#Big Skill: Removing Elements
	dataList[i] = dataList[i].replace(",","")
	#Big Skill: Casting
	dataList[i] = float(dataList[i])

print(dataList)