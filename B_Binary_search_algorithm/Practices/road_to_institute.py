class Point:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_point(self, other) -> float:
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5


def d_f(x: float, a: float, v_out: int, v_in: int) -> float:
    return (v_out * x) / ((x ** 2 + (1 - a) ** 2) ** 0.5) + (v_in * (x - 1)) / (((1 - x) ** 2 + a ** 2) ** 0.5)


def f(current_pos: Point, v_outside: int, v_inside: int) -> float:
    outside_point, inside_point = Point(0, 1), Point(1, 0)
    outside_distance = outside_point.distance_to_point(current_pos)
    inside_distance = inside_point.distance_to_point(current_pos)
    outside_time = outside_distance / v_outside
    inside_time = inside_distance / v_inside
    return outside_time + inside_time


def get_x_coordinate(v_out: int, v_in: int, a: float) -> float:
    outside_point, inside_point = Point(0, 1), Point(1, 0)
    root = None
    left, right = outside_point.x, inside_point.x
    eps = 10 ** -6
    while abs(d_f(right, a, v_out, v_in) - d_f(left, a, v_out, v_in)) > eps:
        mid = (left + right) / 2
        if d_f(mid, a, v_out, v_in) == 0 or abs(d_f(mid, a, v_out, v_in)) < eps:
            root = mid
            break
        elif d_f(left, a, v_out, v_in) * d_f(mid, a, v_out, v_in) < 0:
            right = mid
        else:
            left = mid
    return abs(1 - root)


def main():
    v_outside, v_inside = 5, 3  # map(int, input().split())

    s_percentage = 60  # int(input())
    print(v_outside, v_inside, s_percentage)
    a = s_percentage / 100
    x = get_x_coordinate(v_outside, v_inside, a)

    print(f"{x:.0{6}f}")


if __name__ == "__main__":
    main()
