
# Potenciacion rapida

Para elevar un numero `x` a una potencia `n` hay un algoritmo sencillo que
corre en tiempo `O(n)`:

```c++
int potencia(int x, int n) {
	int y = 1;
	for (int i = 0; i < n; ++i) {
		y = y * x;
	}
	return y;
}
```

Esto tambien se puede escribir recursivamente

```c++
int potencia(int x, int n) {
	if (n == 0) return 1;
	return x * potencia(x, n-1);
}
```

A este codigo le podemos agregar un atajo aprovechando que

    potencia(x, a * b) = potencia(potencia(x, a), b)

Cuando el exponente es par tenemos el caso particular `n = 2*m` entonces:

      potencia(x, 2*m)
    = potencia(potencia(x, 2), m)
    = potencia(x*x, m)
    = potencia(x*x, n/2)

Por lo tanto podemos agregar un atajo a nuestro codigo:

```c++
int potencia(int x, int n) {
	if (n == 0) return 1;
	if (n%2 == 0) return potencia(x*x, n/2);
	return x * potencia(x, n-1);
}
```

Algunas observaciones:

- Si `potencia` se llama con un `n` par, recursiona con `n/2`.
- Si se llama con `n` impar, entonces hace una llamada recursiva con `n-1`, que
  es par, y despues recursiona con `(n-1)/2`.

Entonces, cada uno o dos pasos de recursion, el `n` se divide por dos.

Por lo tanto podemos concluir que esta funcion tiene costo `O(log n)`.

## Potenciacion de otras cosas

Esto mismo anda al hacer operaciones en modulo.

```c++
int const mod = 1000000007;
int mulmod(int x, int y) {
	return ((long long)x) * y % mod;
}
int potmod(int x, int n) {
	if (n == 0) return 1;
	if (n%2 == 0) return potmod(mulmod(x,x), n/2);
	return mulmod(x, pot(x, n-1));
}
```

Y tambien para objetos mas complicados, como matrices

```c++
Matriz matmul(Matriz x, Matriz y) {
	// ... omitido ...
}
Matriz matpot(Matriz x, int n) {
	if (n == 0) return mat_identidad;
	if (n%2 == 0) return matpot(matmul(x,x), n/2);
	return matmul(x, matpot(x, n-1));
}
```

## Otros calculos usando el mismo truco

Sumas geometricas (ya sea en `int`, con o sin modulo, o con matrices)

> TO-DO: explicar el truco

```c++
// devuelve 1 + x + x^2 + x^3 + ... + x^(n-1)
int geosum(int x, int n) {
	if (n == 0) return 0;
	if (n%2 == 0) return (1 + x) * geosum(x*x, n/2);
	return 1 + x * geosum(x, n-1);
}
```
