'''
Topics:
Lists
Dictionaries
Functions

Encapsulation
    - Is a mechanism of wrapping the attributesand code acting on the methods together as a single unit
    - In encapsulation, the attributes of a class will be hidden from other classes and can be access only through the methods of their current class. Therefore, it is also known as 'data hiding'.

    Benefits:
    1. simplifies complexity
    2. protect data

    Note: in python convention
    1. Single Underscore Prefix('_') - to indicate that an attribute or method should be treated as 'private' or 'internal'

Access Modifiers 
    - are used to restrict access to the attributes and methods of class

    Three commonly used access modifiers:
    1. public (+)
        - Accessible from anywhere, both within the class and from outside the class
    2. protected (#)
        - inteded to be used within the class and its subclassess. They can be accessed from outside the class, but it is considered a convention to treat them as a non-public and accessed only by convention
    3. Private (_)
        - meant to be accessed only within the class. They are not accessible from outside the class.
'''
# Encapsulation Example


class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposit successful. New Balance: {self._balance}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal is successful. New Balance: {self._balance}")
        else:
            print("Insufficient fund. Cannot withdraw.")

    def get_balance(self):
        return self._balance


# Create an instance of bank account object
my_account = BankAccount("123456", 2500)
print(my_account._account_number)

# Deposit
my_account.deposit(500)

# Withdrawl
my_account.withdraw(200)

# get balance
print(my_account.get_balance())
