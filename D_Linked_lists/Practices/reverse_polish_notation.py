from typing import List, Dict, Callable


def compute(line: List[str], operations: Dict[str, Callable]) -> int:
    stack = []
    for char in line:
        if char.isdigit():
            stack.append(int(char))
        elif char in operations:
            stack.append(operations[char](stack.pop(), stack.pop()))
        else:
            raise ValueError
    return stack.pop()


def main():
    line = input().split()
    char_operations = {
        "+": lambda y, x: x + y,
        "-": lambda y, x: x - y,
        "*": lambda y, x: x * y,
        "/": lambda y, x: x // y,
        "%": lambda y, x: x % y
    }
    result = compute(line, char_operations)
    print(result)


if __name__ == "__main__":
    main()
