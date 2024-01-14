number=int(input("Enter a four digit number:"))
sum=0
while (number>0):
    digit=number%10
    sum=sum+digit
    number=number//10

print("Sum of the digits:",sum)
