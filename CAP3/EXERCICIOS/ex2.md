# Exercícios

## 1.

### a. `2n + 4n² + 15n`

* Termo dominante: `4n²`
* Big-O: **O(n²)**

### b. `3n² + 16`

* Termo dominante: `3n²`
* Big-O: **O(n²)**

### c. `n³ + n² + 2n`

* Termo dominante: `n³`
* Big-O: **O(n³)**

---

## 2.

O **algoritmo B** realiza menos trabalho, pois:

* A: `n²`
* B: `½n² + ½n`

Para `n` pequeno, os dois podem realizar quantidades parecidas de trabalho. Por exemplo, com `n = 1`, ambos realizam 1 instrução.

Conforme `n` aumenta, o algoritmo B passa a realizar aproximadamente metade das operações do algoritmo A, apresentando um desempenho melhor.

---

## 3.

Comparando `n⁴` com `2ⁿ`, os dois apresentam aproximadamente a mesma quantidade de trabalho quando **n = 16**:

* `16⁴ = 65.536`
* `2¹⁶ = 65.536`

A partir de **n > 16**, o algoritmo `n⁴` começa a apresentar melhor desempenho, pois `2ⁿ` cresce muito mais rapidamente.
