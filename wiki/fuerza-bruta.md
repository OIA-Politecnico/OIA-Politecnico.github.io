
# Fuerza bruta

Fuerza bruta es la idea de probar todas las opciones y tomar la mejor. Como
primera aproximación tenemos, por ejemplo, códigos que prueban todas las ternas
de elementos de un array, hasta encontrar una que verifica alguna condición:

```c++
forn(i, n) {
	forn(j, i) {
		forn(k, j) {
			if (me_sirve(k, j, i)) {
				cout << k << " " << j << " " << i << "\n";
				return 0;
			}
		}
	}
}
```

Pero hay fuerzas brutas más complicadas. Por ejemplo, qué pasa si la cantidad de
elementos que hay que elegir depende del input? O que pasa si hay que probar
todas las posibles combinaciones? Etc.

## Probar todos los conjuntos

Para probar todas las posibles combinaciones podemos aprovechar la
representación binaria de los números. En particular, la colección de los
numeros desde cero hasta dos elevado a la N se corresponde de una forma sencilla
con todos los posibles conjuntos formados por los numeros 1, 2, 3, ..., N.

```c++
for (int s = 0; s < (1 << n); ++s) {
	cout << "{";
	for (int i = 0; i < n; ++i) {
		if ((s >> i) & 1) {
			cout << " " << i;
		}
	}
	cout << " }\n";
}
```

## Probar todas las permutaciones

Para probar todas las permutaciones podemos aprovechar una funcion de la
biblioteca estándar de C++: `next_permutation`.

```c++
vector<int> p(n);
for (int i = 0; i < n; ++i) {
	p[i] = i;
}

do {
	cout << "[";
	for (int i = 0; i < n; ++i) {
		cout << " " << p[i];
	}
	cout << " ]\n";
} while (next_permutation(begin(p), end(p)));
```

## Probar todas las combinaciones de k elementos, dependiendo k del input

Ahora ya se complica y no nos queda otra que usar recursión.

```c++
vector<int> indices;
int probar(int n, int k) {
	if (n == 0) {
		cout << "{";
		for (int x : indices) {
			cout << " " << x;
		}
		cout << " }\n";
	} else {
		elementos.push_back(n - 1);
		probar(n - 1, k - 1);
		elementos.pop_back();
		if (k > n) {
			probar(n - 1, k);
		}
	}
}
```
