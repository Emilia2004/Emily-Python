number = int(input("Enter number: "))
def power_of_2(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n/= 2
    return n == 1
print(power_of_2(number))
