def print_array(array: list) -> None:
    print(" ".join(map(str, array)))


def insertion_sort(array: list) -> None:
    n_iteration_to_print = len(array) // 2 + len(array) % 2
    for n_iteration in range(len(array)):
        if n_iteration == n_iteration_to_print:
            print_array(array)
        key = array[n_iteration]
        index_to_insert = n_iteration - 1
        while key < array[index_to_insert] and index_to_insert >= 0:
            array[index_to_insert + 1] = array[index_to_insert]
            index_to_insert -= 1
        array[index_to_insert + 1] = key


def main():
    array = list(map(int, input().split()))
    insertion_sort(array)
    print_array(array)


if __name__ == "__main__":
    main()
