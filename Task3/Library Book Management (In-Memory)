# -------------------------------
# Library Book Management System
# -------------------------------

# A class to represent a Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    # How the book should be displayed when printed
    def __str__(self):
        return f"'{self.title}' by {self.author}"

# A class to represent the Library
class Library:
    def __init__(self):
        self.books = []  # Store all books in a list
    
    def add_book(self, title, author):
        """Add a new book to the library"""
        self.books.append(Book(title, author))
        print("Book added successfully!")
    
    def search_book(self, title):
        """Search for a book by title (case-insensitive)"""
        for book in self.books:
            if book.title.lower() == title.lower():
                print("Found:", book)
                return
        print("Book not found.")
    
    def show_books(self):
        """Display all books in the library"""
        if not self.books:
            print("No books in library.")
        else:
            print("\nBooks in Library:")
            for book in self.books:
                print(book)

# CLI menu for interacting with Library
def run_library():
    lib = Library()
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Show All Books")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            lib.add_book(title, author)
        elif choice == "2":
            title = input("Enter book title to search: ")
            lib.search_book(title)
        elif choice == "3":
            lib.show_books()
        elif choice == "4":
            print("Exiting Library System")
            break
        else:
            print("Invalid choice! Try again.")

# Run the Library System
run_library()
