ls = []
len_of_list = int(input("Enter len of list: "))
for i in range(len_of_list):
    ls.append(int(input("Enter element of the list: ")))
newls = []
change_index = int(input("Enter the index you want to change: "))
new_element = int(input("Enter new element: "))
if change_index > len_of_list - 1:
    print("Index error")
else:
    for i in range(len(ls)):
        if i == change_index:
            newls.append(new_element)
        newls.append(ls[i])
print(newls)

