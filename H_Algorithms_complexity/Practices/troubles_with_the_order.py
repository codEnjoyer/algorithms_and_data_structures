def partition(array: list, left: int, right: int) -> int:
    if right - left <= 1:
        return left
    i, j = left, right - 1
    pivot = array[right - 1]
    print(pivot)
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


def qsort(array: list, left: int, right: int) -> None:
    if right - left <= 1:
        return
    mid = partition(array, left, right)
    qsort(array, left, mid)
    qsort(array, mid + 1, right)


def main():
    # students = [179, 181, 165, 184, 190, 152, 167]
    students = list(map(int, input().split()))
    qsort(students, 0, len(students))
    print(" ".join(map(str, students)))


if __name__ == "__main__":
    main()
