matrix = [[None for column in range(3)] for row in range(3)]

for row in range(3):
    for column in range(3):
        matrix[row][column] = row * column

for linha in matrix:
    print(linha)
