class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def display(self):
        print(f"Name is: {self.name}, Age is: {self.__age}")

    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age >= 0:
            self.__age = age
        else:
            print("Invalis age")

name = "Jeko"
age = 70
ob = person(name,age)
ob.display()
ob.set_age(12)
print(ob.get_age())

