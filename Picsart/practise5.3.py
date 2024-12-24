a = 6
b = 3
c = 2
def somefunction(a,b,c):
    if isinstance(a, int) and isinstance(b,int) and isinstance(c,int):
        print(a*b*c)
    elif isinstance(a,str) and isinstance(b,int) and isinstance(c,int):
        print(a*b**c)
    elif isinstance(a,str) and isinstance(b,str) and isinstance(c,str):
        print(a+b+c)
    else:
        print("Invalid")
somefunction(a,b,c)
