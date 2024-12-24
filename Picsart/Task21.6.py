def apply(func,iterable):
    return [func(element) for element in iterable]
def double(n):
    return n * 2
ls = [1,2,3]
print(apply(double,ls))
