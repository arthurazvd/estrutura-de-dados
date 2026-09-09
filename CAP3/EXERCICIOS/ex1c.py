
import time

start = time.process_time()

problemSize = 1000000

count = 0
while problemSize > 0:
    problemSize = problemSize // 2
    count += 1

end = time.process_time()

print("Tempo de processamento:", end - start)

#   O procedimento é o mesmo usado com time.time(): registra-se o tempo antes da execução, 
#   executa-se o código e registra-se o tempo depois. A diferença entre os dois valores
#   fornece o tempo de CPU utilizado pelo processo.
