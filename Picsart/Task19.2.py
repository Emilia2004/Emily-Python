ls = [2,6,9,25,1]
def sum_of_elements(list):
    if len(list) == 0:
        return 0
    return list[0] +  sum_of_elements(list[1:])
print(sum_of_elements(ls))
