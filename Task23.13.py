def bar(n):
    ls = []
    for i in range(n):
        def multiply(m):
            return m*i
        ls.append(multiply(2))
    return (ls)

size = int(input("Enter how many functions you want to create: "))
print(bar(size))

