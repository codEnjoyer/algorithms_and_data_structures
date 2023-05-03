from typing import List


class Node:
    data: int
    parent: "Node"
    left: "Node"
    right: "Node"

    def __init__(self, data: int, parent: "Node" or None, left: "Node" = None, right: "Node" = None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


class Tree:
    root: Node

    def __init__(self, array: List[int] = None, root: Node = None):
        self.root = root
        if array and root is None:
            self.from_array(array)

    def add(self, data: int or List[int]) -> None:
        if isinstance(data, int):
            data = [data]

        def _add(node: Node, key: int) -> None:
            if key < node.data:
                if node.left:
                    _add(node.left, key)
                    return
                node.left = Node(key, node)
                return
            if node.right:
                _add(node.right, key)
                return
            node.right = Node(key, node)

        for value_key in data:
            if self.root is None:
                self.root = Node(value_key, None)
                continue
            _add(self.root, value_key)

    def from_array(self, array: List[int], left_border: int or None = None, right_border: int or None = None) -> "Tree":
        if left_border is None:
            left_border = 0
        if right_border is None:
            right_border = len(array)

        def _from_array(left: int, right: int) -> Node or None:
            if left + 1 > right:
                return None
            if left + 1 == right:
                return Node(array[left], None)

            middle = (left + right - 1) // 2
            node = Node(array[middle], None)
            node.left = _from_array(left, middle)
            node.right = _from_array(middle + 1, right)
            if node.left:
                node.left.parent = node
            if node.right:
                node.right.parent = node
            return node

        self.root = _from_array(left_border, right_border)
        return self

    def find(self, key: int, find_from: Node = None) -> Node or None:
        if find_from is None:
            find_from = self.root

        def _find(node: Node) -> Node or None:
            if node is None:
                return None
            if node.data == key:
                return node
            return _find(node.left) if node.data > key else _find(node.right)

        return _find(find_from)

    def delete(self, key: int) -> None:
        if self.root is None:
            return
        found = self.find(key)
        if found is None:
            return

        def _delete(node: Node) -> None:
            if node is None:
                return
            if node.left is None or node.right is None:
                child = node.left if node.left else node.right
                if node is self.root:
                    self.root = child
                    if child:
                        child.parent = None
                if node.parent:
                    if node.parent.left is node:
                        node.parent.left = child
                        if child:
                            child.parent = node.parent
                    else:
                        node.parent.right = child
                        if child:
                            child.parent = node.parent
            else:
                next_node = node.right
                while next_node.left:
                    next_node = next_node.left
                node.data = next_node.data
                _delete(next_node)

        return _delete(found)

    def next(self, key: int, node: Node = None) -> Node or None:
        if node is None:
            node = self.find(key)
            if not node:
                return
        if node.right:
            next_node = node.right
            while next_node.left:
                next_node = next_node.left
            return next_node
        next_node = node
        while next_node.parent and next_node.parent.right is next_node:
            next_node = next_node.parent
        return next_node.parent

    def min(self) -> Node or None:
        if self.root is None:
            return None
        next_node = self.root
        while next_node.left:
            next_node = next_node.left
        return next_node

    def max(self) -> Node or None:
        if self.root is None:
            return None
        next_node = self.root
        while next_node.right:
            next_node = next_node.right
        return next_node

    def list(self) -> List[int] or None:
        if self.root is None:
            return None
        result = []
        node = self.min()
        while node:
            result.append(node.data)
            node = self.next(node.data, node)
        return result


def process_input(tree: Tree) -> bool:
    command, *args = input().split()
    if command == "add":
        tree.add(list(map(int, args)))
        print("Ok")
    elif command == "delete":
        tree.delete(int(args[0]))
        print("Ok")
    elif command == "find":
        node = tree.find(int(args[0]))
        print("Такая банка есть" if node else "Такой банки нет")
    elif command == "min":
        node = tree.min()
        print(node.data if node else "Склад пуст")
    elif command == "max":
        node = tree.max()
        print(node.data if node else "Склад пуст")
    elif command == "list":
        values = tree.list()
        print(" ".join(map(str, values)) if values else "")
    elif command == "exit":
        return False
    return True


def main():
    # array = [1, 3, 4, 10, 13]
    array = list(map(int, input().split()))
    tree = Tree(array)
    is_ongoing = True
    while is_ongoing:
        is_ongoing = process_input(tree)


if __name__ == "__main__":
    main()
