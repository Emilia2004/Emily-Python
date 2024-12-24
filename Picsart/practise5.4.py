def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact
def somefunction(a = None,b = None,c = None,d = None):
    if b == None and c == None and d == None:
        print(factorial(s))
    elif c == None and d == None:
        print(a**b)
    elif d == None:
        print(a*b*c)
    else:
        print(a+b+c+d)
somefunction(2,3,4)
