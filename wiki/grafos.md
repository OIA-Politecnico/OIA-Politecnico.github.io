> Esta sección está en construcción

Se dió una clase virtual el 1ro de Septiembre de 2022.

 - [grabación](https://youtu.be/LwBZqpEdem4)
 - [diapositivas](https://raw.githubusercontent.com/SebastianMestre/taller-oia/master/Diapositivas/2022-09-01%20Grafos%20Arboles%20DFS%20BFS%20Dijkstra%20FloodFill.pdf)

# Definiciones

> TODO: grafo dirigido, paralelas, bucles, antiparalelas, grafo simple, grafo ponderado, caminos (dirigidos), ciclos (dirigidos), longitud, distancia, grado, conectividad, alcanzabilididad, componentes (fuertemente) conexas, cota sobre aristas

- Un grafo es un objeto matemático compuesto de vertices (puntitos) y aristas (lineas que conectan vértices).
- Un grafo es subgrafo de otro cuando se puede obtener borrando algunos vertices y algunas aristas.
- Un subgrafo es recubridor si se puede obtener sin borrar vértices.

## Árboles

definicion, definiciones equivalentes, hojas y raices, enraizamiento

## DAGs

definicion, conexion con DP (?)

## Planaridad

definición, identidad de euler (?), cotas sobre aristas

# representaciones

## lista de adyacencia

```c++
const int MAXN = ...;
vector<int> grafo[MAXN];

// insertar arista (u->v)  --  O(1)
grafo[u].push_back(v);

// borrar arista (u->v) -- O(grado de u)
grafo[u].erase(find(grafo[u].begin(), grafo[u].end(), v));
// alternativamente, haciendo un for sobre grafo[u]

// visitar vecinos de u  --  O(grado de u)
for (int v : grafo[u])
    visitar(v);
```

Si queremos eliminar aristas rápido, cambiamos la representación. Ojo! vector es bastante más rápido en las otras operaciones.

```c++
const int MAXN = ...;
set<int> grafo[MAXN];

// insertar arista (u->v)  --  O(log(N))
grafo[u].insert(v);

// borrar arista (u->v)  --  O(log(N))
grafo[u].erase(v);

// visitar vecinos de u  --  O(grado de u)
for (int v : grafo[u])
    visitar(v);
```

## matriz de adyacencia

```c++
const int MAXN = ...;
bool grafo[MAXN][MAXN];

// insertar arista (u->v)  --  O(1)
grafo[u][v] = true;

// borrar arista (u->v)  --  O(1)
grafo[u][v] = false;

// visitar vecinos de u  --  O(N)
for (int v = 0; v < N; ++v)
    if (grafo[u][v]) visitar(v);
```

## lista de aristas

```c++
struct arista { int u, int v; };

vector<arista> grafo;

// insertar arista (u->v)  --  O(1)
grafo.push_back({u, v});

// borrar arista (u->v) -- O(M)
grafo.erase(find(grafo.begin(), grafo.end(), arista{u,v}));
// alternativamente, haciendo un for sobre grafo

// visitar vecinos de u  --  O(M)
for (arista e : grafo)
    if (e.u == u) visitar(e.v);
```

Si queremos eliminar aristas rápido, cambiamos la representación. Ojo! vector es bastante más rápido en las otras operaciones.

```c++
struct arista { int u, int v; };
bool operator< (arista a, arista b) { // necesario para poder usar set<arista>
    return make_pair(a.u, a.b) < make_pair(b.u, b.v);
}

set<arista> grafo;

// insertar arista (u->v)  --  O(log(M))
grafo.insert({u, v});

// borrar arista (u->v) -- O(log(M))
grafo.erase({u, v});

// visitar vecinos de u  --  O(M)
for (arista e : grafo)
    if (e.u == u) visitar(e.v);
```

# algoritmos

## recorridos

Un recorrido es un orden de los vértices de un grafo que tiene alguna característica especial

Nos permiten procesar los vértices y aristas en órdenes específicos, partiendo de un vértice: “el origen”. Los principales recorridos son:

- en profundidad (“DFS”): avanza hasta atorarse, después retrocede y vuelve a avanzar.
- en anchura (“BFS”): visita los que están a 1 paso, después a 2, etc.
- en distancia (“SPF” o “Dijkstra”): visita en orden de distancia según los pesos.

Si todas las aristas tienen el mismo peso, el recorrido en distancia es equivalente al recorrido en anchura.

Los tres tipos tipos de recorridos se pueden expresar con este pseudocódigo. El tipo de bolsa que usemos determina cuál recorrido se hace.

```
recorrer(src) {
  b = crear_bolsa()
  insertar_bolsa(b, src)
  mientras b no está vacía {
    u = extraer_bolsa(b)
    marco u como visitado
    por cada v, vecino de u que no fue visitado {
      insertar_bolsa(b, v)
    }
  }
}
```


### DFS

recorrido en profundidad

Complejidad: `O(N+M)`

```c++
void dfs(int s) {
    fill(visitado, visitado+N, false);
    stack<int> b;
    b.push(s);
    while (!b.empty()) {
        int u = b.top(); b.pop();
        if (visitado[u]) continue;
        visitado[u] = true;
        for (int v : grafo[u]) {
            b.push(v);
        }

        cout << u << “\n”;
    }
}
```

### BFS

recorrido en anchura

Complejidad: `O(N+M)`

```c++
void bfs(int s) {
    fill(visitado, visitado+N, false);
    queue<int> b;
    b.push(s);
    while (!b.empty()) {
        int u = b.front(); b.pop();
        if (visitado[u]) continue;
        visitado[u] = true;
        for (int v : grafo[u]) {
            b.push(v);
        }

        cout << u << “\n”;
    }
}
```

### Dijkstra

recorrido en distancia

Complejidad: `O((N+M)*log(M))`

## Varios

### Flood fill

Para separar un grafo en componentes conexas, hacemos una serie de recorridos. Luego de cada recorrido, la componente conexa del vertice origen queda completamente marcada. Aprovechamos esto para no volver a visitarla. Así, terminamos haciendo un recorrido por componente, visitando cada vértice una sola vez.

Complejidad: `O(N+M)`

```c++
int cantidad_de_componentes = 0;
for (int u = 0; u < N; ++u) {
    if (!visitado[u]) {
        dfs(u);
        cantidad_de_componentes++;
    }
}
```

## Árboles recubridores

Un árbol recubridor es un subgrafo recubridor que es árbol.

Muchos problemas son más fáciles de resolver sobre árboles que sobre grafos generales. Algunas veces, para resolver un problema alcanza con resolverlo para algun subarbol recubridor particular.

Veamos algunos algoritmos para construir arboles recubridores interesantes.

### DFS-tree

Al hacer un DFS, en el momento que agregamos un vértice a la pila (o hacemos la llamada recursiva, en la implementación recursiva), "recorremos" algunas aristas. Estas aristas, junto a los vertices que visitamos, forman un árbol llamado DFS-tree.

Si tomamos las aristas como dirigidas, este arbol queda enraizado en el vertice inicial del recorrido.

> TO-DO: propiedades, problemas

```c++
struct arista { int u, v;
vector<arista> dfs_tree;

bool visitado[MAXN];
void dfs(int s) {
  stack<int> b;
  b.push(s);
  visitado[s] = true;
  while (!b.empty()) {
    int u = b.top(); b.pop();
    for (int v : grafo[u]) {
      if (visitado[v]) continue;  
      b.push(v);
      visitado[v] = true;

      dfs_tree.push_back({u, v});    // ***
    }
  }
}
```

Se puede hacer algo análogo con el recorrido BFS y el de Dijkstra, pero los arboles que quedan no tienen tantas aplicaciones como el DFS-tree.

### Kruskal

En un grafo ponderado es fácil armar el arbol recubridor de peso minimo (referido a la suma de todas sus aristas). A este lo llamamos arbol recubridor mínimo (ing. Minimum Spanning Tree).

Para hacerlo usamos el algoritmo de Kruskal

La idea es simple: iteramos por las aristas de menor a mayor peso. Si una arista conecta nodos que todavia no están conectados, la agregamos al arbol. Caso contrario, la ignoramos.

Para hacer esos chequeos de "están conectados o no", usamos [union find]( union-find )

```c++
struct arista { int u, v, peso; };

// esto hace que sort sepa como ordenar aristas
bool operator< (arista a, arista b) {
  return a.peso < b.peso;
}

// devuelve las aristas del arbol recubridor minimo
vector<arista> kruskal(vector<arista> grafo) {

  vector<arista> arbol;

  uf_init(); // inicializo el union-find

  sort(grafo.begin(), grafo.end());

  for (arista e : grafo) {
    if (uf_conn(e.u, e.v)) continue; // si no conecta nada nuevo, la ignoro

    arbol.push_back(e);
    uf_join(e.u, e.v); // le aviso al union-find que u y v están conectados
  }

  return arbol;
}
```

# Prim

> TO-DO
