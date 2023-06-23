# Grafos

> Esta sección está en construcción

Se dió una clase virtual el 1ro de Septiembre de 2022.

 - [grabación](https://youtu.be/LwBZqpEdem4)
 - [diapositivas](https://raw.githubusercontent.com/SebastianMestre/taller-oia/master/Diapositivas/2022-09-01%20Grafos%20Arboles%20DFS%20BFS%20Dijkstra%20FloodFill.pdf)

## recorridos

Un recorrido es un orden de los vértices de un grafo que tiene alguna
característica especial.

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

## Aplicacion: separar en componentes conexas

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

