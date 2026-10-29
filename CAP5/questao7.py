class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedSet:
    def __init__(self, source=None):
        self.items = None
        self.size = 0
        if source is not None:
            for item in source:
                self.add(item)

    def add(self, item):
        if item in self:
            return
        self.items = Node(item, self.items)
        self.size += 1

    def __contains__(self, item):
        current = self.items
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.items
        while current is not None:
            yield current.data
            current = current.next


if __name__ == "__main__":
    conjunto = LinkedSet([1, 2, 2, 3])
    conjunto.add(3)
    conjunto.add(4)
    print(list(conjunto))
