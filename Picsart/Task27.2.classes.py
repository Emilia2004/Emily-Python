class Book:
    def __init__(self,title,author,price):
        self.__title = title
        self.__author = author
        self.__price = price
    def set_title(self,title):
        self.__title = title
    def get_title(self):
        return self.__title
    def set_author(self,author):
        self.__author = author
    def get_author(self):
        return self.__author
    def set_price(self,price):
        if price > 10:
            self.__price = price
        else:
            print("Price must be above 10!")
    def get_price(self):
        return self.__price


book = Book("Martin Eden","Jack London",15)
book.set_author("Anything")
print(book.get_author())
print(book.get_price())
book.set_price(5)

