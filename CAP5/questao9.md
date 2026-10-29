# Questão 9

O `add` do `ArraySortedBag` tem complexidade **O(n)** no pior caso. Ele precisa encontrar a posição correta e deslocar os itens seguintes para abrir espaço.

Mesmo que a busca da posição seja feita em **O(log n)**, o deslocamento no array continua sendo **O(n)**.
