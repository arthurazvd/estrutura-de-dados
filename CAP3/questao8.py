import random

def makeRandomList(size):
    lyst = []

    for count in range(size):
        while True:
            number = random.randint(1, size)

            if number not in lyst:
                lyst.append(number)
                break

    return lyst

lista = makeRandomList(10)

print("Lista gerada:", lista)

# Complexidade: O(n²) no pior caso,
# pois "number not in lyst" pode percorrer a lista.