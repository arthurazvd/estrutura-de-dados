class Array:
    def __init__(self, capacity, fillValue=None):
        self.items = [fillValue] * capacity
        self.logicalSize = 0

    def __len__(self):
        return len(self.items)

    def size(self):
        return self.logicalSize

    def __getitem__(self, index):
        if index < 0 or index >= self.logicalSize:
            raise IndexError("Índice fora do tamanho lógico do array")
        return self.items[index]

    def __setitem__(self, index, newItem):
        if index < 0 or index >= self.logicalSize:
            raise IndexError("Índice fora do tamanho lógico do array")
        self.items[index] = newItem


array = Array(3)
array.logicalSize = 2
array[0] = "A"
array[1] = "B"
print(array[0], array[1])
