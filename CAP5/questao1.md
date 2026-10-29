# Questão 1

- Se for a mesma instância, o resultado é imediato: **O(1)**.
- Se os tipos ou os tamanhos forem diferentes, também termina rapidamente: **O(1)**.
- Se as bags tiverem o mesmo tamanho, o método compara a quantidade de cada item usando `count()`. Como `count()` percorre a bag e isso pode acontecer para cada item, o pior caso é **O(n²)**.
- Se encontrar uma diferença logo no começo, pode terminar antes, mas o pior caso continua sendo **O(n²)**.

Isso vale para `ArrayBag` e `LinkedBag`, pois as duas percorrem os itens para contar.
