class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True

class Library(Book):
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
    def borrow_book(self,title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print("Collect")
                else:
                    print("Book not available")
            return 
        print("Book not found")
    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = True
                    print("Book collected back")
                else:
                    print("Book never collected")
            return 
        print("Book not found")
    def display_books(self):
        if not self.books:
            print ("No books in library")
            return
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print (f"{book.title} by author {book.author} - {status}")


b1 = Book("Hari","Ronaldo")
b2 = Book("messi","Someone")

ls = Library()
ls.add_book(b1)
ls.add_book(b2)

ls.display_books()