from collections import namedtuple
from typing import List


def readline() -> (int, int):
    return tuple(map(int, input().split()))


def find_meal(money: int, menu: List[namedtuple("meal", ["price", "caloric"])], taken_meals: List[int],
              caloric: int = 0, n: int = 0):
    global final_order, final_caloric

    if n == len(menu) or money == 0:
        if caloric > final_caloric or (caloric == final_caloric and len(taken_meals) > len(final_order)):
            final_caloric = caloric
            final_order = taken_meals[:]
        return

    if money >= menu[n].price:
        find_meal(money - menu[n].price, menu, taken_meals + [n + 1], caloric + menu[n].caloric, n + 1)

    find_meal(money, menu, taken_meals[:], caloric, n + 1)


def main():
    meal = namedtuple("meal", ["price", "caloric"])
    meals_count, money = readline()
    # meals_count, money = 5, 100
    # meals = [meal(price=100, caloric=500), meal(price=50, caloric=250),
    #          meal(price=50, caloric=250),
    #          meal(price=50, caloric=250), meal(price=50, caloric=250)]
    menu = []
    for _ in range(meals_count):
        meal_description = readline()
        menu.append(meal(price=meal_description[0], caloric=meal_description[1]))

    find_meal(money, menu, [])
    print(len(final_order), final_caloric)
    print(*final_order)


if __name__ == "__main__":
    final_order, final_caloric = [], 0
    main()
