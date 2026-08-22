# Exemplos de funções recursivas do capítulo

def displayRange(lower, upper):
    """Exibe os números de lower a upper (versão recursiva)."""
    if lower <= upper:
        print(lower)
        displayRange(lower + 1, upper)

def ourSum(lower, upper, margin=0):
    """Retorna a soma dos números de lower a upper, e exibe um
    trace dos argumentos e valores de retorno em cada chamada."""
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + ourSum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result

# Função fatorial com helper aninhado
def factorial(n):
    """Retorna o fatorial de n."""
    def recurse(n, product):
        if n == 1:
            return product
        else:
            return recurse(n - 1, n * product)
    return recurse(n, 1)

# Função fatorial com parâmetro padrão
def factorial2(n, product=1):
    """Retorna o fatorial de n."""
    if n == 1:
        return product
    else:
        return factorial2(n - 1, n * product)