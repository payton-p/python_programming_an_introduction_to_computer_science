def main():
    # Dictionaries are mutable.
    dictionary = {"key": "value", "example": "another one", "and": 2, "the": "best", "wow": "ohhh"}

    print(dictionary)
    print(dictionary["example"])

    del dictionary["and"]
    print(dictionary)


if __name__ == "__main__":
    main()
