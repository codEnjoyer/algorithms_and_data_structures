def sort(array: list):
    counter = [0] * 1000
    for number in array:
        counter[number] += 1
    pointer = 0
    for i in range(len(counter)):
        for j in range(counter[i]):
            array[pointer] = i
            pointer += 1


def main():
    array = [1, 2, 3, 1, 1, 6, 4, 2, 4]
    sort(array)
    print(array)


if __name__ == "__main__":
    main()