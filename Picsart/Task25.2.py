def prime_generator(n):
        for i in range(2,n):
            flag = True
            for j in range(2,i//2):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                yield i

n = 100
gen = prime_generator(n)
for i in gen:
    print(i)
