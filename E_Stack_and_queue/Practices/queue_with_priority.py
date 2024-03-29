from collections import deque, namedtuple


def process_push(pq: deque, current_item: namedtuple) -> None:
    index_to_insert = 10 ** 7
    for index, elem in enumerate(pq):
        if elem.importance < current_item.importance:
            index_to_insert = index
            break
    pq.insert(index_to_insert, current_item)


def process_pop_importance(pq: deque, importance: int) -> int:
    try:
        importance_objects = filter(lambda x: x.importance == importance, pq)
        item_to_delete = next(importance_objects)
        output = item_to_delete.number
        pq.remove(item_to_delete)
    except StopIteration:
        output = -1
    return output


def process_popall_importance(pq: deque, importance: int) -> str or int:
    output_numbers = []
    for elem in pq:
        if elem.importance == importance:
            output_numbers.append(elem.number)

    if output_numbers:
        output = " ".join(map(str, output_numbers))
    else:
        output = -1
    return output


def main():
    pq = deque()
    item = namedtuple("item", ["number", "importance"])

    while True:
        command, *args = input().split()

        if command == "push":
            number, importance = map(int, args)
            current_item = item(number, importance)
            process_push(pq, current_item)
            print("ok")

        if command == "pop":
            if args[0] == "top":
                output = -1 if len(pq) == 0 else pq.popleft().number
                print(output)

            else:
                importance = int(args[0])
                output = process_pop_importance(pq, importance)
                print(output)

        elif command == "popall":
            importance = int(args[0])
            output = process_popall_importance(pq, importance)
            pq = deque(filter(lambda x: x.importance != importance, pq))
            print(output)

        elif command == "size":
            print(len(pq))

        elif command == "clear":
            pq.clear()
            print("ok")

        elif command == "exit":
            print("bye")
            break


if __name__ == "__main__":
    main()
