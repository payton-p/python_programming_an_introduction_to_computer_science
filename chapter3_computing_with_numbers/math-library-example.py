import math  # Makes the math library available.


# A program that computes the real roots of a quadratic equation.
# It illustrates the use of the math library. Note: this program crashes
# if the equation has no real roots.
def main():
    print("This program computes the real roots of a quadratic equation.")
    print()

    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))

    discriminant_square_root = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discriminant_square_root) / (2 * a)
    root2 = (-b - discriminant_square_root) / (2 * a)

    print("The solutions are: x1 = " + str(root1) + ", x2 = " + str(root2))


main()
