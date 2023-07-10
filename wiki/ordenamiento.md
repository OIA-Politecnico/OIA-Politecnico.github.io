
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

## Ejemplo de contar numeros distintos

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

## Two Pointers

Muchas veces queremos iterar por un array y a cada elemento buscarle una pareja
en el mismo u otro array.

Una observación común a muchos problemas es que sí el elemento crece, entonces
su pareja también crece (o se mantiene).

Si el array está ordenado, el crecimiento de la pareja se corresponde con que
crezca también su índice en el array.

### ¿Entonces?

Esto significa que para buscar la pareja de un elemento en el array podemos
comenzar la busqueda desde la posicion de la pareja del elemento anterior, en
vez de comenzar desde el principio del array.

Esto parece una optimización menor, pero en realidad pasa la complejidad de
`O(N^2)` a `O(N)`.

### ¿Por qué?

Una forma de programar esta lógica es así:

```c++
int j = 0; // indice de la posible pareja
for (int i = 0; i < N; ++i) {
	while (j < N && !es_compatible(i, j)) j++;
}
```

Es muy importante notar que j siempre crece de a 1 y siempre es menor a N.
Entonces, ¿cuantos pasos puede hacer? A lo sumo N. Por lo tanto este bucle
anidado realiza O(N) iteraciones en total y no O(N^2).

Otra variante de esto es que la pareja decrece cuando el elemento crece, pero se
puede aplicar el mismo tipo de lógica.

### Problemas

- "Días feriados" - Provincial 2017

## Ordenar + DP

En muchos problemas queremos probar todas las combinaciones de elementos tal que
cada elemento sea mayor o igual al anterior, pero sin agarrar repetidos.

Para esto parecería que necesitamos una función recursiva que tome como
argumento el conjunto de los elementos tomados (o que lo vaya manteniendo en una
variable global).

En realidad esto no siempre es así. Si ordenamos los elementos de menor a mayor,
basta con solo considerar elementos que vienen después del ultimo elemento
tomado. Esto permite que el argumento sea sólo el índice del último elemento
tomado, lo cual nos permite hacer [programación dinámica]( dp ).

### Problemas

- 53pts en "Buscando parejas" - Selectivo 2019 Día 1
