def insertion_sort(array: list) -> None:
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        while key < array[j] and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def main():
    array = [5, 3, 1, 2, 4]
    insertion_sort(array)
    print(array)


if __name__ == "__main__":
    main()
