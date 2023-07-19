from typing import List


class Cake:
    price: int
    weight: int
    sliceable: bool
    value: float

    def __init__(self, price: int, weight: int, sliceable: bool):
        self.price = price
        self.weight = weight
        self.sliceable = sliceable
        self.value = price / weight

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __lt__(self, other):
        return self.value < other.value


def get_max_profit(cakes: List[Cake], bag_capacity: int) -> float:
    profit = 0.0
    cakes_sorted = sorted(cakes, key=lambda item: item.value, reverse=True)
    for cake in cakes_sorted:
        if bag_capacity >= cake.weight:
            bag_capacity -= cake.weight
            profit += cake.price
        elif cake.sliceable:
            profit += cake.value * bag_capacity
            break
    return profit


def main():
    n_cakes, bag_capacity = map(int, input().split())
    cakes = []
    for _ in range(n_cakes):
        price, weight, sliceable = input().split()
        cakes.append(Cake(int(price), int(weight), sliceable == 'Д'))
    profit = get_max_profit(cakes, bag_capacity)
    print(f"{profit:.2f}")


if __name__ == "__main__":
    main()
