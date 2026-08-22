def main():
    altura = float(input("Digite a altura inicial da bola: "))
    num_quiques = int(input("Digite o número de quiques: "))

    indice = 0.6
    distancia_total = 0.0
    altura_atual = altura

    for _ in range(num_quiques):
        distancia_total += altura_atual
        altura_atual *= indice
        distancia_total += altura_atual

    if num_quiques == 0:
        distancia_total = 0.0

    print(f"Distância total percorrida: {distancia_total:.2f}")

if __name__ == "__main__":
    main()
