def main():
    iteracoes = int(input("Digite o número de iterações: "))

    soma = 0.0

    for i in range(iteracoes):
        termo = 1 / (2 * i + 1)

        if i % 2 == 0:
            soma += termo
        else:
            soma -= termo

    pi = 4 * soma

    print(f"Valor aproximado de pi: {pi:.10f}")

if __name__ == "__main__":
    main()
