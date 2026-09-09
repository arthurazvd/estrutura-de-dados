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

print("Fibonacci de 10:", resultado)
print("Quantidade de chamadas:", contador[0])

# Complexidade: O(n)
# Com memoização, cada valor de Fibonacci é calculado apenas uma vez.