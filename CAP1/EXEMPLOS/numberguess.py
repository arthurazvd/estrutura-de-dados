# Autor: Ken Lambert
# Joga um jogo de adivinhação de número com o usuário.

import random

def main():
    """Insere os limites do intervalo de números e permite que o usuário
    adivinhe o número do computador até que a suposição esteja correta."""
    smaller = int(input("Digite o número menor: "))
    larger = int(input("Digite o número maior: "))
    myNumber = random.randint(smaller, larger)
    count = 0

    while True:
        count += 1
        userNumber = int(input("Digite seu palpite: "))
        if userNumber < myNumber:
            print("Muito pequeno")
        elif userNumber > myNumber:
            print("Muito grande")
        else:
            print("Você acertou em", count, "tentativas!")
            break

if __name__ == "__main__":
    main()