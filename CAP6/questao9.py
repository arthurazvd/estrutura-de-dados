class ArrayBag:
    def __init__(self, source=None):
        self.items = []
        self.size = 0
        self.position = -1
        if source is not None:
            for item in source:
                self.add(item)

    def add(self, item):
        self.items.append(item)
        self.size += 1

    def __contains__(self, target):
        self.position = -1
        for index in range(self.size):
            if self.items[index] == target:
                self.position = index
                return True
        return False

    def remove(self, target):
        if target not in self:
            raise KeyError(f"{target!r} not in bag")
        index = self.position
        self.items[index] = self.items[self.size - 1]
        self.items.pop()
        self.size -= 1
        self.position = -1

    def __len__(self):
        return self.size

    def __iter__(self):
        return iter(self.items)


class ArraySortedBag(ArrayBag):
    def __init__(self, source=None):
        super().__init__()
        if source is not None:
            for item in source:
                self.add(item)

    def add(self, item):
        low, high = 0, self.size
        while low < high:
            middle = (low + high) // 2
            if self.items[middle] <= item:
                low = middle + 1
            else:
                high = middle
        self.items.insert(low, item)
        self.size += 1

    def __contains__(self, target):
        low, high = 0, self.size - 1
        self.position = -1
        while low <= high:
            middle = (low + high) // 2
            if self.items[middle] == target:
                self.position = middle
                return True
            if self.items[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        return False

    def remove(self, target):
        if target not in self:
            raise KeyError(f"{target!r} not in bag")
        self.items.pop(self.position)
        self.size -= 1
        self.position = -1


if __name__ == "__main__":
    bag = ArraySortedBag([5, 1, 3, 3, 2])
    bag.remove(3)
    assert list(bag) == [1, 2, 3, 5]
    assert 3 in bag and 8 not in bag
    print("Questão 9: testes OK")
