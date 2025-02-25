# Policy based data structures

Policy based data structures es una extensión oculta del compilador GCC. Trae estructuras de datos parecidas a las de STL pero con algunas capacidades especiales.

Por ejemplo, en PBDS hay una estructura estilo `std::set` pero que aparte permite consultar

- el i-esimo elemento de menor a mayor en tiempo O(log N)
- la cantidad de elementos menores a un valor en tiempo O(log N)

La forma recomendada de usarlas es la siguiente:

```c++
#include <ext/pb_ds/assoc_container.hpp> 
using namespace __gnu_pbds;
template<typename Key, typename Val=null_type>
using indexed_set = tree<Key, Val, less<Key>, rb_tree_tag,
                         tree_order_statistics_node_update>;
```

Definiendolo asi se puede usar de la siguiente manera:

```c++
indexed_set<int> A;
A.insert(42);
A.insert(37);
int val = *s.find_by_order(1); // acceso por indice, da 42
int idx = s.order_of_key(37); // cantidad de elementos menores, da 0
int idx = s.order_of_key(38); // da 1
int idx = s.order_of_key(42); // da 1
int idx = s.order_of_key(43); // da 2
```

Las PBDS tienen un gran defecto: no se pueden swappear eficientemente usando la funcion `swap()`. En C++ cualquier estrucutra de la STL se pude swappear en O(1):

```c++
set<int> A, B;
for (int i = 0; i < 1000000; ++i) {
  A.insert(rand());
  B.insert(rand());
}
swap(A, B); // O(1)
```

En cambio las PBDS se swappean en O(N)

```c++
indexed_set<int> A, B;
for (int i = 0; i < 1000000; ++i) {
  A.insert(rand());
  B.insert(rand());
}
swap(A, B); // O(N)
```

Por suerte tienen una forma de swappear eficientemente:

```c++
A.swap(B); // O(1)
```

Esto es importantisimo al hacer problemas con la tecnica small-to-large.

Por ejemplo, consideremos un problema donde nos dan un arbol con valores en los nodos (`val[u]`) donde nos hacen consultas del estilo "`query(u, x)` = cantidad de valores distintos menores a x en el subarbol de u"

Despues de separar las queries por nodo, podemos resolver haciendo un small-to-large:

```c++
indexed_set<int> conj[MAXN];
int val[MAXN];

vector<int> queries_nodo[MAXN];
pair<int,int> queries[MAXQ];
int ans[MAXQ];

void dfs(int u, int p) {
  conj[u].insert(val[u]);

  for (int v : g[u]) if (v != p) {
    if (conj[v].size() > conj[u].size()) {
      conj[v].swap(conj[u]); // si usamos std::swap() da time limit
    }
  }

  for (int v : g[u]) if (v != p) {
    for (int x : conj[v]) {
      conj[u].insert(x);
    }
  }

  for (int i : queries_nodo[u]) {
    int x = queries[i].second;
    ans[i] = conj[u].order_of_key(x);
  }
}
```
