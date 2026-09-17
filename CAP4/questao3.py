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


array = Array(4, 0)
array.grow()
print("Após crescer:", array.items)
array.shrink()
print("Após diminuir:", array.items)
