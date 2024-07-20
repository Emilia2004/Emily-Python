number = 5
def any_function(n):
    if n < 1:
        return
    print(n,end = " ")
    any_function(n-1)
any_function(number)
