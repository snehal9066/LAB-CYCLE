def subp():
  st=input("Enter a string:")
  k=len(st)
  for i in range(0,k+1):
      for j in range(i+1,k+1):
         a=st[i:j]
         b=a[::-1]

         if b==a:
          print(b)
subp()
