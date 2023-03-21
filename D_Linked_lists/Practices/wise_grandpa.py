from collections import Counter, deque
from types import SimpleNamespace as MutableNamedTuple
from typing import Iterable


def fill_sides_and_get_weight(stack: deque, chars: Iterable, line_length: int) -> int:
    potential_left_index, total_weight = 0, 0
    for c in chars:

        potential_right_index = -(potential_left_index + 1)
        potential_weight = (line_length + potential_right_index - potential_left_index) * c.weight
        is_permutation_meaningful = potential_weight > c.weight
        if c.count <= 1 or not is_permutation_meaningful:
            continue

        for _ in range(2):
            stack.insert(len(stack) // 2, c.char)
        c.count -= 2
        potential_left_index += 1
        potential_right_index += 1
        total_weight += potential_weight

    return total_weight


def get_central_part(chars: Iterable) -> str:
    remaining_chars = filter(lambda item: item.count != 0, chars)
    alphabetically_sorted_remaining_chars = sorted(remaining_chars, key=lambda item: item.char)
    return "".join([c.char * c.count for c in alphabetically_sorted_remaining_chars])


def main():
    input_line = input()
    counter = dict(Counter(input_line))
    cyrillic_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    input_weights = map(int, input().split())

    chars = [MutableNamedTuple(char=char, count=counter[char], weight=weight)
             for char, weight in zip(cyrillic_alphabet, input_weights)
             if char in counter]
    chars = tuple(sorted(chars, key=lambda item: (-item.weight, item.char)))

    stack = deque()

    total_weight = fill_sides_and_get_weight(stack, chars, len(input_line))
    central_part = get_central_part(chars)
    stack.insert(len(stack) // 2, central_part)

    print("".join(stack), total_weight)


if __name__ == "__main__":
    main()
