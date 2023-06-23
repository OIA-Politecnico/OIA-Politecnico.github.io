# Grafos

Se dió una clase virtual el 1ro de Septiembre de 2022.

 - [grabación](https://youtu.be/LwBZqpEdem4)
 - [diapositivas](https://raw.githubusercontent.com/SebastianMestre/taller-oia/master/Diapositivas/2022-09-01%20Grafos%20Arboles%20DFS%20BFS%20Dijkstra%20FloodFill.pdf)

---------------

Los grafos son conjuntos de vertices (puntitos) y aristas (rayas que conectan
puntitos). Sirven para representar datos interconectados. Por ejemplo, los
vertices pueden representar ciudades, y las aristas pueden significar que hay
una ruta entre dos ciudades. (otros ejemplos: tableros y jugadas, personas y
amistades, etc.)

![arbol]( img/tree.png )
![dag]( img/dag.png )

Llamamos N a la cantidad de vértices y M a la cantidad de aristas.

## Representación en código

La forma mas común de representar un grafo en un programa
([aunque hay otras]( representar-grafos )) es usando *listas de adyacencia*: por
cada vertice guardo una lista con todos los vertices a los que está conectado
por una arista.

![grafo simple]( img/flyer-graph.png )

```c++
int n = 10;
vector<vector<int>> grafo(n);
grafo[0] = {1, 3};
grafo[1] = {0, 2, 3};
grafo[2] = {1, 5, 7, 8};
grafo[3] = {0, 1, 6};
grafo[4] = {5, 7, 9};
grafo[5] = {2, 4, 6, 7};
grafo[6] = {3, 5, 8, 9};
grafo[7] = {2, 4, 5};
grafo[8] = {2, 6};
grafo[9] = {4, 6};
```

El principal motivo de usar esta representación es que permite
[recorrer el grafo]( recorridos ) eficientemente.

## Problemas con grafos

> 📝 Agregar explicacion de grafos eulerianos y los puentes de Konisberg 📝

Otros problemas famosos (para investigar):

- Circuito y camino euleriano
- Circuito y camino hamiltoniano
- Coloreo de grafos
- Caminos mínimos
- Arbol recubridor mínimo
- Flujo máximo en redes
