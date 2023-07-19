def hanoi(n: int, move_from: str, move_to: str, aux: str) -> None:
    if n == 1:
        print(f"Move from {move_from} to {move_to}")
        return
    hanoi(n - 1, move_from, aux, move_to)
    print(f"Move from {move_from} to {move_to}")
    hanoi(n - 1, aux, move_to, move_from)


def main():
    hanoi(10, "First", "Second", "Third")


if __name__ == "__main__":
    main()
