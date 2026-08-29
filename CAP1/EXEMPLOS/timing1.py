# File: timing1.py
# Imprime os tempos de execução para tamanhos de problema que dobram, usando um único loop.

import time

problemSize = 1000000
print("%12s%16s" % ("Problem Size", "Seconds"))
for count in range(5):
    start = time.time()  # Início do algoritmo
    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1
    elapsed = time.time() - start  # Fim do algoritmo
    print("%12d%16.3f" % (problemSize, elapsed))
    problemSize *= 2