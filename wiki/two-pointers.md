
# Two Pointers

Muchas veces queremos iterar por un array y a cada elemento buscarle una pareja
en el mismo u otro array.

Una observación común a muchos problemas es que sí el elemento crece, entonces
su pareja también crece (o se mantiene).

Si el array está ordenado, el crecimiento de la pareja se corresponde con que
crezca también su índice en el array.

## ¿Entonces?

Esto significa que para buscar la pareja de un elemento en el array podemos
comenzar la busqueda desde la posicion de la pareja del elemento anterior, en
vez de comenzar desde el principio del array.

Esto parece una optimización menor, pero en realidad pasa la complejidad de
`O(N^2)` a `O(N)`.

## ¿Por qué?

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

## Problemas

- "Días feriados" - OIA Jurisdiccional 2017
