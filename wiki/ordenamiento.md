
# Ordenamiento

Ordenar es muy util para resolver problemas. Muchos problemas que son dificiles
o "imposibles" sobre arreglos desordenados, son fáciles o, por lo menos, más
fáciles sobre arreglos ordenados.

Implementar un algoritmo de ordenamiento eficiente no es tan sencillo pero, por
suerte, C++ ya trae uno: `sort(l, r)`.

`sort` toma dos iteradores como argumento. No viene al caso saber qué son. (se
puede googlear) Lo que nos importa es que para ordenar un vector se usa así:

```c++
vector<int> v = { 10, 100, 1 };
sort(begin(v), end(v));
```

<br>

Y para ordenar los primeros `n` elementos de un array se usa así:

```
int a[1000];
sort(a, a+n);
```

## Contar elementos distintos

Algo que surge en muchisimos problemas es contar la cantidad de valores
distintos en un array.

Resulta que si el array está ordenado es muy fácil:

- hay un valor al principio y lo siguen todas sus repeticiones
- si voy avanzando en algún momento puedo encuentrar dos elementos pegados que
  son distintos
- es imposible que ese valor ya haya aparecido porque todos los anteriores eran
  menores
- por lo tanto estoy descubriendo un valor nuevo

Si el array no está ordenado, lo ordenamos y listo.

En código es una cosa así:

```c++
sort(a, a+n);
int cantidad = 1;
forr(i, 1, n) {
	if (a[i-1] != a[i]) {
		cantidad++;
	}
}
```

Estas ideas de "los elementos iguales están juntos" y "tal cosa vale porque
todos los elementos anteriores son menores" son extremadamente comunes y
aparecen en cientos de problemas.

## Ver tambien

- [Two Pointers]( two-pointers )
- [Ordenar + DP]( dp#ordenar )
