from typing import List


def get_max_coins(city: List[List[int]], height: int, width: int) -> int:
    coins_sum = city[:]

    def _fill_top_coins_row() -> None:
        for i in range(1, width):
            coins_sum[0][i] = coins_sum[0][i - 1] + city[0][i]

    def _fill_left_coins_column() -> None:
        for i in range(1, height):
            coins_sum[i][0] = coins_sum[i - 1][0] + city[i][0]

    def _fill_coins_sum() -> None:
        for i in range(1, height):
            for j in range(1, width):
                coins_sum[i][j] = max(coins_sum[i - 1][j], coins_sum[i][j - 1]) + city[i][j]

    _fill_top_coins_row()
    _fill_left_coins_column()
    _fill_coins_sum()

    return coins_sum[height - 1][width - 1]


def main():
    height, width = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(height)]
    print(get_max_coins(city, height, width))


if __name__ == "__main__":
    main()
