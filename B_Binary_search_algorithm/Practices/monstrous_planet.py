def get_index_min_max_pair(legs: list, hands: list):
    left, right = 0, len(legs) - 1
    result = 0
    max_value = float('inf')
    while left <= right:
        middle = (left + right) // 2

        if max_value >= max(legs[middle], hands[middle]):
            result = middle
            max_value = max(legs[middle], hands[middle])

        if legs[middle] > hands[middle]:
            right = middle - 1
        elif legs[middle] < hands[middle]:
            left = middle + 1
        else:
            break
    return result


def main():
    n, m, l = map(int, input().split())
    multi_legs = [list(map(int, input().split())) for _ in range(n)]
    multi_hands = [list(map(int, input().split())) for _ in range(m)]
    q = int(input())

    results = []
    for _ in range(q):
        i, j = map(int, input().split())
        legs = multi_legs[i]
        hands = multi_hands[j]
        found_index = get_index_min_max_pair(legs, hands)

        for k in range(found_index, len(hands) - 1):
            if max(legs[k], hands[k]) == max(legs[k + 1], hands[k + 1]):
                found_index += 1
            else:
                break
        results.append(found_index)
    print(*results, sep='\n')


if __name__ == "__main__":
    main()
