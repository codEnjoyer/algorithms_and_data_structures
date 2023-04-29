from typing import List, Dict
from collections import Counter


class Node:
    symbol: str
    weight: int
    zero: "Node"
    one: "Node"

    def __init__(self, symbol: str, weight: int, zero: "Node" = None, one: "Node" = None):
        self.symbol = symbol
        self.weight = weight
        self.zero = zero
        self.one = one

    def __str__(self):
        return f"Node({self.symbol}, {self.weight}, {self.zero}, {self.one})"

    def __repr__(self):
        return str(self)

    def __add__(self, other: "Node"):
        return Node(self.symbol + other.symbol, self.weight + other.weight, self, other)


def get_huffman_encoding(node: Node, bin_string: str = '') -> Dict[str, str]:
    if not node.zero and not node.one:
        return {node.symbol: bin_string}
    code = {}
    code.update(get_huffman_encoding(node.zero, bin_string + '0'))
    code.update(get_huffman_encoding(node.one, bin_string + '1'))
    return code


def make_tree(nodes: List[Node]) -> Node:
    while len(nodes) > 1:
        first_node = nodes.pop()
        second_node = nodes.pop()
        new_node = first_node + second_node
        nodes.append(new_node)
        nodes = sorted(nodes, key=lambda node: node.weight, reverse=True)
    return nodes.pop()


def main():
    message = 'a'  # input()
    counter = dict(Counter(message))
    nodes = [Node(item[0], item[1]) for item in sorted(counter.items(), key=lambda item: item[1], reverse=True)]
    node_tree = make_tree(nodes)
    encoding = get_huffman_encoding(node_tree)
    total_len = 0
    for char, count in counter.items():
        total_len += len(encoding[char]) * count
    # if not total_len:
    #     print(message)
    # else:
    #     print(total_len)
    print(total_len if total_len else total_len + 1)


if __name__ == "__main__":
    main()
