def listfunc(ls):
    for i in ls:
        print(i,end = " ")
size = int(input("Enter size of list: "))
ls = []
for i in range(size):
    ls.append(int(input("Enter element: ")))
listfunc(ls)
