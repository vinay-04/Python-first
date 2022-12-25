
x=int(input("enter the number: "))
def fact(n):
    j=1
    for e in range(1,n+1):
        j=j*e
    return j

result=fact(x)
print(result)