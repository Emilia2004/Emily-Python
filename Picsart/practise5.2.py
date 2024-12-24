def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact
number = int(input("Enter number:"))
print(f"The factorial of {number} is {factorial(number)}")
