def main():
    nome_arquivo = input("Digite o nome do arquivo: ")

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        while True:
            print(f"\nO arquivo possui {len(linhas)} linhas.")
            numero = int(input("Digite o número da linha (0 para sair): "))

            if numero == 0:
                print("Programa encerrado.")
                break

            if 1 <= numero <= len(linhas):
                print(f"\nLinha {numero}:")
                print(linhas[numero - 1], end="")
            else:
                print("Número de linha inválido.")

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except ValueError:
        print("Digite um número inteiro.")

if __name__ == "__main__":
    main()
