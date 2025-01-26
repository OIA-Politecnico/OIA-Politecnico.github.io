
# Grafos multicapa

Solemos modelar problemas usando grafos con la idea que un nodo es lo mismo que una posicion en el espacio, y la distancia en el grafo es lo mismo que la distancia en este espacio. Veamos un problema que desafia esta idea.

> Hay una ciudad de NxM. Un auto comienza en la esquina (A,B) y tiene que llegar
> a la esquina (C,D).
> 
> El auto quiere llegar de (A,B) hasta (C,D) girando la menor cantidad de veces
> posibles, pero no le importa la distancia que recorre.
> 
> Aparte, hay k esquinas que contienen obstaculos y, por lo tanto, no son transitables.
>
> Encuentre la minima cantidad de giros necesaria.

La idea de este problema es encararlo con el algoritmo de dijkstra, pero donde
el costo corresponde a la cantidad de giros realizados.

Pero esto supone un problema: ¿cómo detectamos el momento en que el auto gira?

Podriamos guardar en cada nodo la arista por la llega a él el camino minimo.
Pero que pasa si hay otro camino (no minimo) que llega a él por otra direccion y
que termina siendo mas conveniente mas adelante?

Esto nos lleva a concluir que tenemos que guardar cuatro costos en cada nodo:
uno por cada direccion posible desde la que se puede llegar a ese nodo.

Esto puede funcionar pero conlleva hacer modificaciones bastante complejas al
algoritmo de Dijkstra. En cambio, podemos modificar el grafo.

En cambio, podemos crear cuatro nodos por cada esquina de la ciudad, una por
cada dirección desde la que se puede llegar a ese nodo. Luego, conectamos los
nodos de esquinas aledañas que se corresponden a distintas direcciones con costo
1 y los que se corresponden a igual dirección con costo 0.

Así, podemos utilizar el algoritmo de dijkstra comun y corriente.

```c++
// codigo complicado que construye el grafo
int di[4] = {0,-1,0,1};
int dj[4] = {1,0,-1,0};
forn(i, n) forn(j, m) forn(d, 4) {
	for (int o=-1; o<=1; ++o) {
		int d2 = (d+o+4)%4;
		int i2 = i+di[d2], j2 = j+dj[d2];
		if (i2 < 0 || i2 >= n || j2 < 0 || j2 >= m) continue;
		if (obstaculo[i2][j2]) continue;
		int u = nodo(i, j, d);
		int v = nodo(i2, j2, d2);
		int costo = d == d2 ? 0 : 1;
		g[u].push_back({v, costo});
	}
}

// contemplamos que puede arrancar en cualquier direccion
// corriendo el dijkstra cuatro veces
int resultado = infinito;
forn(d, 4) {
	int u = nodo(A, B, d);
	// usamos el dijkstra de toda la vida
	auto costos = dijkstra(u);
	forn(d2, 4) {
		int v = nodo(C, D, d2);
		resultado = min(resultado, costos[v]);
	}
}

cout << resultado << "\n";
```

> Como se ve arriba, al trabajar con grafos mas complicados es conveniente
> escribir una funcion `nodo()` que, dada la informacion necesaria para
> identificar un nodo, devuelve el id numerico de ese nodo.
>
> Tambien puede ser conveniente escribir funciones `fila()`, `columna()` y
> `direccion()` que nos permitan recuperar la informacion del nodo.

Podemos pensar que el grafo que construimos tiene cuatro copias del grafo
original o cuatro capas distintas, una por cada direccion de movimiento posible.
De ahi viene el nombre de grafo multicapa.

## Problemas

- millas3 - OIA Jurisdiccional 2024 Nivel 3
- protesta - OIA Nacional 2009 Nivel 2

# Grafos abstractos

En los grafos multicapa tenemos la idea que 'nodo = posicion + algo más', que no
esta tan lejos del tipico 'nodo = posicion'.

Llevando esta idea mas lejos, tenemos problemas donde los grafos representan
cosas completamente abstractas.

> TO-DO: Completar

> Ideas:

> - Secuencias de De Bruijn
> - Teclado de letras
> - 

## Problemas

> TO-DO: completar
