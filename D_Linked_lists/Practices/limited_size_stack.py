from collections import deque


class LimitedSizeStack:
    __count: int
    _size_limit: int
    _container: deque

    def __init__(self, size: int):
        self.__count = 0
        self._size_limit = size
        self._container = deque([0] * size, size)

    def push(self, value: int) -> None:
        self._container.append(value)
        self.__count += 1
        self.__count = min(self.__count, self._size_limit)

    def pop(self) -> int:
        self.__count -= 1
        return self._container.pop()

    @property
    def count(self) -> int:
        return self.__count

    @property
    def size_limit(self) -> int:
        return self._size_limit


def read_file() -> list:
    results = []
    with open("input.txt", 'r') as input_file:
        size_limit = int(input_file.readline())
        stack = LimitedSizeStack(size_limit)
        for line in input_file.readlines():
            if " " in line:
                command = line.strip().split(" ")
                command, value = command[0], int(command[1])
            else:
                command = line.strip()

            if command == "push":
                stack.push(value)
                results.append("ok")
            elif command == "pop":
                results.append(str(stack.pop()))
            elif command == "count":
                results.append(str(stack.count))
            elif command == "exit":
                results.append("bye")
                break
    return results


def write_file(results: list):
    with open("output.txt", "a") as output_file:
        output_file.write("\n".join(results))


def main():
    res = read_file()
    write_file(res)


if __name__ == "__main__":
    main()
