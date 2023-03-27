from queue import PriorityQueue
def main():
    pq = PriorityQueue()
    while True:
        raw_command = input().split()
        command = raw_command[0]

        if command == "push":
            # push number importance
            number, importance = map(int, raw_command)
            pq.put((-importance, number))
            print("ok")
        elif "pop" in command:
            importance = int(raw_command[1])
            if importance == "top":
                # pop top
                try:
                    output = importance_queue[top_importance].popleft()
                except IndexError:
                    output = -1
                print(output)
            elif command == "popall":
                # popall importance
                try:
                    output = " ".join(importance_queue[int(importance)])
                    importance_queue[int(importance)].clear()
                except KeyError or IndexError:
                    output = -1
                print(output)
            else:
                # pop importance
                try:
                    output = importance_queue[int(importance)].popleft()
                except IndexError or KeyError:
                    output = -1
                print(output)
        elif command == "size":
            total_size = reduce(lambda a, b: a + b, [len(queue) for queue in importance_queue.values()])
            print(total_size)
        elif command == "clear":
            for queue in importance_queue.values():
                queue.clear()
            print("ok")
        elif command == "exit":
            print("bye")
            break


if __name__ == "__main__":
    main()
