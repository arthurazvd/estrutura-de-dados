class ArraySortedBag:
    def __init__(self, source=None):
        self.items = sorted(source) if source is not None else []

    def add(self, item):
        position = 0
        while position < len(self.items) and self.items[position] <= item:
            position += 1
        self.items.insert(position, item)

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, ArraySortedBag):
            return False
        if len(self.items) != len(other.items):
            return False
        return all(a == b for a, b in zip(self.items, other.items))

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)


if __name__ == "__main__":
    a = ArraySortedBag([3, 1, 2, 2])
    b = ArraySortedBag([2, 3, 1, 2])
    c = ArraySortedBag([1, 2, 3])
    assert a == b
    assert not (a == c)
    assert a == a
    print("Questão 1: testes OK")
