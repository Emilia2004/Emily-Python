ls = [12,4,86,57,66,48,59]
def bubble(ls):
    for i in range(len(ls)):
        count = 0
        for j in range(len(ls)-1-i):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]
                count += 1
        if count == 0:
            return ls
    return ls    

ls = [12,4,86,57,66,48,59]
list = [1,2,3,3,4,5,6]
print(bubble(list))
print(bubble(ls))

