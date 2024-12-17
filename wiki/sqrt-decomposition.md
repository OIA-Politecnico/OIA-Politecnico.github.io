# Sqrt-Decomposition

Sqrt decomposition es una meta-tecnica muy amplia. La idea es descomponer los
datos segun algun criterio basado en la raiz cuadrada de algo. Por ejemplo:

- Dado un arreglo de longitud N, partirlo en bloques de tamaño raíz de N
  (para poder responder consultas en tiempo raíz de N)
- Dadas U actualizaciones y Q consultas, procesarlas en bloques de raiz de U
  actualizaciones, con un preprocesamiento antes de cada bloque (para procesar
  cada consulta en tiempo raíz de U)
- Dados N separados en grupos, procesar de forma distinta los (potencialmente
  muchos) grupos de tamaño menor a raíz de N y los grupos mayores
- Dado un problema con input de tamaño N y un parametro k, usar dos algoritmos
  distintos cuando k es menor a raíz de N y cuando es mayor

Veamos un ejemplo de la primera

## Problema

Se da un array de N enteros y Q operaciones. Las operaciones pueden ser de dos
tipos:

- Tipo 1: Dados `x` e `i`, asignar `x` en la posicion `i` del array.
- Tipo 2: Dados `l` y `r`, imprimir la suma desde la posicion `l` hasta la
  posicion `r` del array.

### Solución ineficiente

Para las operaciones de tipo 1, modificamos el array directamente. Costo `O(1)`.

Para las operaciones de tipo 2, hacemos un for de `l` hasta `r`. Costo `O(N)`.

Alternativamente, se pueden usar [sumas parciales]( tabla-aditiva ) con los
costos intercambiados.

Ambos enfoques son muy lentos cuando N y Q son grandes y hay una mezcla
homogenea de operaciones de tipo 1 y 2.

### Solución eficiente

Para responder consultas en rango rápidamente, podemos precalcular la respuesta
para bloques de tamaño `K` (nosotros elegimos `K`).

Para las operaciones de tipo 1, recalculamos el resultado para el bloque al que
pertenece `i`. Complejidad `O(K)`.

Para las operaciones de tipo 2, combinamos a lo sumo `N/K` bloques. Lo que sobre
lo contemplamos con un for más. Complejidad `O(N/K + K)`.

Si elegimos `K = sqrt(N)`, ambas operaciones quedan `O(sqrt(N))`.

## Otro problema

Ahora veamos otro problema. Aprovecho para resaltar que hay problemas que
admiten mas de un enfoque con sqrt-decomposition, y este es uno de ellos.

Hay un grafo simple, no dirigido, de N nodos y M aristas, con etiquetas
numericas en los nodos.

Hay dos tipos de operaciones:

1. Dado un nodo `u`, imprimir la suma de las etiquetas de los vecinos de `u`
2. Dado un nodo `u` y un valor `x`, reemplazar el número de `u` con `x`

Cotas:

- `N < 100000`
- `M < 100000`
- La cantidad de consultas es Q. `Q < 100000`
- La cantidad de actualizaciones es U. `U < 100000`


### Solución ineficiente

Representamos el grafo con una lista de adyacencia

1. Iteramos por los vecinos de `u`, sumando la etiqueta a un acumulador. Costo
  `O(grado(u))`
2. Modificamos la etiqueta del nodo `u`. Costo `O(1)`

Si hay `U` actualizaciones y `Q` consultas, esto tiene costo `O(U + QN)` en el
peor caso.

### Solución eficiente A

Separamos los nodos en dos grupos: los que tienen más de raíz de M vecinos y los
que tienen menos. Los llamamos nodos "grandes" y "chicos".

Logicamente, puede haber a lo sumo `2*sqrt(M)` nodos grandes.

Vamos a mantener las sumas de los nodos grandes siempre actualizadas.

Para responder las consultas:

1. Hay dos casos, dependiendo de si `u` es un nodo grande o un nodo chico:

   - Si es grande, su suma ya está calculada y la imprimimos.
   - Si es chico, iteramos por sus vecinos para calcular la suma.

   El costo en el peor caso es `O(sqrt(M))`

2. Modificamos la etiqueta del nodo. Aparte, iteramos por todos los nodos
   grandes fijandonos si `u` es vecino de alguno. En caso de serlo, actualizamos
   su suma restando la etiqueta vieja y sumando la nueva.

   El costo en el peor caso es `O(sqrt(M))`

 Finalmente, el costo total en el peor caso es `O((U+Q) * sqrt(M))`.

### Solución eficiente B

Inicialmente calculamos la suma de cada nodo iterando todo el grafo en `O(N+M)`.

Al hacer actualizaciones no modificamos nada, solo las guardamos en una lista de
actualizaciones, anotando el nodo modificado, la etiqueta vieja y la etiqueta
nueva.

Para hacer una consulta partimos de la suma calculada inicialmente. Después
iteramos por la lista de actualizaciones, y si alguna de ellas afecta el
resultado de la consulta actual, modificamos el resultado de la consulta
restando la etiqueta vieja y sumando la nueva.

El problema de esto es que en cada consulta iteramos por la lista de
actualizaciones, por lo que el costo es `O(N+M+U*Q)`.

Para mejorar esto podemos rehacer el precalculo de `O(N+M)` y limpiar la lista
cada `sqrt(U)` actualizaciones.

Entonces la solucion va a ser:

1. Tomamos la suma que está precalculada e iteramos por la lista de
   actualizaciones, modificandola según corresponda. Costo `O(sqrt(U))`

2. Si ya se hicieron `sqrt(U)` actualizaciones desde el ultimo precalculo,
   hacemos el precalculo.

   Modificamos la etiqueta del nodo y agregamos la actualizacion a la lista de
   actualizaciones.

   El costo es `O(1)` la mayoria de las veces, pero es `O(N+M)` cada `sqrt(U)
   actualizaciones.

 Finalmente, el costo total queda `O((N+M+Q) * sqrt(U))`
