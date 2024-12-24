number = int(input("Enter number: "))
def fibonacci(n):
    ls = [1,1]
    prev = 1
    prev_prev = 1
    curr = 0
    for i in range(2,n):
        curr = prev + prev_prev
        prev_prev = prev
        prev = curr
        ls.append(curr)
    return ls
print(fibonacci(number))
