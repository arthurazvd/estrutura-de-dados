class ArrayBag:
    def __init__(self, capacity=4):
        self.items = [None] * capacity
        self.size = 0

    def add(self, item):
        if self.size == len(self.items):
            self._resize(len(self.items) * 2)
        self.items[self.size] = item
        self.size += 1

    def remove(self, item):
        for index in range(self.size):
            if self.items[index] == item:
                for next_index in range(index, self.size - 1):
                    self.items[next_index] = self.items[next_index + 1]

                self.size -= 1
                self.items[self.size] = None

                if len(self.items) > 4 and self.size <= len(self.items) // 4:
                    self._resize(max(4, len(self.items) // 2))
                return

        raise KeyError(str(item) + " not in bag")

    def _resize(self, capacity):
        new_items = [None] * capacity
        for index in range(self.size):
            new_items[index] = self.items[index]
        self.items = new_items


if __name__ == "__main__":
    bag = ArrayBag()
    for value in range(8):
        bag.add(value)
    bag.remove(3)
    print([bag.items[i] for i in range(bag.size)])
    print("Capacidade:", len(bag.items))
