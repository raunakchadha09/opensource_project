
reversedNumber=0
n=int(input("\nEnter an integer : "))
while n!=0:
  remainder=n%10
  reversedNumber=reversedNumber*10+remainder
  n//=10
print("Reversed Number  : %d\n"%reversedNumber)  

