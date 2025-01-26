
# Algoritmo de Bellman-Ford

En este articulo vamos a ver el algoritmo de Bellman-Ford. Este algoritmo calcula caminos minimos en grafos usando programacion dinamica.

```c++
int dp[MAXN];
forn(u, n) dp[u] = infinito;
dp[v] = 0;
forr(k, n-1) forn(u, n)
	for (auto [u2, c] : g[u])
		dp[u] = min(dp[u], c + dp[u2]);
```

-----------------------

Supongamos que queremos calcular caminos minimos en un grafo pero no conocemos
el algoritmo de Dijkstra. En ese caso tendriamos que inventar nuestro propio
algoritmo. Una idea bastante natural seria escribir una funcion recursiva como
la siguiente:

```c++
struct arista { int nodo, costo; };
vector<
int v;

// camino minimo de u hasta v
int dist(int u) {
	if (u == v) return 0;
	else {
		int ans = infinito;
		for (auto [u2, c] : g[u])
			ans = min(ans, c + dist(u2));
		return ans;
	}
}
```

Pero esto no funciona cuando el grafo tiene ciclos, ya que terminamos con una
recursion infinita. Pero hay un truco que podemos hacer para romper los ciclos:
agregar un parametro extra.

```c++
// camino minimo de u hasta v en k pasos o menos
int dist(int u, int k) {
	if (u == v) return 0;
	else if (k == 0) return infinito;
	else {
		int ans = infinito;
		for (auto [u2, c] : g[u])
			ans = min(ans, c + dist(u2, k-1));
		return ans;
	}
}
```

> Observacion: Si las aristas son positivas, es suficiente tomar k=n-1 porque
> cualquier camino minimo usa a lo sumo n-1 aristas y n nodos. En caso contrario
> pasa varias veces por el mismo nodo (principio del palomar), lo cual implica
> que no es minimo.

Ahora nuestra recursion no tiene ciclos, siempre termina y por lo tanto podemos
aplicar memorizacion, lo cual nos deja con un algoritmo de programacion
dinamica: el algoritmo de Belman-Ford en su forma mas simple, pero no la más
conocida.

Para llegar a la forma mas conocida primero pasamos a forma iterativa.

```c++
int dp[MAXN][MAXN];
forn(k, n) forn(u, n) {
	if (u == v) dp[u][k] = 0;
	else if (k == 0) dp[u][k] = infinito;
	else {
		int ans = infinito;
		for (auto [u2, c] : g[u])
			ans = min(ans, c + dp[u2][k-1]);
		dp[u][k] = ans;
	}
}
```

Ahora tiramos un galerazo y hacemos las actualizaciones sobre una sola capa de la dp.

Este algoritmo no va a ser exactamente equivalente al anterior, pero sigue siendo
correcto: En cada paso `dp[u]` mantiene el costo de un camino que existe en el
grafo y lo vamos actualizando con costos menores, que corresponden a otros
caminos que tambien existen en el grafo.

> TO-DO: idea de relajar distancias en grafo

```c++
int dp[MAXN];
forn(k, n) forn(u, n) {
	if (u == v) dp[u] = 0;
	else if (k == 0) dp[u] = infinito;
	else {
		for (auto [u2, c] : g[u])
			dp[u] = min(dp[u], c + dp[u2]);
	}
}
```

Como ultimo paso separamos los casos base a un nuevo bucle para simplificar un
poco mas la implementacion:

```c++
int dp[MAXN];
forn(u, n) dp[u] = infinito;
dp[v] = 0;
forr(k, n-1) forn(u, n)
	for (auto [u2, c] : g[u])
		dp[u] = min(dp[u], c + dp[u2]);
```

## Deteccion de ciclos negativos

Antes mencionamos que es suficiente hacer n-1 pasos para encontrar un camino
minimo, siempre y cuando las aristas sean positivas. El argumento se basaba en
que un camino minimo no repite vertices, pero esto es verdad si hay aristas
negativas?

NO.

Si un camino repite un vertice es porque contiene un ciclo que pasa por ese
vertice. Si el camino con el ciclo tiene menor costo que el camino sin el ciclo
es porque el costo del ciclo es negativo.

Algo algo algo.

Entonces, si no hay ciclo negativo es verdad que n-1 pasos son suficientes para
encontrar las distnacias minimas. Y resulta que en el caso contrario Belman-Ford
descubre caminos con costo cada vez menor si lo dejamos correr.

Esto nos permite verificar si hay ciclos negativos: Corremos los n-1 pasos de
Belman-Ford. Luego corremos uno mas. Si la tabla cambia en este ultimo paso
entonces hay un ciclo negativo. Si no, no.

```c++
int dp[MAXN];
forn(u, n) dp[u] = infinito;
dp[v] = 0;
forr(k, n-1)
	for (auto [u, v, c] : aristas)
		dp[u] = min(dp[u], c + dp[v]);

int viejo[MAXN];
copy(dp, dp+n, viejo);
for (auto [u, v, c] : aristas)
	dp[u] = min(dp[u], c + dp[v]);

if (!equal(dp, dp+n, viejo)) {
	// hay ciclo negativo!
} else {
	// no hay ciclo negativo!
}
```

