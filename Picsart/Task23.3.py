def apply_twice(f,x):
    return f(f(x))
def square(n):
    return n*n
num = int(input("Enter number you want to square 2 times: "))
print(apply_twice(square,num))
