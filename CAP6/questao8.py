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


if __name__ == "__main__":
    bag = ArrayBag([10, 20, 30, 20])
    bag.remove(20)
    assert len(bag) == 3 and 20 in bag
    bag.remove(10)
    assert len(bag) == 2
    try:
        bag.remove(99)
        raise AssertionError("Deveria falhar ao remover item ausente")
    except KeyError:
        pass
    print("Questão 8: testes OK")
