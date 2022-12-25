p=-1
def find(list ,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['p']=mid
            return True
        else:
            if list[mid]<n:
                l=mid
            else:
                u=mid
        return False
list=[12,32,34,65,78]
n=input("enter no. : ")

if find(list,n):
    print("found at",p+1)
else:
    print("not found")

