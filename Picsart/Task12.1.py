len_of_lists = int(input("Enter length of lists: "))
ls1 = []
ls2 = []
for i in range(len_of_lists):
    ls1.append(int(input("Enter elements of list1: ")))
    ls2.append(int(input("Enter elements of list2: ")))
for i in range(len_of_lists):
    if ls1[i] != ls2[i]:
        print("Not equal!")
        break
else:
    print("Lists are equal!")
