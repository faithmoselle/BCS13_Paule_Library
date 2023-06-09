class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

# getter method
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publication_year(self):
        return self.publication_year

    def is_book_available(self):
        return self.is_available

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(
                f"You've successfully borrowed the book:{self.title} of {self.publication_year} by {self.author}.")
        else:
            print(
                f"We are sorry, the {self.title} by {self.author} of {self.publication_year} is not available.")

    def return_book(self):  # Method for returning
        if not self.is_available:
            self.is_available = False
            print(
                f"{self.title} by {self.author} of {self.publication_year} has been returned.")
        else:
            print(
                f"{self.title} by {self.author} of {self.publication_year} is already available.")


library = []


def display_available_books():
    if not library:
        print("No Books Available")
    else:
        print("\nAvailable Books:")
        for number, book in enumerate(library):
            if book.is_book_available():
                print(
                    f"{number}: {book.get_title()} by {book.get_author()} ({book.get_publication_year()})")


def main():
    while True:
        print("\n1. Add a book to the library")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Display available books")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
# choice 1
        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            publication_year = input(
                "Enter the publication year of the book: ")

            book = Book(title, author, publication_year)
            library.append(book)
            print("Book added to the library.")

        elif choice == "2":

            # choice 2
            display_available_books()
            if library:
                try:
                    booknum = int(
                        input("Enter the book number of the book to borrow: "))
                    if booknum < 0 or booknum >= len(library):
                        print("Invalid book book number.")
                        continue
                    book = library[booknum]
                    book.borrow_book()
                except ValueError:
                    print("Invalid input. Please enter a valid book number.")
            else:
                print("No books available to borrow.")

        elif choice == "3":
            # choice 3
            display_available_books()

            if library:
                try:
                    booknum = int(
                        input("Enter the book number of the book to return: "))
                    if booknum < 0 or booknum >= len(library):
                        print("Invalid book booknum.")
                        continue
                    book = library[booknum]
                    book.return_book()
                except ValueError:
                    print("Invalid input. Please enter a valid book number.")
            else:
                print("No books available to return.")
# choice 4
        elif choice == "4":
            display_available_books()
# choice 5 EXIT
        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
