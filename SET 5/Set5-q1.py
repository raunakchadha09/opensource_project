
reversedInteger=0
n=int(input("Enter an integer : "))
originalInteger=n
while n!=0:
  remainder=n%10
  reversedInteger=reversedInteger*10+remainder
  n//=10
if originalInteger==reversedInteger:
  print("%d: Yes. It's a palindrome number\n"%originalInteger)
else:
  print("%d: No. It's not a palindrome number\n"%originalInteger)