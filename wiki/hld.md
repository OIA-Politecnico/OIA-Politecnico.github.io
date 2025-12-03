# Heavy-Light Decomposition

Dado un arbol con raíz de N nodos, hay una observación super simple, a la cual
le podemos sacar mucho provecho.

**obs:** Entre todos los hijos de la raíz, hay a lo sumo uno cuyo subarbol tiene
`>= N/2` nodos.

Esto nos sirve para optimizar algoritmos bastante brutos, como el siguiente:

```
# O(N^2)
para cada u, nodo del arbol:
  para cada v, hijo de u:
    dfs(v)
```

Si, en cambio, evitamos procesar esos subarboles con muchos nodos, el algoritmo
es O(N log N):

```
# O(N log N)
para cada u, nodo del arbol:
  para cada v, hijo de u:
    if tam_subarbol(v)*2 < tam_subarbol(u):
      dfs(v)
```

> **¿Por qué?**
>
> El costo es la suma de los tamaños de los subarboles que visitamos con un dfs.
>
> Visto de otra manera: la suma de la cantidad de veces que cada nodo es
> visitado por un dfs.
>
> Entonces, imaginate el camino desde un nodo w hasta la raíz, y considerá el
> conjunto de nodos v desde los cuales disparamos llamadas a dfs(v).
>
> El tamaño de ese conjunto, es justamente la cantidad de veces que w es
> visitado por un dfs.
>
> Fijate que si recorremos el camino de abajo hacia arriba, cada vez que
> cruzamos uno de estos nodos, el tamaño del subarbol del nodo al que llegamos
> es al menos el doble que el anterior.
>
> Esto puede pasar a lo sumo log2(N) veces. Si pasara más veces, habría más de N
> nodos en el arbol, lo cual es imposible.

Obviamente, no recorrer uno de los hijos puede romper el algoritmo, asi que
la dificultad de aplicar esta idea es ver cómo podemos arreglarlo. Generalmente,
la forma de hacerlo va a ser guardar el resultado del calculo que hagamos en
cada hijo pesado y usarlo para el calculo en el padre.

## Definiciones

- Dado un nodo u, su **hijo pesado** es el hijo v tal que `tam_subarbol(v)*2 >= tam_subarbol(u)`.

- Dado un nodo u y un hijo v:

  - si v es el hijo pesado de u, entonces la arista (u, v) es **pesada**.
  - si v no es hijo pesado de u, entonces la arista (u, v) es **liviana**.

- un **camino pesado** es un camino que:
  - es un único nodo o es un camino que solo contiene aristas pesadas.
  - su nodo más profundo no tiene hijo pesado.
  - su nodo menos profundo no es un hijo pesado.

- **obs**: en el camino de un nodo u a la raiz, hay a lo sumo log2(N) aristas livianas. (demostrado en la introducción)

Vamos a ver varios algoritmos que surgen de tratar de manera distinta las aristas livianas y pesadas.

Por ejemplo, el algoritmo que vimos antes se puede expresar así:

### Implementación

```c++
int const maxn = 100000;

int n;
vector<int> g[maxn];
int p[maxn]; // padre
int h[maxn]; // hijo pesado (o -1 si no tiene)
int t[maxn]; // tamaño de subarbol

void dfs(int u) {
	t[u] = 1;
	for (int v : g[u]) if (v != p[u]) {
		p[v] = u;
		dfs(v);
		t[u] += t[v];
	}
}
void decompose(int root) {
	forn(u, n) h[u] = -1;
	p[root] = -1;
	dfs(root);
	forn(v, n) {
		if (int u = p[v]; u != -1 && t[v]*2 >= t[u]) {
			h[u] = v;
		}
	}
}

```

## Problema <https://codeforces.com/contest/1174/problem/F>

> Problema interactivo. Te dan un árbol con raíz, de N nodos (`N <= 10^5`). Hay
> un nodo secreto x que hay que descubrir. Para lograrlo podes hacer dos tipos
> de consultas:
>
> - d(u): dado un nodo u te responden la distancia de u a x
> - s(u): dado un nodo u te responden el siguiente nodo en el camino hacia x. u
>   debe ser ancestro de x. si no, te dan wrong answer inmediatamente.
>
> Se pueden realizar **a lo sumo 36 consultas**.

### Solucion

> Nos paramos en la raiz y nos vamos a ir acercando iterativamente al nodo x.
>
> Considera el camino desde la raiz hasta x. Este camino contiene a lo sumo
> `log2(N) <= 17` aristas livianas.
>
> Entre medio de cada par de aristas livianas hay un camino pesado.
>
> Si logramos procesar cada camino pesado y cada arista pesada con una sola
> consulta, lograriamos el limite de consultas del problema.
>
> Si sabemos que el camino arranca metiendose por un camino pesado pero en algun
> momento se sale, es posible calcular en que punto se sale haciendo una
> consulta de distancia en el primer nodo del camino y tambien en el ultimo.
> (hacemos dos consultas de tipo d(u)).
>
> Una vez que sabemos en que nodo se sale del camino pesado, puede haber mas de
> una arista liviana por la que se puede salir. Ahi hay que hacer una consulta
> de tipo s(u).
>
> Esto haria en el peor caso `17 + 2 * 18 = 53` consultas.
>
> Siendo un poco mas ingenioso se puede calcular la consulta de distancia del
> inicio del camino pesado usando los resultados anteriores.
>
> Esto baja la cantidad de consultas a `17 + 18 = 35` en el peor caso.

```c++
int const maxn = 200100;
int n;
vector<int> g[maxn];
int h[maxn], p[maxn], t[maxn];

// ... dfs(), decompose() ...

int d(int u) { // implementa la consulta d(u) del interactivo
	cout << "d " << (u+1) << "\n" << flush;
	int ans; cin >> ans; return ans;
}

int s(int u) { // implementa la consulta s(u) del interactivo
	cout << "s " << (u+1) << "\n" << flush;
	int ans; cin >> ans; return ans-1;
}

int main() {
	cin >> n;
	forn(i, n-1) {
		int u, v; cin >> u >> v; --u; --v;
		g[u].push_back(v);
		g[v].push_back(u);
	}

	decompose(0);

	int top = 0;
	int d_top = d(top);

	while (true) {

		int steps_btm = 0;
		int btm = top;
		while (h[btm] != -1) cerr << btm << "\n", btm = h[btm], steps_btm++;
		int d_btm = d(btm);

		int steps_mid = d_top - (d_top + d_btm - steps_btm) / 2;
		int mid = top;
		forn(_, steps_mid) mid = h[mid];
		int d_mid = d_top - steps_mid;

		if (d_mid == 0) {
			cout << "! " << mid+1 << "\n";
			return 0;
		}

		top = s(mid);
		d_top = d_mid - 1;
	}
}
```

## Idea de procesar el subarbol de cada arista liviana / *Sack*

Cada nodo tiene `O(log(N))` aristas livianas en su camino hacia la raiz. Esto se
puede dar vuelta para llegar a la siguiente observacion:

**obs:** Si iteramos por todo el subarbol de cada hijo liviano, visitamos cada
nodo `O(log(N))` veces.

Esto significa que podemos hacer algoritmos bastante brutos y van a ser
eficientes, siempre y cuando no recorramos el subarbol de cada hijo pesado
muchas veces.

## Problema <https://cses.fi/problemset/task/1139>

> Hay un arbol con raiz, de N nodos (`N <= 2*10^5`), donde cada nodo tiene un
> color. Por cada nodo, nos preguntan cuantos colores distintos aparecen en su
> subarbol.

### Solucion

Tomamos algun camino pesado, y vamos iterando de abajo hacia arriba, manteniendo
un conjunto de colores.

En cada paso insertamos el color del nodo actual y recorremos los subarboles de
todos los hijos livianos del nodo actual, insertando sus colores en el conjunto.

Como todo el subarbol del hijo pesado ya estaba insertado en el conjunto, en
todo momento lo que tenemos es el conjunto de colores del subarbol del nodo
actual, lo cual nos permite responder su cantidad de colores.

Ahora repetimos este algoritmo para cada camino pesado (consideramos nodos que
no son hijos pesados ni tienen hijo pesado como un camino en si mismo).

Para analizar la complejidad, notemos que por cada nodo, insertamos su color en
un conjunto una vez al iterar su camino pesado y una vez por cada arista liviana
que está en su camino hacia la raíz. O sea, a lo sumo `log2(N)+1` veces.

Esto significa que cada nodo se inserta `O(log(N))` veces, por lo que el
algoritmo realiza a lo sumo `O(N log(N))` inserciones en un conjunto. Si usamos
`unordered_set`, obtenemos exactamente esa complejidad.

```c++
int const maxn = 200000;

int n;
vector<int> g[maxn];
int p[maxn], h[maxn], t[maxn];

// ... dfs(), decompose() ...

vector<int> post; // post-orden
int tl[maxn], tr[maxn]; // rango de cada subarbol en el post-orden
void dfs2(int u) {
	tl[u] = post.size();
	for (int v : g[u]) if (v != p[u])
		dfs2(v);
	post.push_back(u);
	tr[u] = post.size();
}

int c[maxn]; //color

int main() {
	cin >> n;
	forn(u, n) cin >> c[u];
	forn(i, n-1) {
		int u, v; cin >> u >> v; --u; --v;
		g[u].push_back(v);
		g[v].push_back(u);
	}

	decompose(0);
	dfs2(0);

	vector<int> ans(n, -1);
	for (int u : post) if (ans[u] == -1) {
		unordered_set<int> colors;
		while (true) {
			colors.insert(c[u]);

			// inserto los colores del subarbol de cada hijo liviano
			for (int v : g[u]) if (v != p[u] && v != h[u])
				forr(i, tl[v], tr[v])
					colors.insert(c[post[i]]);

			ans[u] = colors.size();

			// si v es un hijo pesado, subo. si no, freno.
			if (p[u] != -1 && h[p[u]] == u) u = p[u];
			else break;
		}
	}

	forn(u, n) cout << ans[u] << " \n"[u==n-1];
}
```

## Idea de mover fichitas a la raiz / *small-to-large* / *DSU on trees*

Una forma común de aprovechar la descomposicion en aristas livianas y pesadas
es en problemas donde queremos simular que en cada nodo del árbol comienza una
fichita y esta va a ir caminando hacia la raíz.

Simulando directamente, esto toma tiempo proporcional a la suma de las
profundidades de todos los nodos, que puede ser `O(N^2)`

En cambio, si pudieramos simular el trayecto de cada fichitas por un camino
pesado en O(1) y solo pagaramos las aristas individualmente en el caso de ser
livianas, entonces tendriamos un algoritmo `O(N log(N))`.

Esta misma idea se puede aplicar para el problema anterior.

> La idea va a ser que podemos mantener un set de colores en cada nodo, donde
> cada elemento del set representa una "ficha" correspondiente a cada nodo.
>
> Al cruzar una arista pesada, movemos todas las fichas en O(1) haciendo un
> `std::swap` o `std::move` del set del hijo pesado hacia el set del padre
>
> Al cruzar una arista liviana simplemente movemos las fichas una por una al
> set del nodo padre.

```c++
// ... definir grafo, arreglos y funciones de la descomposicion ...

vector<int> post;
void dfs2(int u) {
	for (int v : g[u]) if (v != p[u])
		dfs2(v);
	post.push_back(u);
}

int c[maxn]; //color

int main() {
	cin >> n;
	forn(u, n) {
		cin >> c[u];
	}
	forn(i, n-1) {
		int u, v; cin >> u >> v; --u; --v;
		g[u].push_back(v);
		g[v].push_back(u);
	}

	decompose(0);
	dfs2(0);

	vector<set<int>> colors(n);
	vector<int> ans(n);

	for (int u : post) {

		// muevo todas las fichitas del hijo pesado en O(1)
		if (h[u] != -1) colors[u] = move(colors[h[u]]);

		// agrego mi fichita
		colors[u].insert(c[u]);

		// muevo fichitas de los hijos livianos una por una
		for (int v : g[u]) if (v != p[u] && v != h[u])
			for (int x : colors[v])
				colors[u].insert(x);

		ans[u] = colors[u].size();
	}

	forn(u, n) cout << ans[u] << " \n"[u==n-1];
}
```

> Comentario de implementacion:
>
> No hace falta guardarse el post-orden y procesar posteriormente.
> Se puede hacer lo mismo escribiendo el codigo directamente en el dfs.
> De esa manera queda un codigo un poco mas corto y simple.
>
> Para la solucion anterior es un poco mas complicado de lograr.


## Idea de construir estructuras de datos sobre los caminos pesados

La aplicacion mas famosa de esta descomposicion es su uso para responder
consultas de suma/max/gcd (o cualquier operacion asociativa) en caminos de un
arbol, donde cada nodo tiene un valor.

**obs:** un camino cualquiera solo toca a lo sumo `2*(log2(N)+1)` caminos
pesados. (Porque un camino `u`--`v` esta contenido en la union entre los caminos
`u`--`raiz` y `v`--`raiz`, que tocan a lo sumo `log2(N)+1` cada uno)

La idea es construir una estructura de datos que permite responder consultas de
rangos en cada camino pesado. (Por ejemplo segment tree)

Para responder una consulta sobre un camino, lo descomponemos en las partes que
caen en distintos caminos pesados y respondemos cada consulta usando la
estructura del camino pesado correspondiente.

En mas detalle, imaginate que queremos calcular una consulta a lo largo del
camino entre dos nodos `u` y `v`.

**obs:** Si `u` y `v` estan en el mismo camino pesado, entonces el camino
`u`--`v` es esta contenido en este camino pesado, y podemos responder la
consulta mediante una consulta en rango.

**obs:** Si `u` y `v` estan en distintos caminos pesados, el camino de `u`--`v`
contiene completamente al menos una de dos cosas:

- el camino `u`--`c[u]`
- el camino `v`--`c[v]`

En particular, el de mayor profundidad entre `c[u]` y `c[v]` siempre esta
contenido. O sea que:

- Si `c[v]` es el mas profundo, podemos partir la consulta sobre el camino
  `u`--`v` en dos partes:

  - `u`--`p[c[v]]` (contenido en un mismo camino pesado)
  - `c[v]`--`v`

- En cambio, si `c[u]` es el mas profundo, podemos partir en:

  - `u`--`c[u]`
  - `p[c[u]]`--`v` (contenido en un mismo camino pesado)


## Implementacion

Aca vemos una forma de implementar pero no es necesariamente la mas corta o la
mas eficiente, si no que apunta a ser entendible. Hay implementaciones de calidad
de competencia en distintos lados en Internet (KACTL, cp-algorithms,
el-vasito-icpc, etc.)

Aparte, nos limitamos al caso de operaciones conmutativas. Resolver el caso
no-conmutativo no es mucho mas dificil, pero complica la implementacion y
distrae de la idea principal. En particular, la implementacion que sigue es para
hacer suma pero deberia ser directo adaptarla para otras operaciones asociativas
y conmutativas (max, min, gcd, etc.)

Veamos la inicializacion de la estructura.

A cada camino pesado le asignamos un id unico, que es el id del nodo de mas
arriba del camino. Aparte, en cada nodo guardamos el id del camino pesado al que
pertenece.

Despues construimos un segment tree sobre cada camino pesado (para esto primero
calculamos el tamaño del camino en cantidad de nodos y despues asignamos valores
al segment tree segun los nodos que componen el camino)

**obs:** la posicion de un nodo en su camino pesado se puede calcular a partir
de su profundidad en el arbol.

```c++
int const maxn = 100000;

int n;               // cantidad de nodos
vector<int> g[maxn]; // arbol como lista de adyacencia
int val[maxn];       // valor de cada nodo

int p[maxn];     // p[u] = padre de u en el arbol
int h[maxn];     // h[u] = hijo pesado de u (o -1 si no tiene)
int t[maxn];     // t[u] = tamaño de subarbol de u
int c[maxn];     // c[u] = comienzo del camino pesado al que pertenece u
int d[maxn];     // d[u] = profundidad de u en el arbol
vector<int> pre; // pre-orden

struct Segtree {
	vector<int> data;
	void init(int n) { /* ... */ }
	int query(int l, int r) { /* ... */ }
	int update(int i, int x) { /* ... */ }
};
Segtree ts[maxn];

void dfs(int u) {
	pre.push_back(u);
	t[u] = 1;
	for (int v : g[u]) if (v != p[u]) {
		p[v] = u;
		d[v] = d[u] + 1;
		dfs(v);
		t[u] += t[v];
	}
}

void decompose(int root) {
	forn(u, n) h[u] = -1;
	d[root] = 0;
	p[root] = -1;
	dfs(root);

	// asignamos ids a los caminos pesados
	// iteramos en preorden para poder propagar c[u] "hacia abajo"
	for (int v : pre) {
		if (int u = p[v]; u != -1 && t[v]*2 >= t[u]) {
			h[u] = v;
			c[v] = c[u];
		} else {
			c[v] = v;
		}
	}

	// construimos segment tree en cada camino pesado
	forn(u, n) if (c[u] == u) {
		int len = 1;
		for (int v = u; v != -1; v = h[v]) {
			len += 1;
		}
		ts[u].init(len);
		for (int v = u; v != -1; v = h[v]) {
			ts[u].update(d[v] - d[u], val[v]);
		}
	}
}
```

Una consulta sobre un camino se calcula recursivamente, separando en los casos
que hablamos antes.

```c++
int query(int u, int v) {
	if (c[u] == c[v]) { // camino contenido en un camino pesado
		int const w = c[u];
		int l = d[u] - d[w];
		int r = d[v] - d[w];
		if (l > r) swap(l, r);
		return ts[w].query(l, r+1);
	}

	if (d[c[u]] < d[c[v]]) { // c[v] es mas profundo
		return query(u, p[c[v]]) + query(c[v], v);
	} else {                 // c[u] es igual o mas profundo
		return query(u, c[u]) + query(p[c[u]], v);
	}
}
```

Esta estructura tambien permite actualizar los valores.

```c++
void update(int u, int x) {
	int w = c[u];
	ts[w].update(d[u] - d[w], x);
}
```

> Para soportar operaciones no conmutativas, en cada camino pesado hay que
> guardar un segment tree con los elementos en orden inverso.
>
> Despues, en el caso base de la consulta, se debe usar ese segment tree en
> orden inverso cuando `l > r` (aparte de ajustar los indices adecuadamente).
