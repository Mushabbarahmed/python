i=5
def factorial(n):
    fac=1

    for i in range(n):
        fac=fac*(i+1)
    return fac
def factorialr(n):
    if n==1:
        return 1
    else:
        return n*factorialr(n-1)
n=int(input("entre the number"))
print(factorial(n))
print(factorialr(n))