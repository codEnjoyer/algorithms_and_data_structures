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
        if root:
            self.root = root
            return
        if array:
            self.from_array(array)

    def add(self, data: int) -> None:
        if self.root is None:
            self.root = Node(data, None)
            return

        def _add(node: Node) -> None:
            if data < node.data:
                if node.left:
                    _add(node.left)
                    return
                node.left = Node(data, node)
                return
            if node.right:
                _add(node.right)
                return
            node.right = Node(data, node)

        return _add(self.root)

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

    def print(self, root: Node = None) -> None:
        if root is None:
            root = self.root

        def _print(node: Node, is_more_nodes_below: List[bool] = None) -> None:
            if node is None:
                return
            if is_more_nodes_below is None:
                is_more_nodes_below = []

            indent = []
            if is_more_nodes_below:
                indent = list(map(lambda b: '│\t' if b else '\t', is_more_nodes_below))
                indent[-1] = "├───" if is_more_nodes_below[-1] else "└───"

            print(f"{''.join(indent)}{node.data}")
            _print(node.left, is_more_nodes_below + [True])
            _print(node.right, is_more_nodes_below + [False])

        return _print(root)


def main():
    array = [1, 3, 4, 9, 10, 10, 13, 15, 16]
    tree = Tree(array)
    tree.print()


if __name__ == "__main__":
    main()
