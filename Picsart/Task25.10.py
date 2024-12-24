def exception_propagator(iterable):
    for i in iterable:
        if i == "error":
            raise ValueError("An error occured")
        yield i
iterable = [1,5,"error",4,6]
gen = exception_propagator(iterable)
for i in gen:
    print(i)
