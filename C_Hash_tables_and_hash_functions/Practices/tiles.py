from typing import List


def find_possible_tiles_count(line: List[int], line_length: int) -> List[int]:
    results = []

    for mirror_index in range(line_length // 2 + 1):
        is_different = False
        for i in range(mirror_index):
            if line[mirror_index - (i + 1)] != line[mirror_index + i]:
                is_different = True
                break
        if not is_different:
            results.append(line_length - mirror_index)

    return results


def main():
    line_length, _ = map(int, input().split())
    line = list(map(int, input().split()))
    results = find_possible_tiles_count(line, line_length)
    print(*results)


if __name__ == "__main__":
    main()
