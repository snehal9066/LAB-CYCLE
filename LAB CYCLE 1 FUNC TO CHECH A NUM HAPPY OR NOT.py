def happynumb(num):
    count=0
    temp=num
    while count<200:
      sum=0
      while(num>0):
        di=num%10
        sum=sum+di**2
        num=num//10
      if sum==1:
        print(temp,"is a happy number")
        break
      else:
        count+=1
        num=sum
      if count==100:
        print(temp,"is not a happy number")
n=int(input("Enter the number:"))
happynumb(n)
