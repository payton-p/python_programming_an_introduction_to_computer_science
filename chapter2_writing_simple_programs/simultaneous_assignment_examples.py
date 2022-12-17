def main():
    # Example of simultaneous assignment.
    print("This is an example of simultaneous assignment.")
    x, y = 1, 2
    print(x)
    print(y)

    # You can also use expressions. 
    x_plus_y, x_minus_y = x + y, x - y
    print("\nSimultaneous assignment can also use expressions.")
    print(x_plus_y)
    print(x_minus_y)

    # This allows you to swap variables.
    x, y = y, x
    print("\nThe values of x and y have been swapped using simultaneous assignment.")
    print(x)
    print(y)

    # Simultaneous assignment using user input.
    score1, score2 = eval(input("Enter to scores separated by a comma: "))
    average = (score1 + score2) / 2
    print("Average: " + str(average))


main()
