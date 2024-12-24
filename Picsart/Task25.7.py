def custom_range(start, end, step):
    size = int((end-start)/step)
    for i in range(size+1):
        yield start 
        start += step

gen = custom_range(0, 5, 0.5)
for i in gen:
    print(i)
