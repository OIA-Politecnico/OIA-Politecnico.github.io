# Caminos minimos

Para calcular caminos minimos en un grafo ponderado usamos el algoritmo de
Dijkstra. Este no es mas que otro [recorrido con bolsa]( recorridos ), donde la
bolsa nos devuelve siempre el nodo con la minima distancia desde el origen del
recorrido.

Para que esto tenga sentido vamos manteniendo la mejor distancia a cada nodo a
medida que recorremos.

Implementamos esa bolsa eficientemente usando `priority_queue`.

```c++
long long const INF = 1000000000000000100;

// lista de adyacencia ponderada
int const MAXN = 100100;
struct arista { int nodo, peso; };
int n;
vector<arista> grafo[MAXN];

// Usamos esto para implementar la cola de prioridad ordenada por distancia
struct camino { int nodo; long long peso; };
bool operator < (camino const& a, camino const& b) {
	return a.peso > b.peso;
}

vector<long long> dijkstra(int s) {
	vector<long long> dist(n, INF);
	vector<bool> vis(n, false);
	priority_queue<camino> pq;
	dist[s] = 0;
	pq.push({s, dist[s]});
	while (!pq.empty()) {
		int u = pq.top().nodo;
		pq.pop();
		if (vis[u]) continue;
		vis[u] = true;
		for (arista e : grafo[p.nodo]) {
			int v = e.nodo;

			// mantengo la distancia a medida que recorro
			dist[v] = min(dist[v], dist[u] + e.peso);

			pq.push({v, dist[v]});
		}
	}
	return dist;
}
```

Parecido que con el BFS, también hay una versión un poco más eficiente que solo
inserta un nodo en la cola de prioridad al encontrar un mejor camino que llega a
él. También tiene la ventaja de que no hace falta mantener la lista de vistados.

```c++
vector<long long> dijkstra(int s) {
	vector<long long> dist(n, INF);
	priority_queue<camino> pq;
	pq.push({s, dist[s] = 0});
	while (!pq.empty()) {
		auto [u, du] = pq.top();
		pq.pop();
		if (du > dist[u]) continue;
		for (auto [v, w] : grafo[u]) {
			auto dv = du + w;
			if (dv >= dist[v]) continue;
			pq.push({v, dist[v] = dv});
		}
	}
	return dist;
}
```

## Modelando problemas con camino minimo

En muchos problemas piden encontrar un camino minimo en un grafo, pero
manteniendo alguna condición extra.

Ahí podemos tener la idea de modificar el algoritmo de Dijkstra para lograrlo,
pero suele ser bastante dificil.

Otra idea que suele ser más fácil es modificar el grafo para que el algoritmo
tradicional calcule la respuesta correcta a nuestro problema.

- Ver este blog de codeforces <https://codeforces.com/blog/entry/45897>
