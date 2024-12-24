ls = [1,2,8,4,7,6]
def operation(data,/,*,oper = "sum"):
    if oper == "sum":
        return sum(data)
    elif oper == "max":
        return max(data)
    elif oper == "min":
        return min(data)
    else:
        return "Try another operation"
print(operation(ls,oper = "min"))

