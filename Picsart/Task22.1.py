def make_multiplier_of(n):
    def mul(i):
        return n * i
    return mul

number = int(input("Enter number: "))
s = make_multiplier_of(number)
multiplier = int(input("Enter multiplying number: "))
print("The final result is: ",s(multiplier))


