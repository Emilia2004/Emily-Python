ls = []
size = int(input("Enter count of people: "))
for i in range(size):
    dict = {}
    t = True
#username validation
    while t:
        dict["Name:"] = input("Enter username: ")
        count = 0
        if len(dict["Name:"]) >= 5 and len(dict["Name:"]) <= 20:
            for i in dict["Name:"]:
                if i.isalpha() or i.isdigit():
                    count += 1
        else:
           print("Try again please!")
        if count == len(dict["Name:"]):
            t = False
        else:
            print("Try again please!")

#mail validation
    while not t:
        dict["Mail:"] = input("Enter email: ")
        if "@" in dict["Mail:"] and (dict["Mail:"].endswith(".com") or dict["Mail:"].endswith(".ru")):
            t = True
        else:
            print("Try again please!")
        

#password validation
    while t:
        dict["Password:"] = input("Enter password: ")
        signs = ["!","@","#","%","^","&","*","(",")","[","]","{","}"]
        upper = 0
        lower = 0
        digit = 0
        sign = 0
        if len(dict["Password:"]) >= 8:
            for i in dict["Password:"]:
                if i.isupper():
                    upper = 1
                elif i.islower():
                    lower = 1
                elif i.isdigit():
                    digit = 1
                elif i in signs:
                    sign = 1
            if upper and lower and digit and sign:
                t = False
            else:
                print("Try again please!")
        else:
            print("Try again please!")



#password repeat validation
    while not t:
        dict["Password repeat:"] = input("Enter password repeat: ")
        if dict["Password repeat:"] == dict["Password:"]:
            t = True
        else:
            print("Try again please!")





#phone numbervalidation
    while t:
        dict["Phone:"] = input("Enter phone number: ")
        if len(dict["Phone:"]) == 9 and dict["Phone:"].startswith("0"):
            t = False
        elif len(dict["Phone:"]) == 12 and dict["Phone:"].startswith("+"):
            t = False
        else:
            print("Try again please!")
    ls.append(dict)

for i in range(size):
     for j, k in ls[i].items():
            print(j,k)
