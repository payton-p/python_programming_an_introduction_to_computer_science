def main():
    # Integer example
    integer = 3
    print(type(integer))

    # Float example
    float_num = 4.0
    print(type(float_num))

    # Normal division always returns a float
    normal_division_example = 3 / 2
    print(normal_division_example)

    # Integer division with two ints
    integer_division_example = 11 // 5
    print(integer_division_example)

    # Integer division with two floats
    integer_division_example = 11.0 // 5.0
    print(integer_division_example)

    # Integer division with one int and one float, the result is cast to float
    integer_division_example = 11 // 5.0
    print(integer_division_example)


if __name__ == "__main__":
    main()
