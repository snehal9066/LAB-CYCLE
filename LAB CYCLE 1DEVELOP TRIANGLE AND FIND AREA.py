def sides():
  x=int(input("Enter the 1st side of the triangle:"))
  y=int(input("Enter the 2nd side of the triangle:"))
  z=int(input("Enter the 3rd side of the triangle:"))
  return x,y,z
def area(p,q,r):
  s=(p+q+r)/2
  ar=(s*(s-p)*(s-q)*(s-r))**1/2
  return ar
def totarea(a1,a2):
  areaen=a1+a2
  print("Total area enclosed by",areaen)
  areacom1=(a1/areaen)*100
  areacom2=(a2/areaen)*100
  print("Area given by triangle 1:",areacom1)
  print("Area given by triangle 2:",areacom2)
s1,s2,s3=sides()
s4,s5,s6=sides()
area1=area(s1,s2,s3)
print("Area of 1st triangle:",area1)
area2=area(s4,s5,s6)
print("Area of 2nd trinagle:",area2)
cont=totarea(area1,area2)
