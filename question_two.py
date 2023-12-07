#i)
class Books:
    def __init__(self,tittle,author,pages):
        self.tittle =tittle
        self.author = author
        self.pages =pages
    def author_information (self):
        return f"{self.tittle},{self.author},{self.pages}"
BOOK1 = Books('PYTHON BASICS','JOAN.N','142 pages')
print(BOOK1.author_information())


#ii)
#
class Books:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

class EBook(Books):
    def __init__(self, title, author, pages, format_type):
        super().__init__(title, author, pages)
        self.format_type = format_type

    def ebook_information(self):
        return f"{self.title}, {self.author}, {self.pages}, {self.format_type}"

BOOK2 = EBook('COMPUTER SCIENCE', 'JOSEPHINE. A', 400, 'EXCEL')
print(BOOK2.ebook_information())


#iii)
class Books:
    def __init__(self,tittle,author,pages):
        self.tittle =tittle
        self.author = author
        self.pages =pages
    def book_title (self):
        return f"{self.tittle}"
BOOK1 = Books('PYTHON BASICS','JOAN.N','142 pages')
print(BOOK1.book_title())    
    
#class is a constructor of a certain object
#object  is a function of the objects