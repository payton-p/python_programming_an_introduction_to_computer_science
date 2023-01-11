def main():
    # Boolean is named after George Boole, a 19th century English mathematician.
    is_a_fun_fact = True
    print("That was a fun fact:", is_a_fun_fact, "\n")

    x = 13

    # if statement example.
    if x % 2 == 0:
        print("x is even.\n")

    # if/else statement example.
    if x % 2 == 0:
        print("x is even.\n")
    else:
        print("x is odd.\n")

    # else-if statement example.
    if x > 13:
        print("x is greater than 13.\n")
    elif x == 13:
        print("x equals 13.\n")
    else:
        print("x is less than 13.\n")

    # Compound conditional example.
    if 13 >= x >= -1:
        print("This is a compound conditional.\n")

    # Exception handling example.
    try:
        k = 5 // 0  # raises divide by zero exception.
        print(k)
    except ZeroDivisionError:
        print("Can't divide by zero.")
    finally:
        # This block is always executed regardless of exception generation.
        print("This is always executed.")


# If the Python interpreter is running a module (the source file) as the main program, it sets the special __name__
# variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the
# module’s name. The module’s name is available as a value to the __name__ global variable. The bit of code below
# protects users from accidentally invoking a script when they didn't intend to. A Python program uses the condition
# if __name__ == "__main__":
# to only run the code inside the if statement when the program is run directly by the Python interpreter. The code
# inside the if statement is not executed when the file's code is imported as a module.
if __name__ == "__main__":
    main()
