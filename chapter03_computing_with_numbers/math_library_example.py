import math  # Makes the math library available.


# A program that computes the real roots of a quadratic equation.
# It illustrates the use of the math library. Note: this program crashes
# if the equation has no real roots.
def main():
    print("This program computes the real roots of a quadratic equation.")
    print()

    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))

    discriminant_square_root = math.sqrt(b * b - 4 * a * c)
    x1 = (-b + discriminant_square_root) / (2 * a)
    x2 = (-b - discriminant_square_root) / (2 * a)

    print("The solutions are: x1 = " + str(x1) + ", x2 = " + str(x2))
    print()

    # We can also pass a negative value for the ndigit argument in round().
    # This will start rounding from the left of the decimal point.
    print(round(123.456, 0))
    print(round(123.456, -1))
    print(round(123.456, -2))
    print(round(123.456, -3))
    print()

    # Examples of integer division and remainder operations with negative numbers.
    # The results are rounded down toward the more negative value.
    print(-10 // 3)  # = -4
    print(10 // -3)  # = -4
    print(-10 // -3)  # = 3
    print()

    # Python’s modulo operator (%) always return a number having the same sign as the denominator.
    # What happens behind the scene is that Python applies the distribute law of Modulo operator
    # which is: (a+b)mod n = [(a mod n)+(b mod n)]mod n
    print(-5 % 4)  # Example: -5 % 4 = (-2 * 4 + 3) % 4 = 3
    print(-10 % 3)  # = 2
    print(10 % -3)  # = -2


if __name__ == "__main__":
    main()
