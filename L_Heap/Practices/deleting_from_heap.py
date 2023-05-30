class Heap:
    items: list

    def __init__(self):
        self.items = []

    def get_size(self) -> int:
        return len(self.items)

    def get_min(self) -> int:
        return self.items[0]

    def add(self, item: int) -> None:
        self.items.append(item)
        self.sift_up(self.get_size() - 1)

    def pop(self) -> int:
        root = self.get_min()
        min_item = self.items.pop()
        if self.items:
            self.items[0] = min_item
            self.sift_down(0)
        return root

    def sift_up(self, index: int) -> None:
        while index > 0:
            parent_index = (index - 1) // 2
            if self.items[parent_index] <= self.items[index]:
                return
            self.items[parent_index], self.items[index] = self.items[index], self.items[parent_index]
            index = parent_index

    def sift_down(self, index: int) -> None:
        while 2 * index + 1 < self.get_size():
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            if right_child_index < self.get_size() and self.items[right_child_index] < self.items[left_child_index]:
                left_child_index = right_child_index
            if self.items[index] <= self.items[left_child_index]:
                return
            self.items[index], self.items[left_child_index] = self.items[left_child_index], self.items[index]
            index = left_child_index

    def print(self) -> None:
        print("---STRUCTURE START---")
        index, step = 0, 1
        size = self.get_size()
        while index < size:
            line = [self.items[i] for i in range(index, min(index + step, size))]
            index += step
            step *= 2
            print(" ".join(map(str, line)))
        print("---STRUCTURE END---")


def main():
    heap = Heap()
    while True:
        command, *args = input().split()
        if command == "exit":
            print("bye")
            break
        elif command == "add":
            item = int(args[0])
            heap.add(item)
            print("ok")
        elif command == "min":
            print(heap.get_min())
        elif command == "size":
            print(heap.get_size())
        elif command == "pop":
            print(heap.pop())
        elif command == "structure":
            heap.print()


if __name__ == "__main__":
    main()
