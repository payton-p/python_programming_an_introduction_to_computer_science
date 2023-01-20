def reverse(string):
    # Return the reverse of a string.
    if string == "":
        return string
    else:
        return reverse(string[1:]) + string[0]


def main():
    print(reverse("Hello"))


if __name__ == "__main__":
    main()
