# Programación dinámica

Si la fuerza bruta es para sacar un par de puntos en cualquier problema, la
programación dinámica sirve para sacar "bastantes" puntos en "bastantes" problemas.

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

## Numeros de fibonacci

La secuencia de fibonacci comienza con los valores cero y uno. Cada elemento de
ahi en adelante es igual a la suma de los dos anteriores. En notacion matemática
tendríamos esto:

```
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)    (si n >= 2)
```

La forma más directa de traducir esto a código es usando una función recursiva:

```c++
int f(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (n >= 2) return f(n-1) + f(n-2);
}
```

El problema con esto es que es extremadamente lento (probá llamar esta función
con distintos valores de n menores a 100 y medir cuanto tiempo toma).

Se vuelve lento porque calcula los mismos valores de f muchas veces. Por
ejemplo, para calcular `f(100)`, ¡tiene que calcular `f(95)` 8 veces!

## Calculo con tabla

Como dice en la introducción, podemos usar una tabla para acelerar el calculo:

```c++
int f(int n) {
  vector<int> tabla(n+1);

  tabla[0] = 0;
  tabla[1] = 1;
  for (int i = 2; i <= n; ++i)
    tabla[i] = tabla[i-1] + tabla[i-1];

  return tabla[n];
}
```

De esta forma, cada valor de la tabla se calcula una sola vez, y tenemos un
programa mucho más eficiente.

En este fue fácil usar una tabla, pero muchas veces se complica.

## Memorización

En cambio podemos aplicar un truco muy sencillo: agregarle una tabla a la
función recursiva. Si el valor ya fue calculado, que devuelva el valor de la
tabla. Si no, que lo calcule y lo guarde en la tabla.

```c++
bool fue_calculado[1000];
int tabla[1000];
int f(int n) {
    if (fue_calculado[n]) return tabla[n];

    int resultado;

    if (n == 0) resultado = 0;
    if (n == 1) resultado = 1;
    if (n >= 2) resultado = f(n-1) + f(n-2);

    tabla[n] = resultado;
    fue_calculado[n] = true;

    return resultado;
}
```

Esto tiene el mismo efecto que el calculo directo con tabla (cada posición se
calcula una sola vez), pero la traducción dada la forma recursiva es mucho más
directa.

Como mantener dos tablas resulta engorroso, podemos trabajar con un valor
especial. Ponemos un "-1" en todas las posiciones de la tabla que no fueron
calculadas, y luego verificar si un valor fue calculado es tan simple como
verificar que sea distinto a `-1`.

```c++
int tabla[1000];
void iniciar_tabla() {
    memset(tabla, -1, sizeof(tabla)); // truquito para llenar de -1
}
int f(int n) {
    if (tabla[n] != -1) return tabla[n];
    if (n == 0) return tabla[n] = 0;
    if (n == 1) return tabla[n] = 1;
    if (n >= 2) return tabla[n] = f(n-1) + f(n-2);
}
```

Aunque todos los algorítmos de programación dinámica se pueden escribir de forma
iterativa en vez de recursiva (y, de hecho, así corren más rápido), la realidad
es que en OIA no suele surgir la necesidad de hacerlo. De ahí surge la
perspectiva (muy útil) que la programación dinámica es una simple optimización
para funciones recursivas.

> 📝 ¿Qué es el espacio de estado de una DP? 📝

> 📝 ¿Cómo se calcula la complejidad de una DP? 📝

### Problemas

- <https://cses.fi/problemset/task/1633>
- <https://cses.fi/problemset/task/1637>
- <https://cses.fi/problemset/task/1744>
- (\*) <https://cses.fi/problemset/task/2413>
- (\*) <https://cses.fi/problemset/task/2181>

## DP sobre arrays y cadenas

Un caso de uso muy común de la DP es para problemas sobre arreglos. En estos
casos el estado de la DP es un índice en ese arreglo (y posiblemente más cosas).
Por ejemplo, pensemos este problema:

> Juancito está en un programa de Guido Kaczka y va a jugar un juego que
> consiste en derribar latas usando una pelota. Primero le dice a Guido cuál
> lata quere derribar y si la derriba se queda con la plata que hay adentro.
>
> Juancito tiene excelente puntería así que no sería problema llevarse toda la
> plata, si no fuera porque la pelota es mas grande que el espacio entre las
> latas.
>
> Resulta que si derriba una lata también derriba las dos vecinas, pero solo se
> lleva la plata que de la lata que él eligió.
>
> Dada la cantidad de plata en las N latas, ¿cuál es la mayor cantidad de plata
> que se puede llevar Juancito?

Como podemos resolverlo?

La solución más directa sería usando una [fuerza bruta recursiva]( backtracking ).

Mirando la lata i-esima tenemos que elegir si tumbarla para conseguir la plata,
o pasar a la siguiente. Como no podemos saber cual es mejor de antemano,
probamos ambas:

```c++
int plata[MAXN];

// buscar(i) = mejor solucion con las latas de i en adelante
int buscar(int i) {
	// Fin de la busqueda: si no hay lata, no hay plata.
	if (i >= n) return 0;

	// Opcion 1: derribo la lata i. La i+1 se cae tambien,
	// paso a la i+2.
	int op1 = plata[i] + buscar(i+2);

	// Opcion 2: salteo la lata i, paso a considerar la i+1.
	int op2 = buscar(i+1);

	return max(op1, op2);
}

int respuesta() {
	return buscar(0);
}
```
<br>

Esta fuerza bruta se convierte muy fácil a una solución de programación
dinámica, agregando memorización:

```c++
int plata[MAXN];
int tabla[MAXN + 2];
int dp(int i) {
	if (tabla[i] != -1) return tabla[i];
	if (i >= n) return 0;
	int op1 = plata[i] + dp(i+2);
	int op2 = dp(i+1);
	return tabla[i] = max(op1, op2);
}
int respuesta() {
	return dp(0);
}
```

> ¡Recordemos llenar la tabla de `-1` antes de llamar `respuesta()`!.

<br>

Las ideas habladas arriba se pueden extender fácilmente a arreglos
multidimensionales, agregando más índices al estado de la DP.

### Problemas

- [Par de pájaros]( https://juez.oia.unsam.edu.ar/task/93 ) / [Vuelo amoroso]( https://juez.oia.unsam.edu.ar/task/136 ) - Nacional 2009 Nivel 2 y 3
- [Reconstruyendo el sendero]( https://juez.oia.unsam.edu.ar/task/116 ) - Nacional 2017 Nivel 2
- (\*) [Al-Garín]( https://juez.oia.unsam.edu.ar/task/4 ) - Provincial 2017 Nivel 3

Algunos problemas clásicos (para googlear):

- longest increasing subsequence
- longest common subsequence
- edit distance

## Longest increasing subsequence (LIS)

Veamos un ejemplo más. Esta vez un problema clásico.

> Dado un array, calcular la logitud de su subsecuencia creciente más larga.
>
> Una secuencia A es subsecuencia de B si podemos llegar de B a A solo
> eliminando elementos.
>
> `[1, 10, 2]` es subsecuencia de `[ 1, 7, 10, 3, 15, 2 ]` porque podemos llegar
> eliminando el `7`, el `3` y el `15`.
>
> Otra forma de verlo es que las subsecuencias de B son las que se pueden formar
> iterando por sus elementos y en cada paso eligiendo ¿me lo quedo o lo borro?.
>
> La subsecuencia creciente mas larga de `[1, 7, 10, 3, 15, 2]` es
> `[1, 7, 10, 15]`, de longitud 4.

Como podemos resolver este problema usando DP?

Hay muchas maneras de plantearlo, veamos un par.

### Forma 1

Nos gustaría armar una función similar a la del problema anterior. Algo de este
estilo:

lis(i) = "longitud de la subsecuencia creciente mas larga con elementos de i en
adelante."

Y que en su implementación pruebe dos opciones (tomo el elemento i o no lo
tomo). Pero sabemos que en una subsecuencia creciente cada elemento debe ser
mayor al anterior. Entonces, ¿cómo hacemos para saber si el elemento que tomamos
es mayor al anterior?  Bueno, vamos a tener que recordar cuál es el último
elemento que agarramos. Para esto agregamos otro argumento nuestra función:

lis(i, j) = "longitud de la subsecuencia creciente mas larga con elementos de i
en adelante, suponiendo que ya agarramos el j"

Ahora sí, esta función va a probar tomar o no tomar el elemento i, pero solo
prueba tomarlo si es mayor al ultimo que se tomó.

```c++
int a[MAXN];
int lis(int i, int j) {

	// Fin de la lista. La subsecuencia mas larga tiene cero elementos
	if (i == n) return 0;

	// No lo tomo. Paso a i+1 sin cambiar el ultimo elemento tomado.
	int ans = lis(i+1, j);

	if (a[i] > a[j]) {
		// Lo tomo. Paso a i+1 sabiendo que se tomó elemento i.
		// Como estoy agregando el elemento i, le sumo uno a la longitud
		// obtenida del resto del arreglo.
		ans = max(ans, 1 + lis(i+1, i));
	}

	return ans;
}
```

Esta definición presenta una incognita: ¿qué valores de i y j pasamos
inicialmente?

Recordemos que i es el punto a partir del cual miramos los elementos y j es un
elemento que consideramos que ya fue tomado. Por lo tanto es lógico que se
cumpla `j < i`. Al mismo tiempo, queremos considerar todos los elementos
posibles, asique nos gustaría un valor de i lo más chico posible. Entonces,
podemos elegir que inicialmente `i = j+1`.

Aparte, al llamar lis desde afuera, j se puede interpretar como "el primer
elemento de la subsecuencia creciente mas larga", pero es imposible saber de
antemano cuál va a ser ese elemento... ¿Entonces? Hacemos lo mismo que venimos
haciendo cuando no sabemos qué valor tomar: probamos todos y nos quedamos con el
mejor.

```c++
int respuesta() {
	int ans = 0;
	for (int j = 0; j < n; ++j) {
		ans = max(ans, 1 + lis(j+1, j));
	}
	return ans;
}
```

¡Ya casí terminamos! Para tener una verdadera solución con programación
dinámica, agreguemosle memorización a la función lis y analicemos la
complejidad:

```c++
int tabla[MAXN+1][MAXN];
int lis(int i, int j) {
	if (tabla[i][j] != -1) return tabla[i][j];

	if (i == n) return 0;
	int ans = lis(i+1, j);
	if (a[i] > a[j]) {
		ans = max(ans, 1 + lis(i+1, i));
	}

	return tabla[i][j] = ans;
}
```

- Tamaño del espacio de estado: O(N^2)
- Complejidad por estado: O(1)
- Complejidad total: O(N^2)

Ejercicio: Modificar el algoritmo para que tenga complejidad O(N \* X), donde
`X` es el mayor valor del arreglo.

### Forma 2

En la sección anterior vimos que fue muy util agregar un argumento que
representa un elemento que ya forma parte de la subsecuencia creciente mas
larga. ¿Qué pasa si partimos de ahí? O sea, ¿será posible armar una función
así?:

lis(j) = "longitud de la subsecuencia creciente mas larga cuyo primer elemento
es j"

Supongamos que el siguiente elemento de la subsecuencia se encuentra en una
posición i. ¿Qué podemos concluir sobre esa posición? Básicamente dos cosas:
primero, que `j < i < n` y después que `a[j] < a[i]`.

Esto no es suficiente para identificar univocamente a i, pero podemos hacer lo
que hacemos siempre: probar todas las opciones que cumplen ambas condiciones y
quedarnos con la mejor.

```c++
int lis(int j) {
	int ans = 1;
	for (int i = j+1; i < n; ++j) {
		if (a[j] < a[i]) {
			ans = max(ans, 1 + lis(i));
		}
	}
	return ans;
}

int respuesta() {
	// Seguimos sin saber cual es el primer elemento... probamos todos.
	int ans = 0;
	for (int j = 0; j < n; ++j) {
		ans = max(ans, lis(j));
	}
	return ans;
}
```

Finalmente agregamos memorización y hacemos el analisis de complejidad:

```c++
int lis(int j) {
	if (tabla[j] != -1) return tabla[j];

	int ans = 1;
	for (int i = j+1; i < n; ++j) {
		if (a[j] < a[i]) {
			ans = max(ans, 1 + lis(i));
		}
	}

	return tabla[j] = ans;
}
```

- Tamaño del espacio de estado: O(N)
- Complejidad por estado: O(N)
- Complejidad total: O(N^2)

Si bien tiene la misma complejidad total que la anterior, este enfoque tiene
un espacio de estados mucho más chico, por lo que su tabla usa mucho menos
memoria.

Ejercicio (\*): Modificar el algoritmo para que tenga complejidad O(N \* X),
donde `X` es el mayor valor del arreglo.

## Ordenar

En muchos problemas queremos probar todas las combinaciones de elementos tal que
cada elemento sea mayor o igual al anterior, pero sin agarrar repetidos.

Para esto parecería que necesitamos una DP cuyo estado es el conjunto de los
elementos tomados.

En realidad esto no siempre es así. Si ordenamos los elementos de menor a mayor,
basta con solo considerar elementos que vienen después del ultimo elemento
tomado. Esto permite que el estado sea sólo el índice del último elemento
tomado.

### Problemas

- 53pts en "Buscando parejas" - Selectivo 2019 Día 1
