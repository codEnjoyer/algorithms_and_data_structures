def get_intersection_count(first: list, second: list) -> list:
    res = []
    hashmap = {}
    for el in first:
        if el not in hashmap:
            hashmap[el] = second.count(el)
        res.append(hashmap[el])
    return res


def main():
    first_array = input().split()
    second_array = input().split()
    final = get_intersection_count(first_array, second_array)

    print(*final)


if __name__ == "__main__":
    main()
