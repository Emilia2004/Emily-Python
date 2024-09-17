from account import account
import datetime
class Transaction():
    def __init__(self,from_account: account.Account,to_account: account.Account,amount: float,transaction_type: str,timestamp: datetime):
        self.__from_account = self.setFromAccount(from_account)
        self.__to_account = self.setToAccount(to_account)
        self.__amount = self.setAmount(amount)
        self.__transaction_type = self.setTransactionType(transaction_type)
        self.__timestamp = self.setTimestamp(timestamp)


    def setFromAccount(self,aaccount):
        if isinstance(aaccount,account.Account):
            self.__from_account = aaccount
        else:
            print("Not Valid account")
    

    def getFromAccount(self):
        return self.__from_account
    

    def setToAccount(self,aaccount):
        if isinstance(aaccount,account.Account):
            self.__to_account = aaccount
        else:
            print("Not Valid account")
        

    def getToAccount(self):
        return self.__to_account
    

    def setAmount(self,amount):
        if isinstance(amount,float):
            self.__amount = amount
        else:
            print("Invalid amount input")
    

    def getAmount(self):
        return self.__amount
    

    def setTransactionType(self,type):
        if isinstance(type,str):
            self.__transaction_type = type
        else:
            print("Invalid type")

        
    def getTransactionType(self):
        return self.__transaction_type
    

    def setTimestamp(self,time):
        if isinstance(time,datetime):
            self.__timestamp = time
        else:
            print("Invalid time")

        
    def getTimestamp(self):
        return self.__timestamp
    

    def log(self) -> None:
        print(f"Transaction is done from {self.__from_account} account")
        print(f"Transaction is done to {self.__to_account} account")
        print(f"Transaction amount is {self.__amount}AMD")
        print(f"Transaction type is {self.__transaction_type}")
        print(f"{self.__timestamp} time is spent")


    
