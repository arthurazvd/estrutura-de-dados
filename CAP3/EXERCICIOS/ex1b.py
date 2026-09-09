problemSizes = [1000, 2000, 4000, 10000, 100000]

print("%12s%16s" % ("Problem Size", "Iterations"))

for problemSize in problemSizes:
    originalSize = problemSize
    count = 0

    while problemSize > 0:
        problemSize = problemSize // 2
        count += 1

    print("%12d%16d" % (originalSize, count))


#   Quando o tamanho do problema dobra, o número de iterações aumenta apenas 1 aproximadamente. 
#   Quando o tamanho aumenta por um fator de 10, o número de iterações aumenta aproximadamente 3 ou 4. 
#   Então o número de iterações cresce de forma logarítmica em relação ao tamanho do problema.