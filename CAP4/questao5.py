class Array:
    def __init__(self, capacity, fillValue=None):
        self.items = [fillValue] * capacity
        self.fillValue = fillValue
        self.logicalSize = 0

    def insert(self, index, item):
        if self.logicalSize == len(self.items):
            self.items += [self.fillValue] * max(1, len(self.items))
        index = max(0, min(index, self.logicalSize))
        for position in range(self.logicalSize, index, -1):
            self.items[position] = self.items[position - 1]
        self.items[index] = item
        self.logicalSize += 1

    def __eq__(self, other):
        if not isinstance(other, Array) or self.logicalSize != other.logicalSize:
            return False
        for index in range(self.logicalSize):
            if self.items[index] != other.items[index]:
                return False
        return True


primeiro = Array(2)
segundo = Array(4)
for valor in (10, 20):
    primeiro.insert(primeiro.logicalSize, valor)
    segundo.insert(segundo.logicalSize, valor)
print(primeiro == segundo)
