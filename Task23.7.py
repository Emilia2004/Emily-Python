func = lambda x : x if x % 2 == 0 else None 
ls = [1,2,3,4,5,6,26]
result = filter(func,ls)
print(list(result))

