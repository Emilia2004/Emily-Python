def get_nth_element(iterable,n):
    iterator = iter(iterable)
    for i in range(n-1):
        next(iterator)
    return next(iterator)
ls = [41,21,10,5,9,65]
n = 3
print(get_nth_element(ls,n))
