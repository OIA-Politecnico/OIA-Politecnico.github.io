Para resolver problemas se suelen aplicar ideas conocidas. Entre algoritmos,
estructuras de datos, y otras técnicas de programación, hay miles de ideas
que podemos aplicar en programación competitiva pero, en mi experiencia,
estas son las que más sirven en OIA.

# Complejidad Asintótica

La [complejidad asíntotica]( complejidad ) (o complejidad, a secas) es una forma de medir a grandes rasgos
la eficiencia de un programa.

## Fuerza Bruta / Backtracking (Brute Force / Backtracking)

La técnica más confiable para sacar un par de puntos en cualquier problema es
la fuerza bruta. Esta consiste en probar todas las soluciones y quedarse con la
mejor, o la unica que es correcta. La forma más común de esto es con varios
`for` anidados.

Osea, los algoritmos de fuerza bruta suelen tener esta pinta:

```c++
for (i = 0; ...) {
  for (j = 0; ...) {
    for (k = 0; ...) {
      for (q = 0; ...) {
        if (es_solucion_valida(i, j, k, q)) {
          return solucion(i, j, k, q);
        }
      }
    }
  }
}
```

Obviamente, atacar un problema con fuerza bruta rara vez nos va a dar un puntaje
alto, principalmente por el alto tiempo de ejecución. Para optimizar esto usamos
el backtracking, una estrategia donde descartamos muchas posibilidades de un tirón.

En general, esto se implementa con varios `if`s dentro de los bucles de la fuerza
bruta.

```c++
for (i = 0; ...) {
  for (j = 0; ...) {
    if (j_es_demasiado_grande(i, j) {
      // si entramos acá, nos salteamos todos los valores de `j` que nos faltan
      // para el `i` actual, y podemos ahorrarnos muchísimas combinaciones.
      break;
    }
    for (k = 0; ...) {
      for (q = 0; ...) {
        if (es_solucion_valida(i, j, k, q)) {
          return solucion(i, j, k, q);
        }
      }
    }
  }
}
```

Si encontramos buenas formas de optimizar el backtracking, a veces podemos robar
un par de puntos más. Sin embargo, no suele ser suficiente para sacar "muchos"
puntos en un problema. Para eso existen las otras técnicas.

Ojo con ponerse a optimizar mucho un backtracking, porque no suele valer la pena.

## Algoritmos Golosos (Greedy Algorithms)

Los algoritmos golosos consisten en tomar la mejor opción en cada paso (bajo algún
concepto de "mejor") de la resolución de un problema, sin considerar lo que puede
pasar después. Muchas veces no conviene usar algoritmos golosos porque tomar la
mejor opción en un principio puede perjudicarnos más adelante.

Por lo general, cuando uno piensa un problema, primero se le ocurre un algoritmo
goloso que parece andar, y después resulta que no anda, o que solo resuelve
algunos casos especiales.

Un ejemplo clásico de esto es el problema de dar el vuelto con la menor cantidad de
billetes/monedas posible.

Consideremos el siguiente algoritmo goloso:

1. Tomo el billete mas grande que no supere lo que tengo que devolver.
2. Separo ese billete y resto su valor a lo que me falta devolver.
3. Si todavia me falta devolver más plata, vuelvo al paso 1.
4. Si no, ya terminé.

Usando billetes con las denominaciones típicas ($1, $2, $5, $10, $20, etc), este
algoritmo siempre da el resultado correcto. Osea que siempre usa la menor cantidad
de billetes posibles. Y, si testeamos el algoritmo apegandonos a estas
denominaciones, es facil terminar convenciendonos de que anda siempre.

En cambio, si vivieramos en un país de locos donde los billetes son de $1, $5 y $7,
podemos encontrarnos con soluciones suboptimas al seguir ese algoritmo. Por ejemplo,
si queremos dar vuelto de $10, la solución óptima es, obviamente, dar dos monedas de
$5 (2 monedas en total) pero el agoritmo nos lleva a dar una moneda de $7 y tres
monedas de $1 (4 monedas en total).

La moraleja es que es fácil creerse que un algoritmo goloso anda, cuando la mayoría
de los problemas no admiten una solución golosa.

Igual, ojo, tampoco es que no sirvan para nada: hay algunos problemas que salen con
100pts usando algoritmos golosos (lo normal es que combinen alguna otra idea, como
ordenamiento), y muchos problemas tienen subtareas que se pueden hacer con algoritmos
golosos, asique son muy útiles para robar puntos.

## Programación Dinámica (DP)

Si la fuerza bruta es para sacar unos pocos puntos en cualquier problema, la
programación dinámica sirve para sacar "bastantes" puntos en "bastantes" problemas.

Generalmente se usa para problemas sobre:

- Tableros
- Arreglos
- Grafos Aciclicos

Aplica cuando el problema tiene subestructura óptima con subproblemas que se solapan.

Decimos que un problema tiene subestructura óptima cuando "Dada una solución óptima,
las partes de esa solución son óptimas para otro problema del mismo tipo"

Para darnos cuenta si un problema tiene subestructura óptima, Hay que pensar "para
atrás": nos imaginamos que el problema ya está resuelto y nos preguntamos si los prefijos
de la solución resuelven el prefijo correspondiente del problema.

## Ordenamiento

Dado un array, puede ser buena idea ordenar sus elementos para lograr algoritmos más eficientes.

Ejemplos:

- En vez de búsqueda lineal en un array arbitrario, que tiene complejidad O(n), podemos hacer búsqueda binaria sobre un array ordenado, que tiene complejidad O(log(n)).
- En vez de n busquedas lineales en el mismo arreglo con complejidad total O(n\*n), podemos aplicar un algoritmo de dos punteros, con complejidad O(n)
- Una vez ordenados los datos, algunos problemas admiten soluciones golosas.
- Una vez ordenados los datos, algunos problemas admiten soluciones con programación dinámica.

```c++
vector<int> vec;

// ...

// ordena los elementos de `vec`
sort(vec.begin(), vec.end());
```

## Búsqueda Binaria (Binary Search)

La [búsqueda binaria]( busqueda-binaria ) es un principio que permite encontrar la mejor opcion entre miles de millones de posibilidades en muy poco tiempo. Esto se logra descartando la gran mayoria de estas opciones sin necesidad de considerarlas.

Muchos problemas se pueden resolver completamente usando busqueda binaria o alguna de sus variaciones.

## Algoritmos Sobre Grafos

A diferencia de otras técnicas que nos permiten encontrar soluciones eficientes a problemas, pero que ya se podían resolver de formas menos eficientes, los [algoritmos de grafos]( grafos ) nos dan la posibilidad de resolver problemas que no serían posibles de otra forma.

Esto lo logran almacenacenando redes de información en nuestros programas, lo cual nos habilita a procesar datos relacionandolos con otros datos que existen en el programa. (Por ejemplo, un pais y sus paises limitrofes).
