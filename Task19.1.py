nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
def flatten_list(ls):
    list = []
    for i in ls:
        if isinstance(i,int):
            list.append(i)
        else:
                list.extend(flatten_list(i))
    return list
flattened = flatten_list(nested_list)  
print(flattened)
