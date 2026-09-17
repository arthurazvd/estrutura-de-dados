class Array:
    def __init__(self, capacity, fillValue=None):
        self.items = [fillValue] * capacity
        self.logicalSize = 0

    def __len__(self):
        return len(self.items)

    def size(self):
        return self.logicalSize


array = Array(5)
print("Tamanho lógico:", array.size())
print("Capacidade:", len(array))
