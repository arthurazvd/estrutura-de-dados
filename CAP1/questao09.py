import math


def main():
    baixo = int(input("Digite o menor número: "))
    alto = int(input("Digite o maior número: "))

    if baixo > alto:
        baixo, alto = alto, baixo

    limite_tentativas = math.ceil(math.log2(alto - baixo + 1))
    tentativas = 0

    while baixo <= alto:
        meio = (baixo + alto) // 2
        tentativas += 1

        print(f"Seu número é {meio}")
        resposta = input("Digite =, < ou >: ").strip()

        if resposta == "=":
            print(f"Boa! Acertei em {tentativas} tentativa(s)!")
            return

        if resposta == "<":
            alto = meio - 1
        elif resposta == ">":
            baixo = meio + 1
        else:
            print("Resposta inválida. Use =, < ou >.")
            tentativas -= 1
            continue

        if tentativas >= limite_tentativas:
            print("Você está trapaceando!")
            return

    print("Não foi possível encontrar o número.")


if __name__ == "__main__":
    main()
