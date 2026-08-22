def main():
    preco = float(input("Digite o preço da compra: R$ "))

    entrada = preco * 0.10
    saldo = preco - entrada

    # Conforme o enunciado:
    # pagamento mensal = 5% do preço restante após a entrada.
    pagamento_mensal = saldo * 0.05
    taxa_mensal = 0.12 / 12

    print("\nTabela de pagamento")
    print("-" * 88)
    print(
        f"{'Mês':>4} {'Saldo atual':>15} {'Juros':>12} "
        f"{'Principal':>14} {'Pagamento':>14} {'Saldo restante':>16}"
    )
    print("-" * 88)

    mes = 1

    while saldo > 0.005:
        juros = saldo * taxa_mensal
        principal = pagamento_mensal - juros

        # Garante que o pagamento consiga reduzir a dívida.
        if principal <= 0:
            print("O pagamento mensal não é suficiente para reduzir a dívida.")
            return

        pagamento = min(pagamento_mensal, saldo + juros)
        principal = pagamento - juros
        saldo_restante = max(0.0, saldo - principal)

        print(
            f"{mes:>4} {saldo:>15.2f} {juros:>12.2f} "
            f"{principal:>14.2f} {pagamento:>14.2f} {saldo_restante:>16.2f}"
        )

        saldo = saldo_restante
        mes += 1

if __name__ == "__main__":
    main()
