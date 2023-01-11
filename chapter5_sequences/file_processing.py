def read_file():
    file = open("file_processing_example.txt", "r")  # open the file
    text = file.read()  # read in the file contents
    print(text)


def read_and_write_file():
    """This program creates a file of usernames from a file of names."""

    # Open the files.
    input_file = open("file_processing_names.txt", "r")
    output_file = open("file_processing_usernames.txt", "w")

    # Process each line of the input file and write to the output file.
    for line in input_file:
        first, last = line.split()
        username = (first[0] + last[:7]).lower()  # create the username

        print(username, file=output_file)  # write to the output file

    # Close both files.
    input_file.close()
    output_file.close()

    print("\nUsernames have been written to:", output_file)


def main():
    read_file()
    read_and_write_file()


if __name__ == "__main__":
    main()
