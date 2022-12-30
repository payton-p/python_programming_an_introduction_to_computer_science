def main():
    # Single leading underscores: _foo
    print(
        "A single leading underscore in front of a variable, a function, or a method name means that these objects " +
        "are used internally. This is more of a syntax hint to the programmer and is not enforced by the Python " +
        "interpreter which means that these objects can still be accessed in one way on another from another script.\n")

    # Single trailing underscores: foo_
    print("There are some situations where you want to use a variable name that is actually a reserved keyword in " +
          "Python such as class , def , type , object , etc. To avoid this conflict, you can add a trailing " +
          "underscore as a naming convention.\n")

    #  Double leading and trailing underscores: __foo__
    print(
        "Double leading and trailing underscores are used to define special universal class methods called dunder " +
        "methods (short for Double Underscore methods). Dunder methods are reserved methods that you can still " +
        "overwrite. They have special behavior and are called differently.\n")

    # Double leading underscores: __bar
    print(
        "Double leading underscores are typically used for name mangling. Name mangling is a process by which the " +
        "interpreter changes the attribute name to avoid naming collisions in subclasses.\n")


main()
