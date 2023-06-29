# Compresión de coordenadas

Algo muy común en problemas es que nos den elementos posicionados a lo largo de
la recta numérica, y que querámos construir una estructura de datos que
contempla toda la porción de la recta que contiene elementos. El problema es
que, si las coordenadas de los elementos son muy grandes (por ejemplo, alrededor
de `10^9`), el costo de construir una estructura de ese tamaño es demasiado
grande. Para resolverlo, aplicamos compresión de coordenadas.

El principio es simple: En vez de trabajar directo con las coordenadas, creamos
una lista con las coordenadas ordenadas de menor a mayor y trabajamos con
indices de esa lista. El máximo índice es O(N) asique nuestra estructura solo
tiene que ser O(N).

```c++
int n; cin >> n;

vector<int> pos(n); forn(i, n) cin >> pos[i];

// creo la lista ordenada
vector<int> compresion = pos;
sort(begin(compresion), end(compresion));

// reemplazo coordenadas por indices
forn(i, n) {
	auto it = lower_bound(begin(compresion), end(compresion), pos[i]);
	int idx = distance(begin(compresion), it);
	pos[i] = idx;
}
```
