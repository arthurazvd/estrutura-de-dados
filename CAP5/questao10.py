class ArrayBag:
    def __init__(self, source=None):
        self.items = list(source) if source is not None else []
        self.modCount = 0

    def add(self, item):
        self.items.append(item)
        self.modCount += 1

    def remove(self, item):
        self.items.remove(item)
        self.modCount += 1

    def clear(self):
        self.items.clear()
        self.modCount += 1

    def __iter__(self):
        expected_mod_count = self.modCount
        index = 0

        while index < len(self.items):
            item = self.items[index]
            yield item
            if self.modCount != expected_mod_count:
                raise RuntimeError("A bag foi modificada durante a iteracao")
            index += 1


if __name__ == "__main__":
    bag = ArrayBag([1, 2, 3])

    try:
        for item in bag:
            print(item)
            if item == 1:
                bag.add(4)
    except RuntimeError as error:
        print(error)
