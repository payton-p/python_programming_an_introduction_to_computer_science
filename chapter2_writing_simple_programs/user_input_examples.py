def main():
    # The input function gets input from the user.
    textual_input = input("Give me your textual input: ")
    print("You entered: " + textual_input + "\n")

    # The eval function evaluates the input of a numeric expression, so it is
    # evaluated to a number.
    expression_input = eval(input("Give me an expression to evaluate: "))
    print("Evaluated to: " + str(expression_input))


main()
