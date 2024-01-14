def empde():
  
  ecode=int(input("Enter your employee code:"))
  ename=input("Enter the employee name:")
  bp=int(input("Enter the basic salary given:"))
  
  return ecode,ename,bp

ec,en,bap=empde()
def grossalary(BP):
  if BP<10000:
    DA=BP*(5/100)
    HRA=BP*(2.5/100)
    MA=500
    GS=BP+DA+HRA+MA
  elif BP>10000 and BP<30000:
    DA=BP*(7.5/100)
    HRA=BP*(5/100)
    MA=2500
    GS=BP+DA+HRA+MA
  elif BP>30000 and BP<50000:
    DA=BP*(11/100)
    HRA=BP*(7.5/100)
    MA=5000
    GS=BP+DA+HRA+MA
  else:
    DA=BP*(25/100)
    HRA=BP*(11/100)
    MA=7000
    GS=BP+DA+HRA+MA
  return GS
gs=grossalary(bap)
def deduction(Bap,Gros):
  if Bap<10000:
    PT=20
    PF=Bap*(8/100)
    IT=0
    ded=PT+PF+IT
  elif Bap>10000 and Bap<30000:
    PT=60
    PF=Bap*(8/100)
    IT=0
    ded=PT+PF+IT
  elif Bap>30000 and Bap<50000:
    PT=60
    PF=Bap*(11/100)
    IT=Bap*(11/100)
    ded=PT+PF+IT
  else:
    PT=80
    PF=Bap*(12/100)
    IT=Bap*(20/100)
    ded=PT+PF+IT
  return ded
d=deduction(bap,gs)
def netsalary(Bp,grs,D):
  if Bp<10000:
    NS=grs-D
  elif Bp>10000 and Bp<30000:
    NS=grs-D
  elif Bp>30000 and Bp<50000:
    NS=grs-D
  else:
    NS=grs-D
  return NS
net=netsalary(bap,gs,d)
print("=====PAYSLIP=====")
print("Employee code is:",ec)
print("Employee name is:",en)
print("Gross Salary is=",gs)
print("Deduction by=",d)
print("Net Salary is=",net)

