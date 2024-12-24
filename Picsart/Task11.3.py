ls = []
len_of_list = int(input("Enter length of list: "))
for i in range(len_of_list):
    ls.append(int(input("Enter element of list: ")))
if len(ls) == 0:
    print("NO element in list")
else:
    x = ls[len(ls)-1]
    del ls[len(ls)-1]
    print(x)
    print("Our list becomes: ",ls)
