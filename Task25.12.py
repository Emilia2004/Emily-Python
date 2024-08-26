def custom_zip(*iterables):
    min = len(iterables[0])
    for i in range(1,len(iterables)):
        if len(iterables[i]) < min:
            min = len(iterables[i])
    for i in range(min):
        ls = []
        for j in range(len(iterables)):
            ls.append(iterables[j][i])
        yield tuple(ls)


ls1 = [1,2,3,"hello"]
ls2 = [4,5,6,7,8]
gen = custom_zip(ls1,ls2)
for i in gen:
    print(i)
