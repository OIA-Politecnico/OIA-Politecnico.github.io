# Flujo

Todo lo que importa sobre flujo se puede aprender estudiando estos 5 problemas:

- Máximo flujo en una red de cañerías (max flow)
- Máxima cantidad de parejas dadas compatibilidades entre dos conjuntos (max matching)
- Conjunto cerrado por aristas, de máxima ganancia (min cut)
- Mínima cantidad de caminos para cubrir todos los nodos de un DAG (min path cover)
- Mínima cantidad de filas y columnas para cubrir todos los elementos de una matriz (min vertex cover)

## Max flow

Una red de flujo es un grafo dirigido con capacidades en las aristas, y dos nodos especiales s y t.

Queremos encontrar el flujo máximo que puede pasar de s a t.

O sea, para cada arista (u, v) tenemos una capacidad c(u, v) que indica cuánta cantidad de flujo puede pasar por esa arista.

Y queremos asignar un flujo f(u, v) a cada arista (u, v) de manera que:

- f(u, v) <= c(u, v)
- Para cada nodo intermedio u, la suma de los flujos que entran a u es igual a la suma de los flujos que salen de u.
- El flujo total que sale de s es máximo.
- Equivalentemente, el flujo total que entra a t es máximo.

Este problema se puede resolver usando el algoritmo de Ford-Fulkerson.

Iniciamos asignando un flujo 0 a todas las aristas.

Luego, mientras sea posible aumentar el flujo, lo aumentamos.

Para esto, podemos enviar flujo por una arista que tiene flujo < capacidad (o sea, que no está saturada), o retroceder por una arista que tiene flujo > 0.

Si al grafo le agregamos todas las aristas inversas, podemos buscar estos caminos con un DFS o BFS. (BFS es más eficiente)

Sorprendentemente este algoritmo completamente goloso es correcto.

### Red residual

Para que la implementación no necesite manejar por separado las aristas originales y las inversas, construimos la red residual:

Definimos la capacidad residual de una arista como r(u,v) = c(u,v) - f(u,v). En el algoritmo, al enviar flujo por una arista, disminuimos el flujo residual de la arista, y aumentamos el flujo residual de la arista inversa.

Como la capacidad no cambia, podemos calcular el flujo al final del algoritmo como f(u,v) = c(u,v) - r(u,v).

### Implementación

```c++

int const maxn = 100100;
int const maxm = 100100;

int n, m;
int s, t; // fuente y sumidero del flujo

vector<int> adj[maxn];         // aristas que salen de cada nodo
pair<int, int> nodes[maxm*2];  // arista i es nodes[i].fst -> nodes[i].snd
int inv[maxm*2];               // arista inversa de la arista i
int r[maxm*2];                 // flujo residual de la arista i
int c[maxm];                   // capacidad de la arista i (solo definido para aristas originales, no inversas)
int f[maxn];                   // flujo de la arista i

bool visited[maxn];            // visitado en el dfs

int dfs(int u, int flow) {
    if (u == t) return flow;
    visited[u] = true;
    for (int i : adj[u]) {
        int v = nodes[i].snd;
        if (!visited[v] && r[i] > 0) {
            int x = dfs(v, min(flow, r[i]));
            if (x > 0) {
                r[i] -= x;
                r[inv[i]] += x;
                return x;
            }
        }
    }
    return 0;
}

int max_flow() {
    int flow = 0;
    while (true) {
        memset(visited, false, sizeof(visited));
        int x = dfs(s, int(1e9));
        if (x == 0) break;
        flow += x;
    }
    return flow;
}

int main() {

    cin >> n >> m;
    for (int i = 0; i < m; ++i) {
        int j = i + m; // arista inversa

        int u, v, ci;
        cin >> u >> v >> ci;

        adj[u].push_back(i);
        adj[v].push_back(j);

        nodes[i] = {u, v};
        nodes[j] = {v, u};

        inv[i] = j;
        inv[j] = i;

        r[i] = ci;
        r[j] = 0;

        c[i] = ci;
    }

    cin >> s >> t;

    int flow = max_flow();

    for (int i = 0; i < m; ++i) {
        f[i] = c[i] - r[i];
        cout << f[i] << " \n"[i == m-1];
    }

    cout << flow << "\n";
}
```

## Max matching

Hay dos conjuntos de elementos (por ejemplo trabajadores y tareas), y queremos encontrar la máxima cantidad de parejas de elementos que pueden ser compatibles entre sí.

Muchos problemas sobre grafos bipartitos se pueden reducir a matching.

A su vez este problema se puede reducir a un problema de flujo máximo.

## Min cut

Nos dan un grafo dirigido con pesos en los nodos, y nos interesa encontrar el conjunto C de nodos que maximiza la suma de los pesos, bajo la restricción de que, si un nodo pertenece a C, entonces todos sus vecinos deben pertenecer a C.

Este se llama problema de la clausura máxima. Se puede reducir a un problema fuertemente relacionado con flujo máximo: el problema del corte mínimo.

### Corte mínimo

Consideremos una red de flujo con fuente s y sumidero t.

Dada una particion de los nodos en dos conjuntos S y T (donde s pertenece a S y t pertenece a T), el corte es el conjunto de aristas que tienen un extremo en S y el otro en T.

La capacidad del corte es la suma de las capacidades de las aristas que pertenecen al corte.

Resulta que la capacidad del corte mínimo es igual al flujo máximo que puede pasar de s a t.

### Reducción de clausura máxima a corte mínimo

- Tomamos el grafo original y agregamos un nuevo nodo s y un nuevo nodo t.

  El conjunto de nodos C se va a corresponder con el conjunto S de la particion del corte mínimo.

- Por cada arista (u, v) del grafo original, agregamos una arista (u, v) con capacidad "infinita" (o sea, muy muy grande).

 Entonces, cualquier corte minimo en la red va a respetar la restricción de que si un nodo pertenece a C, entonces todos sus vecinos deben pertenecer a C. (si no lo hiciera, cortaria una arista con capacidad infinita, lo cual lo haría no mínimo)

- Por cada nodo u con peso negativo w(u), agregamos una arista (u, t) con capacidad -w(u).

  Podemos interpretar esto como que, si un nodo u pertenece a C, entonces debe pagar un costo -w(u) para no pertenecer a C.

  Entonces, si un nodo u pertenece a C, su arista al sumidero t va a pertenecer al corte. Como estamos minimizando el corte, esto implicitamente minimiza el costo total de los nodos que pertenecen a C.

- Modelar los nodos con ganancia positiva es un poquito más indirecto:

  Agregamos una arista (s, u) con capacidad w(u).

  Esto se interpreta como que NO agarrar un nodo tiene un costo w(u).

  O sea, agarrarlo es gratis, pero si no lo agarramos, tenemos un costo w(u).

  Esto tiene el mismo efecto que en el problema original, pero tanto en el caso de agarrar como no agarrar, tenemos un costo w(u) adicional.

  Para corregir esto simplemente le restamos w(u) al costo total (despues de aplicar el algoritmo de corte mínimo).

### Implementación

```c++

struct MaxFlow {
    // Grafo que permite realizar el algoritmo de flujo máximo
    // La implementacion es la que vimos antes, pero encapsulada en una estructura

    void init(int n);
    void add_edge(int u, int v, int c);
    ll max_flow(int s, int t);
};

int const maxn = 100100;

int n, m;
int a[maxn];
vector<int> adj[maxn];

int main() {
    cin >> n >> m;

    forn(i, n) cin >> a[i];

    forn(i, m) {
        int u, v;
        cin >> u >> v; --u; --v;

        adj[u].push_back(v);
    }

    MaxFlow flow;
    flow.init(n+2);

    ll correction = 0;
    int s = n, t = n+1;
    forn(i, n) {
        if (a[i] < 0) flow.add_edge(i, t, -a[i]);
        if (a[i] > 0) flow.add_edge(s, i, a[i]), correction += a[i];
        for (int j : adj[i]) flow.add_edge(i, j, int(1e9));
    }

    cout << correction - flow.max_flow(s, t) << "\n";
    return 0;
}
```

Esta implementacion funciona para encontrar el valor de la clausura máxima, pero no para encontrar el conjunto C.

Es posible reconstruir la particion del corte mínimo a partir de los flujos de las aristas del grafo. (y por lo tanto el conjunto C)

> TODO: explicar como reconstruir la particion del corte mínimo

## Min path cover

Un path cover es un conjunto de caminos que cubren todos los nodos de un grafo.

Se puede reducir a un problema de flujo máximo.

- Teorema de Dilworth: El tamaño del path cover mínimo es igual al número de elementos de la cadena más larga en el orden parcial de los nodos.

La construcción es partiendo cada nodo u en dos nodos u1 y u2.

Cada arista (u, v) del grafo original la convertimos en una arista (u1, v2).

Ahora, la mínima cantidad de caminos que cubren todos los nodos es igual al matching máximo en el grafo bipartito formado por los nodos u1 y u2.

También se puede reconstruir el path cover a partir del matching.

> TODO: explicar como reconstruir el path cover a partir del matching

## Min vertex cover

Consideremos una matriz booleana de NxM.

Nos interesa encontrar el conjunto mínimo de filas y columnas que cubren todos los 1s de la matriz.

### Solucion

Consideremos el grafo bipartito formado por las filas y columnas de la matriz.

Cada 1 de la matriz representa una arista entre una fila y una columna.

El objetivo es encontrar el minimo conjunto de nodos tal que toda arista tenga al menos un extremo en el conjunto.

Este problema es conocido, y se conoce como min vertex cover.

Es NP-hard en grafos generales.

Pero para el caso particular de grafos bipartitos, el tamaño del vertex cover mínimo es igual al del matching máximo.

> TODO: explicar por que es igual al matching máximo
>
> El resultado se llama teorema de Konig.
>
> Podemos demostrar que |min vertex cover| <= |max matching| por teorema de Hall.

También se puede reconstruir el vertex cover a partir del matching.

### Reconstrucción

Brevemente, es greedy.

- Cada arista del matching tendrá exactamente un extremo en el vertex cover.

- Cada nodo que no pertenece al matching, tampoco pertenece al vertex cover.

Estas dos reglas basicamente alcanzan para reconstruir el vertex cover.

Cada nodo fuera del matching, NO pertenece al vertex cover. Cada vecino de
este nodo tiene que pertenecer al vertex cover (o la arista que los conecta no
estaría cubierta).

Pero resulta que ese vecino necesariamente tiene que pertenecer al matching
(se demuestra por contradicción. Si no, habría un camino aumentante, y el
matching no sería máximo).

Entonces, por la primera regla, la pareja de ese nodo no pertenece al vertex cover.

Y entonces sus vecinos necesariamente tienen que pertenecer al vertex cover.

Y así sucesivamente.

Esto resuelve las componentes que tienen nodos fuera del matching.

Si hay una componente conexa que todos sus nodos pertenecen al matching,
entonces pintamos todos los nodos del mismo lado del grafo bipartito, y listo.

> TODO: mejorar la explicación

> TODO: explicar por que funciona

> TODO: implementar la reconstrucción