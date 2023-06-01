from collections import deque
from typing import Dict, Tuple


def add_combination(combination: int, get_from: int, combinations: Dict[int, int], to_visit: deque) -> None:
    if combination not in combinations:
        combinations[combination] = get_from
        to_visit.append(combination)


def bfs(initial_number: int, final_number: int) -> Dict[int, int]:
    number_of_digits = len(str(initial_number))
    digits_helper = 10 ** (number_of_digits - 1)
    combinations = {initial_number: initial_number}
    to_visit = deque()
    to_visit.append(initial_number)
    while to_visit and final_number not in combinations:
        combination = to_visit.popleft()

        first_digit_less_nine = combination // digits_helper < 9
        if first_digit_less_nine:
            incremented_first_digit = combination + digits_helper
            add_combination(incremented_first_digit, combination, combinations, to_visit)

        last_digit_greater_one = combination % 10 > 1
        if last_digit_greater_one:
            add_combination(combination - 1, combination, combinations, to_visit)

        right_cyclic_shift = combination // 10 + digits_helper * (combination % 10)
        add_combination(right_cyclic_shift, combination, combinations, to_visit)

        left_cyclic_shift = combination % digits_helper * 10 + combination // digits_helper
        add_combination(left_cyclic_shift, combination, combinations, to_visit)
    return combinations


def restore_combination_order(combinations: Dict[int, int], final_combination: int) -> Tuple[int]:
    final_order = [final_combination]
    get_from = final_combination
    while combinations[get_from] != get_from:
        final_order.append(combinations[get_from])
        get_from = combinations[get_from]
    return tuple(reversed(final_order))


def main():
    initial_combination = int(input())
    final_combination = int(input())
    combinations = bfs(initial_combination, final_combination)
    final_combination_order = restore_combination_order(combinations, final_combination)
    print("\n".join(map(str, final_combination_order)))


if __name__ == '__main__':
    main()
