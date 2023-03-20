from collections import Counter, deque
from types import SimpleNamespace


def get_line_weight(left_part: str, weights: dict, line_len: int) -> int:
    res = 0
    for left_index, char in enumerate(left_part):
        right_index = -(left_index + 1)
        res += ((line_len + right_index) - left_index) * weights[char]
    return res


def sort_function(item: SimpleNamespace) -> (int, str):
    return -item.weight, item.char


def main():
    input_line = "примерчик"
    input_line = input()
    counter: {str, int} = dict(Counter(input_line))
    cyrillic_alphabet = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
                         "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    # input_weights = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32".split()
    input_weights = input().split()
    values = map(int, input_weights)
    # values = [0] * 32

    chars = [SimpleNamespace(char=char, count=counter[char], weight=weight)
             for char, weight in zip(cyrillic_alphabet, values)
             if char in counter]

    chars = tuple(sorted(chars, key=sort_function))
    stack = deque()
    potential_left_index = 0
    total_weight = 0
    for c in chars:
        potential_right_index = -(potential_left_index + 1)
        potential_weight = (len(input_line) + potential_right_index - potential_left_index) * c.weight
        is_permutation_meaningful = potential_weight > c.weight
        if c.count <= 1 or not is_permutation_meaningful:
            continue
        for _ in range(2):
            stack.insert(len(stack) // 2, c.char)
        c.count -= 2
        potential_left_index += 1
        potential_right_index += 1
        total_weight += potential_weight
    center = "".join(
        (c.char * c.count for c in sorted(filter(lambda item: item.count != 0, chars), key=lambda item: item.char)))
    stack.insert(len(stack) // 2, center)
    print("".join(stack), total_weight)


if __name__ == "__main__":
    main()
