ls = []
len_of_list = int(input("Enter lenght of list: "))
for i in range(len_of_list):
    ls.append(int(input("Enter elements of list: ")))
max = ls[0]
min = ls[0]
for i in range(1,len_of_list):
    if ls[i] > max:
        max = ls[i]
    else:
        min = ls[i]
for i in range(len_of_list):
    if ls[i] == max:
        for j in range(len_of_list):
            if ls[j] == min:
                print("The difference between max and min indexes is: ",i-j)
                break
