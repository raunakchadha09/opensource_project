
print("The program works for the following range of inputs : \n")
print("48-57, 65-90, 97-122 \n")
ch=int(input("\nEnter the number from the range above - "))
flag=0
while flag!=1:
	if 47<ch<58 or 64<ch<91 or 96<ch<123:
		print("\n\tThe character for the given ASCII value is -> %s"%(chr(ch)))
		flag=1
	else:
		ch=int(input("Please enter a value from the given range only! -> "))
		flag=0 