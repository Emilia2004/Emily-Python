ls = []
len_of_list = int(input("Enter len of list: "))
for i in range(len_of_list):
    ls.append(int(input("Enter element of list: ")))
newls = []
count = 0
change_element = int(input("Enter element you want to remove: "))
for i in range(len(ls)):
    if ls[i] == change_element:
        del ls[i]
        break
    newls.append(ls[i])
    count += 1
if count == len(ls):
    print("NO such an element")
else:
    for i in range(count,len(ls)):
        newls.append(ls[i])
print(newls)

