# Exercícios

## 1. Busca binária

Lista:

`20, 44, 48, 55, 62, 66, 74, 88, 93, 99`

Índices:

`0, 1, 2, 3, 4, 5, 6, 7, 8, 9`

### a. Procurando o valor 90

| esquerda | direita | meio | valor |
| ---: | ----: | -------: | ----: |
|    0 |     9 |        4 |    62 |
|    5 |     9 |        7 |    88 |
|    8 |     9 |        8 |    93 |

Como `90 < 93`, procuramos à esquerda. Porém, `left = 8` e `right = 7`, então a busca termina.

**Resultado:** 90 não está na lista.

### b. Procurando o valor 44

| esquerda | direita | meio | valor |
| ---: | ----: | -------: | ----: |
|    0 |     9 |        4 |    62 |
|    0 |     3 |        1 |    44 |

O valor encontrado está no índice **1**.

---

## 2. Busca baseada em estimativa

Podemos modificar a busca binária para tentar calcular onde o nome provavelmente está na lista, em vez de sempre pegar o meio.

Por exemplo, ao procurar por "Smith", podemos começar mais perto do final da lista.

Essa mudança pode deixar algumas buscas mais rápidas, mas a complexidade continua sendo O(log n).