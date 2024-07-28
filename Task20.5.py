product = {
        "type" : "car",
        "name" : "mercedes",
        "colour" : "black",
        "birth" : 2008 }
def display_product(*,type,name,colour,birth):
    print(type,name,colour,birth)
display_product(**product)
