# Árboles recubridores

Un árbol recubridor es un subgrafo recubridor que es árbol.

Muchos problemas son más fáciles de resolver sobre árboles que sobre grafos generales. Algunas veces, para resolver un problema alcanza con resolverlo para algun subarbol recubridor particular.

Veamos algunos algoritmos para construir arboles recubridores interesantes.

## DFS-tree

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

## Arbol recubrido mínimo: algoritmo de Kruskal

En un grafo ponderado es posible armar el arbol recubridor de peso minimo (referido a la suma de todas sus aristas). A este lo llamamos arbol recubridor mínimo.

Para hacerlo usamos el algoritmo de Kruskal

Iteras por las aristas de menor a mayor peso, agergandolas a un nuevo grafo. Si agregarla no genera ciclo, la agrego (chequear con [union find]( union-find )).


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
  sort(begin(grafo), end(grafo));
  for (arista e : grafo) {
    if (uf_conn(e.u, e.v)) continue; // si genera ciclo, la ignoro
    arbol.push_back(e);
    uf_join(e.u, e.v); // conecto u y v en el union-find
  }
  return arbol;
}
```


### Algunas cuestiones sobre Kruskal (para reflexionar)

- Por que está garantizado que el resultado es conexo si el grafo es conexo?

- Por qué está garantizado que el resultado es árbol si el grafo es conexo?

Esas dos condiciones juntas significan que encuentra un árbol recubridor

- Por qué está garantizado que la arista mas pesada del grafo -- llamemosla (u,v) -- no se usa si existe un camino u--v que usa solo aristas mas livianas?

- Un poco mas generalmente: Si existe un camino (u,v) usando solo aristas de peso \<x en el grafo, también existe un camino (u,v) con la misma propiedad en el resultado de kruskal. ¿Por qué? (distancia min-max)

- Por qué está garantizado que encuentra el árbol que minimiza la suma de aristas (arbol recubridor minimo)?

### Problema para pensar:

Te dan un grafo ponderado. Separar las aristas en tres grupos.

- Las que no pertenecen a ningun MST
- Las que pertenecen a algunos MST
- Las que pertenecen todos los MST

## 📝 Prim 📝

El algoritmo de Prim ofrece una forma alternativa de calcular el arbol
recubridor minimo de un grafo.

El algoritmo es casi identico al algoritmo de Dijkstra para calcular
distancias minimas.

> 📝 distancia min-max 📝
