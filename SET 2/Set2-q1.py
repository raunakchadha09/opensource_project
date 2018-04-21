n1=0
n2=1
number=int(input("Enter the number of elements - "))
print (n1,n2," \n",end="")
for i in range(2,number):
  n3=n1+n2
  print (n3)
  n1=n2
  n2=n3
