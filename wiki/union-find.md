# Union-find

El problema de la conectividad en grafos plantea la cuestion de responder rapidamente si dos nodos de un grafo estan conectados. Una forma de resolver este problema es separar el grafo en componentes conexas, pintar cada una de un color distinto, y plantear que dos nodos estan conectados si tienen el mismo color. Si tenemos un grafo con N nodos, M aristas y se hacen Q consultas, este algoritmo tiene complejidad O(N+M+Q), que es la menor posible.

Esto se vuelve mas dificil si aparte de responder consultas de conectividad se intercalan U operaciones de agregar aristas. Como primera solución podemos implementar las operaciones tal cual son (agregar una arista a la lista de adyacencia), y hacer un DFS para responder cada consulta de conectividad. Esta solución tendría complejidad O((N+M)\*Q+U). ¿Podemos hacerlo más rápido?

## Solución más eficiente

Para hacerlo más rápido volvemos a la idea de separar por componentes. Solo hace falta una forma rápida de verificar si dos nodos pertenecen a la misma componente y una forma rápida de combinar dos componentes.

La forma en que logramos esto es manteniendo un nodo especial en cada componente conexa, al que llamamos representante, y el cual será posible encontrar eficientemente partiendo desde cualquier nodo de la componente. Para saber si dos nodos están en la misma componente conexa basta con verificar que el representante de sus componentes sea el mismo.

Cada nodo tiene un representante. El representante de una componente es el unico nodo de la componente que es su propio representante. Para encontrar el representante de una componente podemos pararnos en cualquier nodo de la componente y movernos al representante hasta llegar a un nodo que es su propio representante.

Por ejemplo, si los nodos 1, 3 y 7 forman una componente, podriamos tener la siguiente situacion:

- el representante de 1 es 7
- el representante de 7 es 3
- el representante de 3 es 3 (si mismo)

Entonces, para encontrar el representante de la componente al que pertenece 1 comenzamos en 1, pasamos a 7 y luego a 3, dónde terminamos.

```c++
int rep[MAXN];

// inicializa la estructura de datos
void init() {
  for (int i = 0; i < MAXN; ++i)
    rep[i] = i;
}

// devuelve el representante de la componente de i
// O(n)
int find(int i) {
  int r = i;
  while (r != rep[r]) r = rep[r];
  return r;
}

// responde si dos nodos están conectados
// O(n)
bool conectado(int i, int j) {
  return find(i) == find(j);
}
```

Para combinar dos componentes, hacemos que el representante de una componente se vuelva representante de ambas. Esto se hace haciendo que el nodo representante de una componente sea el representante del nodo representante de la otra componente.

```c++
// conecta dos nodos
// O(n)
void conectar(int i, int j) {
  rep[find(i)] = find(j);
}
```

## Compresión de caminos

El problema del algoritmo de arriba es que, como cada llamada a `find` recorre una cadena de representantes (que puede llegar a medir O(N) en algunos casos), todas las operaciones tienen costo O(N).

Para evitar esto, aplicamos la técnica de compresión de caminos: cada vez que buscamos un representante, también hacemos que el representante de la componente sea representante directo de todos los nodos que tocamos. Así, nos ahorramos caminar toda esa cadena la proxima vez que necesitemos saber el representante de algún nodo de la cadena.

Es decir, hacemos esta modificación a la función `find`.

```c++
// devuelve el representante de la componente de i y
// comprime el camino desde i hasta él
// O(1) amortizado
int find(int i) {
  int r = i;
  while (r != rep[r]) r = rep[r];
  while (i != rep[i]) i = exchange(rep[i], r); // agregamos esta linea
  return r;
}

// referencia de la funcion exchange
// https://es.cppreference.com/w/cpp/utility/exchange
```

Resulta que con este cambio, la función `representante` tiene complejidad O(1) amortizado. (osea, hacer Q operaciones toma O(Q) tiempo, aunque algunas operaciones pueden tomar mas que otras, incluso O(Q)). Con esto, todas las operaciones se vuelven `O(1)` amortizado.

> Esto es un poco mentira. La cota real es `O(alfa(n))` amortizado, donde alfa es la inversa de la función de Ackermann, asique podria ser mas alto cuando n es muy muy grande... pero alfa(1.000.000.000.000.000.000) es menor a 5 asique para fines prácticos es cierto.

## Implementación corta para competencias

Hay una forma recursiva mucho mas corta:

```c++
int rep[MAXN];

void init() {
  for (int i = 0; i < MAXN; ++i)
    rep[i] = i;
}

int find(int i) {
  if (rep[i] != i) rep[i] = find(rep[i]);
  return rep[i];
}

void join(int i, int j) {
  rep[find(i)] = find(j);
}

bool conn(int i, int j) {
  return find(i) == find(j);
}
```

### Problemas

- <https://cses.fi/problemset/task/1666> (resolver sin DFS, usando union-find)

## Extensión: tamaños de componentes

Se puede modificar el union-find para que mantenga el tamaño de cada componente. Para lograrlo, agregamos un array `tam` que, por cada representante de componente, mantiene el tamaño de su componente.

```c++
int tam[MAXN];

// O(1) amortizado
int tam_comp(int i) {
	return tam[find(i)];
}
```

Para mantenerlo actualizado, modificamos `join`:

```c++
// O(1) amortizado
void join(int i, int j) {
  i = find(i); j = find(j);
  if (i == j) return; // ya están en la misma componente, no hago nada
  rep[i] = j;

  tam[j] += tam[i]; // j ahora es representante de todos, le agrego el tamaño de i
  tam[i] = 0;       // i ya no es mas representante, lo pongo en cero para no confundirme
}
```

## Extensión: miembros de componentes

Se puede modificar el union-find para mantenter los miembros de cada componente, pero empeora un poco la complejidad. Al apuntar un representante a otro, movemos los nodos de uno hacia el otro.

Si lo hacemos sin cuidado volvemos a caer en complejidad O(N). Para optimizarlo, tomamos la precaucion de siempre mover los nodos de la componente más chica hacia la más grande. Si bien esto parece un detalle menor, en realidad asegura que tengamos complejidad O(log(N)) amortizado.

```c++
// O(log(n))
void join(int i, int j) {
  i = find(i); j = find(j);
  if (i == j) return;
  rep[i] = j;

  if (nodos[i].size() > nodos[j].size()) swap(i, j);

  for (int k : nodos[i])
    nodos[j].push_back(k);
  nodos[i].clear();
}
```

- ejercicio: (\*) ¿Por qué hacer N joins con este algoritmo solo toma `O(N*log(N))` tiempo?

