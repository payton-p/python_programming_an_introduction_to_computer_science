# The word polymorphism means having many forms. In programming, polymorphism means the same function name (but
# different signatures) being used for different types. The key difference is the data types and number of arguments
# used in function.

# Polymorphism with Inheritance:
# In Python, Polymorphism lets us define methods in the child class that have the same name as the methods in the
# parent class. In inheritance, the child class inherits the methods from the parent class. However, it is possible to
# modify a method in a child class that it has inherited from the parent class. This is particularly useful in cases
# where the method inherited from the parent class doesn’t quite fit the child class. In such cases, we re-implement
# the method in the child class. This process of re-implementing a method in the child class is known as
# Method Overriding.
class Bird:
    @staticmethod
    def intro():
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly, but some cannot.")


class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


# Polymorphism with a function and objects:
# It is also possible to create a function that can take any object, allowing for polymorphism.
def example(obj):
    obj.flight()


def main():
    # len() used for a string.
    print(len("geeks"))

    # len() used for a list.
    print(len([10, 20, 30]))
    print()

    # Polymorphism and inheritance.
    obj_bird = Bird()
    obj_sparrow = Sparrow()
    obj_ostrich = Ostrich()

    obj_bird.intro()
    obj_bird.flight()

    obj_sparrow.intro()
    obj_sparrow.flight()

    obj_ostrich.intro()
    obj_ostrich.flight()
    print()

    # Polymorphism with a function and objects.
    example(obj_bird)
    example(obj_sparrow)
    example(obj_ostrich)


if __name__ == "__main__":
    main()
