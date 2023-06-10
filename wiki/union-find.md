Union find es una estructura de datos que soporta tres operaciones. Crear un nodo, conectar dos nodos, y consultar si dos nodos están conectados (incluso pasando por otros nodos).

La forma en que logramos esto es separando los nodos en grupos. Cada grupo tiene un "representante" o "dueño". Para saber si dos nodos están conectados basta con verificar que tengan el mismo representante.

Implementaremos un algoritmo eficiente para encontrar el representante de un nodo.

# Funcionamiento

Cada nodo tiene un "representante directo".

El representante de un grupo es su propio representante directo.

Para encontrar el representante de cualquier otro nodo, nos paramos en ese nodo y nos movemos al representante directo hasta llegar a un nodo que es su propio representante directo.

Por ejemplo, si los nodos 1, 3 y 7 forman un grupo, podriamos tener la siguiente situacion.

- el representante directo de 1 es 7
- el representante directo de 7 es 3
- el representante directo de 3 es 3 (si mismo)

Entonces, para encontrar el representante de 1, comenzamos en 1, pasamos a 7, luego a 3 y terminamos.

```c++
const int MAXN = 1000000;

int representante_directo[MAXN];

// inicializa la estructura de datos
void init() {
  for (int i = 0; i < MAXN; ++i)
    representante_directo[i] = i;
}

// devuelve el representante del grupo de i
// O(n)
int representante(int i) {
  int resultado = i;
  while (resultado != representante_directo[resultado]) {
    resultado = representante_directo[resultado];
  }
  return resultado;
}

// responde si dos nodos están conectados
// O(n)
bool conectado(int i, int j) {
  return representante(i) == representante(j);
}
```

Para conectar dos nodos, hacemos que el representante de uno de los grupos se vuelva representante de ambos.

Para lograr esto, hacemos que sea representante directo del viejo representante del otro grupo.

```c++
// conecta dos nodos
// O(n)
void conectar(int i, int j) {
  representante_directo[representante(i)] = representante(j);
}
```

# Compresión de caminos

El problema del algoritmo de arriba es que cada operación tiene complejidad `O(n)`. Esto se debe a que cada llamada a `representante` debe recorrer una cadena de representantes directos. Tras una serie de conexiones, es posible que queden cadenas de longitud `O(n)`.

Para evitar esto, aplicamos la técnica de compresión de caminos: cada vez que buscamos un representante, también hacemos que el representante del grupo sea representante directo de todos los nodos que tocamos.

Es decir, hacemos esta modificación a la función `representante`.

```c++
// devuelve el representante del grupo de i
// O(1) amortizado
int representante(int i) {
  int resultado = i;
  vector<int> camino;                                               // ***
  while (resultado != representante_directo[resultado]) {
    camino.push_back(resultado);                                    // ***
    resultado = representante_directo[resultado];
  }
  for (int nodo : camino) representante_directo[nodo] = resultado;  // ***
  return resultado;
}

```

Resulta que con este cambio, la función `representante` tiene complejidad `O(1)` amortizado. (osea, hacer n operaciones toma `O(n*1)` tiempo, aunque algunas operaciones pueden tomar mas que otras, incluso `O(n)`)

Con esto, todas las operaciones se vuelven `O(1)` amortizado.

> Esto es un poco mentira. La cota real es `O(alfa(n))` amortizado, donde alfa es la inversa de la función de Ackermann, asique podria ser mas alto cuando n es muy muy grande... pero alfa(1.000.000.000.000.000.000) es menor a 5 asique para fines prácticos es cierto.

# Implementación real

La implementación vista hasta ahora es puramente educativa. Para facilitar la escritura, se presenta una forma recursiva mucho mas corta.

```c++
const int MAXN = 1000000;
int uf[MAXN];

// O(1) amortizado
int find(int i) {
  if (uf[i] == i) return i;    // si es su propio representante directo, listo
  return uf[i] = find(uf[i]);  // si no, el representante directo pasa a ser el representante
}

// O(1) amortizado
void join(int i, int j) {
  uf[find(i)] = find(j);
}

// O(1) amortizado
bool conn(int i, int j) {
  return find(i) == find(j);
}
```

# extensión: tamaños de grupos

Se puede modificar el union-find para que mantenga el tamaño de cada grupo.

Para lograrlo, agregamos un array `tam` que, por cada representante de grupo, mantiene el tamaño de su grupo.

Para mantenerlo actualizado, modificamos `join`.

```c++
int uf_tm[MAXN];

// O(1) amortizado
int tam(int i) {
  return uf_tm[find(i)];
}

// O(1) amortizado
void join(int i, int j) {
  i = find(i); j = find(j);
  uf_tm[j] += uf_tm[i]; uf_tm[i] = 0; // ahora j es el representante de todos, asique "muevo" el tamaño de i hacia j.
  uf[i] = j;
}
```

# extension: miembros de grupos

Se puede modificar el union-find para mantenter los miembros de cada grupo, pero empeora un poco la complejidad.

Al apuntar un representante a otro, movemos los nodos de uno hacia el otro.

```c++
vector<int> uf_nodos;

// O(1) amortizado
int tam(int i) {
  return uf_nodos[find(i)].size();
}

// O(n)
void join(int i, int j) {
  i = find(i); j = find(j);
  if (i == j) return;

  for (int k : uf_nodos[i])
    uf_nodos[j].push_back(k);
  uf_nodos[i].clear();

  uf[i] = j;
}
```

El problema con esto es que tiene complejidad `O(n)`, debido al for que agregamos.

Para optimizarlo, hacemos que se muevan los nodos del grupo más chico hacia el más grande

```c++
// O(log(n))
void join(int i, int j) {
  i = find(i); j = find(j);
  if (i == j) return;

  if (tam(i) > tam(j))  // ***
    swap(i, j);         // ***

  for (int k : uf_nodos[i])
    uf_nodos[j].push_back(k);
  uf_nodos[i].clear();

  uf[i] = j;
}
```

Con este cambio logramos una complejidad de `O(log(n))` amortizado. (ejercicio: pensar por qué hacer n joins toma `O(n*log(n))` tiempo)


# Problemas

https://cses.fi/problemset/task/1666 - CSES Building Roads (resolver sin DFS, usando union-find)