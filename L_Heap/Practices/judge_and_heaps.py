class Cake:
    price: int
    weight: int
    unit_value: float

    def __init__(self, price: int, weight: int):
        self.price = price
        self.weight = weight
        self.unit_value = - price / weight

    def __lt__(self, other: "Cake"):
        return self.unit_value < other.unit_value

    def __le__(self, other: "Cake"):
        return self.unit_value <= other.unit_value

    def __gt__(self, other: "Cake"):
        return self.unit_value > other.unit_value

    def __ge__(self, other: "Cake"):
        return self.unit_value >= other.unit_value


class Heap:
    items: list

    def __init__(self):
        self.items = []

    def get_size(self) -> int:
        return len(self.items)

    def get_min(self) -> Cake:
        return self.items[0]

    def add(self, item: Cake) -> None:
        self.items.append(item)
        self.sift_up(self.get_size() - 1)

    def pop(self) -> Cake:
        root = self.get_min()
        min_item = self.items.pop()
        if self.items:
            self.items[0] = min_item
            self.sift_down(0)
        return root

    def sift_up(self, index: int) -> None:
        while index > 0:
            parent_index = (index - 1) // 2
            if self.items[parent_index] <= self.items[index]:
                return
            self.items[parent_index], self.items[index] = self.items[index], self.items[parent_index]
            index = parent_index

    def sift_down(self, index: int) -> None:
        while 2 * index + 1 < self.get_size():
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            if right_child_index < self.get_size() and self.items[right_child_index] < self.items[left_child_index]:
                left_child_index = right_child_index
            if self.items[index] <= self.items[left_child_index]:
                return
            self.items[index], self.items[left_child_index] = self.items[left_child_index], self.items[index]
            index = left_child_index


def get_max_profit(cakes: Heap, bag_capacity: int) -> float:
    profit = 0.0
    while cakes.get_size() > 0:
        cake = cakes.pop()
        if bag_capacity >= cake.weight:
            profit += cake.price
            bag_capacity -= cake.weight
        else:
            piece_price = bag_capacity * - cake.unit_value
            profit += piece_price
            break
    return profit


def main():
    n_cakes, bag_capacity = map(int, input().split())
    cakes = Heap()
    for _ in range(n_cakes):
        price, weight = map(int, input().split())
        cakes.add(Cake(price, weight))
    profit = get_max_profit(cakes, bag_capacity)
    print(f"{profit:.2f}")


if __name__ == "__main__":
    main()
