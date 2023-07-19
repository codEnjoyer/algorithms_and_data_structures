def merge(array: list, left: int, mid: int, right: int) -> None:
    global counter
    p1, p2, res_p = left, mid, 0
    buffer = [0] * (right - left)
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
            counter += mid - p1
            p2 += 1
        res_p += 1
    for i in range(left, right):
        array[i] = buffer[i - left]


def merge_sort(array: list, left: int = 0, right: int = None) -> None:
    if right is None:
        right = len(array)
    if right - left <= 1:
        return
    middle = (left + right) // 2
    merge_sort(array, left, middle)
    merge_sort(array, middle, right)
    merge(array, left, middle, right)


def main():
    pebbles = [int(input()) for _ in range(int(input()))]
    # pebbles = [179, 4, 3, 2, 1, 1]
    merge_sort(pebbles)
    # print(t)
    print(counter)
    # print(pebbles)


if __name__ == "__main__":
    counter = 0
    main()
