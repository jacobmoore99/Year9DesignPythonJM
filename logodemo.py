print("1")
print("2")
print("3")
print("4")
print("5")
print("****************")

#how about 1 to 500
#there is a patern
#loop structure, specifically a for loop can be used to represent patterns

#<count> <check> <change>
#check: is count < check
for i in range(1, 5, 1):
	print(i)
#trace
#
# i =1
# i | i , 5 |
# 1 | 1 < 5 - True | run the loop
# etc.
#
#

print("*********")
for i in range(-345, 369, 1):
	#loop code block
	print(i)

print("*********")
for i in range(345, -46, -1):
	#loop code block
	print(i)