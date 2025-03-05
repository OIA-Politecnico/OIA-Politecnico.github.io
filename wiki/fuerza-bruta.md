
# Fuerza bruta

Fuerza bruta o "busqueda exhaustiva" es la idea de probar todas las opciones y
tomar la mejor.

Por ejemplo, para encontrar el par de elementos cuyo producto es lo mas grande
posible podemos probar todas las parejas.

```c++
pair<int,int> mejor = {-1, -1}
int puntaje_mejor   = -1;
forn(i, n) forn(j, i) {
	int puntaje = a[i] * a[j];
	if (puntaje > puntaje_mejor) {
		puntaje_mejor = puntaje;
		mejor = {i, j};
	}
}
```

Hay formas mas comodas de codearlo: con `tuple` podemos usar la funcion `max()`.

```c++
tuple<int, int, int> mejor = {-1, -1, -1};
forn(i, n) forn(j, i)
	mejor = max(mejor, {a[i] * a[j], i, j});
```

Pero hay fuerzas brutas más complicadas. Por ejemplo, que pasa si hay que probar
todas las combinaciones de 10 elementos. ¿Escribimos 10 bucles anidados? ¿Y si
la cantidad de elementos depende de la entrada?

### Todas las combinaciones

Para probar todas las posibles combinaciones podemos aprovechar que los numeros
se guardan en binario.

```c++
forn(s, (1<<n)) {
	forn(i, n) if (s&(1<<i)) cout << " " << i;
	cout << "\n";
}
// si n = 3 imprime:
//
// 0
// 1
// 0 1
// 2
// 0 2
// 1 2
// 0 1 2
```

### Todas las combinaciones de tamaño fijo

Si queremos solo las combinaciones de cierta cantidad de elementos podemos
filtrar usando `__builtin_popcount()`, que devuelve la cantidad de bits
prendidos de un numero.

```c++
forn(s, (1<<n)) if (__builtin_popcount(s) == 2) {
	forn(i, n) if (s&(1<<i)) cout << " " << i;
	cout << "\n";
}
// si n = 3 imprime:
// 0 1
// 0 2
// 1 2
```

### Todas las permutaciones

Para probar todas las permutaciones podemos usar `next_permutation`, de la
biblioteca estandar.

```c++
vector<int> p(n);
forn(i, n) p[i] = i;
do {
	forn(i, n) cout << " " << p[i];
	cout << "\n";
} while (next_permutation(begin(p), end(p)));
// si n = 3 imprime:
// 0 1 2
// 0 2 1
// 1 0 2
// 1 2 0
// 2 0 1
// 2 1 0
```

## Busquedas eficientes

En los ejemplos de arriba hacemos la implementacion mas corta posible para no
perder tiempo. Pero estas implementaciones no son tan eficientes. Por ejemplo,
para iterar por las combinaciones de un cierto tamaño iteramos por todas las
`2^N` combinaciones posibles y filtramos las del tamaño deseado.

En cambio podemos diseñar programas que recorren solo los elementos deseados.
Estos programas muchas veces son recursivos.

Por ejemplo para iterar por todas las combinaciones de tamano k entre n
elementos:

```c++
vector<int> elementos;
int probar(int n, int k) {
	if (n == 0) {
		if (k == 0) {
			for (int x : elementos) cout << " " << x;
			cout << "\n";
		}
	} else {
		elementos.push_back(n - 1);
		probar(n - 1, k - 1); // agarro el elemento n-1
		elementos.pop_back();
		if (n > k) probar(n - 1, k); // no lo agarro
	}
}
// al llamar probar(3, 2) imprime:
// 2 1
// 2 0
// 1 0
```

Otro punto: si iteramos por todas las permutaciones y procesamos cada una vamos
a tener costo `O(N! * N)`. En cambio, si las construimos recursivamente, podemos
compartir computos entre las permutaciones que estan en la misma rama. Asi,
muchas veces podemos bajar el costo a `O(N!)`.

```c++
int mejor_valor = 0;

vector<int> p(n);
forn(i, n) p[i] = i;
do {
	int valor = 0;
	forr(i, 1, n) valor += p[i-1] * p[i];
	mejor_valor = max(mejor_valor, valor);
} while (next_permutation(begin(p), end(p)));
```


```c++
int valor = 0;
int mejor_valor = 0;

int n;
vector<int> p;
void iniciar() {
	p.resize(n);
	forn(i, n) p[i] = i;
}
void probar(int i) {
	if (i == n) {
		mejor_valor = max(mejor_valor, valor);
		return;
	}
	for (int j = i; j < n; ++i) {
		swap(p[i], p[j]);
		if (i > 0) valor += p[i-1] * p[i];

		probar(i+1);

		if (i > 0) valor -= p[i-1] * p[i];
		swap(p[i], p[j]);
	}
}
```

Otro truco seria cortar ramas si podemos ir dandonos cuenta que es imposible que
superen la mejor solucion encontrada hasta el momento. Esta es la idea
fundamental detras del [backtracking]( backtracking ), una tecnica un poco mas
avanzada.
