# Questão 4 — Diagrama de classes

Uma organização possível é fazer as classes concretas de conjunto herdarem das classes de bag correspondentes, sobrescrevendo `add` para impedir duplicatas.

```text
        AbstractCollection
                |
           AbstractBag
           /         \
      ArrayBag     LinkedBag
          |             |
       ArraySet      LinkedSet
```

`ArraySet` herda a representação baseada em array; `LinkedSet` herda a representação por nós encadeados. Os métodos `add` dessas classes só inserem o item quando ele ainda não existe.
