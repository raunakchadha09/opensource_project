count=0
n=int(input("Enter any number - "))
while n!=0:
	n//=10
	count+=1
print ("The count - %d"%count)