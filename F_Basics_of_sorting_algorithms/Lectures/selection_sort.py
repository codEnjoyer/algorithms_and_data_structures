def selection_sort(array: list) -> None:
    for i in range(len(array)):
        pt = i
        for j in range(i + 1, len(array)):
            if array[j] < array[pt]:
                pt = j
        array[i], array[pt] = array[pt], array[i]


def habr_selection_sort(data: list) -> None:
    for i, e in enumerate(data):
        mn = min(range(i, len(data)), key=data.__getitem__)
        data[i], data[mn] = data[mn], e


def main():
    array = [5, 1, 4, 3, 2]
    habr_selection_sort(array)
    # selection_sort(array)
    print(array)


if __name__ == "__main__":
    main()
