ls = [3,8,9,65,23,45]
def len_list(ls):
    if not ls:
        return 0
    return 1 + len_list(ls[1:])
print(len_list(ls))
