
# Segment Tree

Segment tree es una estructura de datos que permite hacer consultas en rango y modificaciones.

```
consultar(L, R)  { return A[L] + A[L+1] + ... + A[R-2] + A[R-1]; }
actualizar(I, X) { A[I] = X; }
```

Ya vimos que esto se puede lograr con actualizaciones en O(1) y consultas en O(N) sin usar ninguna estructura especial. (osea, es rapido cuando hay muchas actualizaciones y pocas consultas)

Tambien vimos que se puede con actualizaciones en O(N) y consultas en O(1) usando tabla aditiva. (rápido cuando hay pocas actualizaciones y muchas consultas)

¿Pero qué hacemos cuándo hay cantidades de consultas y actualizaciones del mismo orden?

¡Acá viene el segment tree!, que tiene complejidad O(log N) tanto para consultas como para actualizaciones.

Internamente, precaclula los resultados en bloques cuyo tamaño son distintas potencias de dos.

> 📝 Agregar un diagrama de verdad 📝

```
[                      16                      ]
[           8          ][           8          ]
[     4    ][     4    ][     4    ][     4    ]
[  2 ][  2 ][  2 ][  2 ][  2 ][  2 ][  2 ][  2 ]
[1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1]
```

Para realizar una consulta, separa el rango pedido en unos pocos bloques y calcula la respuesta sumando esos bloques.

```
            [##########]
                        [####]
         [#]                  [#]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
          ^                       ^
          L                       R
```


Para realizar actualizaciones, recalcula todos los bloques que cubren una posicion. Para que esto sea rápido, se asegura de que cada posición esté cubierta por pocos bloques.

```
[##############################################]
[######################]
            [##########]
            [####]
               [#]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
                ^
                I
```

## Detalles de implementación

Para lograr todo lo que se explica arriba, el segment tree guarda sus datos en forma de arbol: Cada bloque de tamaño 4 es igual a la suma de dos bloques de tamaño 2, cada uno de tamaño 8 se forma con dos bloques de tamaño 4, y así sucesivamente.

Resulta que hay una forma muy cortita de implementar esta lógica usando un *arbol binario implicito*. Osea, en vez de representar ese arbol en memoria, como haríamos con un grafo cualquiera, vamos a seguir algunas reglas que nos permiten usar un simple arreglo:

- El nodo 0 no se usa.
- El nodo 1 es la raíz.
- El nodo `2*x` es el hijo izquierdo del nodo `x`
- El nodo `2*x+1` es el hijo derecho del nodo `x`
- Para todo `x!=1`, el nodo `x/2` (redondeado hacia abajo) es el padre del nodo `x`.

Siguiendo esto, tenemos el siguiente arbol:

> 📝 Agregar un diagrama de verdad 📝

```
             1
            / \
          /     \
        /         \
       2           3
      / \         / \
     /   \       /   \
    4     5     6     7
  /  \  /  \  /  \  /  \
  8  9 10 11 12 13 14 15
```

Así, la raiz representa el rango completo. Su hijo izquierdo representa la primera mitad y su hijo derecho representa la segunda. Aparte, cada hoja representa posiciones especificas del rango.

```
[                       1                      ]
[           2          ][           3          ]
[     4    ][     5    ][     6    ][     7    ]
[  8 ][  9 ][ 10 ][ 11 ][ 12 ][ 13 ][ 14 ][ 15 ]
```

Para lograr una **consulta** recorremos el arbol de forma top-down, comenzando por la raiz.

- Si el nodo está completamente cubierto por la consulta, entonces lo usamos para formar la respuesta y devolvemos el valor de ese nodo.
- Si el nodo está completamente fuera de la consulta, entonces no lo usamos para formar la respuesta y devolvemos 0.
- En los casos restantes, el nodo cubre parcialmente la consulta y hace falta separarlo en dos mitades para lograr una separación adecuada. En ese caso devolvemos la suma de la consulta evaluada en el hijo izquierdo (`2*x`) y la consulta evaluada en el hijo derecho (`2*x+1`).

Para lograr una **actualización** primero actualizamos la hoja correspondiente con la posición que se busca actualizar.

Después recalculamos el valor del padre, y del padre del padre, y así hasta llegar a la raíz.

## Implementación de referencia

```c++
int const ST_LEN = 1 << 20; // 2 elevado a la 20
int st[ST_LEN*2];

void init() {
	for (int i = 1; i < 2*ST_LEN; ++i) st[i] = 0;
}

int ql, qr; // rango de la consulta

// i es el nodo actual
// l es el inicio del rango correspondiente al nodo actual
// r es el final del rango correspondiente al nodo actual
int query_aux(int i, int l, int r) {
	// rango contenido en la consulta, devuelvo el resultado
	if (qr <= l && r <= qr) return st[i];

	// rango fuera de la consulta, ignorar
	if (r <= ql || qr <= l) return 0;

	// interseccion parcial, divido en sub-rangos
	int m = (l+r)/2;
	return query_aux(i*2,l,m) + query_aux(i*2+1,m,r);
}
int query(int l, int r) {
	ql = l; qr = r;
	return query_aux(1, 0, ST_LEN);
}

int update(int i, int x) {
	i += ST_LEN;
	// modifico la hoja
	st[i] = x;
	// actualizo todos sus ancestros
	while (i /= 2) st[i] = st[i*2] + st[i*2+1];
}
```

## Otras operaciones

Si bien lo presentamos como una forma mas "balanceada" de hacer sumas en rango, ¡el segment tree es mucho más poderoso!

A diferencia de la tabla aditiva, el segment tree se puede adaptar a muchas operaciones distintas. En particular, funciona con cualquier operación asociativa que tenga elemento neutro, y solo tenemos que cambiar 4 lineas.

Algunas operaciones asociativas conocidas (y su elemento neutro):

- mínimo (+inf o `INT_MAX`)
- máximo (-inf o `INT_MIN`)
- xor (0)
- suma (0)
- producto (1)
- suma modular (0)
- producto modular (1)
- mayor común divisor (depende del problema)

Por ejemplo, haríamos así para calcular mínimos en rango (las lineas cambiadas tienen un `***`)

```c++
int const ST_LEN = 1 << 20;
int st[ST_LEN*2];
void init() {
	for (int i = 1; i < 2*ST_LEN; ++i) st[i] = INT_MAX;    // ***
}
int ql, qr;
int query_aux(int i, int l, int r) {
	if (qr <= l && r <= qr) return st[i];
	if (r <= ql || qr <= l) return INT_MAX;                // ***
	int m = (l+r)/2;
	return min(query_aux(i*2,l,m), query_aux(i*2+1,m,r));  // ***
}
int query(int l, int r) {
	ql = l; qr = r;
	return query_aux(1, 0, ST_LEN);
}
int update(int i, int x) {
	i += ST_LEN;
	st[i] = x;
	while (i /= 2) st[i] = min(st[i*2], st[i*2+1]);        // ***
}
```

## Aplicación muy avanzada para contar cantidad de ceros consecutivos

Creo que, siendo que puede hacer consultas en rango de cualquier operacion asociativa, queda claro que segment tree es una estructura muy potente. Lo que no es nada obvio en un principio es lo potente que son algunas operaciones asociativas.

En particular, si no nos limitamos a guardar simples enteros, y vamos mas alla.

Digamos que queremos soportar la operacion contar(L, R) = "longitud de la mayor seguidilla de 0s consecutivos en el rango [L..R)".

Vamos a diseñar una operación asociativa que se ajuste a este caso.

Si tengo dos rangos pegados y quiero averiguar la longitud de la mayor seguidilla de 0s en la union de los dos rangos. Qué información necesito?

- La mayor seguidilla del lado izquierdo
- La mayor seguidilla del lado derecho
- La mayor seguidilla que cruza (formada por el mayor sufijo del lado izquierdo, y el mayor prefijo del lado derecho)

```c++
int unir(int mayor_izq, int mayor_sufijo_izq, int mayor_der, int mayor_prefijo_der) {
	return max({mayor_izq, mayor_der, mayor_sufijo_izq + mayor_prefijo_der});
}
```

El problema es que, para despues poder combinar esta información con otros
rangos y construir rangos aún más grandes, voy a necesitar todas las cosas que
usé para calcular la mayor seguidilla. En particular, el mayor prefijo y el
mayor sufijo del rango total.

Osea, no nos va a alcanzar con devolver un entero, si no que tendremos que
devolver una estructura que contiene:

- mayor seguidilla en total
- mayor prefijo
- mayor sufijo

A su vez, para calcular esas cosas será conveniente saber la longitud del rango
y si el rango completo está conformado por ceros.

```c++
struct Ceros {
	int longitud;
	bool todo_cero;
	int izq, der, total;
};
```

Calcular estas cosas no es demasiado complicado. Comenzamos por calcular la longitud y la condición `todo_cero`:

```c++
Ceros unir(Ceros a, Ceros b) {
	int longitud = a.longitud + b.longitud;
	bool todo_cero = a.todo_cero && b.todo_cero;
	// ...
}
```

Con esto podemos calcular el mayor prefijo y el mayor sufijo, tomando en cuenta
que si alguna de las dos mitades está compuesta enteramente por ceros, el mayor
sufijo o prefijo puede cruzar el punto medio.

```c++
Ceros unir(Ceros a, Ceros b) {
	// ...
	int izq = a.todo_cero ? a.longitud + b.izq : a.izq;
	int der = b.todo_cero ? a.der + b.longitud : b.der;
	// ...
}
```

Finalmente, calculamos la mayor seguidilla de ceros y devolvemos la estructura.

```c++
Ceros unir(Ceros a, Ceros b) {
	// ...
	int total = max({a.total, b.total, a.der + b.izq});
	return {longitud, todo_cero, izq, der, total};
}
```

Puede ser sorprendente, pero esta operación también es asociativa, por lo que, si encontramos un elemento neutro, ¡podemos usarla en un segment tree!

Verificarlo queda como ejercicio al lector, pero el elemento neutro es este: `Ceros { .longitud=0, .todo_cero=true, .izq=0, .der=0, .total=0}`

Como ultimo paso solo queda aplicar esta operación en un segment tree.

```c++
struct Ceros {
	int longitud;
	bool todo_cero;
	int izq, der, total;
};

Ceros unir(Ceros a, Ceros b) {
	int longitud = a.longitud + b.longitud;
	bool todo_cero = a.todo_cero && b.todo_cero;
	int izq = a.todo_cero ? a.longitud + b.izq : a.izq;
	int der = b.todo_cero ? a.der + b.longitud : b.der;
	int total = max({a.total, b.total, a.der + b.izq});
	return {longitud, todo_cero, izq, der, total};
}
Ceros const neutro = {0, true, 0, 0, 0};

int const ST_LEN = 1 << 20;
Ceros st[ST_LEN*2];
void init() {
	for (int i = 1; i < 2*ST_LEN; ++i) st[i] = neutro;
}
int ql, qr;
Ceros query_aux(int i, int l, int r) {
	if (qr <= l && r <= qr) return st[i];
	if (r <= ql || qr <= l) return neutro;
	int m = (l+r)/2;
	return unir(query_aux(i*2,l,m), query_aux(i*2+1,m,r));
}
Ceros query(int l, int r) {
	ql = l; qr = r;
	return query_aux(1, 0, ST_LEN);
}
void update(int i, Ceros x) {
	i += ST_LEN;
	st[i] = x;
	while (i /= 2) st[i] = unir(st[i*2], st[i*2+1]);
}

// escondemos el segment tree y la estructura Ceros
// con funciones mas lindas de usar
void asignar(int i, int x) {
	if (x == 0) update(i, {1, true, 1, 1, 1});
	else        update(i, {1, false, 0, 0, 0});
}
int contar(int l, int r) {
	return query(l, r).total;
}

int main() {
	int n; cin >> n;

	init();
	forn(i,n) {
		int x; cin >> x;
		asignar(i, x);
	}

	int q; cin >> q;
	forn(i, q) {
		int t; cin >> t;
		if (t == 1) { // dado un indice i (1<=i<=n) y un valor x, asigna el valor en ese indice
			int i, x; cin >> i >> x; i--;
			asignar(i, x);
		} else { // devuelve la mayor seguidilla de 0s consecutivos en el intervalo [l,r] (1<=l<=r<=n)
			int l, r; cin >> l >> r; l--;
			cout << contar(l, r) << "\n";
		}
	}
}
```


