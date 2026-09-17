class Grid:
    def __init__(self, rows, columns, fillValue=0):
        self.data = [[fillValue for column in range(columns)] for row in range(rows)]

    def getHeight(self):
        return len(self.data)

    def getWidth(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        return "\n".join(" ".join(str(item) for item in row) for row in self.data)


class Matrix(Grid):
    def _same_size(self, other):
        return self.getHeight() == other.getHeight() and self.getWidth() == other.getWidth()

    def __add__(self, other):
        if not self._same_size(other):
            raise ValueError("As matrizes devem ter as mesmas dimensões")
        result = Matrix(self.getHeight(), self.getWidth())
        for row in range(self.getHeight()):
            for column in range(self.getWidth()):
                result[row][column] = self[row][column] + other[row][column]
        return result

    def __sub__(self, other):
        if not self._same_size(other):
            raise ValueError("As matrizes devem ter as mesmas dimensões")
        result = Matrix(self.getHeight(), self.getWidth())
        for row in range(self.getHeight()):
            for column in range(self.getWidth()):
                result[row][column] = self[row][column] - other[row][column]
        return result

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Matrix(self.getHeight(), self.getWidth())
            for row in range(self.getHeight()):
                for column in range(self.getWidth()):
                    result[row][column] = self[row][column] * other
            return result
        if self.getWidth() != other.getHeight():
            raise ValueError("Dimensões incompatíveis para multiplicação")
        result = Matrix(self.getHeight(), other.getWidth())
        for row in range(self.getHeight()):
            for column in range(other.getWidth()):
                for index in range(self.getWidth()):
                    result[row][column] += self[row][index] * other[index][column]
        return result


a = Matrix(2, 2)
b = Matrix(2, 2)
a[0][:], a[1][:] = [1, 2], [3, 4]
b[0][:], b[1][:] = [5, 6], [7, 8]
print("Soma:\n", a + b, sep="")
print("Multiplicação:\n", a * b, sep="")
