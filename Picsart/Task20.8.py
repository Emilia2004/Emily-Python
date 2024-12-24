def update(**kwargs):
    for i,j in kwargs.items():
        print(f"{i} : {j}")

def user(**kargs):
    print("Updating settings!")
    update(**kargs)

user(name = "Bob",language = "Armenian",university = "YSU")
