def subkd():
    s=input("Enter a string:")
    k=int(input("Enter the length:"))
    t=len(s)
    sub=[]
    for i in range(0,t+1):
      for j in range(i+1,t+1):
        sub.append(s[i:j])
    print(sub)
    for a in sub:
      b=set(a)

      if len(b)==k:
        print("distinct characters")
        print(b)

subkd()
