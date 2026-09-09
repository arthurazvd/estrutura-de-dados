def reverse(lista):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda < direita:
        lista[esquerda], lista[direita] = lista[direita], lista[esquerda]
        esquerda += 1
        direita -= 1

    return lista

lista = [1, 2, 3, 4, 5]

print("Lista original:", lista)
print("Lista invertida:", reverse(lista))

# Complexidade: O(n)