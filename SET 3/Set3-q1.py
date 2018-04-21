k=0;count=0;count1=0;space=1
rows=int(input("Enter number of rows : "))
for i in range(1,rows+1):
  for j in range(space,rows-i+1):
    print("  ",end="")
    count+=1
  while k!=2*i-1:
    if count<=rows-1:
      print("%d "%(i+k),end="")
      count+=1
    else:
      count1+=1
      print("%d "%(i+k-2*count1),end="")
    k+=1
  count1=0;count=0;k=0
  print("")

