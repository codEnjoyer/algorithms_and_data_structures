
def binary_search(array: list, search: int, left_border: int = None, right_border: int = None) -> int:
    """Finds index of "search" in "array" via recursive binary search algorithm."""
    if left_border is None:
        left_border = -1
    if right_border is None:
        right_border = len(array)

    if left_border + 1 >= right_border:
        return right_border
    middle = (left_border + right_border) // 2
    if array[middle] >= search:
        return binary_search(array, search, left_border, middle)
    else:
        return binary_search(array, search, middle, right_border)


def main():
    numbers = [7, 10, 15, 21, 30]
    print(binary_search(numbers, 30))


if __name__ == "__main__":
    main()
