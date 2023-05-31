from ast import literal_eval


def get_parents(tree: dict, key: int, node: int, parents: list = None) -> list or None:
    if parents is None:
        parents = [key]
    if key not in tree:
        return None
    connected_nodes = tree[key]
    if node in connected_nodes:
        return parents
    for connected_node in connected_nodes:
        a = get_parents(tree, connected_node, node, parents + [connected_node])
        if a is not None:
            return a


def get_common_parent(tree: dict, first_node: int, second_node: int) -> int:
    root_node = tuple(tree.keys())[0]
    first_parents = get_parents(tree, root_node, first_node)
    second_parents = get_parents(tree, root_node, second_node)
    return get_common_element(first_parents, second_parents)


def get_common_element(first: list, second: list) -> int:
    for first_el in reversed(first):
        if first_el in second:
            return first_el


def main():
    _ = int(input())
    tree = literal_eval(input())
    first_node, second_node = map(int, input().split())
    print(get_common_parent(tree, first_node, second_node))


if __name__ == "__main__":
    main()
