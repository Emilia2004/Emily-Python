def power_factory(n):
    def raising(i):
        return n ** i
    return raising
num = int(input("Enter number: "))
power = int(input("Enter power: "))
func = power_factory(num)
print(f"The {power} power of the number {num} is {func(power)}")
