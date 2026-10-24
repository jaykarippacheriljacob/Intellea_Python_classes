#####
# Classes, Objects and the __init__ Constructor

# 1. Class - A blueprint that defines what data (attributes) and actions (methods) its objects will have.
class Student:
    pass

# 2. pass - A placeholder that does nothing; used when a block must exist but has no code yet.

# 3. Object (instance) - A real item created from a class, with its own data.
student1 = Student()

# 4. Attribute - A variable stored inside an object, accessed with dot notation.
student1.name = "ravi"
print(student1.name)            # ravi

# 5. __init__() - The constructor; runs automatically when an object is created, to set its starting data.
# 6. self - Refers to the current object; must be the first parameter of every method.
class Student:
    def __init__(self, name, age, course):
        self.name = name        # Stores the value inside this object
        self.age = age
        self.course = course

# 7. Method - A function defined inside a class that works with the object's data.
    def display(self):
        print(f"{self.name}, {self.age}, {self.course}")

# 8. Creating objects with arguments - Values are passed to __init__ (self is passed automatically).
student1 = Student("ravi", 20, "python")
student2 = Student("meena", 21, "data analysis")

# 9. Calling a method - Use object.method(); Python passes the object as self.
student2.display()              # meena, 21, data analysis

# 10. Updating an attribute - Assign a new value through the object.
student1.age = 21

# 11. Class attribute - Defined directly in the class; shared by all objects.
class Student:
    institute = "Intellea"      # Same for every student
    def __init__(self, name):
        self.name = name        # Different for each student

print(Student("ravi").institute)    # Intellea

# 12. __str__() - Defines what print(object) shows; must return a string.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"

print(Student("ravi", 20))      # Student: ravi, Age: 20

#####
# Instance Methods, Class vs Instance Attributes

# 1. Instance method - A method that works on one object's data, accessed through self.
class Student:
    def display_details(self):
        print("Student name:", self.name)

# 2. Instance attribute - Set with self.attr; each object has its own separate value.
# 3. Class attribute - Set directly in the class body; one value shared by all objects.
class Employee:
    company = "ABC Company"     # Class attribute (shared)
    def __init__(self, name):
        self.name = name        # Instance attribute (per object)

emp1 = Employee("ravi")
emp2 = Employee("meena")

# 4. Accessing a class attribute - Works through the class or any object.
print(Employee.company)         # ABC Company
print(emp1.company)             # ABC Company

# 5. Changing a class attribute through the class - Affects every object.
Employee.company = "XYZ Ltd"
print(emp2.company)             # XYZ Ltd

# 6. Assigning through an object - Creates a new instance attribute for that object only, hiding the shared one.
emp1.company = "Freelance"
print(emp1.company)             # Freelance
print(emp2.company)             # XYZ Ltd (unchanged)

# 7. Methods that change state - A method can update the object's attributes, which persist after the call.
class BankAccount:
    bank_name = "ABC BANK"
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount          # Balance stays updated for this object

# 8. Conditions inside methods - Methods can validate input before changing data.
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

# 9. Objects are independent - Each account keeps its own balance.
acc1 = BankAccount("Hema", 10000)
acc2 = BankAccount("Ravi", 5000)
acc1.deposit(2000)
print(acc1.balance)             # 12000
print(acc2.balance)             # 5000 (unchanged)

#####
# Inheritance, Method Overriding and super()

# 1. Inheritance - A child class gets all the attributes and methods of a parent class, so shared code is written once.
# 2. Parent class (base class) - The class whose features are passed down.
class Bankaccount:
    def __init__(self, name, acc_num):
        self.name = name
        self.acc_num = acc_num

    def display(self):
        print("Account holder name: ", self.name)
        print("Account number: ", self.acc_num)

# 3. Child class (derived class) - Written as class Child(Parent); inherits everything from the parent.
class Savingsaccount(Bankaccount):
    pass                        # No code of its own; uses the parent's __init__ and display()

# 4. Using inherited methods - The child object can call the parent's methods directly.
account1 = Savingsaccount("meena", 1287513)
account1.display()
# Account holder name:  meena
# Account number:  1287513

# 5. Method overriding - The child defines a method with the same name as the parent's, replacing it for child objects.
class Savingsaccount(Bankaccount):
    def display(self):          # Replaces Bankaccount.display() for Savingsaccount objects
        print("Current Account")
        print("Account holder name: ", self.name)
        print("Account number: ", self.acc_num)

# 6. super() - Calls the parent class's version of a method, so the child can reuse it and add extra details.
class Currentaccount(Bankaccount):
    # 7. super().__init__() - Lets the parent set up its attributes, then the child adds its own.
    def __init__(self, name, acc_num, interest_rate):
        super().__init__(name, acc_num)       # Parent sets name and acc_num
        self.interest_rate = interest_rate    # Extra attribute only the child has

    # 8. Extending a method with super() - Runs the parent's code, plus new lines before or after it.
    def display(self):
        print("Current Account")              # Added before the parent's output
        super().display()                     # Parent prints name and account number
        print("Interest rate: ", self.interest_rate)   # Added after

account1 = Currentaccount("meena", 1287513, 7)
account1.display()
# Current Account
# Account holder name:  meena
# Account number:  1287513
# Interest rate:  7

#####
# Encapsulation

# 1. Encapsulation - Bundling data and the methods that use it into one class, and restricting direct access to some of that data.
# 2. Without encapsulation - Any code can read or change the attribute directly, even to invalid values.
# class Bankaccount:
#     def __init__(self, balance):
#         self.balance = balance
# a1 = Bankaccount(1000000)
# a1.balance = -500             # Nothing stops this

# 3. Private attribute (__name) - Two leading underscores hide the attribute from outside the class.
class Bankaccount:
    def __init__(self, balance):
        self.__balance = balance                # Private: only methods of this class can use it

    # 4. Controlled access - Public methods are the only way to read or change private data.
    def check_balance(self):
        print("Current balance: ", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited: ", amount)

a1 = Bankaccount(1000000)
# print(a1.__balance)           # AttributeError: 'Bankaccount' object has no attribute '__balance'
a1.check_balance()              # Current balance:  1000000
a1.deposit(2345)                # Amount deposited:  2345
a1.check_balance()              # Current balance:  1002345

# 5. Protected attribute (_name) - One underscore is a convention meaning "internal use", but Python doesn't block access.


#####
# Polymorphism and the __str__ Method

# 1. Polymorphism - "Many forms": the same method name behaves differently depending on the object's class.
class Developer:
    def work(self):
        print("Developer is writing code.")

class Trainer:
    def work(self):
        print("Trainer is teaching students.")

developer = Developer()
trainer = Trainer()
developer.work()                # Developer is writing code.
trainer.work()                  # Trainer is teaching students.

# 2. Polymorphism in a loop - One call works on different object types, each responding its own way.
for person in [Developer(), Trainer()]:
    person.work()

# 3. __str__ and polymorphism - print() calls each class's own __str__, so the same call gives different output.
class Student:
    def __str__(self):
        return "this is a student"

class Employee:
    def __str__(self):
        return "this is an employee"

print(Student())                # this is a student
print(Employee())               # this is an employee
