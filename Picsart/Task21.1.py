def my_map(func,iterable):
    result = []
    for i in iterable:
        result.append(func(i))
    return result
def double(item):
    return item * 2

print(my_map(double,[1,5,6,3,7]))
