class ArraySortedBag:
    def __init__(self, source=None):
        self.items = []
        if source is not None:
            for item in source:
                self.add(item)

    def add(self, item):
        position = 0
        while position < len(self.items) and self.items[position] <= item:
            position += 1
        self.items.insert(position, item)

    def __contains__(self, item):
        low = 0
        high = len(self.items) - 1

        while low <= high:
            middle = (low + high) // 2
            if self.items[middle] == item:
                return True
            if self.items[middle] < item:
                low = middle + 1
            else:
                high = middle - 1
        return False

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)


if __name__ == "__main__":
    bag = ArraySortedBag([5, 2, 4, 1, 3, 3])
    print(list(bag))
    print(4 in bag)
    print(9 in bag)
