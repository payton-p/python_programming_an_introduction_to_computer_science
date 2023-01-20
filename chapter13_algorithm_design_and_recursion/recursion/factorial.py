def factorial(n):
    # Return the factorial of n.
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    print(factorial(3))


if __name__ == "__main__":
    main()
