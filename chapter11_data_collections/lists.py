def main():
    # Python lists can mix data types.
    number_list = ["Hey", 1, 2, 3, 3.0]
    print(number_list)

    # Example of a membership check.
    print(3 in number_list)

    # Python lists are dynamic (aka mutable).
    number_list[0] = "Hello"
    print(number_list)

    number_list.append(13)
    print(number_list)

    del number_list[2]
    print(number_list)


if __name__ == "__main__":
    main()
