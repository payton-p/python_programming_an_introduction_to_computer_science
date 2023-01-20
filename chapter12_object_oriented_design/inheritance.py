# Inheritance allows us to define a class that inherits all the methods and properties from another class. A parent
# class is the class being inherited from, also called a base class. A child class is the class that inherits from
# another class, also called a derived class.

class Person:
    # The __init__() function is called automatically every time the class is being used to create a new object.
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Create a class named Student, which will inherit the properties and methods from the Person class.
class Student(Person):
    pass  # use the pass keyword when you do not want to add any other properties or methods to the class


class Teacher(Person):
    # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    # The child's __init__() function overrides the inheritance of the parent's __init__() function.
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname + " Jr."


class Senior(Person):
    # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function.
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


class Child(Person):
    # Python also has a super() function that will make the child class inherit all the methods and properties from its
    # parent.
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


def main():
    student = Student("Joe", "Allen")
    student.printname()

    teacher = Teacher("Tina", "Bell")
    teacher.printname()

    senior = Senior("Joan", "Jones")
    senior.printname()

    child = Child("Tommy", "Tiller")
    child.printname()


if __name__ == "__main__":
    main()
