from typing import Dict, List


class Node:
    is_end: bool
    children: Dict[str, "Node"]

    def __init__(self):
        self.is_end = False
        self.children = {}

    def __str__(self):
        return f"{self.is_end} {tuple(self.children.keys())}"

    def __repr__(self):
        return str(self)


class Trie:
    root: Node

    def __init__(self):
        self.root = Node()

    def add(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end = True

    def get_first_x_words_by_prefix(self, prefix: str, x: int) -> list:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        words_with_prefix = []
        self._get_first_x_words(node, prefix, words_with_prefix)

        return sorted(filter(lambda word: len(word) > len(prefix), words_with_prefix))[:x]

    def _get_first_x_words(self, node: "Node", prefix: str, words_with_prefix: List[str]) -> None:
        if node.is_end:
            words_with_prefix.append(prefix)
        for char in node.children:
            self._get_first_x_words(node.children[char], prefix + char, words_with_prefix)
        return None

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return str(self)


def main():
    trie = Trie()
    while True:
        command, *args = input().split()
        if command == "exit":
            print("bye")
            break
        elif command == "add":
            trie.add(args[0])
            print("ok")
        elif command == "get":
            result = trie.get_first_x_words_by_prefix(args[0], int(args[1]))
            print(" ".join(result)) if result else print("empty")


if __name__ == "__main__":
    main()
