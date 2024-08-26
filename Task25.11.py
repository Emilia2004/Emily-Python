def custom_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        res = next(it)
    else:
        res = initializer

    yield res
    for i in it:
        res = func(res,i)
        yield res

numbers = [1, 2, 3, 4, 5]
gen = custom_reduce(lambda x, y: x + y, numbers)

for i in gen:
    print(i)
