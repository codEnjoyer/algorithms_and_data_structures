class Heap:
    items: list

    def __init__(self):
        self.items = []

    def get_size(self) -> int:
        return len(self.items)

    def get_min(self) -> int:
        return self.items[0]

    def add(self, value: int) -> None:
        self.items.append(value)
        self.sift_up(self.get_size() - 1)

    def sift_up(self, index: int) -> None:
        """
        At start, we have an index of the element that we want to sift up. Then we find the index of its parent. After
        that we compare the value of the element with the value of its parent. If the value of the element is less than
        the value of its parent, then we swap them. We repeat this process until the value of the element is greater
        than the value of its parent or until we reach the root of the heap.
        :param index: It is an index of the element that we want to sift up
        :return:
        """

        while index > 0:
            parent_index = (index - 1) // 2
            if self.items[parent_index] <= self.items[index]:
                return
            self.items[parent_index], self.items[index] = self.items[index], self.items[parent_index]
            index = parent_index


def main():
    heap = Heap()
    while True:
        command, *args = input().split()
        if command == "exit":
            print("bye")
            break
        elif command == "add":
            value = int(args[0])
            heap.add(value)
            print("ok")
        elif command == "min":
            print(heap.get_min())
        elif command == "size":
            print(heap.get_size())


if __name__ == "__main__":
    main()
