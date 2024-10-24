from abc import abstractmethod
class Car:
    def __init__(self,make,model,price):
        self.make = make
        self.model = model
        self.price = price

    
    @abstractmethod
    def show_car_type(self):
        ...

class Electric(Car):
    def __init__(self, make, model, price):
        super().__init__(make, model, price)

    def show_car_type(self):
        print("Electric car")

class Hybrid(Car):
    def __init__(self, make, model, price):
        super().__init__(make, model, price)

    def show_car_type(self):
        print("Hybrid")    


class Customer:
    def __init__(self,name,info):
        self.__name = name
        self.__info = info
        self.purchases = []
    
    def purchase_car(self,car,seller):
        if seller.sell_car(car):
            self.purchases.append(car)
        else:
            print("No such car")

class Salespeople:
    def __init__(self,name,rate):
        self.__name = name
        self.__rate = rate
        self.cars = []
        self.history = []

    def add_car(self,car):
        self.cars.append(car)

    def sell_car(self,car):
        if car in self.cars:
            self.history.append(car)
            self.cars.remove(car)
            return True
        else:
            return False
        
    def view_history(self):
        for item in self.history:
            print(item.model,item.make)




