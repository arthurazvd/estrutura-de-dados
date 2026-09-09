def buscaOrdenada(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
        if lista[i] > alvo:
            return -1
    return -1


lista = [10, 20, 30, 40, 50, 60, 70, 80]

resultado = buscaOrdenada(lista, 70)

print(resultado)

# Complexidade:
# Melhor caso: O(1)
# Pior caso: O(n)
# Caso médio: O(n)
