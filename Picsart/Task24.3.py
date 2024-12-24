def validate(fn):
    def wrapper(*args,**kwargs):
        for arg in args:
            if not isinstance(arg,int) or arg < 0:
                return "Arguments must be positive integers"
        for kwarg in kwargs.values():
            if not isinstance(kwarg,int) or arg < 0:
                return "Arguments must be positive integers"

        return fn(*args,**kwargs)
    return wrapper

def add(a:int,b:int,*,c:int):
    return a+b+c


print(validate(add)(6,1,c=3))
