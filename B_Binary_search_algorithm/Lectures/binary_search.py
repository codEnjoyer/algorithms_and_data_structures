# region Basic realization
from typing import List


def binary_search(array: list, search: int) -> int:
    """Finds index of "search" in "array" via binary search algorithm."""
    left_border, right_border = 0, len(array) - 1
    middle = (left_border + right_border) // 2
    while left_border <= right_border:
        if array[middle] < search:
            left_border = middle + 1
        elif array[middle] > search:
            right_border = middle - 1
        else:
            return middle
    return -1


# endregion

# region Removing duplicates
def remove_element_at_index(array: list, index: int) -> int:
    """Removes element at index "index" from "array"."""
    for i in range(index + 1, len(array)):
        array[i - 1] = array[i]
    return len(array) - 1


def remove_duplicates(array: list) -> int:
    """Removes duplicates from list "array"."""
    length = len(array)
    i = 0
    while i < length:
        is_found_duplicate = False
        for k in range(i + 1, length):
            if array[i] == array[k]:
                is_found_duplicate = True
                break
        if is_found_duplicate:
            remove_element_at_index(array, i)
        else:
            i += 1
            length -= 1
    return length


# endregion

# region Searching for spot to insert
class Player:
    rating: int
    nickname: str

    def __init__(self, rating: int, nickname: str):
        self.rating = rating
        self.nickname = nickname

    def __str__(self):
        return f"Nickname: \"{self.nickname}\", rating: {self.rating}"

    def __repr__(self):
        return self.__str__()


def find_spot_to_insert(array: List[Player], player: Player) -> int:
    left, right = 0, len(array)
    while left < right:
        middle = (left + right) // 2
        if array[middle].rating < player.rating:
            left = middle + 1
        else:
            right = middle
    return left


# endregion

def main():
    numbers = [0, 1, 2, 3, 4]
    remove_element_at_index(numbers, 3)
    remove_element_at_index(numbers, 1)
    print(numbers)

    players = [Player(1000, 'a'), Player(1300, 'b'), Player(1500, 'c'),
               Player(1600, 'd'), Player(1600, 'e'), Player(3000, 'f')]
    new_player = Player(1600, 'g')

    spot_index = find_spot_to_insert(players, new_player)
    print(spot_index)

    players.insert(spot_index, new_player)
    print("\n".join(map(str, players)))


if __name__ == "__main__":
    main()
