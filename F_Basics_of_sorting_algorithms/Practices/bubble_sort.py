def print_array(array: list) -> None:
    print(" ".join(list(map(str, array))))


def bubble_sort(array: list, n_iterations_to_print: int) -> None:
    was_printed = False

    for n_element in range(len(array)):
        has_swapped_elements = False
        if n_element == n_iterations_to_print:
            print_array(array)
            was_printed = True

        for j in range(len(array) - n_element - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                has_swapped_elements = True

        if not has_swapped_elements:
            if not was_printed:
                print_array(array)
            break

    if n_iterations_to_print >= len(array):
        print_array(array)


def main():
    array = list(map(int, input().split()))
    n_iterations_to_print = int(input())

    bubble_sort(array, n_iterations_to_print)

    print_array(array)


if __name__ == "__main__":
    main()
