from typing import List

word_len_after_compression = 4


def main():
    table = []
    word = input()
    fill_table(word, table)
    print(table[-1][-1])


def fill_table(word: str, table: List[List[str or None]]):
    word_len = len(word)
    for sub_len in range(word_len):
        table.append([None] * (word_len - sub_len))
        for sub_pos in range(word_len - sub_len):
            sub_repeats_count = 1
            sub = word[sub_pos:(sub_pos + sub_len + 1)]
            if sub_len + 1 > word_len_after_compression:
                sub, sub_repeats_count = get_string_pattern(sub)
                sub = dynamic_compress(sub, sub_pos, table)
            table[sub_len][sub_pos] = f"{sub_repeats_count}({sub})" if sub_repeats_count != 1 else sub


def dynamic_compress(word: str, index: int, table: List[List[str or None]]) -> str:
    result = word
    word_len = len(word)
    if word_len <= word_len_after_compression:
        return result
    for end in range(word_len - 1):
        left = table[end][index]
        right = table[word_len - end - 2][index + end + 1]
        if len(left) + len(right) < len(result):
            result = left + right
    return result


def get_string_pattern(word: str) -> (str, int):
    final_sub = word
    word_len = len(word)
    repeats = 1
    for k_times in range(1, word_len // 2 + 1):
        if word_len % k_times != 0:
            continue
        sub = word[:k_times]
        repeats_count = word_len // k_times
        if word == sub * repeats_count and k_times + 3 < word_len:
            final_sub = sub
            repeats = repeats_count
            break
    return final_sub, repeats


if __name__ == '__main__':
    main()
