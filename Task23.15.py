def uppercase(s):
    return s.upper()
def lowercase(s):
    return s.lower()
def titlecase(s):
    return s.title()
def reversing(s):
    rev = s[::-1]
    return rev

dict = {"upper" : uppercase,
        "lower" : lowercase,
        "title" : titlecase,
        "reverse" : reversing
        }

def manipulate_string(s,operation):
    st = dict[operation]
    return st(s)

string = input("Enter string message: ")
op = input("Enter operation: ")
print("The final result is:",manipulate_string(string,op))
