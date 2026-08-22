# Exemplos de operações com arquivos do capítulo

import random
import pickle

# --- Escrever números em um arquivo ---
def write_numbers():
    f = open("integers.txt", 'w')
    for count in range(500):
        number = random.randint(1, 500)
        f.write(str(number) + "\n")
    f.close()

# --- Ler números de um arquivo ---
def read_numbers():
    f = open("integers.txt", 'r')
    theSum = 0
    for line in f:
        line = line.strip()
        number = int(line)
        theSum += number
    print("A soma é", theSum)
    f.close()

# --- Ler números com split ---
def read_numbers_split():
    f = open("integers.txt", 'r')
    print("A soma é", sum(map(int, f.read().split())))
    f.close()

# --- Pickle: salvar objetos ---
def pickle_save():
    lyst = [60, "A string object", 1977]
    fileObj = open("items.dat", "wb")
    for item in lyst:
        pickle.dump(item, fileObj)
    fileObj.close()

# --- Pickle: carregar objetos ---
def pickle_load():
    lyst = list()
    fileObj = open("items.dat", "rb")
    while True:
        try:
            item = pickle.load(fileObj)
            lyst.append(item)
        except EOFError:
            fileObj.close()
            break
    print(lyst)