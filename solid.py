#   1. Single Responsibility Principle 
#   Bad example 
class car:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour

    def car_company(self):
        return f"Car company is {self.name}"

    def car_appearance(self):
        return f"Car is {self.colour}"
    
#   Solution

class car:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour

class company:
    def car_company(self,car):
        return f"Car company is {car.name}"
    
class colour:
    def car_appearance(self,car):
        return f"Car is {car.colour}"
    

#   2. Open/Closed Principle
#   Bad example

class sorting_books:
    def booktype(self,type):
        if type == "Fiction":
            return f"Book is type of Fiction"
        
        elif type == "Adventure":
            return f"Book is type of Fiction"

#   Solution
from abc import ABC, abstractmethod

class sorting_books(ABC):
    @abstractmethod
    def sorting(self):
        ...

class sorting_fiction(sorting_books):
    def sorting(self):
        return "Book is type of fiction"

class sorting_adventure(sorting_books):
    def sorting(self):
        return "Book is type of adventure"
    
class sorting_detective(sorting_books):
    def sorting(self):
        return "Book is type of detective"
    

#   3. Liskov Substitution Principle
#   Bad example

class plant:
    def blooming(self):
        return "Blooming"

class grass(plant):
    def blooming(self):
        raise NotImplementedError("Grass doesn't bloom")
    
#   Solution

class plant:
    def growing(self):
        return "growing"

class flower(plant):
    def blooming(self):
        return "blooming"
    
class grass(plant):
    def growing(self):
        return "growing"


#   4. Interface Segregation Principle
#   Bad example

class university:
    def studying(self):
        return "studying"
    def drinking_coffee(self):
        return "drinking coffee"

class student(university):
    def studying(self):
        return "Student is studying"
    def drinking_coffee(self):
        return "Student is drinking coffee"
    
class professor(university):
    def studying(self):
        return NotImplementedError("Professor doesn't study")
    def drinking_coffee(self):
        return "Professor is drinking coffee"

#   Solution
class study:
    def studying(self):
        pass

class coffee:
    def drinking_coffee(self):
        pass

class student(study,coffee):
    def studying(self):
        return "Student is studying"
    def drinking_coffee(self):
        return "Student is drinking coffee"
    
class professor(coffee):
    def drinking_coffee(self):
        return "Professor is drinking coffee"
    

#   5. Dependency Inversion Principle 
#   Bad example

class fruit_selling:
    def sell_fruit(self,fruit):
        return f"selling {fruit}"
    
class goods_selling:
    def __init__(self):
        self.fruit = fruit_selling()
    
    def sell(self,fruit):
        self.fruit.sell_fruit(fruit)

#   Solution

from abc import ABC, abstractmethod

class goods_selling(ABC):
    @abstractmethod
    def sell(self, good):
        pass

class fruit_selling(goods_selling):
    def sell(self, fruit):
        return f"Selling {fruit}"
class bread_selling(goods_selling):
    def sell(self, bread):
        return f"Selling {bread}"


