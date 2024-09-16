from account import account
class Customer:
    def __init__(self,name: str,contact_info: str, accounts: list[account.Account]):
        self.__name = name
        self.__contact_info = contact_info
        self.__accounts = accounts
        self.__transaction_history = []


    def setName(self,name):
        if isinstance(name,str):
            self.__name = name
        else:
            print("Name must be string!")


    def getName(self):
        return self.__name
    

    def setContactInfo(self,info):
        if isinstance(info,str):
            self.__contact_info = info
        else:
            print("Invalid info")


    def getContactInfo(self):
        return self.__contact_info
    

    def setAccount(self,aaccount):
        if isinstance(aaccount,account.Account):
            self.__accounts = aaccount
        else:
            print("Invalid account")


    def getAccount(self):
        return self.__accounts
    

    def add_account(self, aaccount: account.Account) -> None:
        self.__accounts.append(aaccount)


    def view_accounts(self) -> None:
        for account in self.__accounts:
            print(account)

    def add_transaction(self,type,amount):
        history = {"type" : type,
                   "amount" : amount}
        self.__transaction_history.append(history) 
    def view_transaction_history(self) -> None:
        for i in self.__transaction_history:
            print(i)



