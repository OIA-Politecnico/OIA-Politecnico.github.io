Los algoritmos golosos consisten en tomar la mejor opción en cada paso, sin
considerar lo que puede pasar después. Muchas veces no conviene usar algoritmos
golosos porque tomar la mejor opción en un principio puede perjudicarnos más
adelante.

Hay que tener cuidado con *el problema de la fruta golosa*: pienso un problema y
se me ocurre un algoritmo goloso. Lo programo, lo envío y resulta que era fruta.

Esto pasa porque muchos algoritmos golosos resuelven correctamente los casos
"más fáciles" o simplemente algunos casos "especiales", pero no generalizan al
caso general.

Por ejemplo en el problema de dar el vuelto con la menor cantidad de
billetes/monedas posible tenemos el este algoritmo goloso:

1. Tomo el billete mas grande que no supere lo que tengo que devolver.
2. Separo ese billete y resto su valor a lo que me falta devolver.
3. Si todavia me falta devolver más plata, vuelvo al paso 1.
4. Si no, ya terminé.

Usando billetes con las denominaciones típicas ($1, $2, $5, $10, $20, etc), este
algoritmo siempre da el resultado correcto (siempre usa la menor cantidad
de billetes posibles)

¡Pero resulta que es fruta!

Si los billetes fueran de $1, $5 y $7, este algoritmo genera soluciones
suboptimas! Por ejemplo, si queremos dar vuelto de $10, la solución óptima es
dar dos monedas de $5 (2 monedas en total) pero el agoritmo nos lleva a dar una
moneda de $7 y tres monedas de $1 (4 monedas en total).