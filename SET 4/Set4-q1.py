
from math import pow as p
binaryNumber=input("\nEnter a binary number : ")

#CONVERTING BIN TO OCT      
binaryNumber=int(binaryNumber)
binary=binaryNumber
octalNumber=0;decimalNumber=0;i=0
while binaryNumber!=0:
  decimalNumber+=(binaryNumber%10)*int(p(2,i))
  i+=1
  binaryNumber//=10
i=1
while (decimalNumber!=0):
  octalNumber+=(decimalNumber%8)*i
  decimalNumber//=8
  i*=10
print("\n\n\t%d in binary is %d in octal"%(binary,octalNumber))
