from llist import dllist


def main():
    q_left = deque()
    q_right = deque()
    for line_num in range(int(input())):
        raw_command = input().split()
        if len(raw_command) == 1:
            q_not_empty = q_left if len(q_left) else q_right
            q_not_empty.popleft()
            continue
        char, number = raw_command[0], int(raw_command[1])
        if char == "+":
            q_right.append(number)
        elif char == "*":
            index_to_insert = (len(q_left) + len(q_right)) // 2 + 1
            if index_to_insert >= len(q_left):
                q_right.insert(index_to_insert - len(q_left) - 1, number)
            else:
                q_left.append(number)
        elif char == "!":
            q_left.appendleft(number)
        print(q_left, q_right, sep="\n")


if __name__ == "__main__":
    main()
