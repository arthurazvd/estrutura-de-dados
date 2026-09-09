problemSize = int(input("Digite o tamanho do problema: "))

count = 0

while problemSize > 0:
    problemSize = problemSize // 2
    count += 1

print("Número de iterações:", count)