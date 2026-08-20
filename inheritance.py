# py inheritance allows to transmit the methode from a class o another class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def personname(self):
        print(self.firstname, self.lastname)
# create an object p1 that uses the class methode
p1 = Person("John", "Doe")
p1.personname()

## let's create a child class that will inherit the parent class methode
class Student(Person):
    pass # if we do not need to add another properties in this class we can just put the pass statement
s1 = Student("Mike", "Olson")
s1.personname()

# giving an __init__ function to the child class
# this will override the __init__ function inherited from the parent
# to keep both __ini__ function we need to declare the parent methode in after the properties of the child class
class Trainee(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
t1 = Trainee("Jane", "Newman")
t1.personname()

## the super() function
class Employee(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.enrollyear = 2020 # adding property
e1 = Employee("Jack", "Cooper")
e1.personname()
print(e1.enrollyear)

## adding properties as a new variable in the __init__ function
class Student(Person):
    def __init__(self, fname, lname, gyear):
        super().__init__(fname, lname)
        self.graduationyear = gyear
s2 = Student("Elisabeth", "Osborn", 2019)
s2.personname()
print(s2.graduationyear)

## add methode
class Student(Person):
    def __init__(self, fname, lname, gyear):
        super().__init__(fname, lname)
        self.graduationyear = gyear

    def welcome(self):
        print("welcome to " + self.firstname + " " + self.lastname + " class of " + str(self.graduationyear))

s1 = Student("Mike", "Olson", 2018)
s2 = Student("Elisabeth", "Osborn", 2019)
s3 = Student("Mohamed", "Khader", 2020)
s4 = Student("Hajaharivelo", "Ravoavy", 2022)

s1.welcome()
s2.welcome()
s3.welcome()
s4.welcome()