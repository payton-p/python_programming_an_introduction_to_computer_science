def main():
    # In Python, strings are not mutable.

    example = "carpe diem "
    print(example[2])  # indexing example
    print(example[-1])  # you can also use negative indices

    print(example[1:4])  # this is how you slice
    print(example[:4])
    print(example[4:])
    print(example[:])

    print(example + ". Yay!")  # the plus sign is used for concatenation
    print(example * 3)  # the asterisk is used for repetition

    print(len(example))  # returns the length of the string

    for character in example:  # iterates over the characters in a string
        print(character)


main()
