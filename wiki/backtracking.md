
# Backtracking

- [CSES - Chessboard and Queens](https://cses.fi/problemset/task/1624)
- [Codeforces - Help Caretaker](https://codeforces.com/contest/142/problem/C)
- [OIA - Consigamos un solo color](https://juez.oia.unsam.edu.ar/task/112) (\*)

En un monton de problemas, la solución más directa es probar todas las posibilidades y quedarse con la mejor. La cantidad de posibilidades suele ser exponencial en el tamaño del problema asique esto muchas veces no entra, pero con algunas optimizaciones puede entrar para N chico (incluso hasta N=100, dependiendo del problema)

Fundamentalmente, vamos a ver como convertir un programa lento que luce así:

    for
      for
        for
          if
            if
              if
                ....

En un programa mucho más rápido que tiene esta pinta:

    for
      if
        for
          if
            for
              if
                ...

Hay algunas diferencias entre problemas de busqueda (donde queremos construir algo que cumple una propiedad) y problemas de optimización (donde aparte queremos maximizar una funcion de puntaje), asique veamos uno y uno.

# Problema de búsqueda: N Reinas

Enunciado: Colocar N reinas de ajedrez en un tablero de NxN sin que se amenacen.

> En el ajedrez, una reina amenaza a todas las piezas que estan en la misma fila, columna o diagonal.

## Solucion

Vamos a numerar las posiciones del tablero de la siguiente manera:

        0   1   2   3   4   5   6   7
    0 [ 0][ 1][ 2][ 3][ 4][ 5][ 6][ 7]
    1 [ 8][ 9][10][11][12][13][14][15]
    2 [16][17][18][19][20][21][22][23]
    3 [24][25][26][27][28][29][30][31]
    4 [32][33][34][35][36][37][38][39]
    5 [40][41][42][43][44][45][46][47]
    6 [48][49][50][51][52][53][54][55]
    7 [56][57][58][59][60][61][62][63]

Así, se puede calcular el número de una posición a partir de su número de fila y de columna (`posicion = fila * N + columna`) y viceversa también (`fila = posicion / N; columna = posicion % N`).

Entonces, la solución más directa (para un tamaño de tablero N constante) es poner N fors anidados que prueban las posiciones de las reinas.

```c++
void reinas() {
	int const N = 5;
	forn(i1, N*N) forn(i2, N*N) forn(i3, N*N) forn(i4, N*N) forn(i5, N*N) {
		if (!se_amenazan(i1, i2, i3, i4, i5)) {
			imprimir_tablero(i1, i2, i3, i4, i5);
			return;
		}
	}
}
// Implementar se_amenazan() e imprimir_tablero() queda de ejercicio :)
```

Esto no anda si la cantidad de reinas depende del input, pero se puede hacer lo mismo con recursion para manejar una cantidad variable de reinas.

```c++
int N; // tamaño del tablero
vector<int> posiciones;

// n es la cantidad de reinas ya colocadas
// la funcion devuelve si pudo colocar N reinas sin que se amenacen o no
bool colocar(int n) {
	if (n == N) {
		if (se_amenazan(posiciones)) return false;
		imprimir_tablero(posiciones);
		return true;
	}

	forn(i, N*N) {
		posiciones[n] = i;
		if (colocar(n+1)) return true;
	}
	return false;
}

void reinas(int tamano) {
	N = tamano;
	posiciones.resize(tamano);
	colocar(0);
}
```

La idea es asignar la posición de una reina, recursivamente poner el resto de las reinas y si no se pudo retrocedemos y seguimos probando con otras posiciones.

Esto anda, pero para N=6 ya es super lento. Por suerte tiene un par de cosas que son obviamente lentas:

- Para una misma configuración de reinas, prueba todas las permutaciones
- Pone reinas en posiciones ya amenazadas

O sea, no solo prueba configuraciones como esta, que ya era obviamente invalida al colocar la segunda reina:

    [R1][R2][R3][R4][R5]
    [  ][  ][  ][  ][  ]
    [  ][  ][  ][  ][  ]
    [  ][  ][  ][  ][  ]
    [  ][  ][  ][  ][  ]

Si no que también prueba todas sus posibles variantes como por ejemplo esta:

    [R4][R2][R1][R5][R3]
    [  ][  ][  ][  ][  ]
    [  ][  ][  ][  ][  ]
    [  ][  ][  ][  ][  ]
    [  ][  ][  ][  ][  ]

Para resolver el primer punto forzamos algun orden entre las reinas así no probamos todas las permutaciones. Por ejemplo, podemos decidir que cada reina que colocamos va en una posición mayor a todas las anteriores.

Implementativamente, es facil de adaptar el programa: agregamos un parametro que indica la primera posicion a probar. Al recursionar, pasamos la posición elegida más uno.

```c++
bool colocar(int n, int i0) {
	// ...

	forr(i, i0, N*N) {
		posiciones[n] = i;
		if (colocar(n+1, i+1)) return true;
	}

	// ...
}
```

Al no probar permutaciones, se dividió la complejidad por `factorial(N)`. Con esto va rápido hasta N=8. No cambió tanto, pero es fácil de hacer y al combinarla con la proxima optimización se potencia bastante.

Ahora resolvemos el segundo punto.

La idea es verificar si la configuracion elegida es válida en cada paso de la busqueda en vez de solo al final.

Si modificamos `se_amenazan()` tal que tome la cantidad de reinas colocada, lo podemos codear fácil asi:

```c++
bool colocar(int n, int i0) {
	if (se_amenazan(posiciones, n)) return false;

	// ...
}
```

En general no es fácil calcular cuánto va a acelerar el programa este tipo de cosas, pero en este programa en particular, esta optimización nos permite acotar el programa a `O(factorial(N))`. (porque, al poner una pieza por fila y columna, el array de posiciones es una permutacion).

Bueno, en realidad la complejidad es mucho menor que N factorial, pero se re complica el análisis :(.

## Optimizaciones especificas al problema

Estas dos optimizaciones tal cual se ven arriba se pueden aplicar a cualquier problema, pero es muy común tunearlas para el problema particular.

Por ejemplo, podemos combinar el orden de las reinas con la idea de que cada reina va en una fila distinta y forzar a que `colocar(n)` siempre coloque una reina en la fila `n`:

Como esto codifica el orden en el parametro `n`, ya no hace falta el otro parametro `i0`.

```c++
bool colocar(int n) {
	// ...

	int fila = n;
	forn(columna, N) {
		int i = fila * N + columna;
		posiciones[n] = i;
		if (colocar(n+1)) return true;
	}

	// ...
}
```

El chequeo de validez tambien se puede optimizar para este problema.

Si mantenemos un conjunto de columnas y diagonales amenazadas, podemos solo colocar reinas en posiciones que no estan amenazadas. Y, si nunca ponemos reinas que se amenazan, no hace falta verificarlo al principio de la funcion ni en el caso base.

```c++
bool col[MAXN];
bool diag1[MAXN];
bool diag2[MAXN];
bool colocar(int n) {
	if (n == N) {
		// El tablero es valido por construccion :D
		imprimir_tablero();
		return true;
	}

	int fila = n;
	forn(columna, N) {
		int i = fila * N + columna;

		int d1 = fila + columna;
		int d2 = fila - columna + (N-1);

		if (col[columna] || diag1[d1] || diag2[d2]) continue;

		// marco como ocupadas
		col[columna] = diag1[d1] = diag2[d2] = true;

		posiciones[n] = i;
		if (colocar(n+1)) return true;

		// marco como libres
		col[columna] = diag1[d1] = diag2[d2] = false;
	}

	return false;
}
```

> Un ultimo truco seria guardar los arreglos de booleanos con mascaras de bits y pasarlos como argumento de la recursion en vez de que sean globales, pero se pone bastante el feo el código.

Estos trucos especificos al problema pueden servir para sumarle 4 o 5 al máximo N que puede manejar nuestro código. Parece poco, pero en problemas de backtracking es bastante.

# Problema de optimización: tractores

Enunciado: Colocar la mayor cantidad de tractores posibles en un tablero de NxM, sin que se solapen. Un tractor se puede rotar multiplos de 90 grados, y puede tener una de las siguientes formas:

    ###    #       #       #
     #     ###     #     ###
     #     #      ###      #

> Vamos a ver cómo calcular la máxima cantidad sin devolver la configuración que la logra, pero sería fácil cambiar el código para que también la devuelva.

## Solución

De nuevo, la idea es hacer una función recursiva que va poniendo y sacando tractores. En los problemas de optimización aplican las mismas optimizaciones que a los problemas de busqueda:

- En vez de poner tractores en cualquier lugar, y verificar que sea una configuración válida (sin tractores solapados) al final, podemos evitar construir configuraciones inválidas

- Para no probar permutaciones de la misma configuración, podemos forzar un orden entre los elementos (que la esquina superior izquierda de cada tractor esté en una posición mayor a la de todos los anteriores)

Para no ser completamente repetitivo, vamos a arrancar con esas optimizaciones ya implementadas.

La principal diferencia entre un problema de optimización y uno de busqueda es que no podemos cortar la busqueda después de encontrar una configuración válida cualquiera, sino que tenemos que seguir explorando porque puede haber configuraciones mejores.

Esto hace que los problemas de optimización sean, a grandes rasgos, más difíciles de optimizar que los de búsqueda.

```c++
int N, M;
bool tablero[MAXN][MAXN];

int tractores(int n, int i0) {

	int mejor_calidad = n;
	forr(i, i0, N*M) {
		forn(rotacion, 4) {
			if (!tractor_dentro_del_tablero(i, rotacion)) continue;
			if (tractor_solapa_tablero(i, rotacion)) continue;

			poner_tractor(i, rotacion);

			int calidad = tractores(n+1, i+1);
			if (calidad > mejor_calidad) mejor_calidad = calidad;

			sacar_tractor(i, rotacion);
		}
	}

	return mejor_calidad;
}
// todas las funciones para manipular el tablero son ejercicios :shrug:
```

Esto anda, pero toma 36 segundos en resolver el caso de 8x8.

La principal optimización se llama "branch and bound". La idea es calcular una cota superior a la calidad que se puede obtener en una rama de la busqueda. Si no es mayor a la mejor calidad ya encontrada (globalmente), no hace falta seguir explorando esa rama.

Por ejemplo, en este problema sabemos que un tractor ocupa 5 posiciones y la cantidad de posiciones libres desde `i0` en adelante es a lo sumo `N*M-i0`. Por lo tanto, siendo super optimistas, la máxima cantidad de tractores que podriamos llegar a poner es `(N*M-i0)/5`.

La implementación es así:

```c++
int mejor_calidad_global = 0;
int tractores(int n, int i0) {

	int mejor_calidad = n;

	int calidad_optimista = n + (N*M-i0)/5;
	if (calidad_optimista <= mejor_calidad_global)
		return mejor_calidad;

	forr(i, i0, N*M) {
		// ...
	}
		
	// ...

}
```

Esto baja el tiempo de 36 segundos a 6 segundos (Para N=8, M=8).

El tiempo de ejecución puede variar mucho dependiendo de la cota que logremos calcular. Si calculamos una cota más ajustada (o sea mas baja, pero que sigue siendo cota superior), el backtracking anda mucho más rápido.

Por ejemplo, si contamos las casillas realmente libres mirando el tablero:

```c++
int tractores(int n, int i0) {
	// ...

	int libres = 0;
	forr(i, i0, N*M) {
		int fila = i / M, columna = i % M;
		if (!tablero[fila][columna]) libres++;
	}
	int calidad_optimista = n + libres/5;

	// ...
}
```

Con este cambio pasamos de 6 segundos a 0,3 segundos (N=8, M=8)

El tiempo de ejecución no solo varía mucho según la cota que calculamos. También depende mucho del orden en que se prueban las distintas posibilidades.

Si recorremos las posibles soluciones en orden creciente, nunca vamos a eliminar opciones porque todas las opciones futuras pueden llevar a una solución mejor.

O sea, si las primeras soluciones que se intentan son todas malas, no se van a saltear las que son intermedias. En cambio, si primero se prueban algunas mas o menos buenas, se van a saltear todas las que son malas e intermedias.

Esto se puede ver eligiendo las posiciones de los tractores en orden inverso:

```c++
int tractores(int n, int i0) {
	// ...

	// dforr va bajando de NM-1 hasta i0 en vez de ir subiendo
	dforr(i, i0, N*M) {
		forn(rotacion, 4) {
			if (!tractor_dentro_del_tablero(i, rotacion)) continue;
   			// ...
		}
	}

	// ...
}
```

Con este cambio se vuelve lentísimo.

Hay problemas de backtracking que se pueden resolver con solo elegir el orden correcto. Por ejemplo, [el problema del caballito](https://es.wikipedia.org/wiki/Problema_del_caballo), donde queremos encontrar un camino de caballo en un tablero de ajedrez, que toque cada posición del tablero exactamente una vez.

En ese problema, si hacemos un backtracking que primero intenta moverse hacia posiciones con la mínima cantidad de vecinos disponibles, termina corriendo en tiempo lineal!

Si no sabemos qué orden elegir, una opción es usar un orden aleatorio. Esto no suele ser tan bueno, pero también evita casos super malos que pueden surgir al elegir siempre la primera opción disponible. Por ejemplo, en el problema de las N reinas elegir un orden aleatorio funciona super bien, y nos permite resolver el problema para N=100 casi instantaneamente.
