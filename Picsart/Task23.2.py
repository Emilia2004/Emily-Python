def make_adder(n):
    def adder(i):
        return n+i
    return adder

number = int(input("Enter number: "))
adder1 = make_adder(number)
print("Adding 100 to number:",adder1(100))
