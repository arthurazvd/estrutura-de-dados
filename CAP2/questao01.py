import os

def explorar(tipo):
    print("\n" + "=" * 50)
    print(f"EXPLORANDO: {tipo.__name__}")
    print("=" * 50)

    print("\nMétodos disponíveis:")
    print(dir(tipo))

    opcao = input("\nDeseja abrir a documentação? (s/n): ").lower()

    if opcao == "s":
        help(tipo)

def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    colecoes = {
        "1": str,
        "2": list,
        "3": tuple,
        "4": set,
        "5": dict
    }
    
    for i in range(10):
        limpar_tela()
        print("\n" + "-" * 40)
        print("EXPLORAÇÃO DE COLEÇÕES PYTHON")
        print("-" * 40)
        print("1 - str")
        print("2 - list")
        print("3 - tuple")
        print("4 - set")
        print("5 - dict")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            break

        if opcao in colecoes:
            explorar(colecoes[opcao])
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()