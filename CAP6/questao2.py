class AbstractBag:
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

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, AbstractBag) or len(self) != len(other):
            return False
        unmatched = list(other)
        for item in self:
            try:
                unmatched.remove(item)
            except ValueError:
                return False
        return not unmatched


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
        while current is not None:
            yield current.data
            current = current.next


if __name__ == "__main__":
    bag = LinkedBag([1, 2, 2])
    assert len(bag) == 3
    assert 2 in bag and 9 not in bag
    assert bag == LinkedBag([2, 1, 2])
    print("Questão 2: testes OK")
