
num=int(input("Enter any four digit number:"))
odd=1
even=1
for i in range(4):
  digit=num%10
  if i==0 or i==2:
      
    even=even*digit
    num=num//10
  if i==1 or i==3:
      
    odd=odd*digit
    num=num//10
diff=odd-even
print("Difference b/w pro of dig at odd and pro of dig at even is:",diff)
