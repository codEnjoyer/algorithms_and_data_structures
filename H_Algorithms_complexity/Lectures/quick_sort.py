from random import randrange


# region lectures Implementation
def partition(array: list, left: int, right: int) -> int:
    if right - left < 1:
        return left
    i, j = left, right - 1
    x = array[left + randrange(right - left)]
    while i < j:
        while array[i] < x:
            i += 1

        while array[j] > x:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
        else:
            break
    return i


def qsort(array: list, left: int, right: int) -> None:
    if right - left <= 1:
        return
    while right - left > 1:
        m = partition(array, left, right)
        if m - left > right - m:
            qsort(array, m, right)
            right = m
        else:
            qsort(array, left, m)
            left = m
# endregion

# region SO Implementation


# def partition(array: list, left: int, right: int):
#     pivot = left
#     for i in range(left + 1, right + 1):
#         if array[i] <= array[left]:
#             pivot += 1
#             array[i], array[pivot] = array[pivot], array[i]
#     array[pivot], array[left] = array[left], array[pivot]
#     return pivot
#
#
# def qsort(array: list, begin: int = 0, end: int = None):
#     if end is None:
#         end = len(array) - 1
#
#     def _quicksort(arr: list, left: int, right: int):
#         if left >= right:
#             return
#         pivot = partition(arr, left, right)
#         _quicksort(arr, left, pivot - 1)
#         _quicksort(arr, pivot + 1, right)
#
#     return _quicksort(array, begin, end)


# endregion

def main():
    array = [3, 5, 1, 2, 4, 5, 3]
    qsort(array, 0, len(array))
    print(array)


if __name__ == "__main__":
    main()
