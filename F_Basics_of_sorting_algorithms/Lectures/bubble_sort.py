def bubble_sort(array: list, n_iterations: int = None) -> None:
    if n_iterations is None:
        n_iterations = len(array)
    for i in range(n_iterations):
        has_swapped_elements = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                has_swapped_elements = True
        if not has_swapped_elements:
            break


def main():
    array = [5, 4, 3, 2, 1]
    bubble_sort(array)
    print(array)


if __name__ == "__main__":
    main()
