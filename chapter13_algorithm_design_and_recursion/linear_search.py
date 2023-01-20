def main():
    example_list = [2, 3, 5, 7]
    print(3 in example_list)  # "in" uses linear search
    print(example_list.index(5))  # .index() uses linear search
    # print(example_list.index(0)) # throws an exception as zero is not in the list


if __name__ == "__main__":
    main()
