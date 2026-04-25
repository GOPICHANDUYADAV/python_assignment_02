#library book management
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def display_info(self):
        status = "Available" if self.is_available else "Not Available"
        print("Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.isbn)
        print("Status:", status)

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f'"{self.title}" has been checked out.')
        else:
            print(f'"{self.title}" is already checked out.')

    def return_book(self):
        self.is_available = True
        print(f'"{self.title}" has been returned.')



book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")

book1.display_info()
book1.check_out()
book1.check_out()
book1.return_book()
book1.display_info() 



