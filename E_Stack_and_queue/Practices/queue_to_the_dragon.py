from collections import deque


def main():
    q_left, q_right = deque(), deque()
    for _ in range(int(input())):
        char, *args = input().split()

        total_len = len(q_left) + len(q_right)
        middle_index = total_len // 2 + total_len % 2

        if middle_index > len(q_left):
            q_left.append(q_right.popleft())
        elif middle_index < len(q_left):
            q_right.appendleft(q_left.pop())

        if char == "-":
            print(q_left.popleft())
            continue

        number = int(args[0])
        if char == "+":
            q_right.append(number)
        elif char == "*":
            q_right.appendleft(number)
        elif char == "!":
            q_left.appendleft(number)


if __name__ == "__main__":
    main()
