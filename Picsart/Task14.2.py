ls = []
size = int(input("Enter count of people: "))
for i in range(size):
    dict = {}
    dict["Name:"] = input("Enter name: ")
    dict["Surname:"] = input("Enter surname: ")
    dict["Id:"] = int(input("Enter ID: "))
    dict["Mail:"] = input("Enter email: ")
    dict["Password:"] = input("Enter password: ")
    dict["Phone:"] = int(input("Enter phone number: "))
    ls.append(dict)
name = input("Enter the name you are searching for: ")
flag = True
for i in range(size):
        if ls[i]["Name:"] == name:
            for j, k in ls[i].items():
                print(j,k)
            flag = False
if flag:
    print("Not found")
    

