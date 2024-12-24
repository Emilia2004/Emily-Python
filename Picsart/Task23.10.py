def make_config(key,value):
    dict = {}
    def dictionary():
        dict[key] = value
        return dict
    return dictionary

print(make_config("age",12)())
print(make_config("name","Ann")())


