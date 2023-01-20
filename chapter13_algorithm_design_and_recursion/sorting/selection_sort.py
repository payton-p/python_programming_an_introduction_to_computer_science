def selection_sort(array, size):
    for i in range(size):
        min_index = i

        for j in range(i + 1, size):
            # Select the minimum element in every iteration.
            if array[j] < array[min_index]:
                min_index = j

        # Swap the elements to sort the array.
        (array[i], array[min_index]) = (array[min_index], array[i])


def main():
    example_list = [890, 2, 5, 3, 5, 3, 27]
    selection_sort(example_list, len(example_list))
    print(example_list)


if __name__ == "__main__":
    main()
