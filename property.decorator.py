#   Task 1
class Person:
    def __init__(self,age):
        self.age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError  

#   Task2
class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width
    
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,height):
        if height > 0:
            self.__height = height
        else:
            raise ValueError
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,width):
        if width > 0:
            self.__width = width
        else:
            ValueError

    def area(self):
        return self.__height * self.__width
    
    def perimetr(self):
        return 2*(self.__width + self.__height)


#   Task 3  
class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self,celsius):
        self.__celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self,celsius):
        return (self._celsius * 9/5) + 32


#   Task 4
class Descriptor:
    def __get__(self, instance, owner):        
        return instance._score

    def __set__(self, instance, score):
        if 0 <= score <= 100:
            instance._score = score
        else:
            raise ValueError("Score must be between 0 and 100.")

class Student:
    score = Descriptor()

    def __init__(self, name, score):
        self.name = name
        self.score = score  


#   Task5

class ValidateString:
    def __init__(self,str):
        self.string = str

    @property
    def string(self):    
        return self.__string
    @string.setter
    def string(self,str):
        if str != "":
            self.__string = str
        else:
            raise ValueError
    
class User:
    def __init__(self,name):
        user = ValidateString(name)
        self.username = user.string


#   Task6

class Salary:
    def __init__(self,salary):
        self.salary = salary
    
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError
class Employee:
    def __init__(self,name,sal):
        salar = Salary(sal)
        self.name = name
        self.salary = salar.salary



#   Task7

class RangeDescriptor:
    def __init__(self,value):
        self.value = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self,valuee):
        if valuee >= 0 and valuee <= 100:
            self.__value = valuee
        else:
            raise ValueError

class Product:
    def __init__(self,value):
        price = RangeDescriptor(value)
        self.price = price.value


#   Task8
class ValidatePassword:
    def __init__(self,password):
        self.password = password

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        count = 0
        if len(password) >= 8:
            for i in password:
                if i.isdigit():
                    count += 1
        if count > 0:
            self.__password = password
        else:
            raise ValueError
        
class Account:
    def __init__(self,input):
        password = ValidatePassword(input)
        self.password = password.password

