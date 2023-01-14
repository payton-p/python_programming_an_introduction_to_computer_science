def main():
    # for loop example.
    print("for loop example:")
    for i in range(3):
        print(i)

    # while loop example.
    print("\nwhile loop example:")
    x = 0
    while x < 3:
        print(x)
        x += 1

    # Boolean operator examples. Note, the order of precedence from high to low is "not", "and", then "or."
    y = 2
    if not y == 1:
        print("\nExample using not.")
    if y == 2 or y == 4:  # Note that Python Boolean operators are short circuit operators.
        print("Example using or.")
    if y % 2 == 0 and y == 2:
        print("Example using and.")

    # Example using break.
    for letter in 'Python':
        if letter == 'h':
            break

        print('Current Letter :', letter)


if __name__ == "__main__":
    main()
