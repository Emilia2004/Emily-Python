def my_filter(func,iterable):
    result = []
    for i in iterable:
        if func(i):
            result.append(i)
    return result
def even(n):
    if n%2 == 0:
        return True
    return False

print(my_filter(even,[2,8,15,23,16,22,100]))
