import ipdb 
class Author:
    all = []
    def __init__(self, name):
        self.name = name 
        Author.all.append(self)

    def contracts(self):
        # look through all contracts
        # save the ones with the matching Author

        # matching_contracts = []
        # for contract in Contract.all:
        #     if(contract.author == self):
        #         matching_contracts.append(contract)
        # return matching_contracts
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        #return books for associated contracts
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(author=self, book=book, date=date, royalties=royalties)
    
    '''
    sum = 0 
        [
            c2 300, sum = 0 + 300
            c1 200, sum = 300 + 200 
            c9 200, sum = 500 + 700
        ]
    '''
    def total_royalties(self):
        #look through all contracts
        #sum all the royalties 
        # sum = 0
        # for contract in self.contracts():
        #     sum += contract.royalties
        # return sum

        return sum([contract.royalties for contract in self.contracts()])
    
    def __repr__(self):
        return f'<Author name={self.name} />'
class Book:
    all=[]
    def __init__(self, title):
        self.title = title 
        Book.all.append(self)

    def contracts(self):
        #look through all contracts
        #filter out ones that match current book 
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        #look through all associated contracts
        #extract the author from contract
        return [contract.author for contract in self.contracts()]
    
    def __repr__(self):
        return f'<Book title={self.title} />'
class Contract:
    all=[]
    def __init__(self, author, book, date, royalties):
        self.author = author 
        self.book = book 
        self.date = date 
        self.royalties = royalties 
        Contract.all.append(self)

    @classmethod 
    def contracts_by_date(cls, date):
        #look through all contracts 
        #filter out based on date 
        #contract 
        return [ contract for contract in cls.all if contract.date == date]

    @property 
    def author(self):
        return self._author 
    @author.setter 
    def author(self, new_author):
        if(not isinstance(new_author, Author)):
            raise Exception('author must be class Author')
        else: 
            self._author = new_author

    @property 
    def book(self):
        return self._book 
    @book.setter 
    def book(self, new_book):
        if(not isinstance(new_book, Book)):
            raise Exception('book must be class Book')
        else: 
            self._book = new_book

    @property 
    def date(self):
        return self._date 
    @date.setter 
    def date(self, new_date):
        if(not isinstance(new_date, str)):
            raise Exception('date must be class str')
        else: 
            self._date = new_date

    @property 
    def royalties(self):
        return self._royalties 
    @royalties.setter 
    def royalties(self, new_royalties):
        if(not isinstance(new_royalties, int)):
            raise Exception('royalties must be class int')
        else: 
            self._royalties = new_royalties
    
    def __repr__(self):
        return f'<Contract date={self.date} royalties={self.royalties} author={self.author} book={self.book} />'

b1 = Book(title="h1")
b2 = Book(title="h2")
a1 = Author(name="rowling")

b3 = Book(title="fellowship")
a2 = Author(name="tolkein")

c1 = Contract(royalties=33, book=b1, author=a1, date="June 1995")
c2 = Contract(royalties=88, book=b2, author=a1, date="Aug 1996")
# ipdb.set_trace()
