# Lazy propagation

Actualizaciones en rango

```c++
consultar(L, R)  { return A[L] + A[L+1] + ... + A[R-2] + A[R-1]; }
actualizar(L, R, X) { for I = L...R { A[I] += X; } }
```

De la misma formar que el segment tree descompone un rango en pocos bloques para
calcular el resultado de una consulta, es posible descomponer un rango en pocos
bloques para actualizar todos los elementos del rango rápidamente.

La idea es modificar solo los bloques necesarios para cubrir el rango. Por
ejemplo, si queremos sumar +3 a cada elemento de un rango podríamos hacer estas
modificaciones:

```
[                                              ]
[                      ][                      ]
[          ][    +6    ][    +6    ][          ]
[    ][ +3 ][    ][    ][    ][    ][    ][    ]
        ^                             ^
        L                             R
```

> Notar que a cada nodo le sumamos una cantidad correspondiente a la longitud
> del rango que representa.

El problema surge al realizar una consulta en alguno de los nodos que se
encuentran por debajo de los nodos modificados. En este caso, se nos pierde la
modificación.

```
[                                              ]
[                      ][                      ]
[          ][    +6    ][    +6    ][          ]
[    ][ +3 ][    ][####][####][    ][    ][    ]
                    ^           ^
                    L           R
```

La solución es relativamente sencilla. Al actualizar un nodo dejamos marcado en
sus hijos que quedó pendiente aplicarles esa actualización. La proxima vez que
se acceda a esos nodos, se debe aplicar y dejar marcada la operación pendiente
en sus hijos (y así hasta que la operación se propague hasta una hoja, que no
tiene hijos).

De esta forma, a medida que accedemos al arbol, siempre vemos nodos que estan
completamente actualizados, incluso si hay nodos con actualizaciones pendientes
más profundo en el subarbol.

## Implementación de referencia

```c++
// !!! ADVERTENCIA: Código no testeado !!!

int const ST_LEN = 1<<20;
int st[ST_LEN*2];
int lazy[ST_LEN*2];

void init() {
	for (int i = 1; i < ST_LEN*2; ++i) st[i] = lazy[i] = 0;
}

void propagate(int i, int l, int r) {
	if (i < ST_LEN) {
		lazy[i*2] += lazy[i];
		lazy[i*2+1] += lazy[i];
	}
	st[i] += lazy[i] * (r-l);
	lazy[i] = 0;
}

int ql, qr, qx;

int query_aux(int i, int l, int r) {
	propagate(i, l, r);
	if (ql <= l && r <= qr) return st[i];
	if (qr <= l || r <= ql) return 0;
	int m = (l+r)/2;
	return query_aux(i*2,l,m) + query_aux(i*2+1,m,r);
}
int query(int l, int r) {
	ql = l; qr = r;
	return query_aux(1, 0, ST_LEN);
}

void update_aux(int i, int l, int r) {
	propagate(i, l, r);
	if (ql <= l && r <= qr) { lazy[i] = qx; propagate(i, l, r); return; }
	if (qr <= l || r <= ql) return;
	int m = (l+r)/2;
	update_aux(i*2,l,m); update_aux(i*2+1,m,r);
	st[i] = st[i*2] + st[i*2+1];
}
void update(int l, int r, int x) {
	ql = l; qr = r; qx = x;
	update_aux(1, 0, ST_LEN);
}
```

## Otras operaciones

Al igual que el segment tree común, la idea de lazy propagation aplica a muchas
operaciones distintas (aunque no a cualquiera, ya que tiene que ser posible
calcular el resultado de un nodo sin calcular los resultados de los subárboles).

Algunas mas o menos conocidas:

- consulta de suma, actualizacion de suma
- consulta de suma, actualización de producto
- consulta de max o min, actualización de suma
- consulta de max y min, actualización de producto (al multiplicar por negativo se intercambia max y min)
- consulta de suma, actualizacion de reemplazar x por 1-x

## Problemas

> TODO: Agregar problemas de lazy propagation!!
