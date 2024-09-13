class Shopping_cart:
    def __init__(self,items):
        self.__items = items

    def add(self,item):
        self.__items.append(item)
        return self.__items
    def remv(self,item):
        a =  self.__items(item)
        del a
        return self.__items
    def count(self):
        return len(self.__items)
    
mycart = Shopping_cart(["book","bread","apple"])
print(mycart.count())
print(mycart.add("pen"))
print(mycart.count())
