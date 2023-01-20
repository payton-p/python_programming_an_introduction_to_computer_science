# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of
# wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and
# methods directly and can prevent the accidental modification of data. (https://www.geeksforgeeks.org/)

# Create a base class.
class Base:
    def __init__(self):
        # Protected members are accessible within the class and also available to its subclasses. To define a
        # protected member, prefix the member name with a single underscore _. Protected data members are used when you
        # implement inheritance and want to allow data members access only to child classes.
        self._a = 2  # protected member

        # We can strengthen variables in the class by marking them private. To define a private variable add two
        # underscores as a prefix at the start of a variable name. Private members are accessible only within the
        # class, so we can’t access them directly from the class objects.
        self.__b = "Hello"  # private member

        # The public member is accessible from inside or outside the class.
        self.c = 3  # public member


# Create a derived class.
class Derived(Base):
    def __init__(self):
        Base.__init__(self)  # call constructor of Base class
        print("Calling the protected member of the base class:", self._a)

        self._a = 3  # modify the protected variable
        print("Calling the modified protected member outside the base class:", self._a)

        # Uncommenting the next line will raise an AttributeError because the attribute is private.
        # print("Calling private member of base class: ", self.__b)


def main():
    obj1 = Derived()
    obj2 = Base()

    # Call the protected member. It can be accessed, but should not be done due to convention.
    print("Accessing protected member of obj1:", obj1._a)
    print("Accessing protected member of obj2:", obj2._a)


if __name__ == "__main__":
    main()
