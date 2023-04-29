from typing import List
from collections import namedtuple


def solve(gymnasts: List[namedtuple("gymnast", ["lifts", "weight"])]) -> int:
    gymnasts.sort(key=lambda g: ((g.weight + g.lifts), g.weight))
    tower = []
    sum_weight, counter = 0, 0
    for gymnast in gymnasts:
        if gymnast.lifts >= sum_weight:
            counter += 1
            sum_weight += gymnast.weight
            tower.append(gymnast)
            tower.sort(key=lambda g: g.weight)
        elif tower[-1].weight > gymnast.weight:
            sum_weight -= tower.pop().weight
            tower.append(gymnast)
            tower.sort(key=lambda g: g.weight)
            sum_weight += gymnast.weight
    return counter


def main():
    gymnast = namedtuple("gymnast", ["lifts", "weight"])
    # region 15 тест
    # gymnasts = [gymnast(lifts=17, weight=27), gymnast(lifts=26, weight=22), gymnast(lifts=19, weight=44),
    #             gymnast(lifts=54, weight=11), gymnast(lifts=13, weight=56), gymnast(lifts=37, weight=33),
    #             gymnast(lifts=49, weight=22), gymnast(lifts=11, weight=60), gymnast(lifts=55, weight=18),
    #             gymnast(lifts=30, weight=45), gymnast(lifts=63, weight=16), gymnast(lifts=13, weight=66),
    #             gymnast(lifts=52, weight=30), gymnast(lifts=39, weight=43), gymnast(lifts=71, weight=11),
    #             gymnast(lifts=41, weight=42), gymnast(lifts=36, weight=47), gymnast(lifts=10, weight=77),
    #             gymnast(lifts=59, weight=29), gymnast(lifts=75, weight=15), gymnast(lifts=13, weight=80),
    #             gymnast(lifts=63, weight=31), gymnast(lifts=85, weight=10), gymnast(lifts=36, weight=61),
    #             gymnast(lifts=26, weight=72), gymnast(lifts=52, weight=47), gymnast(lifts=83, weight=17),
    #             gymnast(lifts=13, weight=90), gymnast(lifts=83, weight=21), gymnast(lifts=32, weight=72),
    #             gymnast(lifts=82, weight=23), gymnast(lifts=68, weight=41), gymnast(lifts=50, weight=59),
    #             gymnast(lifts=35, weight=77), gymnast(lifts=67, weight=45), gymnast(lifts=25, weight=87),
    #             gymnast(lifts=81, weight=33), gymnast(lifts=16, weight=98), gymnast(lifts=75, weight=39),
    #             gymnast(lifts=42, weight=73), gymnast(lifts=43, weight=73), gymnast(lifts=90, weight=27),
    #             gymnast(lifts=35, weight=83), gymnast(lifts=66, weight=56), gymnast(lifts=65, weight=60),
    #             gymnast(lifts=69, weight=57), gymnast(lifts=96, weight=30), gymnast(lifts=39, weight=89),
    #             gymnast(lifts=83, weight=46), gymnast(lifts=75, weight=55), gymnast(lifts=60, weight=72),
    #             gymnast(lifts=70, weight=62), gymnast(lifts=40, weight=94), gymnast(lifts=70, weight=66),
    #             gymnast(lifts=36, weight=100), gymnast(lifts=68, weight=73), gymnast(lifts=43, weight=100),
    #             gymnast(lifts=81, weight=64), gymnast(lifts=68, weight=89), gymnast(lifts=93, weight=74),
    #             gymnast(lifts=89, weight=82), gymnast(lifts=75, weight=100), gymnast(lifts=78, weight=97),
    #             gymnast(lifts=99, weight=78), gymnast(lifts=91, weight=89)]
    # endregion 15 тест
    gymnasts = []
    for _ in range(int(input())):
        line = input().split(';')
        gymnasts.append(gymnast(lifts=int(line[1]), weight=int(line[2])))
    res = solve(gymnasts)
    print(res)


if __name__ == "__main__":
    main()
