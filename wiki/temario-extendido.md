# Grafos

- Nociones elementales y definiciones de teoria de grafos
- Circuito euleriano, teorema de existencia <=>, algoritmos para construirlo
- Circuito hamiltoniano (NP completo en general), teoremas de Ore / Dirac
- Representación de grafos en memoria
- Matriz de Adyacencia
- Matriz de Incidencia
- Listas de Adyacencia
- Lista de incidencia
- Grafo Implícito

## BFS:

- Basico.
- BFS con cola de dos puntas [Aristas 0 y 1]
- BFS con K+1 bolsas [aristas 0..K]

## DFS

- Con stack
- Recursivo
- Back Edges
- Tree Edges
- Forward Edges
- Cross Edges

## Dijkstra

- En N^2
- En (N + M) lg N
- Distancia Min-Max (Prim)

## Bellman-Ford

- Vision como programacion dinamica.
- Implementacion tipica.
- Variante para contar caminos entre pares de nodos.

## Floyd-Warshall

- Vision como programacion dinamica.
- Implementacion tipica.
- Variante para contar caminos entre pares de nodos.
- Producto de matrices de adyacencia / Potencias de la matriz de adyacencia.

## Reconstrucción de caminos en algoritmos de camino mínimo

- Guardando padres
- Chequeando la cuentita de la DP
- "Truquito de dar vuelta origen y destino (y trasponer el grafo si es dirigido) así al recorrer los padres queda el camino al derecho."

## Detección y tratamiento de ciclos negativos

- Con Floyd
- Con Bellman Ford

## Kruskal

- Descripción e implementación, con referencia a Union-Find
- Relación del Minimum Spanning Tree con la distancia Min-Max.
- Aplicación a calcular la distancia min-max todos contra todos en N^2
- Solución alternativa para el mismo problema: hacerlo en el mismo Kruskal que calcula el MST

## Flujo y derivados:

- Matching Maximo Bipartito O(VE)
- Flujo Maximo / Corte Minimo
- Edmonds-Karp
- Dinitz
- Algoritmos de Preflow-Push
- Manejo, entendimiento y manipulación de la red residual de un grafo.
- Teoremas de König, Hall y Menger.
- Mínimo Cubrimiento por Caminos. Mínima Partición en Caminos. Teorema de Dilworth
- Flujo de costo minimo.
- Vertex cover / Independent set en grafo bipartito

## DAGs:

- Ordenamiento Topologico
- Clausura transitiva (aplica a cualquier grafo pero es muy común en DAGs)
- Componentes Biconexas (Puntos de articulación, puentes)
- Componentes Fuertemente Conexas
- Camino/Ciclo euleriano

## Árboles:

- Detección,recorrido.
- Representación de arbol con raiz: Padre de cada nodo
- Representación de arbol con raiz:Lista de adyacencia del dirigido "bajando desde la raíz".
- Radio, centro y diámetro de un árbol en tiempo lineal.

## Grafos planares

- Fórmula de Euler
- Los grafos planares son ralos
- Dualidad
- Construir Grafo dual de un grafo planar (dado el embedding)
- Max-clique en grafo planar

# Análisis de complejidad

- Entendimiento de la notacion asintotica (La O grande de "O(N)")
- Analisis amortizado de complejidad
- Nocion de P, NP, NP completo, algoritmo polinomial, etc
- Problemas NP completos conocidos
- "Problemas que no se sabe que estén en P ni se sabe que sean NP completo (Factorización entera, logaritmo discreto, isomorfismo de grafos)"

# Algoritmos de Ordenamiento

- Busqueda lineal y busqueda binaria (con LA RECETA)
- Counting Sort
- MergeSort
- QuickSort
- Mediana (o elemento iesimo) en tiempo lineal esperado (n\_th element)
- HeapSort
- BubbleSort
- InsertionSort
- RadixSort

# Estructuras de datos

- Arreglos
- STL (set, multiset, map, multimap, vector, queue, stack, deque, priority\_queue, list, etc)
- Policy based data structures de GCC (en especial indexed\_set)
- Listas enlazadas
- Colas
- Pilas
- Tries
- Hashing
- Árbol binario de búsqueda
- ABB balanceado (por ej, Treap)
- Heap (para priority queue), heapsort, heapify en O(N)
- Union Find (Implementacion con listas y con arbol)
- RMQ (Segment tree sobre arreglo)
- Sliding Windows, Sliding-RMQ (para en O(N) calcular el RMQ de subarreglos de un tamaño K dado)
- Binary lifting en árbol con raíz
- LCA en O(lg n) (reduccion a RMQ, o binary lifting) distancias en un árbol en O(lg n)
- Tablas Aditivas (prefix sums)
- Binary Index Tree (Fenwick Tree)
- Estructuras de datos persistentes (con path copying)
- RMQ/Fenwick 2D
- Heavy Light Decomposition
- Estructuras de datos para arboles dinamicos (link-cut trees)

# Algoritmos de raiz cuadrada

- sqrt-decomposition: Separar la secuencia del input en bloques de sqrt(N)
- Algoritmo de MO: separar queries por posicion inicial en bloques de sqrt(N)
- Combinar dos algoritmos O(nk) y O(n^2/k)
- Agrupar updates en bloques de sqrt(U), hacer queries iterando por las updates dentro de cada bloque
- Hay <= sqrt(N) elementos que aparecen >= sqrt(N) veces
- Si una suma es igual a N, hay <= sqrt(N) valores distintos

# Strings

- Knuth Morris Pratt (KMP), y su tablita de bordes.
- Rabin-Karp, y uso del concepto de hash en general.
- xor-hashing y sum-hashing con una tabla de números aleatorios
- Suffix Array (Algoritmo de Larsson y Sadakane), LCP

# Programacion Dinamica

- Recursion (en matematica, en programacion, recursion mutua)
- Maxima subsecuencia creciente (En O(n^2), y su variante en O(n lg n))
- Cálculo del triangulo de pascal
- Longest common subsequence
- Edit distance mínima (La común, y permitiendo swaps adyacentes)
- Producto de matrices con costo minimo
- "En una matriz yendo de una esquina a la otra solo bajando y para la derecha,
-  maximizar la suma de las casillas visitadas."
- Knapsack (Problema de la mochila), Subset Sum
- Dar vuelto usando una cantidad minima de monedas
- Optimal Binary Search Tree en O(n^3) y O(n^2) (Knuth optimization)
- Divide and conquer optimization
- Dada una string par de {,(,[,],),} dar la minima cantidad de cambios necesarios para que sea valida.
- Dinámicas con máscaras de bits: TSP y muchas otras.
- Dinámicas con "frente": Poner fichitas / tubitos en un tablero, y muchas otras

# Matemática y afines

- Punto flotante: Conocerlos, saber que existe el error, cuentitas basicas, uso de EPSILON en los if
- Potenciacion logaritmica
- Recurrencias lineales
- Sistemas de ecuaciones lineales
- Truquito para matrices banda. Casos especiales de interes: Bidiagonales, Tridiagonales, Adyacencias en una grilla rectangular.
- Calculo de determinantes, matriz inversa (algoritmo de Gauss)
- Operaciones aritmeticas con enteros de longitud arbitraria
- Combinatoria y probabilidad
- Principios de la suma y del producto
- Coeficientes binomiales / triangulo de pascal
- Inclusion-exclusion
- Linealidad de la esperanza / técnica "contribution to the sum"
- Distribución de la suma de dos variables aleatorias (convolucion)
- Convolucion rápida usando FFT
- Números de Catalan
- Cadenas de Markov
- Young Tableaux

# Teoría de números

- Teorema fundamental de la aritmetica
- Aritmetica modular
- MCD (Algoritmo de euclides)
- Inverso Modular (Con euclides extendido o con pequeño teorema de Fermat)
- Teorema Chino del Resto
- Producto de matrices
- Criba de eratostenes
- Chequeo de primalidad raiz(N)
- Chequeo de primalidad eficiente probabilistico
- Funciones multiplicativas, función de Mobius

# Geometria

- Vectores (Suma, Resta)
- Producto escalar
- Norma, distancia euclidea (pitagoras)
- Producto vectorial
- Area de triangulos / paralelogramos, detección de sentido de giro
- Area de poligonos
- Representaciones de recta, segmento, etc estilo lineal (vectores / puntos + direccion)
- Chequear si un punto esta en un poligono / en un segmento / en una recta / en un plano
- Chequear si esta en poligono convexo en lg N
- Chequear si está en un poligono no convexo en O(N)
- Teorema de Pick
- Compresion de coordenadas
- Par de puntos mas cercano en O(n lg n)
- Capsula convexa en O(n lg n)
- Par de puntos mas lejano en O(n lg n), O(n) dada ya la capsula convexa
- Rotating calipers
- Interseccion de dos segmentos
- Distancia entre dos segmentos
- Sweep Line (Es MUY importante la idea de sweep line / sweep circle / sweep sarasa)
- Dualidad punto / linea
- Interseccion circulo - circulo y circulo - recta
- Suma de Minkowski, aplicación a distancia entre polígonos convexos
- Convex Hull Trick

# Divide and conquer

- Elemento mayoria en n lg n usando *solamente* comparaciones por igualdad entre elementos.
- Par de puntos mas cercano en O(n lg n)
- Strassen
- Karatsuba
- Armado de fixtures (aunque hay una alternativa constructiva muy elegante y simple)
- Greedies
- Dar vuelto usando una cantidad minima de monedas
- Ordenamiento de trabajos con distintos tiempos de ejecución para minimizar el tiempo de finalización promedio.
- Optimo cubrimiento de intervalo por subintervalos.
- Codigos de Huffman
- Maxima subsecuencia creciente (resolviendo "mínima partición en subsecuencias no crecientes" + Dilworth)

# Backtracking

- Fuerza Bruta
- for if for if for if
- Tipica implementacion recursiva cuando no se sabe la cantidad de pasos.
- Branch and bound
- Problema de las n reinas.
- Cubrir un tablero con fichitas.
- Sudoku.
- Problemas NP Completos: Maximum independent set, Minimum dominating set, subset sum, etc.

# Teoría de juegos

- Propiedad Universal de las posiciones P/G
- Cálculo con DP de posiciones ganadoras y perdedoras.
- Idea de la criba para llenar tablitas como la anterior.
- Variante de la DP donde el que gana trata de ganar rápido y el que pierde de perder lento.
- Juegos combinatorios imparciales: Sumar de juegos.
- Nim. Misére Nim.
- Grundy Numbers, cálculo de los grundy numbers en tiempo lineal en el grafo, con DP. Cálculo del Grundy Number de una suma de juegos (el xor de los grundies).
- Algoritmo minimax para juegos de suma cero de informacion perfecta.

# Teoría de lenguajes

- Gramatica BNF
- Autómatas Finitos
- Expresiones Regulares
- Parsing Recursivo Descendente predictivo (con "prediccion artesanal")
- Gramaticas libres de contexto
