def squared():
    for i in range(1,21):
        yield i * i


gen = squared()
for i in gen:
    print(i)
