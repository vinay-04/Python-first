i=int(input("enter no."))
for x in range(2,i,1):
    if (i%x==0):
        print("Not prime")
        break
else:
    print("Prime Number")
