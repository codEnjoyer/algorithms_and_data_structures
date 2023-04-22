def partition(array: list, left: int, right: int) -> int:
    if right - left <= 1:
        return left
    i, j = left, right - 1
    pivot = array[right - 1]
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] >= pivot and j > 0:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
        else:
            break
    array[i], array[right - 1] = array[right - 1], array[i]
    return i


def kth_element(array: list, k: int) -> int:
    left, right = 0, len(array)
    while True:
        mid = partition(array, left, right)
        if mid == k:
            return array[mid]
        elif k < mid:
            right = mid
        else:
            left = mid


def main():
    # array = [6, 0, 2]
    array = list(map(int, input().split()))
    # k = 1
    k = int(input())
    r = kth_element(array, k)
    print(r)


if __name__ == "__main__":
    main()
