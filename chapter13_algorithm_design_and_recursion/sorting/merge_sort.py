def merge(array, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    # Create temp arrays.
    tmp_left = [0] * n1
    tmp_right = [0] * n2

    # Copy data to temp arrays.
    for i in range(0, n1):
        tmp_left[i] = array[left + i]

    for j in range(0, n2):
        tmp_right[j] = array[middle + 1 + j]

    # Merge the temp arrays back into array[left..right]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray
    while i < n1 and j < n2:
        if tmp_left[i] <= tmp_right[j]:
            array[k] = tmp_left[i]
            i += 1
        else:
            array[k] = tmp_right[j]
            j += 1

        k += 1

    # Copy the remaining elements of tmp_left[], if there are any.
    while i < n1:
        array[k] = tmp_left[i]
        i += 1
        k += 1

    # Copy the remaining elements of tmp_right[], if there are any.
    while j < n2:
        array[k] = tmp_right[j]
        j += 1
        k += 1


# left is for left index and right is for right index of the sub-array of the array to be sorted.
def merge_sort(array, left, right):
    if left < right:
        # Same as (l + r) // 2, but avoids overflow for large l and h.
        middle = left + (right - left) // 2

        # Sort first and second halves.
        merge_sort(array, left, middle)
        merge_sort(array, middle + 1, right)
        merge(array, left, middle, right)


def main():
    array = [12, 11, 13, 5, 6, 7]
    print("Given array is:", array)

    n = len(array)
    merge_sort(array, 0, n - 1)
    print("\nSorted array is:", array)


if __name__ == "__main__":
    main()
