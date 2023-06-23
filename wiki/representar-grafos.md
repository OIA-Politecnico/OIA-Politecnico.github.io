
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
for (int v : grafo[u]) visitar(v);
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
for (int v : grafo[u]) visitar(v);
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
for (int v = 0; v < N; ++v) if (grafo[u][v]) visitar(v);
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
for (arista e : grafo) if (e.u == u) visitar(e.v);
```

