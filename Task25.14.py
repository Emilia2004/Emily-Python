def custom_map(func,iterable):
    for i in iterable:
        yield func(i)

gen = custom_map(lambda x:x*x,[1,2,3,7,8,9])
for i in gen:
    print(i)
