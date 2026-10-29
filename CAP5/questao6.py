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


if __name__ == "__main__":
    conjunto = ArraySet([1, 2, 2, 3])
    conjunto.add(3)
    conjunto.add(4)
    print(list(conjunto))
