from collections import namedtuple
from typing import List


def get_cake_worth(cake: namedtuple("cake", ["price", "weight"])) -> float:
    if not cake.price:
        return float("inf")
    return cake.weight / cake.price


def get_max_profit(cakes: List[namedtuple("cake", ["price", "weight"])], bag_capacity: int) -> float:
    profit = 0.0
    cakes_sorted = sorted(cakes, key=get_cake_worth)
    for cake in cakes_sorted:
        if bag_capacity >= cake.weight:
            bag_capacity -= cake.weight
            profit += cake.price
        else:
            cake_piece = bag_capacity / cake.weight
            profit += cake.price * cake_piece
            break
    return profit


def main():
    n_cakes, bag_capacity = map(int, input().split())
    # n_cakes, bag_capacity = 5, 1000
    cake = namedtuple("cake", ["price", "weight"])
    cakes = []
    for _ in range(n_cakes):
        price, weight = map(int, input().split())
        cakes.append(cake(price, weight))
    # cakes = [cake(price=0, weight=1000), cake(price=500, weight=1000000)]
    profit = get_max_profit(cakes, bag_capacity)
    # print(cakes)
    print(f"{profit:.2f}")


if __name__ == "__main__":
    main()
