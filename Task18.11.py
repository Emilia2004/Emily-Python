number = int(input("Enter number: "))
def sum_of_digits(n):
    if n == 0:
        return 0
    return sum_of_digits(n//10) + n % 10
print(sum_of_digits(number))
