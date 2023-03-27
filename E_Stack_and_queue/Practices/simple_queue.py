from collections import deque


def process_input(q: deque) -> bool:
    raw_command = input().split()
    command = raw_command[0]
    if len(raw_command) == 2:
        q.append(raw_command[1])
        print("ok")
    elif command == "pop":
        print(q.popleft())
    elif command == "front":
        print(q[0])
    elif command == "size":
        print(len(q))
    elif command == "view":
        print(", ".join(q))
    elif command == "clear":
        q.clear()
        print("ok")
    elif command == "exit":
        print("bye")
        return False
    return True


def main():
    q = deque()
    is_ongoing = True
    while is_ongoing:
        is_ongoing = process_input(q)


if __name__ == "__main__":
    main()
