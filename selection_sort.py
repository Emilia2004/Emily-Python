def selection(ls):
    size = len(ls)
    for i in range(size):
        min_index = i
        for j in range(i+1,size):
            if ls[j] < ls[min_index]:
                min_index = j
        ls[min_index],ls[i] = ls[i],ls[min_index]
    return ls

ls = [12,56,47,1,21]
print(selection(ls))