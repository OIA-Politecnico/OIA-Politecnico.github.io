# Búsqueda binaria

> Mariano tiene 35 ladrillos, y los quiere usar para construir una escalera maciza. Cada nivel de la escalera va a usar un ladrillo menos que el anterior. Por ejemplo, una escalera de 4 niveles sería una cosa así:
>
>        #
>       ##
>      ###
>     ####
>
> Los 35 ladrillos de mariano son suficientes para construir una escalera de 7 niveles pero no para construir una de 8, ya que harían falta 36 ladrillos (1+2+3+4+5+6+7+8).
>
> Dada una cantidad de ladrillos N, ¿cuántos niveles de escalera se pueden construir?
>
> Nota: para construir una escalera de K niveles se necesitan K\*(K+1)/2 ladrillos.
>
> ### Cota
>
> 1 <= N <= 5 \* 10^18

La forma más directa de resolver este problema sería probar con un nivel, con dos, con tres y así hasta encontrar una cantidad de niveles que sea imposible de construir con N ladrillos.  Si se pueden construir K niveles, esto tiene complejidad O(K).

Para saber si es suficientemente rápido tendríamos que ver qué tan grande puede ser K en el peor caso. Resulta que si N<=5\*10^18 entonces K<=3,16\*10^9. Como normalmente se pueden hacer 10^8 operaciones por segundo, esto es demasiado lento (31,6 segundos).

## Solución más rápida

**Observación:** Si no nos alcanza para construir K niveles, tampoco alcanza para construir K+1 ni K+2 ni K+3, etc.

En otras palabras, si probamos con todos los numeros naturales K, la secuencia de respuestas a la pregunta *¿Puedo construir K niveles con N ladrillos?* va a tener esta pinta:

    SI, SI, ... (muchos SI) ..., SI, SI, NO, NO, NO, ... (NO hasta el infinito)

De ahí sacamos la idea de que no hace falta probar todos los numeros: puedo ir saltando y, si me paso, retroceder. Por ejemplo, si saltamos de 1000 en 1000, al final solo tenemos que verificar uno por uno a 1000 valores de K (los que están entre medio del ultimo que me dio que sí y el primero que me dio que no). Podemos estimar que este algoritmo resuelve el caso N = 5\*10^18 en aproximadamente 0,03 segundos.

- Ejercicio: acá elegimos un salto de 1000. ¿Cuál sería el mejor salto posible en términos de N?

Aunque esa solución es suficientemente rápida para este problema, igual tiene que evaluar más de 3 millones de valores de K (Si elegimos bien el salto, se puede bajar a aproximadamente cien mil). Veamos una forma de hacerlo evaluando unos 30 valores de K.

## Solución aún más rápida

Vamos a volver a aprovechar que si nos pasamos se puede retroceder.

Supongamos que sabemos un valor a para el cual es posible construir esa cantidad de niveles y un valor b para el cual no es posible construir esa cantida de niveles. (Por ejemplo, siempre puedo construir un nivel y nunca puedo construir N+1).

En otras palabras, K está entre a y b. Como no sabemos exactamente K, podemos probar con una elección razonable: el punto medio entre a y b, m=(a+b)/2.

- Si se pueden construir m niveles, entonces K está entre m y b. (m toma el rol de a)
- Si no se pueden construir m niveles, entonces K está entre a y m. (m toma el rol de b)

En ambos casos la cantidad de posibilidades se divide a la mitad. Si inicialmente tenemos N posibilidades, ¿cuántas veces lo tengo que dividir a la mitad para que me quede solo una?

    N * (1/2) * (1/2) * (1/2) * ... (x veces) = 1
                                            N = 1 * 2 * 2 * 2 * ... (x veces)
                                            N = 2^x
                                      log2(N) = x

O sea, este algoritmo solo evalua O(log(N)) valores de K.

En la práctica, muchas veces elegimos el valor de b a mano porque es más fácil que calcular un valor razonable a partir de N. Por ejemplo antes vimos que K siempre es menor a 3,2\*10^9, asique podemos hard-codear ese valor. Entonces, nuestro algoritmo solo termina haciendo log2(3,2\*10^9) =~ 32 evaluaciones

```c++
long long buscar(long long N) {
  long long a = 1, b = 3200000000;
  while (b - a > 1) {
    long long m = (a + b) / 2;
    if (m*(m+1)/2 <= N) {
      a = m;
    } else {
      b = m;
    }
  }
  return a;
}
```

## Forma general de la búsqueda binaria

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

## Implementación de referencia

```c++
// Suponiendo que P(a) es false y P(b) es true
// Encuentra el punto de corte
pair<int, int> busqueda_binaria(int a, int b) {
	while (b - a > 1) {
		int m = (a+b)/2;
		if (P(m)) {
			b = m;
		} else {
			a = m;
		}
	}

	// en este punto esta garantizado que:
	// - P(a) == false
	// - P(b) == true
	// - a + 1 = b
	return {a, b};
}
```

## Aplicacion a búsqueda en un array ordenado

```c++
// Encuentra x en un array ordenado
// Devuelve el índice de la primera aparición de x, si la hay
// Devuelve -1 si no hay ningún x
int encontrar(int arr[], int n, int x) {

	// Idea: búsqueda binaria con la condición "P(m) = arr[m] >= x"

	int a = -1; // Me imagino que arr[-1] <  x
	int b = n;  // Me imagino que arr[n]  >= x

	while (b - a > 1) {
		int m = (a+b)/2;
		if (arr[m] >= x) {
			b = m;
		} else {
			a = m;
		}
	}

	// Ahora se que:
	//   arr[b] >= x (o que b ==  n)
	//   arr[a] <  x (o que a == -1)

	// Para estar seguro, me fijo que b sea un indice valido y
	// que el elemento en esa posicion realmente sea x
	if (b != n && arr[b] == x) {
		return b;
	} else {
		return -1;
	}
}
```
