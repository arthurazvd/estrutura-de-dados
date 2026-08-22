def main():
    salario_hora = float(input("Digite o salário por hora: R$ "))
    horas_regulares = float(input("Digite o total de horas regulares: "))
    horas_extras = float(input("Digite o total de horas extras: "))

    pagamento_regular = salario_hora * horas_regulares
    pagamento_extra = horas_extras * 1.5 * salario_hora
    pagamento_total = pagamento_regular + pagamento_extra

    print(f"Pagamento semanal: R$ {pagamento_total:.2f}")

if __name__ == "__main__":
    main()
