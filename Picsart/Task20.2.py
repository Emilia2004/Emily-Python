ls = []
size = int(input("Enter quantity of items: "))
for i in range(size):
    ls.append(int(input("Enter prices of items: ")))
taxx = int(input("Enter tax: "))
def price_calculator(*args,tax = 0):
    sum = 0
    for i in args:
        sum += i
    sum += tax
    return sum
print(price_calculator(*ls,tax = taxx))
