n=int(input("Enter the number of months:"))
n1=1
n2=1
n3=0
print("MONTHS \t\t RABBITS")
for j in range(n):
      if j==0:
         print(j+1,'\t\t',n1)
      elif j==1:
         print(j+1,"\t\t",n2)
      else:
            n3=n1+n2
            print(j+1,"\t\t",n3)
            n1=n2
            n2=n3
