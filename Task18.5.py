ls = [2,6,9,20,36,11]
def elements(ls):
    if not ls:
        return
    print(ls[0])
    elements(ls[1:])
elements(ls)
