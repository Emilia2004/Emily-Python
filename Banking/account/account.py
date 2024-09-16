from abc import ABC,abstractmethod
class Account(ABC):
    
    def __init__(self,account_number:int, balance:float, account_type:str ):
        self.__account_number = account_number
        self.__account_type = account_type
        self.__balance = balance
    
    
    def setBalance(self,balance):
        if balance >= 0 and isinstance(balance,float):
            self.__balance=balance
        else:
            print("Invalid balance")
    
    
    def getBalance(self):
        return self.__balance
    

    
    
    def setAccountNumber(self,number):
        if number > 0 and isinstance(number,int):
            self.__account_number = number
        else:
            print("Account number must be higher than 0")
    
    
    def getAccountNumber(self):
        return self.__account_number
    
    
    def setAccountType(self,type):
        if isinstance(type,str):
            self.__account_type = type
        else:
            print("Invalid account type")
    
    
    def getAccountType(self):
        return self.__account_type
    


    @abstractmethod
    def deposit(self,amount: float) -> None:
        ...
    
    @abstractmethod
    def withdraw(self,amount: float) ->None:
        ...   
    
    @abstractmethod
    def transfer(self,destination:"Account",amount: float) -> None:
        ...
    
    @abstractmethod
    def show_balance(self) -> None:
        ...
    
    @abstractmethod
    def get_account_type(self) -> str:
        ...


class CheckingAccount(Account):
    
    
    def __init__(self, account_number: int, balance: float, account_type:str, overdraft_limit: float): 
        super().__init__(account_number, balance, account_type)
        self.__overdraft_limit = overdraft_limit
    
    
    def setOverdraftLimit(self,limit):
        if limit >= 0:
            self.__overdraft_limit = limit
        else:
            print("Limit must be positive number")

    def getOverdraftLmit(self):
        return self.__overdraft_limit
        
    
    def deposit(self,amount:float):
        if amount >= 0:
            print(f"Deposit of {amount}AMD is available. You will have {amount+self.__balance}AMD on your account")
        else:
            print("Deposit can't be lower than 0")
    
    
    def withdraw(self, amount: float):
        if amount > 0 and amount <= self.__balance:
            print(f"Withdrawal of {amount}AMD is available. You will have {self.__balance-amount}AMD on your account")
        elif amount < 0:
            print("Withdrawal can't ne lower than 0")
        elif amount > self.__balance:
            print("Insufficient funds")

    
    
    def transfer(self, destination: Account, amount: float):
        if amount > 0 and amount <= self.__balance:
            print(f"Transer of {amount}AMD to {destination} is available. You will have {self.__balance-amount}AMD on your account")
        elif amount < 0:
            print("Transfer amount can't ne lower than 0")
        elif amount > self.__balance:
            print("Insufficient funds")
    
    
    def show_balance(self):
        return self.__balance
    
    
    def get_account_type(self):
        return self.__account_type


class SavingsAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type:str, interest_rate: float): 
        super().__init__(account_number, balance, account_type)
        self.__interest__rate = interest_rate
    

    def setInterestRate(self,rate):
        if rate > 0:
            self.__interest__rate


    def getInterestRate(self):
        return self.__interest__rate
    

    def deposit(self,amount:float):
        if amount >= 0:
            print(f"Deposit of {amount}AMD is added successfully.You will have {self.__balance+amount*self.__interest__rate/100}AMD additionaly on your account")
            self.__balance += amount*self.__interest__rate/100        
        else:
            print("Deposit can't be lower than 0")
    
    
    def withdraw(self, amount: float):
        if amount > 0 and amount <= self.__balance:
            print(f"Withdrawal of {amount}AMD is available. You will have {self.__balance-amount*self.__interest__rate/100}AMD on your account")
            self.__balance -= amount*self.__interest__rate/100
        elif amount < 0:
            print("Withdrawal can't ne lower than 0")
        elif amount > self.__balance:
            print("Insufficient funds")
    
    
    def transfer(self, destination: Account, amount: float):
        if amount > 0 and amount <= self.__balance:
            print(f"Transer of {amount}AMD to {destination} is done successfully. You have {self.__balance-amount*self.__interest__rate/100}AMD on your account")
            self.__balance -= amount*self.__interest__rate/100
        elif amount < 0:
            print(f"Transfer amount can't ne lower than 0")
        elif amount > self.__balance:
            print("Insufficient funds")
    
    def show_balance(self):
        return self.__balance
    
    
    def get_account_type(self):
        return self.__account_type
    

class JointAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type:str,interest_rate:float, joint_owners: list[str]): 
        super().__init__(account_number, balance, account_type,interest_rate)
        self.__joint_owners = joint_owners

    
    def setJointOwners(self,owners):
        if len(owners) >= 1:
            self.__joint_owners = owners
    

    def getJointOwners(self):
        return self.__joint_owners
    


    def add_owner(self, customer_name: str) -> None:
        self.__joint_owners.append(customer_name)


    def deposit(self,amount : float):
        if amount >= 0:
            print(f"Deposit of {amount}AMD is added successfully.You will have {self.__balance+amount*self.__interest__rate/100}AMD additionaly on your account")
            self.__balance += amount*self.__interest__rate/100        
        else:
            print("Deposit can't be lower than 0")
    
    
    def withdraw(self, amount: float):
        if amount > 0 and amount <= self.__balance:
            print(f"Withdrawal of {amount}AMD is available. You will have {self.__balance-amount*self.__interest__rate/100}AMD on your account")
            self.__balance -= amount*self.__interest__rate/100
        elif amount < 0:
            print("Withdrawal can't ne lower than 0")
        elif amount > self.__balance:
            print("Insufficient funds")
    
    
    def transfer(self, destination: Account, amount: float):
        if amount > 0 and amount <= self.__balance:
            print(f"Transer of {amount}AMD to {destination} is done successfully. You have {self.__balance-amount*self.__interest__rate/100}AMD on your account")
            self.__balance -= amount*self.__interest__rate/100
        elif amount < 0:
            print(f"Transfer amount can't ne lower than 0")
        elif amount > self.__balance:
            print("Insufficient funds")

        
    def show_balance(self):
        return self.__balance
    
    
    def get_account_type(self):
        return self.__account_type
    










