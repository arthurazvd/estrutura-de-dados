def fibonacci(n, memo, counter):
    counter[0] += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1, memo, counter) + fibonacci(n - 2, memo, counter)
    return memo[n]

contador = [0]

resultado = fibonacci(10, {}, contador)

print("Resultado:", resultado)
print("Chamadas:", contador[0])

# Exemplo:
# contador = [0]
# resultado = fibonacci(10, {}, contador)
# print(resultado)
# print("Chamadas:", contador[0])
