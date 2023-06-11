Para resolver problemas se suelen aplicar ideas conocidas. Entre algoritmos,
estructuras de datos, y otras técnicas de programación, hay miles de ideas
que podemos aplicar en programación competitiva pero, en mi experiencia,
estas son las que más sirven en OIA.

# Complejidad Asintótica

La [complejidad asíntotica]( complejidad ) (o complejidad, a secas) es una forma
de medir a grandes rasgos la velocidad de un programa. Es una de las principales
herramientas que usamos para ahorrar tiempo durante una prueba.

Si pensamos una solución pero la complejidad es demasiado alta, no hace falta
gastar tiempo en programarla y enviarla, porque sabemos que no va a dar muchos
puntos.

## Ordenamiento

Dado un array, casi siempre es buena idea ordenar sus elementos para lograr
algoritmos más eficientes (siempre y cuando esto no cambie la respuesta al
problema).

Ejemplos:

- En vez de búsqueda lineal en un array arbitrario, que tiene complejidad O(n),
  podemos hacer búsqueda binaria sobre un array ordenado, que tiene complejidad
  O(log(n)).
- En vez de n busquedas lineales en el mismo arreglo con complejidad total
  O(n\*n), podemos aplicar un algoritmo de dos punteros, con complejidad O(n).
- Una vez ordenados los datos, algunos problemas admiten soluciones golosas.
- Una vez ordenados los datos, algunos problemas admiten soluciones con
  programación dinámica.

```c++
vector<int> vec = {10, 1, 5, 20};

// ordena los elementos de `vec`
sort(vec.begin(), vec.end());
```

## Fuerza Bruta / Backtracking

La forma más confiable de sacar un par de puntos en cualquier problema es usando
[fuerza bruta o backtracking ]( backtracking ).

La fuerza bruta consiste en probar todas las soluciones posibles y quedarse con
la mejor, o la unica que es correcta. Atacar un problema con fuerza bruta rara
vez nos va a dar un puntaje alto, principalmente por el alto tiempo de ejecución.

Para optimizar esto usamos el backtracking, una estrategia donde descartamos
muchas posibilidades de un tirón. Si encontramos buenas formas de optimizar el
backtracking, a veces podemos robar un par de puntos más. Pero ojo con ponerse a
optimizar mucho un backtracking, porque no suele valer la pena.

## Algoritmos Golosos (Greedy)

Los [algoritmos golosos]( greedy ) consisten en tomar la mejor opción en cada
paso, sin considerar lo que puede pasar después. Muchas veces no conviene usar
algoritmos golosos porque tomar la mejor opción en un principio puede
perjudicarnos más adelante.

Hay que tener cuidado con *el problema de la fruta golosa*: pienso un problema y
se me ocurre un algoritmo goloso. Lo programo, lo envío y resulta que era fruta.

Esto pasa porque muchos algoritmos golosos resuelven correctamente los casos
"más fáciles" o simplemente algunos casos "especiales", pero no generalizan al
caso general.

Tampoco es que no sirvan para nada: hay problemas que salen usando algoritmos
golosos (lo normal es que combinen alguna otra idea, como ordenamiento), y
muchos problemas tienen subtareas que se pueden hacer con algoritmos golosos,
asique son muy útiles para robar puntos.

## Programación Dinámica (DP)

Si la fuerza bruta es para sacar un par de puntos en cualquier problema, la
[programación dinámica]( dp ) sirve para sacar "bastantes" puntos en "bastantes"
problemas.

La idea general es separar cada problema en subproblemas del mismo tipo que se
solapan. Cada uno de esos subproblemas también se resolverá separando en
sub-subproblemas, y así sucesivamente.

Entonces, si guardamos las soluciones a todos los subproblemas de tamaño 1 en una
tabla, podemos aprovecharlas para construir las soluciones a los de tamaño 2.
Esas para los de tamaño 3, y así sucesivamente hasta construir la solución al
problema total.

Generalmente se usa para problemas sobre:

- Tableros
- Arreglos
- Grafos Aciclicos

Un problema se puede resolver con programación dinámica cuando tiene
"subestructura óptima", que significa mas o menos que la solución se puede
construir combinando soluciones a subproblemas. (No es tan importante, pero se
puede googlear)


## Búsqueda Binaria (Binary Search)

La [búsqueda binaria]( busqueda-binaria ) es un principio que permite encontrar
la mejor opcion entre miles de millones de posibilidades en muy poco tiempo.
Para lograr esto trabaja iterativamente, descartando la mitad de las
posibilidades en cada paso sin necesidad de considerarlas una por una.

Hay muchos problemas que salen con busqueda binaria o alguna de sus variaciones.

## Algoritmos Sobre Grafos

A diferencia de otras técnicas que nos permiten encontrar soluciones eficientes
a problemas, pero que ya se podían resolver de formas menos eficientes, los
[algoritmos de grafos]( grafos ) nos dan la posibilidad de resolver problemas
que no serían posibles de otra forma.

Esto lo logran almacenacenando redes de información en nuestros programas, lo
cual nos habilita a procesar datos relacionandolos con otros datos que existen
en el programa. (Por ejemplo, un pais y sus paises limitrofes).
