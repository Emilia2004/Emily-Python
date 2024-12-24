def make_accumulator(start=0):
    def add(n):
        nonlocal start;
        start += n
        return start
    return add
start = int(input("Enter start value: "))
func = make_accumulator(start)
adding = int(input("Enter adding value: "))
print(func(adding))
print(func(adding))
print(func(adding))

