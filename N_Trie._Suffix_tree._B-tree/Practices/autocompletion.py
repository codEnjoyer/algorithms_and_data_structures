from typing import Dict, List, NamedTuple


class Word(NamedTuple):
    word: str
    count: int


class Node:
    is_end: bool
    children: Dict[str, "Node"]
    word_count: int

    def __init__(self):
        self.is_end = False
        self.children = {}
        self.word_count = 0

    def __str__(self):
        return f"{self.is_end} {tuple(self.children.keys())}"

    def __repr__(self):
        return str(self)


class Trie:
    root: Node

    def __init__(self, words: List[str] = None):
        self.root = Node()
        if words is not None:
            for word in words:
                self.add(word)

    def add(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end = True
        node.word_count += 1

    def get_most_suitable_word(self, prefix: str) -> str or None:
        node = self._get_prefix_last_node(prefix)
        if node is None:
            return None

        prefix_words_with_count = []
        self._get_prefix_words_with_count(node, prefix, prefix_words_with_count)

        most_frequent_words = self._get_most_frequent_words(prefix_words_with_count)
        most_frequent_words.sort(key=lambda word: (len(word), word))
        return most_frequent_words[0]

    def _get_prefix_last_node(self, prefix: str) -> Node or None:
        node = self.root
        if prefix == " ":
            return node
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def _get_prefix_words_with_count(self, node: Node, prefix: str,
                                     prefix_words_with_count: List[Word]) -> None:
        if node.is_end:
            prefix_words_with_count.append(Word(word=prefix, count=node.word_count))
        for char in node.children:
            self._get_prefix_words_with_count(node.children[char], prefix + char, prefix_words_with_count)
        return None

    @staticmethod
    def _get_most_frequent_words(prefix_words_with_count: List[Word]) -> List[str]:
        most_frequent_words = []
        max_count = max(prefix_words_with_count, key=lambda item: item.count).count
        for word, count in prefix_words_with_count:
            if count == max_count:
                most_frequent_words.append(word)
        return most_frequent_words

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return str(self)


def main():
    words = input().split()
    trie = Trie(words)
    while True:
        command, *args = input().split()
        if command == "exit":
            print("bye")
            break
        elif command == "+":
            trie.add(args[0])
            print("ok")
        elif command == "?":
            prefix = args[0] if args else ""
            word = trie.get_most_suitable_word(prefix)
            print(word)


if __name__ == "__main__":
    main()
