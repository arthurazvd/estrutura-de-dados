def insertionSort(lista):
    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > valor:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = valor


def quicksort(lista):
    if len(lista) <= 1:
        return lista

    if len(lista) < 50:
        insertionSort(lista)
        return lista

    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]

    return quicksort(menores) + iguais + quicksort(maiores)

lista = [64, 25, 12, 22, 11, 90, 34, 5]

print("Lista original:", lista)
print("Lista ordenada:", quicksort(lista))

# O uso do Insertion Sort em listas pequenas pode melhorar
# o desempenho, pois evita várias chamadas recursivas.
# O melhor limite pode ser testado com listas de 50, 500 e 5000 itens.