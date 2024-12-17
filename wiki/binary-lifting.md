# Binary Lifting

Tambien conocida como "estructura de los saltitos con potencias de dos".

```c++
// representacion de arbol tipica, donde cada nodo tiene el id del padre
struct Nodo {
	int padre;
}

Nodo nodos[MAXN];

// da k saltitos "hacia arriba". En el peor caso hace N pasos.
int ancestro(int u, int k) {
	for (; k >= 1; k -= 1) u = nodos[u].padre;
	return u;
}
```

Ligera mejora: ir el doble de rapido guardando saltitos de tamaño 2

```c++
struct Nodo {
	int padre;
	int abuelo;
}

Nodo nodos[MAXN];

// En el peor caso hace (N/2) pasos.
int ancestro(int u, int k) {
	for (; k >= 2; k -= 2) u = nodos[u].abuelo;
	for (; k >= 1; k -= 1) u = nodos[u].padre;
	return u;
}
```

Podemos seguir esta idea, guardando el ancestro de distancia 4, 8, 16, ... y así
para cada potencia de dos.

Logicamente, no necesitamos una potencia de dos mas grande que N, asique con
guardar `log(N)` saltitos alcanza.

Aparte, para hacer un salto de distancia k, lo podemos pensar como que hay que
descomponer k como suma de potencias de dos. O sea, podemos aprovechar la
representacion binaria de k.

Pensando esto, tiene sentido que vamos a usar cada potencia de dos a lo sumo una
vez.

```c++
struct Nodo {
	int ancestro[LOGN];
}

Nodo nodos[MAXN];

// Hace log(N) pasos.
int ancestro(int u, int k) {
	dforn(i, LOGN) {
		// si k tiene el bit i prendido, salto pow(2,i) para arriba
		if (k & (1<<i)) u = nodos[u].ancestro[i];
	}
	return u;
}
```

# Mejora: Sumar valores en ancestros

Si cada nodo tiene un valor, podemos imaginar una consulta que pide sumar los
valores de k ancestros de un nodo (o encontrar el maximo, el minimo, el MCD, los
tres maximos, etc.)

En la implementación típica hariamos así:

```c++
struct Nodo {
	int valor;
	int padre;
}

Nodo nodos[MAXN];

int sumar(int u, int k) {
	int x = 0;
	for (; k >= 1; k -= 1) x += nodos[u].valor,
		                   u  = nodos[u].padre;
	return x;
}
```

Si guardamos en cada nodo, aparte de su valor, la suma de su valor y su padre,
la de los primeros 4 ancestros, los primeros 8, 16, etc. Entonces podemos
aplicar la misma idea de antes, de ir sumando segun los digitos de `k` en
binario.

```c++
struct Nodo {
	int suma[MAXN];
	int ancestro[MAXN];
};

int sumar(int u, int k) {
	int x = 0;
	dforn(i, LOGN)
		if (k & (1<<i)) x += nodos[u].suma[i],
			            u  = nodos[u].ancestro[i];
	return x;
}
```

## Mejora: búsqueda binaria en ancestros

Si tenemos una condicion que es falsa en un nodo, pero al acercarse a la raiz
hay un punto en el cual se vuelve verdadera y despues es siempre verdadera,
podemos hacer busqueda binaria usando esta estructura.

La idea es ir fijandose si al hacer un salto la condicion sigue siendo falsa. En
caso de que sí, hacemos ese salto. En caso de que no, probamos con un salto más
chico.

```c++
int ultimo_falso(int u, auto&& condicion) {
	assert(!condicion[u]);
	dforn(i, LOGN)
		if (!condicion(nodos[u].ancestro[i]))
			u = nodos[u].ancestro[i];
}
```

## Mejora: LCA

Esta estructura se puede usar para calcular el menor ancestro común entre dos
nodos.

## Mejora: Sumar valores en caminos

Cualquier camino entre dos nodos pasa por el LCA de los dos. Esto permite
descomponer el camino en una parte que son todos ancestros de un nodo y otra que
son todos ancestros del otro.

Para calcular la suma en cada parte podemos usar la tecnica de suma en ancestros
que vimos antes.

## Mejora: Búsqueda binaria en un caminos

Siguiendo la misma idea de recien, podemos hacer busqueda binaria mirando dos
partes de un camino por separado.

## Version con O(N) memoria

Esto ya es esoterico y poco util, pero hay una estructura similar pero que usa
`O(N)` memoria.

Esta version de la estructura guarda solo dos saltos en cada nodo: uno hacia su
padre y otro hacia un ancestro más lejano.

El chiste es que la distancia a ese ancestro más lejano se elije por separado en
cada nodo, de una forma que se puede llegar rápido a cualquier ancestro.

Ver más acá: <https://codeforces.com/blog/entry/74847>
