def first_big_letter(st):
    for i in st:
        if i.isupper():
            print(i)
            break
string = input("Enter text: ")
first_big_letter(string)
