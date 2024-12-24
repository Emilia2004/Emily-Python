def max_in_list(ls):
    max = ls[0]
    for i in range(1,len(ls)):
        if ls[i] > max:
            max = ls[i]
    print("Maximum element is:",max)
def min_in_list(ls):
    min = ls[0]
    for i in range(1,len(ls)):
        if ls[i] < min:
            min = ls[i]
    print("Minimum element is:",min)
size = int(input("Enter size of list: "))
ls = []
for i in range(size):
    ls.append(int(input("Enter element: ")))
if size > 0:
    max_in_list(ls)
    min_in_list(ls)
else:
    print("Invalid size")
