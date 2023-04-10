from typing import Iterable


def permutations(n: int, word: str = "", alphabet: Iterable[chr] = map(chr, range(1072, 1104))) -> None:
    if n < 1:
        print(word)
        return
    for char in alphabet:
        permutations(n - 1, word + char)


def main():
    permutations(3)


if __name__ == "__main__":
    main()
