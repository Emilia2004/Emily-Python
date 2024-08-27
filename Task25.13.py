def custom_filter(func,iterable):
    for item in iterable:
        if func(item):
            yield item

gen = custom_filter(lambda x: x if x % 2 == 0 else None, [1,2,3,4,5,6,22,26])
for i in gen:
    print(i)

