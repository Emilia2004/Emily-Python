def compose(f,g):
    return lambda x:f(g(x))
def double(a):
    return 2*a
def adding_10(a):
    return a + 10
func = compose(double,adding_10)
num = int(input("Enter number: "))
result = func(num)
print("Result after adding 10 then doubling is:",result)

