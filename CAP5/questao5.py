class ArrayBag:
    def __init__(self, source=None):
        self.items = list(source) if source is not None else []

    def clone(self):
        return ArrayBag(self.items)


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedBag:
    def __init__(self, source=None):
        self.items = None
        if source is not None:
            for item in source:
                self.add(item)

    def add(self, item):
        self.items = Node(item, self.items)

    def __iter__(self):
        current = self.items
        while current is not None:
            yield current.data
            current = current.next

    def clone(self):
        return LinkedBag(list(self))


if __name__ == "__main__":
    bag1 = ArrayBag([2, 3, 4])
    bag2 = bag1.clone()
    print(list(bag1.items) == list(bag2.items))
    print(bag1 is bag2)

    linked1 = LinkedBag([2, 3, 4])
    linked2 = linked1.clone()
    print(list(linked1) == list(linked2))
    print(linked1 is linked2)
