class Example:
    # The self parameter in the definition is a bookkeeping detail. We would still say this method has one parameter.
    def __init__(self, sides):  # this is the constructor
        self.sides = sides
        self.value = 1  # Sets a default value

    # This method returns the string representation of the object. This method is called when print() or str() function
    # is invoked on an object. This method must return a String object.
    def __str__(self):
        return "Return the string representation of the object."
