
c=input("\nEnter a character : ")
while len(c)!=1:
	c=input("\nPlease enter a character of length 1 only! -> ")
print ("ASCII of %s -> %d"%(c,ord(c)))