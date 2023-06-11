# Tabla aditiva


## Problema

Se da un array de N enteros y Q operaciones. Las operaciones son del siguiente tipo:

- Dados `l` y `r`, imprimir la suma desde la posicion `l` hasta la posicion `r` del array.

# Idea general

Tomo un arreglo A y calculo las sumas de todos los prefijos en el arreglo P.

```
n = 8
A = [ 1,  3,  6,  5,  2,  7,  1,  4]
P = [ 1,  4, 10, 15, 17, 24, 25, 29]
      0   1   2   3   4   5   6   7
```

Ahora puedo calcular consultas de suma de rangos en O(1) restando un prefijo de otro.

Por ejemplo, la suma del rango A[2, 5) (osea `A[2]+A[3]+A[4]`) es 17−4=13 (la suma del cero al cinco (sin incluir), menos la suma del cero al dos (sin incluir))

En otras palabras: `A[2]+A[3]+A[4] = (A[0]+A[1]+A[2]+A[3]+A[4]) - (A[0]+A[1])`

## Detalles de implementación

En una implementación real, agrego un cero inicial para ahorrarme algunos `+1` y `-1` en el código:

```
n = 8
A = [ 1,  3,  6,  5,  2,  7,  1,  4]
P = [ 0,  1,  4, 10, 15, 17, 24, 25, 29]
      0   1   2   3   4   5   6   7   8
```

Esto permite calcular la suma del rango A[l, r) en O(1) mediante `P[r]-P[l]`.

## Implementacion de referencia

```c++
int A[MAXN];
ll  P[MAXN];
int n;

void init() {
	P[0] = 0;
	for (int i = 0; i < n; ++i) {
		P[i+1] = P[i] + A[i];
	}
}

// suma de l a r (sin incluir r)
ll suma(int l, int r) {
	return P[r] - P[l];
}

void update(int p, int x) {
	A[p] = x;
	init();
}
```
