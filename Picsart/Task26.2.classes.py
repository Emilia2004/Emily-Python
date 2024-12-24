class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name is:",self.name)
        print("Age is:",self.age)

name = input("Enter name of user: ")
age = int(input("Enter age of user: "))
ob = Person(name,age)
ob.display()
