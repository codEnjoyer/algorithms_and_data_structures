def z_function(line: str):
    line_length = len(line)
    sub_indexes = [0] * line_length
    sub_len = 0
    r = 0
    for index in range(1, line_length):
        if index <= r:
            sub_indexes[index] = min(r - index + 1, sub_indexes[index - sub_len])
        while (index + sub_indexes[index] < line_length) and (
                line[sub_indexes[index]] == line[index + sub_indexes[index]]):
            sub_indexes[index] += 1
        if index + sub_indexes[index] - 1 > r:
            sub_len = index
            r = index + sub_indexes[index] - 1
    return sub_indexes


def main():
    line = input()
    z = z_function(line)
    line_length = len(line)
    for index, elem in enumerate(z):
        if index + elem == line_length and line_length % index == 0:
            print(line_length // index, line[:index])
            break


if __name__ == "__main__":
    main()
