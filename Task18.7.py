string = "family"
def reverse(st):
    if not st:
        return ""
    return reverse(st[1:]) + st[0]
print(reverse(string))
