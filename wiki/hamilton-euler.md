<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script src="mathjax-config.js"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Caminos Eulerianos y Hamiltonianos

## Camino Hamiltoniano

Encontrar un ciclo simple o camino simple que usa todos los vértices de un grafo
simple conexo

Este problema es [NP-Completo]( complejidad#np-completos ), por lo que no hay
solución eficiente en el caso general.

### Soluciones

- [Fuerza bruta]( backtracking ) en \\(O(N! \cdot N)\\), anda
  hasta \\(N=12\\)

  ```c++
  // true si existe camino simple que visita el conjunto s y termina en u
  // la idea es ver si hamilton({0,1,2,...,n-1}, u) es true para algún u
  bool hamilton(set<int> s, int u) {
  	if (s.size() == 1) return true;
  	s.erase(u);
  	for (int v : s)
  		if (existe_arista(u, v) && hamilton(s, v))
  			return true;
  	return false;
  }
  ```

- [Programación dinámica]( dp ) (con subconjuntos) en \\(O(2^{N} \cdot N)\\),
  anda hasta \\(N=20\\)

  ```c++
  bool visto[1<<MAXN][MAXN];
  bool memo[1<<MAXN][MAXN];
  bool hamilton(int s, int u) {
  	if (visto[s][u]) return memo[s][u];
  	visto[s][u] = true;
  	if (__builtin_popcount(s.size()) == 1) return memo[s][u] = true;
  	int s2 = s ^ (1<<u);
  	forn(v, n) if (s2 & (1<<v))
  		if (existe_arista(u, v) && hamilton(s2, v))
  			return memo[s][u] = true;
  	return memo[s][u] = false;
  }
  ```

## Camino Euleriano

Un ciclo o camino que usa todas las aristas de un grafo simple conexo

- Existe ciclo si y solo si hay exactamente cero nodos de grado impar
- Existe camino si y solo si hay exactamente dos nodos de grado impar
- Hay condiciones análogas para dirigidos

Aunque es re parecido al anterior, resulta que este problema sale en tiempo
lineal!

### Solución

Esta solución corre en tiempo lineal pero se puede hacer bastante más rápida
usando `std::list` en vez de `std::unordered_map`.

```c++
unordered_set<int> g[maxn];
vector<int> camino;
void borrar_arista(int u, int v) {
	g[u].erase(v);
	g[v].erase(u); // solo si es no-dirigido
}
void dfs(int u) {
	while (!g[u].empty()) {
		int v = *begin(g[u]);
		borrar_arista(u, v);
		dfs(v);
	}
	camino.push_back(u);
}
vector<int> euleriano(int inicial) {
	camino.clear();
	dfs(u);
	reverse(begin(camino), end(camino));
	return camino;
}
```
