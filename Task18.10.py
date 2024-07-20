word = input("Enter word: ")
def polindrome(st):
    if not st:
        return True
    if st[0] != st[len(st)-1]:
        return False
    return polindrome(st[1:-1])
print(polindrome(word))
