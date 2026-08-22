import math

def main():
    raio = float(input("Digite o raio da esfera: "))

    diametro = 2 * raio
    circunferencia = 2 * math.pi * raio
    area = 4 * math.pi * raio ** 2
    volume = (4 / 3) * math.pi * raio ** 3

    print(f"Diâmetro: {diametro:.2f}")
    print(f"Circunferência: {circunferencia:.2f}")
    print(f"Área da superfície: {area:.2f}")
    print(f"Volume: {volume:.2f}")

if __name__ == "__main__":
    main()
