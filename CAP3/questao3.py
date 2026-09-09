def expo(number, exponent):
    resultado = 1

    for _ in range(exponent):
        resultado *= number

    return resultado

print("Resultado:", expo(2, 5))

# Complexidade: O(n), onde n é o expoente.