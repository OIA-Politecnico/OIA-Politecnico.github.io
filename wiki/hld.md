# Heavy-Light Decomposition

Imaginate un arbol con raiz, de N nodos.

Enfocarse en una arista (u, v), donde v es el padre de u.

Decimos que (u, v) es **"pesada"** si el tamaño del subárbol de u es más de la
mitad del tamaño del subárbol de v.

En tal caso, decimos que u es un **"hijo pesado"** de v.

A las aristas que no son pesadas las llamamos **"livianas"**.

**obs:** un nodo no puede tener más de un hijo pesado.

**obs:** en un camino desde la raíz hasta una hoja puede haber a lo sumo log2(N)
aristas livianas. (por qué? porque al cruzar una arista liviana se divide el
tamaño del subarbol a la mitad. esto no puede pasar muchas veces)

**obs:** si un camino está a una gran profundidad en el grafo, el camino desde
la raiz hacia este va a estar compuesto de largas seguidillas de aristas pesadas
interrumpidas por unas pocas aristas livianas. A estas seguidillas de aristas
pesadas les decimos **"caminos pesados"**.

**Problema:** <https://codeforces.com/contest/1174/problem/F>
 
> Problema interactivo. Te dan un árbol con raíz, de N nodos (`N <= 10^5`). Hay
> un nodo secreto x que hay que descubrir. Para lograrlo podes hacer dos tipos
> de consultas:
>
> - d(u): dado un nodo u te responden la distancia de u a x
> - s(u): dado un nodo u te responden el siguiente nodo en el camino hacia x. u
>   debe ser ancestro de x. si no, te dan wrong answer inmediatamente.
>
> Se pueden realizar **a lo sumo 36 consultas**.

**Solucion**

> Nos paramos en la raiz y nos vamos a ir acercando iterativamente al nodo x.
>
> Considera el camino desde la raiz hasta x. Este camino contiene a lo sumo
> `log2(N) <= 17` aristas livianas.
>
> Entre medio de cada par de aristas livianas hay un camino pesado.
>
> Si logramos procesar cada camino pesado y cada arista pesada con una sola
> consulta, lograriamos el limite de consultas del problema.
>
> Si sabemos que el camino arranca metiendose por un camino pesado pero en algun
> momento se sale, es posible calcular en que punto se sale haciendo una
> consulta de distancia en el primer nodo del camino y tambien en el ultimo.
> (hacemos dos consultas de tipo d(u)).
>
> Una vez que sabemos en que nodo se sale del camino pesado, puede haber mas de
> una arista liviana por la que se puede salir. Ahi hay que hacer una consulta
> de tipo s(u).
>
> Esto haria en el peor caso `17 + 2 * 18 = 53` consultas.
>
> Siendo un poco mas ingenioso se puede calcular la consulta de distancia del
> inicio del camino pesado usando los resultados anteriores.
>
> Esto baja la cantidad de consultas a `17 + 18 = 35` en el peor caso.

## Idea de procesar cada el subarbol de cada arista liviana / *Sack*

TODO: introduccion

> **Problema:** <https://cses.fi/problemset/task/1139>
> 
> Hay un arbol con raiz, de N nodos (`N <= 2*10^5`), donde cada nodo tiene un
> color. Por cada nodo, nos preguntan cuantos colores distintos aparecen en su
> subarbol.

### Solucion

Tomamos algun camino pesado, y vamos iterando de abajo hacia arriba, manteniendo
un conjunto de colores.

En cada paso insertamos el color del nodo actual y recorremos los subarboles de
todos los hijos livianos del nodo actual, insertando sus colores en el conjunto.

Como todo el subarbol del hijo pesado ya estaba insertado en el conjunto, en
todo momento lo que tenemos es el conjunto de colores del subarbol del nodo
actual, lo cual nos permite responder su cantidad de colores.

Ahora repetimos este algoritmo para cada camino pesado (consideramos nodos que
no son hijos pesados ni tienen hijo pesado como un camino en si mismo).

Para analizar la complejidad, notemos que por cada nodo, insertamos su color en
un conjunto una vez al iterar su camino pesado y una vez por cada arista liviana
que está en su camino hacia la raíz. O sea, a lo sumo `log2(N)+1` veces.

Esto significa que cada nodo se inserta `O(log(N))` veces, por lo que el
algoritmo realiza a lo sumo `O(N log(N))` inserciones en un conjunto. Si usamos
`unordered_set`, obtenemos exactamente esa complejidad.

## Idea de mover fichitas a la raiz / *small-to-large* / *DSU on trees*

Una forma común de aprovechar la descomposicion en aristas livianas y pesadas
es en problemas donde queremos simular que en cada nodo del árbol comienza una
fichita y esta va a ir caminando hacia la raíz.

Simulando directamente, esto toma tiempo proporcional a la suma de las
profundidades de todos los nodos, que puede ser `O(N^2)`

En cambio, si pudieramos simular el trayecto de cada fichitas por un camino
pesado en O(1) y solo pagaramos las aristas individualmente en el caso de ser
livianas, entonces tendriamos un algoritmo `O(N log(N))`.

Esta misma idea se puede aplicar

## Idea de construir estructuras de datos sobre los caminos pesados

Posiblemente la aplicacion mas famosa de la descomposicion, se puede usar para
hacer consultas de suma/max o cualquier operacion asociativa en caminos de un
arbol. (tipicamente se suponen operaciones que tambien son conmutativas para
facilitar la implementacion)

La idea es armar un segment tree de suma o alguna estructura similar sobre cada
camino pesado. Ahora, para hacer una consulta de suma a lo largo de un camino,
podemos observar lo siguiente.

Cualquier camino entre dos nodos (u,v) sube de u al LCA de u y v y despues baja
a v.

Podemos responder las dos partes del camino por separado y despues sumar.

Para lograr una consulta que va de u y solo sube podemos primero responder la
parte de la consulta que esta sobre el camino pesado de u.

Despues pasamos al padre del nodo mas alto del camino pesado y respondemos la
parte que cae en su camino pesado.

Repetimos este algoritmo hasta llegar tan arriba como se necesite.

En todo este algoritmo solo podemos tocar `log2(N)+1` caminos pesados (porque
para pasar de un camino pesado a otro tenemos que cruzar una arista liviana y
solo hay a lo sumo `log2(N)`), entonces podemos responder todas las consultas en
`O(log(N))` consultas de segment tree, con un costo de `O(log(N)^2)`
