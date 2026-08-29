# 2. Comparação entre as coleções do Python e Java

Ao comparar as coleções do Python com as do Java, dá para perceber que os dois possuem estruturas parecidas, mas a forma de trabalhar com elas é um pouco diferente.

| Python  | Java                          | Diferença                                 |
| ------- | ----------------------------- | ----------------------------------------- |
| `list`  | `ArrayList` / `LinkedList`    | Usadas para armazenar elementos em ordem  |
| `tuple` | Não possui equivalente direto | A `tuple` do Python não pode ser alterada |
| `set`   | `HashSet`                     | Não permite elementos repetidos           |
| `dict`  | `HashMap`                     | Armazena informações em chave e valor     |
| `str`   | `String`                      | Usadas para trabalhar com textos          |

Por exemplo, no Python podemos criar uma lista simplesmente assim:

```python
lista = [1, 2, 3]
```

Enquanto no Java precisamos declarar o tipo e escolher uma implementação:

```java
List<Integer> lista = new ArrayList<>();
```

Outra diferença é que no Python `list`, `set`, `dict` e `tuple` já são estruturas próprias da linguagem. No Java, as coleções são organizadas através de interfaces como `List`, `Set` e `Map` e classes que implementam essas interfaces, como `ArrayList`, `HashSet` e `HashMap`.

No geral, as duas linguagens possuem coleções com funções semelhantes, mas o Python deixa o uso delas mais simples e direto.
