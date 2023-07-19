from random import shuffle


# region Basic Realization
# def merge(first: list, second: list) -> list:
#     res = []
#     first_pointer, second_pointer = 0, 0
#     while first_pointer < len(first) or second_pointer < len(second):
#         if first_pointer == len(first):
#             res.append(second[second_pointer])
#             second_pointer += 1
#             continue
#         if second_pointer == len(second):
#             res.append(first[first_pointer])
#             first_pointer += 1
#             continue
#         if first[first_pointer] < second[second_pointer]:
#             res.append(first[first_pointer])
#             first_pointer += 1
#         else:
#             res.append(second[second_pointer])
#             second_pointer += 1
#     return res
#
#
# def merge_sort(array: list) -> list:
#     if len(array) <= 1:
#         return array
#     middle = len(array) // 2
#     return merge(
#         merge_sort(array[:middle]),
#         merge_sort(array[middle:])
#     )
# endregion

def merge(array: list, left: int, mid: int, right: int, buffer: list) -> None:
    p1, p2, res_p = left, mid, 0
    while p1 < mid or p2 < right:
        if p1 == mid:
            buffer[res_p] = array[p2]
            p2 += 1
            res_p += 1
            continue
        if p2 == right:
            buffer[res_p] = array[p1]
            p1 += 1
            res_p += 1
            continue
        if array[p1] < array[p2]:
            buffer[res_p] = array[p1]
            p1 += 1
        else:
            buffer[res_p] = array[p2]
            p2 += 1
        res_p += 1
    for i in range(left, right):
        array[i] = buffer[i - left]


def merge_sort(array: list, left: int = None, right: int = None, buffer: list = None) -> None:
    if left is None:
        left = 0
    if right is None:
        right = len(array)
    if buffer is None:
        buffer = [0] * right
    if right - left <= 1:
        return
    middle = (left + right) // 2
    merge_sort(array, left, middle, buffer)
    merge_sort(array, middle, right, buffer)
    merge(array, left, middle, right, buffer)


def main():
    first = [1, 3, 4, 5, 5, 6]
    second = [2, 3, 3, 6, 8, 8]
    to_sort = [1, 2, 3, 3, 3, 4, 5, 5, 6, 6, 8, 8]
    shuffle(to_sort)
    # result = merge(first, second)
    merge_sort(to_sort)
    print(to_sort)


if __name__ == "__main__":
    main()
