profundidade = 3
linhas = 4
colunas = 4
array3d = [[[0 for column in range(colunas)] for row in range(linhas)] for depth in range(profundidade)]

for depth in range(profundidade):
    for row in range(linhas):
        for column in range(colunas):
            array3d[depth][row][column] = depth * 100 + row * 10 + column

print(array3d[2][3][3])
