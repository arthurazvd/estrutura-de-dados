array3d = [
    [[0, 1], [10, 11]],
    [[100, 101], [110, 111]],
    [[200, 201], [210, 211]],
]

for row in range(len(array3d[0])):
    for column in range(len(array3d[0][row])):
        for depth in range(len(array3d)):
            print(array3d[depth][row][column], end=" ")
        print()
