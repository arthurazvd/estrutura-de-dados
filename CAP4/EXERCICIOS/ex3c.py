grid = [[4, 7, 2], [8, -3, 5], [1, 6, 9]]

row = len(grid)
column = len(grid[0])
encontrado = False

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] < 0:
            row = r
            column = c
            encontrado = True
            break
    if encontrado:
        break

print("Posição:", row, column)
