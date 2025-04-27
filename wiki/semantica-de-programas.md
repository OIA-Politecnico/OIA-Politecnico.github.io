
# Semantica y razonamiento sobre programas

## Razonamiento ecuacional

El razonamiento ecuacional es la idea de aplicar sustituciones, plantear 
ecuaciones, despejar variables, aplicar funciones a ambos lados de la igualdad y
muchos otros trucos que practicamos en matematica, pero en expresiones de un
lenguaje de programacion.

Obviamente podemos hacerlo con expresiones numericas.

Por ejemplo, si en un programa tenemos una variable `hipotenusa` y una variable
`cateto2` y queremos averiguar el valor de una variable `cateto1` sabiendo que
estos son los lados de un triangulo rectangulo, podemos aplicar el teorema de
Pitagoras y aplicar una serie de manipulaciones algebraicas

    cateto1 * cateto1  +  cateto2 * cateto2  =  hipotenusa * hipotenusa
                          cateto1 * cateto1  =  hipotenusa * hipotenusa - cateto2 * cateto2
                    raiz(cateto1 * cateto1)  =  sqrt(hipotenusa * hipotenusa - cateto2 * cateto2)
                                    cateto1  =  sqrt(hipotenusa * hipotenusa - cateto2 * cateto2)

Pero esto no se queda ahi. Esta misma idea se puede aplicar con objetos mucho
mas complejos, como listas, cadenas, vectores y grafos.

Por ejemplo, consideremos estas dos expresiones:

      (str1 + str2).size()
	= str1.size() + str2.size()

Esta claro que, aunque los procedimientos que realizan estos programas son muy
distintos, el resultado que generan es siempre identico y, aun asi, uno de
los dos es mucho mas eficiente que el otro.

Imaginemos un caso mas complicado.

- sort toma un vector y devuelve una copia ordenada, en O(N log N)
- merge toma dos vectores ordenados y devuelve un tercero vector ordenado, con los elementos de los dos anteriores, en O(N)
- concat toma dos vector y devuelve un tercero, su concatenacion

	// todas estas expresiones son equivalentes, pero algunas son mas costosas que otras
	// ordenar de menor a mayor costo
	// cambia el orden si suponemos que sort es O(N) si su input ya esta ordenado
	  sort(merge(sort(a), sort(b)))
    = sort(concat(sort(a), sort(b)))
	= merge(sort(a), sort(b))
    = sort(concat(a, b))

## Logica de Hoare

Estos dos programas "A" y "B" son equivalentes.

	// A
	sort(begin(v), end(v);
	sort(begin(v), end(v);

	// B
	sort(begin(v), end(v);

Por que? Bueno obviamente, porque ordenar una lista dos veces es lo mismo que
ordenarla una sola vez: La primera vez se ordena y la segunda no pasa
absolutamente nada, porque la lista ya se encuentra ordenada.

Refinando un poco la idea, tenemos que en realidad lo que esta pasando es que
estos dos sub-programas son equivalentes dentro del contexto en el que viven:

    // A
	// suponiendo que v ya esta ordenado
	sort(begin(v), end(v);
	// entonces v esta ordenado

    // B
	// suponiendo que v ya esta ordenado

	// entonces v esta ordenado

Y en la linea anterior tenemos el mismo sub-programa:

    // sin suponer nada sobre v
	sort(begin(v), end(v));
	// entonces v esta ordenado

El hecho de que el primer sort hace que v quede ordenado nos permite aprovechar
la equivalencia de los otros subprogramas y eliminar la segunda llamada
redundante a sort.

Veamos un ejemplo mas interesante.

Los siguientes dos sub-programas son equivalentes, pero solo gracias a la
suposicion que hacen.

	// A
	// suponiendo que v esta ordenado
    auto it = find(begin(v), end(v), x);
	bool encontrado = it != end(v);

	// B
	// suponiendo que v esta ordenado
    auto it = lower_bound(begin(v), end(v), x);
	bool encontrado = it != end(v) && *it == x;

En este caso resulta ser muy importante la suposicion, ya que nos permite pasar
de usar un algoritmo O(N) a uno O(log N).

La Logica de Hoare es un formalismo que surge de observar que:

- el significado de un programa (el resultado que calcula) depende de las
  suposiciones que hace sobre el estado de las variables antes de su ejecucion
  matematicamente.
- para poder entender como se comporta un programa de varias lineas debemos
  entender que efecto tiene la primera linea sobre las variables y tomar eso en
  cuenta como suposicion para la(s) siguiente(s) linea(s).

La logica de hoare se basa en plantear "ternas de Hoare"

    {P}    // pre-condicion
	C      // sub-programa
	{Q}    // post-condicion

Se lee "si antes del programa C se cumple la propiedad P, entonces despues se
cumple la propiedad Q", donde P y Q son proposiciones que hablan sobre las
variables del entorno

Ejemplo interesante: como optimizar el algoritmo de test de primalidad (TO-DO)

