class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = False

class Library():
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print(f"Book added to the library")
        
    def issue_book(self,title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"Book has been issued {title}")
                else:
                    print(f"Book {title} already issues")
            else:
                print("book not found")

    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print(f"Book {title} has been returned")
                else:
                    print(f"Book {title} was not issued")
            else:
                print("Book not found")

b1 = Book("ROnaldo","Hari")
b2 = Book("Messi","Someone")

l = Library()
l.add_book("HOD")