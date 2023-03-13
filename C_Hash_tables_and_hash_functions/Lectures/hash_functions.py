class Primitive:
    values = [0, 0, 14, 99, 30, 42, 87, 71]

    @staticmethod
    def get_index_by_key(key: str) -> int:
        return len(key)

    def get_value_by_key(self, key: str) -> int:
        index = self.get_index_by_key(key)
        return self.values[index]


def main():
    primitive = Primitive()
    print(primitive.get_value_by_key("Ия"))


if __name__ == "__main__":
    main()
