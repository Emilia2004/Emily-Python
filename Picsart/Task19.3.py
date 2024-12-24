list = []
size = 5
for i in range(size):
    list.append(int(input("Enter elements: ")))
def ascending(ls):
    if not ls or len(ls) == 1:
        return True
    if ls[0] > ls[1]:
        return False
    return ascending(ls[1:])
print(ascending(list))
