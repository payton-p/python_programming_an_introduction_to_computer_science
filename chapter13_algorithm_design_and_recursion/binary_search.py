def binary_search(item_to_find, list_to_search):
    low = 0
    high = len(list_to_search) - 1
    while low <= high:  # there is still a range to search
        mid = (low + high) // 2  # position of middle item

        item_in_list = list_to_search[mid]
        if item_to_find == item_in_list:  # found x in list, return the index
            return mid
        elif item_to_find < item_in_list:  # x is in lower half of range
            high = mid - 1  # move top marker down
        else:  # x is in upper half
            low = mid + 1  # move bottom marker up

    return -1  # nothing left to search, x is not in the list


def main():
    example_list = [2, 3, 5, 7]
    print(binary_search(3, example_list))


if __name__ == "__main__":
    main()
