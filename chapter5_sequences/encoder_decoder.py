def decode():
    print("This program converts a sequence of Unicode numbers into the string of text that it represents.\n")

    encoded_message = input("Please enter the Unicode-encoded message: ")

    # Convert a sequence of Unicode numbers into a string of text.
    message = ""
    for num_string in encoded_message.split():
        code_num = eval(num_string)
        message = message + chr(code_num)

    print("\nThe decoded message is:", message)


def encode():
    print(
        "This program converts a textual message into a sequence of numbers representing the Unicode encoding of the "
        + "message.\n")

    message = input("Please enter the message to encode: ")

    print("\nHere is the encoded message:")

    # Convert a textual message into a sequence of numbers, utilizing the underlying Unicode encoding.
    for ch in message:
        print(ord(ch), end=" ")


def main():
    decode()
    encode()


main()
