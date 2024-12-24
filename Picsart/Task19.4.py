number = int(input("Enter number: "))
def prime(n):
    count = 0
    for i in range(1,n//2+1):
        if n % i == 0:
            count += 1
    if count == 1:
        return True
    return False
print(prime(number))
