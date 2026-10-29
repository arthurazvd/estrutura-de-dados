# Questão 6 — Diagrama de classes

Uma classe de conjunto ordenado pode herdar de `ArraySet` e manter seus elementos em ordem crescente. Assim, ela preserva a regra de não aceitar duplicatas e acrescenta busca binária.

```text
        AbstractCollection
                |
           AbstractBag
                |
             ArrayBag
                |
             ArraySet
                |
          ArraySortedSet
```

A herança direta de `ArraySet` permite reaproveitar a interface e a regra de unicidade; `ArraySortedSet` redefine a inserção e a busca para manter a ordem e usar busca binária.
