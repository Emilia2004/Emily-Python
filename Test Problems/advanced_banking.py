from abc import abstractmethod
class Account:
    def __init__(self,number,balance,type):
        self.__number = number
        self.__balance = balance
        self.__type = type
        self.__transactions = []


    @abstractmethod
    def deposit(self,amount):
        ...
    
    @abstractmethod
    def withdraw(self,amount):
        ...   
    
    @abstractmethod
    def transfer(self,destination,amount):
        ...
    
    @abstractmethod
    def show_balance(self):
        ...


class IndividualAccount(Account):
    def __init__(self, number, balance, type):
        self.__number = number
        self.__balance = balance
        self.__type = type
        self.transactions = []

    def deposit(self,amount:float):
        if amount >= 0:
            self.transactions.append(Transaction(amount, "Deposit"))

        else:
            print("Deposit can't be lower than 0")
    
    
    def withdraw(self, amount: float):
        if amount > 0 and amount <= self.__balance:
            self.transactions.append(Transaction(amount, "Withdraw"))

        elif amount < 0:
            print("Withdrawal can't ne lower than 0")
        elif amount > self.__balance:
            print("Insufficient funds")

    
    
    def transfer(self, destination: Account, amount: float):
        if amount > 0 and amount <= self.__balance:
            self.transactions.append(Transaction(amount, "Transfer"))

        elif amount < 0:
            print("Transfer amount can't ne lower than 0")
        elif amount > self.__balance:
            print("Insufficient funds")
    
    
    def show_balance(self):
        return self.__balance
    


class Customer:
    def __init__(self, name, info):
        self.__name = name
        self.__info = info
        self.__account = []
   
    
    def view_transaction_history(self):
        for item in self.__account:
            for transaction in item.transactions:
                print(transaction)    
    def add_account(self,account):
        self.__account.append(account)



class Transaction:
    def __init__(self,amount,type,state = "debited"):
        self.__amount = amount
        self.__type = type
        self.__state = state

    def __str__(self):
        return f"{self.__type}, {self.__amount}"
   
        



