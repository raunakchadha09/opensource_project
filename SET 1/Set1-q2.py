result=0
number=input("\nEnter any three digit number - ")
while len(number)!=3:
	number=input("ERROR! The number inputted isn't a three digit number, input again! -> ")
number=int(number)
originalNumber=number
while originalNumber!=0:
	remainder=originalNumber%10
	result+=remainder**3
	originalNumber//=10
if result==number:
	print("\n\t%d is an armstrong number!!\n"%(number))
else:
	print("\n\t%d is not an armstrong number!!!\n"%(number))
