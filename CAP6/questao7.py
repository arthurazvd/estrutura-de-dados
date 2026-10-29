class ArraySet:
    def __init__(self, source=None):
        self.items = []
        if source is not None:
            for item in source:
                self.add(item)

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def __contains__(self, item):
        return item in self.items

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)


class ArraySortedSet(ArraySet):
    def add(self, item):
        if item in self:
            return
        low, high = 0, len(self.items)
        while low < high:
            middle = (low + high) // 2
            if self.items[middle] < item:
                low = middle + 1
            else:
                high = middle
        self.items.insert(low, item)

    def __contains__(self, item):
        low, high = 0, len(self.items) - 1
        while low <= high:
            middle = (low + high) // 2
            if self.items[middle] == item:
                return True
            if self.items[middle] < item:
                low = middle + 1
            else:
                high = middle - 1
        return False


if __name__ == "__main__":
    values = ArraySortedSet([5, 2, 4, 2, 1, 3])
    assert list(values) == [1, 2, 3, 4, 5]
    assert 4 in values
    assert 8 not in values
    values.add(3)
    assert len(values) == 5
    print("Questão 7: testes OK")
