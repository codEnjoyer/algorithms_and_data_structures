def get_connectivity_component(nodes: tuple, node_index: int, connectivity_component: list = None) -> list:
    if connectivity_component is None:
        connectivity_component = []
    if node_index == -1 or node_index in connectivity_component:
        return connectivity_component
    connectivity_component += [node_index]
    for node_i in nodes[node_index]:
        connectivity_component = get_connectivity_component(nodes, node_i, connectivity_component)
    return connectivity_component


def main():
    nodes_count, connectivity_node = map(int, input().split())
    array = tuple(tuple(map(int, input().split())) for _ in range(nodes_count))
    print(*sorted(get_connectivity_component(array, connectivity_node)))


if __name__ == "__main__":
    main()
