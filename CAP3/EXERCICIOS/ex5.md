## 1.

O **Quicksort** escolhe um elemento como **pivô** e divide a lista em duas partes: menores e maiores que o pivô. Depois, ele repete o processo em cada parte. Assim, em situações normais, consegue chegar a **O(n log n)**.

## 2.

O Quicksort não é sempre **O(n log n)** porque depende da escolha do pivô. No pior caso, o pivô fica sempre em uma das extremidades, deixando uma parte com quase todos os elementos.

Exemplo:

`1, 2, 3, 4, 5, 6, 7, 8, 9, 10`

## 3.

Duas outras formas de escolher o pivô são:

* Escolher o **primeiro elemento** da lista.
* Escolher um elemento **aleatório** da lista.

## 4.

É uma boa ideia porque o **Insertion Sort funciona bem com listas pequenas**.
Então, quando a lista tiver menos de 30 elementos, usar Insertion Sort pode ser mais rápido do que continuar dividindo a lista com Quicksort.

## 5.

O **Merge Sort** divide a lista em partes menores e depois junta essas partes já ordenadas.
A divisão acontece em aproximadamente **log n níveis**, e em cada nível são processados **n elementos**.

Por isso, no pior caso, sua complexidade é **O(n log n)**.
