number = 5
def any_function(n):
    if n < 1:
        return
    any_function(n-1)
    print(n,end = " ")
any_function(number)
