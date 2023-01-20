def anagrams(string):
    # Return a list of all anagrams of a string.
    if string == "":
        return [string]
    else:
        anagram_list = []
        for word in anagrams(string[1:]):
            for pos in range(len(word) + 1):
                anagram_list.append(word[:pos] + string[0] + word[pos:])

        return anagram_list


def main():
    print(anagrams("hey"))


if __name__ == "__main__":
    main()
