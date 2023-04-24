from __future__ import annotations
from functools import total_ordering
from typing import List, Tuple
from heapq import heappush, heappop


@total_ordering
class Box:
    weight: int
    lifts: int

    def __init__(self, weight: int, lifts: int):
        self.weight = weight
        self.lifts = lifts

    def _is_valid_operand(self, other: Box):
        return hasattr(other, "weight") and hasattr(other, "lifts")

    def __eq__(self, other: Box):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.weight, self.lifts) == (other.weight, other.lifts)

    def __lt__(self, other: Box):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.lifts + self.weight) < (other.lifts + other.weight)

    def __str__(self):
        return f"{type(self).__name__} with weight = {self.weight} and lifting capacity = {self.lifts}"

    def __repr__(self):
        return f"{type(self).__name__}({self.weight}, {self.lifts})"


def solve(boxes: List[Box]) -> int:
    if not boxes:
        raise ValueError
    boxes_sorted = sorted(boxes)
    pq: List[Tuple[int, Box]] = []
    sum_weight, counter = 0, 0
    for i in range(len(boxes_sorted) - 1):
        if boxes_sorted[i].lifts >= sum_weight:
            counter += 1
            sum_weight += boxes_sorted[i].weight
            heappush(pq, (boxes_sorted[i].weight - boxes_sorted[i + 1].weight, boxes_sorted[i]))
        elif pq[0][1].weight > boxes_sorted[i].weight:
            box_to_swap = heappop(pq)[1]
            sum_weight -= box_to_swap.weight
            heappush(pq, (boxes_sorted[i].weight - box_to_swap.weight, boxes_sorted[i]))
            sum_weight += boxes_sorted[i].weight

    return counter


def main():
    # оно не работает, но я пытался :)
    boxes: List[Box] = [Box(1, 1), Box(2, 2), Box(3, 3)]
    max_boxes_count = solve(boxes)
    print(max_boxes_count)


if __name__ == "__main__":
    main()
