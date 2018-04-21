
from math import pow as p
binaryNumber=input("\nEnter a binary number : ")
 
#FOR CONFIRMING THAT USER's INPUT IS A BINARY NUMBER ONLY
flag=0                
while flag==0:
  temp_bin=binaryNumber
  if len(binaryNumber)==1:
    if binaryNumber=='0' or binaryNumber=='1':
      flag=1
    else:
      binaryNumber=input("Please input a valid binary number - ")
      temp_bin=binaryNumber
      flag=0
  else:
    init=0
    while init!=len(temp_bin)-1:
      init+=1
      if temp_bin[init]=='0' or temp_bin[init]=='1':
        flag=1 
      else:
        print("Error!The number inputted is not a binary number!! Kindly enter only 0's and 1's!")
        binaryNumber=input("\nEnter the binary number again : ")
        temp_bin=binaryNumber
        init=0
        flag=0

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
