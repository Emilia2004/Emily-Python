def even():
    yield [x for x in range(1,51) if x % 2 == 0]


gen = even()
print(next(gen))
