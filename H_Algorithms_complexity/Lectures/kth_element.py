from quick_sort import partition


def kth_element(array: list, k: int) -> int:
    left, right = 0, len(array)
    while left + 1 < right:
        m = partition(array, left, right)
        if k < m:
            right = m
        else:
            left = m
    return array[left]


def median(array: list) -> int:
    return kth_element(array, len(array) // 2)


def main():
    array = [0, 1, 2, 3, 4, 5]
    k = 2
    r = kth_element(array, k)
    print(r)


if __name__ == "__main__":
    main()
