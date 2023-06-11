# Búsqueda binaria

Una propiedad binaria (o un predicado, o una condición) es monótona si vale hasta cierto punto y luego deja de valer o viceversa.
Por ejemplo P(n) = "n < 5"
P es true hasta 4 y a partir de 5 vale false

La búsqueda binaria es un algoritmo para hallar dicho punto, llamado "la frontera" que en este ejemplo está entre 4 y 5

La idea es comenzar con un valor donde sabes que P vale, y otro donde sabés que no vale. Probás un valor intermedio y vas actualizando los valores hasta hallarla:

1. Consideramos un intervalo `[a, b)`, donde la condición no vale en `a`, y sí vale en `b`.
2. Probamos si la propiedad vale en el punto medio entre `a` y `b`, que llamamos `m`.
3. Si la propiedad vale, pasamos a considerar el intervalo `[a, m)`.
4. Si no vale, pasamos a considerar el intervalo `[m, b)`.
5. Repetimos esto mientras que la diferencia entre `a` y `b` sea mayor a 1.

En otras palabras, la busqueda binaria sirve para contestar preguntas de la pinta:

> ¿A partir de qué punto vale tal propiedad?

Por ejemplo:

> ¿Cuánto contrapeso necesita mi catapulta para alcanzar el castillo?
> 
> ¿A partir de qué posición me paso del elemento del array (ordenado) que estoy buscando? (como en un diccionario ordenado alfabéticamente)

Este tipo de busqueda tiene complejidad O(log n) (donde n es la diferencia inicial
entre a y b). En cambio, la busqueda lineal (ir probando cada valor, uno por uno)
tiene complejidad O(n).

Algunas formas comunes de aplicarla son:

- Buscar elementos en un arreglo ordenado
- Ver a partir de qué valor anda un greedy
- Mas generalmente: convertir un problema a su versión de decisión

## Implementación de referencia

```c++
// Suponiendo que P(a) es false y P(b) es verdadero
// Encuentra el punto de corte
pair<int, int> busqueda_binaria(int a, int b) {
	while (b - a > 1) {
		int m = (a+b)/2;
		if (P(m)) {
			b = m;
		} else {
			a = m;
		}
	}

	// en este punto esta garantizado que:
	// - P(a) == false
	// - P(b) == true
	// - a + 1 = b
	return {a, b};
}
```

## Aplicacion a búsqueda en un array ordenado

```c++
// Encuentra x en un array ordenado
// Devuelve el índice de la primera aparición de x, si la hay
// Devuelve -1 si no hay ningún x
int encontrar(int arr[], int n, int x) {

	// Idea: búsqueda binaria con la condición "P(m) = arr[m] >= x"

	int a = -1; // Me imagino que arr[-1] <  x
	int b = n;  // Me imagino que arr[n]  >= x

	while (b - a > 1) {
		int m = (a+b)/2;
		if (arr[m] >= x) {
			b = m;
		} else {
			a = m;
		}
	}

	// Ahora se que:
	//   arr[b] >= x (o que b ==  n)
	//   arr[a] <  x (o que a == -1)

	// Para estar seguro, me fijo que b sea un indice valido y
	// que el elemento en esa posicion realmente sea x
	if (b != n && arr[b] == x) {
		return b;
	} else {
		return -1;
	}
}
```
