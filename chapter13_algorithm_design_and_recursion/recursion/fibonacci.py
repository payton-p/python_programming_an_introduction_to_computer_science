# This is an elegant solution, but a horribly inefficient function. It performs a lot of duplicate computations.
def get_fibonacci_number(n):
    if n < 3:
        return 1
    else:
        return get_fibonacci_number(n - 1) + get_fibonacci_number(n - 2)


def main():
    # Get the nth number in the Fibonacci sequence.
    print(get_fibonacci_number(4))


if __name__ == "__main__":
    main()
