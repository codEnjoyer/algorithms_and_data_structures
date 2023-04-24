from __future__ import annotations
from functools import total_ordering
from typing import List


@total_ordering
class Segment:
    left: int
    right: int

    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right

    def _is_valid_operand(self, other: Segment):
        return hasattr(other, "left") and hasattr(other, "right")

    def __eq__(self, other: Segment):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.left, self.right) == (other.left, other.right)

    def __lt__(self, other: Segment):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.right, self.left) < (other.right, other.left)

    def __str__(self):
        return f"{type(self).__name__} with left border = {self.left}, right border = {self.right}"

    def __repr__(self):
        return f"{type(self).__name__}({self.left}, {self.right})"


def solve(segments: List[Segment]) -> int:
    if not segments:
        raise ValueError
    segments_sorted = sorted(segments)
    last_right = segments_sorted[0].left
    answer = 0
    for segment in segments_sorted:
        if segment.left >= last_right:
            answer += 1
            last_right = segment.right
    return answer


def main():
    segments: List[Segment] = [Segment(2, 4), Segment(1, 5), Segment(2, 3), Segment(1, 5),
                               Segment(1, 2), Segment(2, 3), Segment(3, 4), Segment(6, 7),
                               Segment(1, 9), Segment(4, 9)]
    print(segments[0])
    print(segments)
    max_segments_count = solve(segments)
    print(max_segments_count)


if __name__ == "__main__":
    main()
