def main():
    # Definite loop example. This particular loop pattern is called a counted loop.
    # The variable after the keyword "for" is called the loop index. The
    # function range is used for generating a sequence of numbers on the fly.
    for i in range(10):
        print(i)
    print("End of the first loop example.\n")

    # Another loop example
    for i in [0, 1, 3, 5]:
        print(i)
    print("End of the second loop example.\n")

    # Compare what these prints return
    print(range(3))
    print(list(range(3)))  # turns it into an explicit list


if __name__ == "__main__":
    main()
