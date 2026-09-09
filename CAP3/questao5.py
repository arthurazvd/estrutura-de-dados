def selectionSort(lista, reverse=False):
    for i in range(len(lista) - 1):
        indice = i

        for j in range(i + 1, len(lista)):
            if not reverse:
                if lista[j] < lista[indice]:
                    indice = j
            else:
                if lista[j] > lista[indice]:
                    indice = j

        lista[i], lista[indice] = lista[indice], lista[i]

    return lista

lista = [64, 25, 12, 22, 11]

print("Lista original:", lista)

print("Ordem crescente:", selectionSort(lista.copy()))

print("Ordem decrescente:", selectionSort(lista.copy(), reverse=True))

# reverse=False -> ordem crescente
# reverse=True  -> ordem decrescente
