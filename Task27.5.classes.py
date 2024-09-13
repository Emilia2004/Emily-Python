class Product:
    def __init__(self,id,name,quantity):
        self.__product_id = id
        self.__product_name = name
        self.__quantity_in_stock = quantity

    def SetId(self,id):
        self.__product_id = id
    def GetId(self):
        return self.__product_id
    def SetName(self,name):
        self.__product_name = name
    def GetName(self):
        return self.__product_name
    def AddStock(self,quantity):
        self.__quantity_in_stock += quantity
    def ReduceStock(self,quantity):
        if self.__quantity_in_stock >= quantity:
            self.__quantity_in_stock -= quantity
        else:
            print("Can't do operation!")


concealer = Product(1212,"Concelear",150)

print(concealer.GetName())
concealer.AddStock(50)
concealer.SetId(1213)
print(concealer.GetId())
