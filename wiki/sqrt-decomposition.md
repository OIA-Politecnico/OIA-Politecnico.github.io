
# Descomposición en raíz cuadrada (sqrt-decomposition)

Se dió una clase virtual el 6 de octubre de 2022

- [Diapositivas](https://raw.githubusercontent.com/SebastianMestre/taller-oia/master/Diapositivas/2022-10-6%20Rangos%20TablaAditiva%20SqrtDecomposition%20Bucketing.pdf)

--------------------

## Problema

Se da un array de N enteros y Q operaciones. Las operaciones pueden ser de dos tipos:

- Tipo 1: Dados `x` e `i`, asignar `x` en la posicion `i` del array.
- Tipo 2: Dados `l` y `r`, imprimir la suma desde la posicion `l` hasta la posicion `r` del array.

## Solución ineficiente

Para las operaciones de tipo 1, modificamos el array directamente. Complejidad `O(1)`.

Para las operaciones de tipo 2, hacemos un for de `l` hasta `r`. Complejidad `O(N)`.

Alternativamente, se pueden usar [sumas parciales]( tabla-aditiva ) con los costos intercambiados.

Ambos enfoques son muy lentos cuando N y Q son grandes y hay una mezcla homogenea de operaciones de tipo 1 y 2.

## Idea general

Para responder consultas en rango rápidamente, podemos precalcular la respuesta para bloques de tamaño `K`.

Para las operaciones de tipo 1, recalculamos el resultado para el bloque al que pertenece `i`. Complejidad `O(K)`.

Para las operaciones de tipo 2, combinamos a lo sumo `N/K` bloques. Lo que sobre lo contemplamos con un for más. Complejidad `O(N/K + K)`.


Solemos elegir aproximadamente `K = sqrt(N)`, así ambas operaciones quedan `O(sqrt(N))`

## Implementación de referencia

```c++
int const MAXN = 200000;
int const K = 512; // aproximadamente sqrt(200000)
int const BUCKETS = (MAXN + K - 1) / K;

int A[MAXN];
ll B[BUCKETS];

int n;

void init() {
	forn(i, BUCKETS) B[i] = 0;
	forn(i, n) B[i/K] += A[i];
}

// suma de l hasta r (sin incluir r)
int query(int l, int r) {
	int lb = l/K, rb = r/K, res = 0;
	if (lb == rb) { // ambas puntas en el mismo bloque
		forr(i,l,r) res += A[i];
	} else { // puntas en distintos bloques
		forr(i,l,(lb+1)*K) res += A[i];
		forr(i,lb+1,rb)    res += B[i];
		forr(i,rb*K,r)     res += A[i];
	}
	return res;
}

void update(int p, int x) {
	int pb = p/K;
	A[p] = x; B[pb] = 0;
	forn(i, K) B[pb] += A[pb*K + i];
}
```