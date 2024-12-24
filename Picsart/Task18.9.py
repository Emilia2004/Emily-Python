string = input("Enter string: ")
def print_newline(st):
    if not st:
        return 
    print(st[0])
    print_newline(st[1:])
print_newline(string)
