def function_without_return_statement():
    x = 2 + 3


def main():
    print(function_without_return_statement())  # prints None

    # Python passes parameters by value (not by reference). Passing mutable objects is a unique case. If you are passing
    # a mutable object, such as a list, to a function, and the function alters the object’s state, that state change
    # will be visible to the caller when the function returns.


if __name__ == "__main__":
    main()
