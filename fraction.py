class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.setNumerator(numerator)
        self.setDenominator(denominator)

    def setNumerator(self,numerator:int):
        if isinstance(numerator,int):
            self.__numerator = numerator
        else:
            raise ValueError("Numerator must be integer")
        
    def getNumerator(self):
        return self.__numerator
    
    def setDenominator(self,denominator:int):
        if denominator == 0:
            raise ZeroDivisionError
        if isinstance(denominator,int):
            self.__denominator = denominator
        else:
            raise ValueError("Denominator must be integer")
        
    def getDenominator(self):
        return self.__denominator
    
    def __str__(self) -> str:        
        return f"{self.__numerator}/{self.__denominator}"    
    
    def __repr__(self) -> str:
        fraction = self.lowestterm(self.__numerator,self.__denominator)
        return f"Fraction({fraction.__numerator}, {fraction.__denominator})"
    
    def lowestterm(self,nominator,denominator):
        divisor = 1
        if nominator < denominator:
            for i in range(2,nominator+1):
                if nominator % i == 0 and denominator % i == 0:
                    divisor = i
        else:
            for i in range(2,denominator+1):
                if nominator % i == 0 and denominator % i == 0:
                    divisor = i
        nominator //= divisor
        denominator //= divisor
        return Fraction(nominator,denominator)
            
    def __add__(self, other):
        if isinstance(other,Fraction):
            numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
            denominator = self.__denominator * other.__denominator
        elif isinstance(other,int):
            numerator = self.__numerator + other * self.__denominator
            denominator = self.__denominator
        else:
            raise ValueError("Can't implement + operation")
        return self.lowestterm(numerator,denominator)
    
    def __sub__(self,other):
        if isinstance(other,Fraction):
            numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
            denominator = self.__denominator * other.__denominator
        elif isinstance(other,int):
            numerator = self.__numerator - other * self.__denominator
            denominator = self.__denominator
        else:
            raise ValueError("Can't implement - operation")
        return self.lowestterm(numerator,denominator)
    
    def __mul__(self,other):
        if isinstance(other,Fraction):
            numerator = self.__numerator * other.__numerator
            denominator = self.__denominator * other.__denominator
        elif isinstance(other,int):
            numerator = self.__numerator * other
            denominator = self.__denominator
        else:
            raise ValueError("Can't implement * operation")
        return self.lowestterm(numerator,denominator)

    def __truediv__(self,other):
        if isinstance(other,Fraction):
            numerator = self.__numerator * other.__denominator
            denominator = self.__denominator * other.__numerator
        elif isinstance(other,int):
            numerator = self.__numerator 
            denominator = self.__denominator * other
        else:
            raise ValueError("Can't implement / operation")
        return self.lowestterm(numerator,denominator)
    
    def __eq__(self, other):
        if isinstance(other,Fraction):
            f1 = self.lowestterm(self.__numerator,self.__denominator) 
            f2 = self.lowestterm(other.__numerator,other.__denominator)
            return f1.__numerator == f2.__numerator and f1.__denominator == f2.__denominator
        elif isinstance(other,int):
            f1 = self.lowestterm(self.__numerator,self.__denominator) 
            return f1.__numerator == f1.__denominator * other
        else:
            raise ValueError("Can't do == operation")
        return False
    
    def __ne__(self, other):
        if isinstance(other,Fraction):
            if self.lowestterm(self.__numerator,self.__denominator) != self.lowestterm(other.__numerator,other.__denominator):
                return True
        elif isinstance(other,int):
            if int(self.lowestterm(self.__numerator,self.__denominator)) != other:
                return True
        else:
            raise ValueError("Can't do != operation")
        return False
    
    def __lt__(self, other):
        if isinstance(other,Fraction):
            if self.__numerator * other.__denominator < self.__denominator * other.__numerator:
                return True
        elif isinstance(other,int):
            if self.__numerator < other * self.__denominator:
                return True
        else:
            raise ValueError("Can't do < operation")
        return False
    
    def __le__(self, other):
        if isinstance(other,Fraction):
            if self.__numerator * other.__denominator <= self.__denominator * other.__numerator:
                return True
        elif isinstance(other,int):
            if self.__numerator <= other * self.__denominator:
                return True
        else:
            raise ValueError("Can't do <= operation")
        return False
    
    def __gt__(self, other):
        if isinstance(other,Fraction):
            if self.__numerator * other.__denominator > self.__denominator * other.__numerator:
                return True
        elif isinstance(other,int):
            if self.__numerator > other * self.__denominator:
                return True
        else:
            raise ValueError("Can't do > operation")
        return False
    
    def __ge__(self, other):
        if isinstance(other,Fraction):
            if self.__numerator * other.__denominator >= self.__denominator * other.__numerator:
                return True
        elif isinstance(other,int):
            if self.__numerator >= other * self.__denominator:
                return True
        else:
            raise ValueError("Can't do >= operation")
        return False
    
    def __hash__(self):
        return hash((self.__numerator, self.__denominator))
    
    def __float__(self) -> float:
        return self.__numerator / self.__denominator
    
    def __int__(self) -> int:
        return self.__numerator // self.__numerator
    
    def __neg__(self) -> int:
        return -1*(Fraction(self.__numerator,self.__denominator))
    
    def mixed(self):
        if self.__numerator >= self.__denominator:
            num = self.__numerator // self.__denominator
        else:
            raise ValueError
        return f"{num} {self.__numerator - num * self.__denominator}/{self.__denominator}"
    
    def __iadd__(self, other):
        if isinstance(other,Fraction):
            self.__numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
            self.__denominator = self.__denominator * other.__denominator
        elif isinstance(other,int):
            self.__numerator = self.__numerator + other * self.__denominator
            self.__denominator = self.__denominator
        else:
            raise ValueError("Can't implement + operation")
        return self.lowestterm(self.__numerator,self.__denominator)
    
    def __isub__(self,other):
        if isinstance(other,Fraction):
            self.__numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
            self.__denominator = self.__denominator * other.__denominator
        elif isinstance(other,int):
            self.__numerator = self.__numerator - other * self.__denominator
            self.__denominator = self.__denominator
        else:
            raise ValueError("Can't implement - operation")
        return self.lowestterm(self.__numerator,self.__denominator)


