class Author:
    def __init__(self, name):
        self.name = name 
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    def books(self):
        return [contract.book for contract in self.contracts()]
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    def total_royalties(self):
        total = 0
        for i in self.contracts():
            total += i.royalties
        return total
class Book:
    def __init__(self, title):
        self.title = title 
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    def authors(self):
        return [contract.author for contract in self.contracts()]
class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author 
        self.book = book 
        self.date = date 
        self.royalties = royalties
        Contract.all.append(self)
    @classmethod 
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    @property 
    def author(self):
        return self._author 
    @author.getter
    def author(self):
        return self._author 
    @author.setter 
    def author(self, val):
        if(isinstance(val, Author)):
            self._author = val 
        else:
            raise Exception
        
    @property 
    def book(self):
        return self._book 
    @book.getter
    def book(self):
        return self._book 
    @book.setter 
    def book(self, val):
        if(isinstance(val, Book)):
            self._book = val 
        else:
            raise Exception
        
    @property 
    def date(self):
        return self._date 
    @date.getter
    def date(self):
        return self._date 
    @date.setter 
    def date(self, val):
        if(isinstance(val, str)):
            self._date = val 
        else:
            raise Exception
        
    @property 
    def royalties(self):
        return self._royalties 
    @royalties.getter
    def royalties(self):
        return self._royalties 
    @royalties.setter 
    def royalties(self, val):
        if(isinstance(val, int)):
            self._royalties = val 
        else:
            raise Exception