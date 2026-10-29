# Questão 2

O operador `+` cria uma nova bag com os itens da primeira e depois adiciona os itens da segunda.

- `ArrayBag`: **O(n + m)** no tempo médio, considerando o custo amortizado do redimensionamento.
- `LinkedBag`: **O(n + m)**, pois precisa copiar os itens e adicionar os da outra bag.

Aqui, `n` é a quantidade de itens da primeira bag e `m` a quantidade de itens da segunda.
