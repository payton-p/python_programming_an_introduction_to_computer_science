# Computes the factorial of a number. Illustrates a for loop with an accumulator.
def main():
    n = eval(input("Please enter a whole number: "))
    factorial = 1
    for factor in range(n, 1, -1):
        factorial = factorial * factor
    print(str(n) + "! = " + str(factorial))


main()
