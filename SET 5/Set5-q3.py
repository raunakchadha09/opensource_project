
rows=int(input("Enter rows to print : "))
stars=1; spaces=rows-1;
for i in range(1,rows*2):
  for j in range(1,spaces+1):
    print (" ",end="")
  for j in range(1,stars*2):
    print ("*",end="")
  print ("")
  if (i<rows):
    spaces-=1
    stars+=1
  else:
    spaces+=1
    stars-=1
