class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedBag:
    def __init__(self, source=None):
        self.head = None
        self.size = 0
        self._target_node = None
        self._previous_node = None
        if source is not None:
            for item in source:
                self.add(item)

    def add(self, item):
        self.head = Node(item, self.head)
        self.size += 1

    def __contains__(self, target):
        self._target_node = None
        self._previous_node = None
        previous = None
        current = self.head
        while current is not None:
            if current.data == target:
                self._target_node = current
                self._previous_node = previous
                return True
            previous = current
            current = current.next
        return False

    def remove(self, target):
        if target not in self:
            raise KeyError(f"{target!r} not in bag")

        target_node = self._target_node
        previous_node = self._previous_node
        if previous_node is None:
            self.head = target_node.next
        else:
            previous_node.next = target_node.next

        self.size -= 1
        self._target_node = None
        self._previous_node = None

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next


if __name__ == "__main__":
    bag = LinkedBag([1, 2, 3, 2])
    bag.remove(2)
    assert len(bag) == 3 and list(bag).count(2) == 1
    bag.remove(1)
    assert 1 not in bag
    try:
        bag.remove(99)
        raise AssertionError("Deveria falhar ao remover item ausente")
    except KeyError:
        pass
    print("Questão 10: testes OK")
