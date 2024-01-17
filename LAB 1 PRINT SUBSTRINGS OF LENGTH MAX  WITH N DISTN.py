def subkdm():
    s=input("Enter a string:")
    t=len(s)
    sub=[]
    l1=[]
    for i in range(0,t+1):
      for j in range(i+1,t+1):
        sub=set(s[i:j])
        l=len(sub)
        l1.append(l)
    ma=max(l1)
    for i in range(0,t+1):
      for j in range(i+1,t+1):
        sub=set(s[i:j])
        l=len(sub)
        if l==ma:
          print(sub)

subkdm()
