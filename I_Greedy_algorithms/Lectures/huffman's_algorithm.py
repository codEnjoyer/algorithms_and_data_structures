from __future__ import annotations
from functools import total_ordering
from heapq import heappush, heappop
from typing import Union, List, Tuple, Dict


@total_ordering
class Node:
    weight: int
    zero: Node
    one: Node
    char: chr

    def __init__(self, weight: int, zero: Union[Node, None], one: Union[Node, None], char: Union[chr, None]):
        self.weight = weight
        self.zero = zero
        self.one = one
        self.char = char

    def _is_valid_operand(self, other: Node):
        return hasattr(other, "weight") and hasattr(other, "zero") and hasattr(other, "one") and hasattr(other, "char")

    def __eq__(self, other: Node):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.weight, self.zero, self.one, self.char) == (other.weight, other.zero, other.one, other.char)

    def __lt__(self, other: Node):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.weight < other.weight

    def __str__(self):
        return f"{type(self).__name__}({self.weight}, {self.zero}, {self.one}, {self.char})"

    def __repr__(self):
        return f"{type(self).__name__}({self.weight}, {self.zero}, {self.one}, {self.char})"


def dfs(cur_node: Node, cur_code: List[int] = None, char_code: Dict[chr, int] = None) -> Dict[chr, int]:
    if cur_code is None:
        cur_code = []
    if char_code is None:
        char_code = {}

    def _dfs(cur_node: Node, cur_code: List[int], char_code: Dict[chr, int]) -> Union[Dict[chr, int], None]:
        if cur_node.zero is None:
            code_to_print = "".join(map(str, cur_code))
            print(f"""Code for '{cur_node.char}': {code_to_print}""")
            char_code[cur_node.char] = int(code_to_print)
            return
        cur_code.append(0)
        _dfs(cur_node.zero, cur_code, char_code)
        cur_code.pop()
        cur_code.append(1)
        _dfs(cur_node.one, cur_code, char_code)
        return char_code

    return _dfs(cur_node, cur_code, char_code)


def huffman(s: str) -> Dict[chr, int]:
    const_size = 256
    char_counts = [0] * const_size
    for char_count in s:
        char_counts[ord(char_count)] += 1
    pq: List[Tuple[int, Node]] = []
    for index, char_count in enumerate(char_counts):
        if char_count > 0:
            heappush(pq, (char_count, Node(char_count, None, None, chr(index))))
    while len(pq) > 1:
        t1 = heappop(pq)[1]
        t2 = heappop(pq)[1]
        new_node = Node(t1.weight + t2.weight, t1, t2, t1.char + t2.char)
        heappush(pq, (t1.weight + t2.weight, new_node))
    return dfs(heappop(pq)[1])


def main():
    print(huffman("abracadabra"))


if __name__ == "__main__":
    main()
