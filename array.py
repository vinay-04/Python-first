from array import *
ar=array('i',[])
n=int(input("enter len"))
for i in range(n):
    x=int(input("enter next val"))
    ar.append(x)
print(ar)
sr=int(input("search"))
k=1
for y in ar:
    if y==sr:
        print(k,"term")
        break
    k+=1