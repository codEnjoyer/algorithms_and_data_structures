class DynamicArray:
    values = [0] * 8
    size = 8
    current_index = 0

    class KeyValuePair:
        key: str
        value: str

        def __init__(self, key: str, value: str):
            self.key = key
            self.value = value

    def add(self, value: int) -> None:
        self.values[self.current_index] = value
        self.current_index += 1
        if self.current_index > self.size:
            self.resize(self.size * 2)

    def resize(self, new_size: int) -> None:
        new_values = [0] * new_size
        for i in range(new_size):
            new_values[i] = self.values[i]
        self.values = new_values
        self.size = new_size


def main():
    pass

if __name__ == "__main__":
    main()
