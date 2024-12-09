# Recorridos en grafos

Un recorrido es un orden de los vértices de un grafo, que tiene alguna
característica especial.

Nos permiten procesar los vértices y aristas en órdenes específicos, partiendo
de un vértice distinguido, que llamamos "origen". Los principales recorridos
son:

- en profundidad (DFS): avanza por un camino arbitrario hasta atorarse, después
  retrocede hasta encontrar un camino no explorado y vuelve a avanzar.
- en anchura (BFS): visita los vértices que están a un paso del origen, después
  a los que están a dos, a tres, etc.
- en distancia (SPF o Dijkstra): En un grafo ponderado, visita los vértices en
  orden de distancia al origen, según los pesos de las aristas.
- en distancia min-max (Prim): En un grafo ponderado, visita los vértices en
  orden de distancia min-max al origen, según los pesos de las aristas.

> TODO: explicar distancia min-max o sacarlo (no es tan importante)

Si todas las aristas tienen el mismo peso, el recorrido en distancia es
equivalente al recorrido en anchura.

## Recorridos con bolsas

Hay varios recorridos se pueden expresar con este pseudocódigo. El tipo de bolsa
que usemos determina cuál recorrido se hace:

```
recorrer(src) {
  b = crear_bolsa()
  insertar_bolsa(b, src)
  mientras b no está vacía {
    u = extraer_bolsa(b)
    si u fue visitado lo salteo
    marco u como visitado
    por cada v, vecino de u {
      insertar_bolsa(b, v)
    }
  }
}
```

### Aplicacion: *flood fill*, separar en componentes conexas

Es notable que un recorrido con bolsa siempre visita todos los nodos que son
alcanzables desde `src`. (su componente conexa si el grafo no es dirigido)

Esto tiene una consecuencia inmediata: para separar un grafo en componentes
conexas, basta con hacer una serie de recorridos, uno por cada nodo que no haya
sido visitado en un recorrido anterior.

```c++
int cantidad_de_componentes = 0;
for (int u = 0; u < N; ++u) {
    if (!visitado[u]) {
        recorrer(u);
        cantidad_de_componentes++;
    }
}
```

Esto puede parecer O(N^2) pero en realidad no lo es!

Como solo lanzamos recorridos en vertices no visitados, cada componente se
recorrerá una sola vez, por lo que cada vertice se visitará una sola vez,
y tendremos complejidad `O(N+M)`.

### DFS y BFS como recorridos con bolsa

```c++
void dfs(int s) {
    stack<int> b;
    b.push(s);
    while (!b.empty()) {
        int u = b.top(); b.pop();
        if (visitado[u]) continue;
        visitado[u] = true;
        for (int v : grafo[u]) b.push(v);
        cout << u << "\n";
    }
}

void bfs(int s) {
    queue<int> b;
    b.push(s);
    while (!b.empty()) {
        int u = b.front(); b.pop();
        if (visitado[u]) continue;
        visitado[u] = true;
        for (int v : grafo[u]) b.push(v);
        cout << u << "\n";
    }
}
```

Acá mostramos solamente el uso de pilas y colas para lograr recorridos DFS y BFS
respectivamente, pero variando la bolsa se pueden lograr recorridos muy
interesantes. Esto es especialmente útil para construir recorridos "máximos" y
"mínimos".

Por ejemplo, podriamos insertar los nodos a la bolsa acompañados de un número
y usar una bolsa que siempre nos devuelva el nodo cuyo número sea mínimo.

Este número se podría ser la suma de pesos de las aristas que se tomaron en el
recorrido hasta llegar al nodo. (En este caso logramos un algoritmo que
encuentra caminos de peso mínimo, conocido como algoritmo de Dijkstra), o podría
ser el peso de la arista más pesada que se tomó para llegar al nodo (En este
caso logramos otro algoritmo conocido, que calcula caminos "min-max").

Es aún más interesante cuando ajustamos el funcionamiento de la bolsa o los
valores que insertamos acorde al problema que estamos resolviendo.

### Problemas

- [OIA Nivel 3 Nacional - Número de Erdos-Darwin]( https://juez.oia.unsam.edu.ar/task/53 )
- [CSES - Building Roads](https://cses.fi/problemset/task/1666)
- [CSES - Message Route](https://cses.fi/problemset/task/1667)
- [CSES - Shortest Routes I](https://cses.fi/problemset/task/1671)
- (\*) [CSES - Monsters](https://cses.fi/problemset/task/1194/)

## DFS típico

Si bien el código de arriba implementa un recorrido DFS, esa no es la forma más
común de lograrlo. En cambio, solemos usar recursión para lograr un código más
corto y más fácil de tunear.

```c++
void dfs(int u) {
  visitado[u] = true;
  for (int v : grafo[u]) {
    if (!visitado[v]) {
      dfs(v);
    }
  }
}
```

Una de las ventajas de esto es que ahora tenemos en el codigo un lugar
correspondiente al momento *ANTES* de que se visiten los vecinos y otro
correspondiente al momento *DESPUÉS* de que se visiten todos los vecinos.

Esto es útil un muchos algoritmos (órden topológico, puentes, puntos críticos,
componentes biconexas, fuertemente conexas, etc.)

### Orden topológico

El orden topológico de un grafo dirigido sin ciclos es una permutación de los
vértices donde cada vértice aparece antes que todos los vértices a hacia los que
tiene aristas (todas las aristas van de izquierda a derecha).

En un DFS no podemos garantizar que al procesar un nodo u no se haya todavia
procesado ninguno de sus vecinos, pero sí podemos garantizar un procesamiento
DESPUÉS de que se haya procesado todos los vecinos. Esto nos permite construir
un órden topologico inverso. Posteriormente lo podemos dar vuelta y obtener un
orden topológico.

```c++
int n;
vector<int> g[MAXN];

vector<int> topologico_inverso;
void dfs(int u) {
  visitado[u] = true;
  for (int v : grafo[u]) {
    if (!visitado[v]) {
      dfs(v);
    }
  }
  topologico_inverso.push_back(u);
}

vector<int> orden_topologico() {
  for (int u = 0; u < n; ++i) {
    if (!visitado[u]) {
      dfs(u);
    }
  }
  vector<int> topologico = topologico_inverso;
  reverse(begin(topologico), end(topologico));
  return topologico;
}
```
