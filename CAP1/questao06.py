def main():
    nome_arquivo = input("Digite o nome do arquivo: ")

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            print("\nRelatório de pagamento")
            print("-" * 50)
            print(f"{'Funcionário':<20}{'Horas':>10}{'Salário':>15}")
            print("-" * 50)

            for linha in arquivo:
                partes = linha.split()

                if len(partes) != 3:
                    continue

                sobrenome = partes[0]
                salario_hora = float(partes[1])
                horas = float(partes[2])

                salario = salario_hora * horas

                print(f"{sobrenome:<20}{horas:>10.2f}{salario:>15.2f}")

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except ValueError:
        print("O arquivo contém dados inválidos.")

if __name__ == "__main__":
    main()
