class Array:
    def __init__(self, capacity, fillValue=None):
        if capacity < 1:
            raise ValueError("A capacidade deve ser positiva")
        self.items = [fillValue] * capacity
        self.fillValue = fillValue
        self.logicalSize = 0
        self.initialCapacity = capacity

    def __len__(self):
        return len(self.items)

    def size(self):
        return self.logicalSize

    def grow(self):
        self.items += [self.fillValue] * len(self.items)

    def shrink(self):
        nova_capacidade = max(self.initialCapacity, len(self.items) // 2)
        if nova_capacidade >= self.logicalSize:
            self.items = self.items[:nova_capacidade]

    def insert(self, index, item):
        if self.logicalSize == len(self.items):
            self.grow()
        index = max(0, min(index, self.logicalSize))
        for position in range(self.logicalSize, index, -1):
            self.items[position] = self.items[position - 1]
        self.items[index] = item
        self.logicalSize += 1

    def pop(self, index):
        if index < 0 or index >= self.logicalSize:
            raise IndexError("Índice fora do tamanho lógico do array")
        item = self.items[index]
        for position in range(index, self.logicalSize - 1):
            self.items[position] = self.items[position + 1]
        self.logicalSize -= 1
        self.items[self.logicalSize] = self.fillValue
        if self.logicalSize <= len(self.items) // 4:
            self.shrink()
        return item


array = Array(2)
array.insert(0, "A")
array.insert(1, "C")
array.insert(1, "B")
print(array.items, "removido:", array.pop(1))
print(array.items)
