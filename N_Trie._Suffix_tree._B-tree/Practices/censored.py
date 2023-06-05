from typing import Dict


class Node:
    is_banned: bool
    children: Dict[str, "Node"]

    def __init__(self):
        self.is_banned = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_banned = True

    def censor_word(self, word: str) -> int or None:
        node = self.root
        is_banned = False
        ban_word_pos_in_word = 0
        for char in word:
            if char not in node.children:
                node = self.root
                ban_word_pos_in_word += 1
                continue

            node = node.children[char]
            if node.is_banned:
                is_banned = True
                break

        return ban_word_pos_in_word if is_banned else None


def fill_trie_with_ban_words(trie: Trie, ban_words_count: int) -> None:
    for _ in range(ban_words_count):
        ban_word = input().lower()
        trie.add(ban_word)


def main():
    trie = Trie()

    ban_words_count = int(input())
    fill_trie_with_ban_words(trie, ban_words_count)

    lines_count = int(input())
    found_ban_word, ban_word_line_num, ban_word_pos_in_line = censor_text(trie, lines_count)

    if found_ban_word:
        print(ban_word_line_num + 1, ban_word_pos_in_line + 1)
    else:
        print("Одобрено")


def censor_text(trie: Trie, lines_count: int) -> (bool, int, int):
    found_ban_word = False
    ban_word_line_num, ban_word_pos_in_line = None, None

    for line_num in range(lines_count):
        if found_ban_word:
            break
        words = input().lower().split(" ")
        ban_word_pos_in_words = 0
        for word in words:
            ban_word_pos_inside_word = trie.censor_word(word)
            if ban_word_pos_inside_word is not None:
                found_ban_word = True
                ban_word_line_num = line_num
                ban_word_pos_in_line = ban_word_pos_in_words + ban_word_pos_inside_word
                break
            ban_word_pos_in_words += len(word) + 1
    return found_ban_word, ban_word_line_num, ban_word_pos_in_line


if __name__ == "__main__":
    main()
