def separate_string_by_max_substring(line: str) -> (int, str):
    for k_times in range(len(line), 0, -1):
        sub_len = len(line) // k_times
        if sub_len * k_times != len(line):
            continue
        t = line[:sub_len]
        p = t * k_times
        if p == line:
            return k_times, p[:sub_len]


def main():
    line = input()
    print(*separate_string_by_max_substring(line))


if __name__ == "__main__":
    main()
