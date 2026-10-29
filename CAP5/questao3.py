class ArrayBag:
    def __init__(self, capacity=4):
        self.items = [None] * capacity
        self.size = 0

    def add(self, item):
        if self.size == len(self.items):
            self._resize(len(self.items) * 2)

        self.items[self.size] = item
        self.size += 1

    def _resize(self, capacity):
        new_items = [None] * capacity
        for index in range(self.size):
            new_items[index] = self.items[index]
        self.items = new_items


if __name__ == "__main__":
    bag = ArrayBag()
    for value in [2, 3, 4, 5, 6, 7]:
        bag.add(value)
    print([bag.items[i] for i in range(bag.size)])
