def fibo():
    x=int(input("Till : "))
    fib=0
    i=0
    j=1
    while (fib <=x):
        fib=i+j
        j=i
        i=fib
        print(fib)
fibo()