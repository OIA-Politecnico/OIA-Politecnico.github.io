## Árboles recubridores

Un árbol recubridor es un subgrafo recubridor que es árbol.

Muchos problemas son más fáciles de resolver sobre árboles que sobre grafos generales. Algunas veces, para resolver un problema alcanza con resolverlo para algun subarbol recubridor particular.

Veamos algunos algoritmos para construir arboles recubridores interesantes.

### DFS-tree

Al hacer un DFS, "recorremos" algunas aristas. Estas aristas, junto a los
vertices que visitamos, forman un árbol recubridor llamado DFS-tree.

Si tomamos las aristas como dirigidas, este arbol queda enraizado en el vertice inicial del recorrido.

> 📝 propiedades, problemas 📝

```c++
struct arista { int u, v; };
vector<arista> dfs_tree;

bool visitado[MAXN];
void dfs(int u) {
  visitado[u] = true;
  for (int v : grafo[u]) {
    if (!visitado[v]) {
      dfs_tree.push_back({u, v});  // ***
      dfs(u);
    }
  }
}
```

### Kruskal

En un grafo ponderado es fácil armar el arbol recubridor de peso minimo (referido a la suma de todas sus aristas). A este lo llamamos arbol recubridor mínimo.

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

# 📝 Prim 📝

El algoritmo de Prim ofrece una forma alternativa de calcular el arbol
recubridor minimo de un grafo.

El algoritmo es casi identico al algoritmo de Dijkstra para calcular
distancias minimas.

> 📝 distancia min-max 📝
