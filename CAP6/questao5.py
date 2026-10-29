class AbstractCollection:
    def __init__(self, source=None):
        self.size = 0
        if source is not None:
            for item in source:
                self.add(item)

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __contains__(self, target):
        return any(item == target for item in self)

    def add(self, item):
        raise NotImplementedError


class AbstractBag(AbstractCollection):
    pass


class ArrayBag(AbstractBag):
    def __init__(self, source=None):
        self.items = []
        super().__init__(source)

    def add(self, item):
        self.items.append(item)
        self.size += 1

    def __iter__(self):
        return iter(self.items)


class ArraySet(ArrayBag):
    def add(self, item):
        if item not in self.items:
            self.items.append(item)
            self.size += 1


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedBag(AbstractBag):
    def __init__(self, source=None):
        self.head = None
        super().__init__(source)

    def add(self, item):
        self.head = Node(item, self.head)
        self.size += 1

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


class LinkedSet(LinkedBag):
    def add(self, item):
        if item not in self:
            self.head = Node(item, self.head)
            self.size += 1


if __name__ == "__main__":
    array_set = ArraySet([1, 2, 2, 3])
    array_set.add(3)
    assert list(array_set) == [1, 2, 3]
    assert len(array_set) == 3

    linked_set = LinkedSet([1, 2, 2, 3])
    linked_set.add(3)
    assert len(linked_set) == 3
    assert set(linked_set) == {1, 2, 3}
    print("Questão 5: testes OK")
