def mean(numeros):
    """Retorna a média dos números da lista."""
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
    return sum(numeros) / len(numeros)


def median(numeros):
    """Retorna a mediana dos números da lista."""
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")

    ordenados = sorted(numeros)
    tamanho = len(ordenados)
    meio = tamanho // 2

    if tamanho % 2 == 1:
        return ordenados[meio]

    return (ordenados[meio - 1] + ordenados[meio]) / 2


def mode(numeros):
    """Retorna a moda da lista.

    Em caso de empate, retorna o menor valor entre os que possuem
    a maior frequência.
    """
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")

    frequencias = {}

    for numero in numeros:
        frequencias[numero] = frequencias.get(numero, 0) + 1

    maior_frequencia = max(frequencias.values())
    modas = [
        numero for numero, frequencia in frequencias.items()
        if frequencia == maior_frequencia
    ]

    return min(modas)


def main():
    numeros = [10, 8, 7, 7, 9, 10, 7]

    print("Números:", numeros)
    print("Média:", mean(numeros))
    print("Mediana:", median(numeros))
    print("Moda:", mode(numeros))


if __name__ == "__main__":
    main()
