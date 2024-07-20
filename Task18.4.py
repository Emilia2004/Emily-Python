number = int(input("Enter number: "))
sum = 0
def sum_of_number(n):
    global sum;
    if n == 1:
        return 1
    sum += n + sum_of_number(n-1)
    return sum
print(f"The sum the first {number} numbers is {sum_of_number(number)}")
