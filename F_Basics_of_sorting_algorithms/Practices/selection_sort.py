def print_array(array: list) -> None:
    print(" ".join(map(str, array)))


def selection_sort(array: list) -> None:
    n_iteration_to_print = len(array) // 2
    for n_iteration, element in enumerate(array):
        if n_iteration == n_iteration_to_print:
            print_array(array)

        min_element_index = min(range(n_iteration, len(array)), key=array.__getitem__)
        array[n_iteration], array[min_element_index] = array[min_element_index], element


def main():
    array = list(map(int, input().split()))
    selection_sort(array)
    print_array(array)


if __name__ == "__main__":
    main()
