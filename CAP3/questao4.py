def expo(number, exponent):
    if exponent == 0:
        return 1

    if exponent % 2 == 1:
        return number * expo(number, exponent - 1)

    metade = expo(number, exponent // 2)
    return metade * metade

print("Resultado:", expo(2, 5))

# Complexidade: O(log n)