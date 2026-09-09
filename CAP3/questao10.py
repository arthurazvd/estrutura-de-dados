def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("=== TESTE DO FATORIAL ===")
print("Fatorial de 5:", factorial(5))

# Fatorial recursivo:
# Cada chamada cria uma nova chamada até chegar em 0.
# Complexidade de memória: O(n)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\n=== TESTE DO FIBONACCI ===")
print("Fibonacci de 6:", fibonacci(6))

# Fibonacci recursivo:
# Cria várias chamadas ao mesmo tempo e pode chegar a O(n) níveis.
# Complexidade de memória: O(n)