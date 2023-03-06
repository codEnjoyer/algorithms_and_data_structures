from typing import Dict


def get_hashmap(array: list) -> Dict[int, list]:
    hashmap = {}
    for i in range(len(array)):
        if array[i] not in hashmap:
            hashmap[array[i]] = [i]
        else:
            hashmap[array[i]].append(i)
    return hashmap


def find_spot_value(array: list, number: int, hashmap: dict) -> int:
    max_value = 0
    try:
        indexes_of_number = hashmap[number]
    except KeyError:
        return 0
    try:
        all_matches_count = len(indexes_of_number)
    except KeyError:
        return 0
    for i in range(len(indexes_of_number)):
        left_similar_count = i + 1
        right_dissimilar = len(array) - (indexes_of_number[i] + (all_matches_count - left_similar_count + 1))
        max_value = max(max_value, left_similar_count * right_dissimilar)
    return max_value


def read_input() -> list:
    return list(map(int, input().split()))


def main():
    orcs_heights = read_input()
    grimmorhus_heights = read_input()
    hm = get_hashmap(orcs_heights)
    calculated_values = {}
    results = []
    for g_height in grimmorhus_heights:
        if g_height in calculated_values:
            results.append(calculated_values[g_height])
        else:
            value = find_spot_value(orcs_heights, g_height, hm)
            calculated_values[g_height] = value
            results.append(value)

    print(" ".join(map(str, results)))


if __name__ == "__main__":
    main()
