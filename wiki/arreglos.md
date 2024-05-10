
# Arreglos

Los arreglos son listas de valores de algun tipo (todos los valores del mismo
tipo). Los valores se organizan de izquierda a derecha y se definen posiciones
dentro del arreglo, entre medio de los elementos.

Por ejemplo, un arreglo `A` de 5 elementos y sus posiciones:

```
A = [ 33 , 15 , 20 , -8 , 70 ]
    ^    ^    ^    ^    ^    ^
    0    1    2    3    4    5
```

Los sub-arreglos son pedazos de los arreglos, definidos por dos posiciones. Por
ejemplo, el sub-arreglo de `A` definido por las posiciones `1` y `3` se denomina
`A[1..3]` y luce asi:

```
A = [ 33 , 15 , 20 , -8 , 70 ]
         ^~~~~~~~~~^
         1         3
```

Si el arreglo tiene `N` elementos, el sub-arreglo `0..N` equivale al arreglo
entero. Por ejemplo, el sub-arreglo `A[0..5]`:


```
A = [ 33 , 15 , 20 , -8 , 70 ]
    ^~~~~~~~~~~~~~~~~~~~~~~~~^
    0                        5
```

Un sub-arreglo definido por posiciones `l` y `r` tiene longitud `r-l`. Por
ejemplo `A[1..3]` tiene longitud `3-1 = 2`, y `A[0..5]` tiene longitud `5-0 = 5`.

Los arreglos nos permiten acceder a sus elementos segun su posicion.

`A[i]` es el elemento a la derecha de la posicion `i`. No es posible acceder al
elemento a la derecha de la ultima posicion, ya que este no existe (mejor dicho,
hacerlo puede provocar un error). Por ejemplo:

```
A = [ 33 , 15 , 20 , -8 , 70 ]
    ^    ^    ^    ^    ^    ^
    0    1    2    3    4    5

A[0] == 33
A[1] == 15
A[4] == 70
A[5] == ERROR!
```

Normalmente usamos el bucle `for` para procesar todos los elementos de un
arreglo de izquierda a derecha:

```c++
int const N = 5;
int A[N] = { 33, 15 , 20 , -8 , 70 };
for (int i = 0; i < N; ++i) {
	cout << A[i] << endl;
}
```

## Operaciones interesantes

```c++

// llena el rango l..r del array A con el valor x
// usar llenar(A,0,n,x) para llenar todo
void llenar(int A[], int l, int r, int x) {
	for (int i = l; i < r; ++i) {
		A[i] = x;
	}
}

// invierte el rango l..r del array A
// usar invertir(A,0,n) para invertir todo
void invertir(int A[], int l, int r) {
	while (l < r) {
		swap(A[l], A[r]);
		l++;
		r--;
	}
}

// intercambia los elementos l..m con los elementos m..r en el array A
void rotar(int A[], int l, int m, int r) {
	invertir(A, l, m);
	invertir(A, m, r);
	invertir(A, l, r);
}

// devuelve la suma de los elementos l..r de A
int suma(int A[], int l, int r) {
	int resultado = 0;
	for (int i = l; i < r; ++i) {
		resultado = resultado + A[i];
	}
	return resultado;
}

// devuelve el maximo de los elementos l..r de A
int maximo(int A[], int l, int r) {
	int resultado = INT_MIN; // minimo valor posible de un entero, es el "elemento neutro" de la operacion max
	for (int i = l; i < r; ++i) {
		resultado = max(resultado, A[i]);
	}
	return resultado;
}

// construye las sumas parciales de A[l..r] en B[0..(r-l+1)]
void sumas_parciales(int A[], int l, int r, int B[]) {
	B[0] = 0;
	int j = 0;
	for (int i = l; i < r; ++i, ++j) {
		B[j+1] = B[j] + A[i];
	}
}

int busqueda_lineal(int A[], int l, int r, int x) {
	for (int i = l; i < r; ++i) {
		if (A[i] == x) {
			return i;
		}
	}
	return r;
}

int busqueda_lineal(int A[], int l, int r, int x) {
	while (l < r && A[l] != x) l++;
	return l;
}

```
