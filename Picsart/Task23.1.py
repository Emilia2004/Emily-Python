x = lambda i: lambda num : num * i
number = int(input("Enter number: "))
func = x(number)
print("Doubled value is:",func(2))

