# Técnicas de strings

- KMP es para buscar un string de longitud N adentro de otra de longitud M en complejidad O(N+M). Es de notebook

- La idea de hashing es hacer cuentitas con los caracteres de una string para que te de un numero. Entonces si los nros son iguales hay alta probabilidad de que las strings tambien. En programación competitiva si usás un hash razonable de 64 bits podes asumir que la probabilidad es 100%. Así podes comparar strings en O(1) si antes haces un precalculo.

- Se puede hacer tablita aditiva de hashes asique para comparar substrings no hace falta precalcular todos los hashes. (ver la pandilla strings/hashing.cpp). Con esa idea también podes buscar una string adentro de otra en O(N+M). Eso se llama Rabin-Karp

## Temas más avanzados

- Como funciona KMP (qué representa el precalculo y como funciona la busqueda)
- Suffix array y LCP (como se usan, no hacen falta como se calculan)
- Z function (como se usa, no como se calcula)
- Probabilidad de que los hashes colisionen
- xor hashing (en mi experiencia esto es mas para codeforces pero puede llegar a servir)
- Suffix tree
- Suffix automaton
- Aho-Corasick
