def make_memoize(f):
    cache = {}
    def func(*args):
        if args in cache:
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result
    return func

def square(n):
    return n * n
print(make_memoize(square)(3))


