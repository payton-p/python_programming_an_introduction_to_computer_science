def main():
    # In Python, lists are mutable.

    print([1, 2] + [3, 4])  # plus sign concatenates lists
    print([1, 2] * 3)  # the asterisk is used for repetition

    example = [1, 3, 5, 7, 9]
    print(example[3:])  # slicing

    print(len(example))  # get the length

    mixed_list = [1, "Hello", 4, "Hey", (3, 4)]  # you can have multiple types of items in the same list
    print(mixed_list)

    # Show that lists are mutable.
    print(example)
    example[0] = 13
    print(example)


if __name__ == "__main__":
    main()
