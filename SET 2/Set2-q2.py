
rows=int(input("Enter number of rows : "))
space=0
for i in range(rows,0,-1):
  for j in range(space,rows-i):
    print("  ",end="")
  for k in range(i,2*i):
    print("* ",end="")
  for l in range(0,i-1):
    print("* ",end="")
  print("")
  
