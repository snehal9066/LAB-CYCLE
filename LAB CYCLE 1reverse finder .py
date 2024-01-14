
num=int(input("Enter any 4 digit number:"))
rev=0
while(num>0):
  digit=num%10
  rev=rev*10+digit
  
  num=num//10
  
print("The reversed four digit number is:",rev)

