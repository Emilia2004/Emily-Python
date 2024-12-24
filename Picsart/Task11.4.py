ls = []
len_of_list = int(input("Enter length of list: "))
for i in range(len_of_list):
    ls.append(int(input("Enter element of list: ")))
for i in range(len(ls)):
    del ls[len_of_list-i-1]
print(ls)
