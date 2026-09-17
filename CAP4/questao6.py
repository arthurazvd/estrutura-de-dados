class Array:
    def __init__(self, capacity, fillValue=None):
        self.items = [fillValue] * capacity
        self.logicalSize = 0

    def __len__(self):
        return self.logicalSize

    def __getitem__(self, index):
        if index < 0 or index >= self.logicalSize:
            raise IndexError
        return self.items[index]

    def __str__(self):
        return str(self.items[:self.logicalSize])

    def append(self, item):
        if self.logicalSize == len(self.items):
            self.items += [None] * max(1, len(self.items))
        self.items[self.logicalSize] = item
        self.logicalSize += 1


array = Array(4)
array.append("A")
array.append("B")
print(array)
for item in array:
    print(item)

print("O __iter__ pode ser removido porque __getitem__ permite a iteração pela sequência. O __str__ deve exibir apenas os itens até o tamanho lógico.")
