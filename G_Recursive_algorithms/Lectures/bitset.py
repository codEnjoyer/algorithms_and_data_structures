from typing import List


class Bitset:
    _data: List[int]

    def __init__(self, n: int = 0):
        size = n // 32
        self._data = [0] * (size + 1)

    def get(self, index: int) -> int:
        x = self._data[index // 32]
        return (x >> (index % 32)) & 1

    def set(self, index: int, value: int) -> None:
        if self.get(index) == value:
            return
        self._data[index // 32] ^= 1 << (index % 32)

    def print(self, n: int) -> None:
        for i in range(n):
            print(self.get(i), end="")
        print()


def bitset_permutations(n: int, k: int, x: int = 0) -> None:
    if n - x <= k:
        return
    if x == n:
        bitset.print(n)
        return
    bitset.set(x, 0)
    bitset_permutations(n, k, x + 1)
    bitset.set(x, 1)
    bitset_permutations(n, k - 1, x + 1)


bitset = Bitset()


def main():
    global bitset
    n = 16
    bitset = Bitset(n)
    bitset_permutations(n, 8)


if __name__ == "__main__":
    main()
