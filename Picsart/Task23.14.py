def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "Can't divide"
    return a/b
dict = {"+" : add,
        "-" : sub,
        "*" : mul,
        "/" : div
        }

def calculate(operand1,operand2,operator):
    op = dict[operator]
    return op(operand1,operand2)

op1 = int(input("Enter 1st operand: "))
op2 = int(input("Enter 2nd operand: "))
oper = input("Enter operator: ")
print("The final result is:",calculate(op1,op2,oper))
