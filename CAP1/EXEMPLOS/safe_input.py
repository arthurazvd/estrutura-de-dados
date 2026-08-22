# Autor: Ken Lambert
# Demonstra uma função que captura erros de formato de número durante a entrada.

def safeIntegerInput(prompt):
    """Solicita ao usuário um inteiro e retorna o inteiro se estiver bem formado.
    Caso contrário, imprime uma mensagem de erro e repete este processo."""
    inputString = input(prompt)
    try:
        number = int(inputString)
        return number
    except ValueError:
        print("Erro no formato do número:", inputString)
        return safeIntegerInput(prompt)

if __name__ == "__main__":
    age = safeIntegerInput("Digite sua idade: ")
    print("Sua idade é", age)