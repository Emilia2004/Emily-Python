def fibonacci_generator(n):
    a = 1
    b = 1
    for _ in range(n):
        yield a
        r = b
        b = a+b
        a = r


n = int(input("Enter number: "))
gen = fibonacci_generator(n)
for i in range(n):
    print(next(gen))
        
