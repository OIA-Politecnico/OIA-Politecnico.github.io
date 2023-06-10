Una propiedad binaria (o un predicado, o una condición) es monótona si vale hasta cierto punto y luego deja de valer o viceversa.
Por ejemplo P(n) = "n < 5"
P es true hasta 4 y a partir de 5 vale false

La búsqueda binaria es un algoritmo para hallar dicho punto, llamado "la frontera" que en este ejemplo está entre 4 y 5

La idea es comenzar con un valor donde sabes que P vale, y otro donde sabés que no vale. Probás un valor intermedio y vas actualizando los valores hasta hallarla:

1. Consideramos un intervalo `[a, b)`, donde la condición no vale en `a`, y sí vale en `b`.
2. Probamos si la propiedad vale en el punto medio entre `a` y `b`, que llamamos `m`.
3. Si la propiedad vale, pasamos a considerar el intervalo `[a, m)`.
4. Si no vale, pasamos a considerar el intervalo `[m, b)`.
5. Repetimos esto mientras que la diferencia entre `a` y `b` sea mayor a 1.

En otras palabras, la busqueda binaria sirve para contestar preguntas de la pinta:

> ¿A partir de qué punto vale tal propiedad?

Por ejemplo:

> ¿Cuánto contrapeso necesita mi catapulta para alcanzar el castillo?
> 
> ¿A partir de qué posición me paso del elemento del array (ordenado) que estoy buscando? (como en un diccionario ordenado alfabéticamente)

Este tipo de busqueda tiene complejidad O(log n) (donde n es la diferencia inicial
entre a y b). En cambio, la busqueda lineal (ir probando cada valor, uno por uno)
tiene complejidad O(n).

Algunas formas comunes de aplicarla son:

- Buscar elementos en un arreglo ordenado
- Ver a partir de qué valor anda un greedy
- Mas generalmente: convertir un problema a su versión de decisión