# Access and Modifier example
class Car:
    def __init__(self, make, model, year):
        self._make = make  # protected attribute
        self._model = model  # protected attribute
        self.__year = year  # private attribute

    def start_engine(self):
        self.__ignite_spark_plug()
        print("Engine start...")

    def __ignite_spark_plug(self):
        print("Spark plug ignited!")

    # getter method

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self.__year


my_car = Car("Toyota", "Camry", 2022)
print(my_car.get_make())
print(my_car.get_model())
print(my_car.get_year())

my_car.start_engine()
# print(my_car.__year)

'''
230609 - Main Activity

Activity 1: Building a Library Catalog System

Objective: Implement a library catalog system using encapsulation principles.

Instructions:

Define a class called Book with the following attributes and methods:

Attributes:

title : The title of the book.
author: The author of the book.
publication_year: The year the book was published.
is_available: Indicates whether the book is available for borrowing.

Methods:

__init__(self, title, author, publication_year): Initializes the book object with the given title, author, and publication year. Set is_available to True by default.
get_title(self): Returns the title of the book.
get_author(self): Returns the author of the book.
get_publication_year(self): Returns the publication year of the book.
is_book_available(self): Returns the availability status of the book.
borrow_book(self): Marks the book as borrowed (sets is_available to False).
return_book(self): Marks the book as returned (sets is_available to True).
Create a list called library to store the book objects.

Implement the following functionality in the main program:

- Prompt the user to enter book details (title, author, publication year).
- Create a Book object with the provided details and add it to the library list.
- Repeat the above step to add multiple books to the library.
- Display the available books in the library.
- Prompt the user to choose a book to borrow by entering its index.
-- If the chosen book is available, mark it as borrowed and display a success message. Otherwise, display an error message.
  --- Display the available books in the library again.
  --- Prompt the user to choose a book to return by entering its index.
  --- If the chosen book is not available, mark it as returned and display a success message. Otherwise, display an error message.
  --- Display the available books in the library one final time.

 Note: You can use the input() function to get user input and the print() function to display messages and book information.

 Add your activity GitHub link
 Screen your code-based and output and paste in our lecture SB account

Grading:
			First 1-10 submission without errors --> 100 points
			Second 11-20 submission without errors --> 90 points
			Third 21-30 submission without errors --> 85
			the rest without errors --> 80
			Late submission or submission with error --> 60
'''
