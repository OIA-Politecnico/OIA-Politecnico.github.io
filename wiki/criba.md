# Criba de Eratóstenes

La [criba de Eratóstenes (Wikipedia)](https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes)
es un algoritmo eficiente para encontrar los divisores de todos los números
hasta una cota. La idea clave es que es mucho más fácil encontrar los múltiplos
de un número que sus divisores.

**Observación:** un número "p" es divisor de un número "x" si y solo si "x" es
múltiplo de "p".

Por cada valor posible de "p", el algoritmo recorre todos sus múltiplos "x" y
guarda "p" en la lista de divisores de "x". Luego de completar este proceso,
cada número tendrá todos sus divisores.

```c++
vector<int> divisores[MAXN];

void init_criba() {

  for (int p = 1; p < MAXN; ++p) {

    // itero por los múltiplos de p menores a MAXN
    for (int x = 0; x < MAXN; x += p) {

      // x es múltiplo de p => p es divisor de x
      divisores[x].push_back(p);
    }
  }
}
```

Analicemos la complejidad.

El for de adentro itera desde `0` hasta `n`, haciendo saltos de longitud `p`.
Entonces, hace a lo sumo `n/p` iteraciones. Tomando en cuenta que `p` toma los
valores `1,2,3,...,n`, la cantidad total de iteraciones es a lo sumo
`n/1 + n/2 + n/3 + ... + n/n`.

Haciendo factor común `n` tenemos `n*(1/1 + 1/2 + 1/3 + ... + 1/n)`. Resulta que
`1/1 + 1/2 + 1/3 + ... + 1/n` es aproximadamente `ln(n)` (ver [Número armónico
(Wikipedia)](https://es.wikipedia.org/wiki/N%C3%BAmero_arm%C3%B3nico) para más
información).

Asique la cantidad total de iteraciones es aproximadamente `n*ln(n)`. Osea, la
criba tiene complejidad `O(n*log(n))`.

# Para buscar primos

Una aplicación común de la criba es buscar números primos. (Esto es lo que
explica el articulo de Wikipedia, asique si no está clara esta sección, puede
servir revisarlo)

**Definición:** un número es primo si tiene exactamente 2 divisores.

Entonces, dada la criba que vimos arriba, podemos definir la función `es_primo`
fácilmente:

```c++
bool es_primo(int x) {
  return divisores[x].size() == 2;
}
```

Esto es bastante bueno. Podemos responder si un número menor a `MAXN` es primo o
no en `O(1)`, a cambio de un precomputo (construir la criba) de tiempo
`O(N*log(N))`.

Pero bueno, se puede tunear la criba para tener un precomputo más barato. Como
primer paso, modificamos el algoritmo de la criba para que solo guarde un
arreglo de booleanos.

Vamos a mantener un array que tiene true en todos los números que ya sabemos que
no son primos. Por cada número mayor a 1, marcamos que sus múltiplos son
compuestos. Al llegar a un número que no fue marcado, es porque es primo.

**Observacion:** Un número mayor a 1 es compuesto si tiene un divisor primo
menor a si mismo.

Esta observación nos dice que no hace falta marcar los múltiplos de números
compuestos, nos alcanza con marcar los múltiplos de números primos.

Con estas dos ideas, armamos el siguiente código:

```c++
// criba[x] es true si x es mayor a 1 y tiene un divisor no trivial
bool criba[MAXN];

void init_criba() {

  criba[0] = true; // 0 no es primo
  criba[1] = true; // 1 no es primo

  for (int p = 2; p < MAXN; ++p) {
    if (criba[p]) continue; // p no es primo, lo salteo

    // p es primo, pero sus múltiplos mayores no
    for (int x = 2*p; x < MAXN; x += p) {
      criba[x] = true;
    }
  }
}

bool es_primo(int x) {
  return !criba[x];
}
```

Agregar ese if baja la complejidad a `O(n*log(log(n)))`, pero no es fácil de
demostrar.

# Para factorizar numeros en primos

Otro uso común de la criba es para encontrar los divisores primos de un numero.

**Observación:** La criba descubre los divisores en orden de menor a mayor.

**Observación:** Para todo numero, su menor divisor distinto a 1 es primo.

Esto nos da un algoritmo obvio para encontrar el menor divisor primo de un
numero: Tomamos el segundo elemento de la lista de divisores ¡Resulta que esto
es suficiente para encontrar todos los factores primos!

Si expresamos un número `n` según su factorización prima, tenemos una cosa así:

```
n = p1^e1 * p2^e2 * p3^e3 * ... * pk^ek

donde p1, p2, p3, ..., pk son primos y estan ordenados de menor a mayor.
```

Como la criba nos permite encontrar p1 rápidamente, podemos calcular `n/p1`:

```
n/p1 = pi^(e1-1) * p2^e2 * p3^e3 * ... * pk^ek
```

Si justo e1 era igual a 1, entonces tenemos que

```
n/p1 = p2^e2 * p3^e3 * ... * pk^ek
```

Y por lo tanto el segundo elemento de la lista de divisores de `n/p1` va a ser p2.

En otras palabras, si conocemos un factor primo de un numero, podemos borrarlo y
buscar otro. Al repetir este proceso terminamos encontrandolos a todos,
repetidos tantas veces como indica su exponente en la factorización (Si bien
esto puede parecer una desventaja, en realidad suele ser lo que queremos).

```c++
vector<int> factorizar(int n) {
	vector<int> factores;
	while (n > 1) {
		int p = divisores[n][1];
		factores.push_back(p);
		n /= p;
	}
	return factores;
}
```

### Optimización

Esto está bastante bien pero, como volvimos a usar la lista de divisores,
tenemos mayor uso de memoria y tiempo. Pero no hay que preocuparse porque se
puede optimizar igual de bien que antes.

**Observación:** A nuestro algoritmo solo le interesa saber el minimo divisor
primo de cada numero, no todos los divisores.

De entrada esto nos dice que, igual que antes, no hace falta iterar por los
múltiplos de los numeros compuestos, asique podemos conseguir la cota
`O(n*log(log(n)))` tanto tiempo como en memoria.

Pero aún más, como solo nos interesa el menor de ellos, solo necesitamos guardar
un elemento por cada numero, por lo que podemos tener `O(n)` memoria. El truco es
que guardamos un divisor por cada numero y, si ya fue asignado por un primo
menor, no lo tocamos.

```c++
// si x≤1, criba[x] = 0
// si no, criba[x] es el menor factor primo de x
int criba[MAXN];

void init_criba() {
  criba[0] = 0;
  criba[1] = 0;
  for (int p = 2; p < MAXN; ++p) {
    if (criba[p] != 0) continue;
    for (int x = p; x < MAXN; x += p) {

      // Si x ya está marcado entonces ya tiene su menor
      // factor primo, así que no lo vuelvo a marcar.
      if (criba[x] == 0) criba[x] = p;
    }
  }
}

vector<int> factorizar(int n) {
	vector<int> factores;
	for (; n > 1; n /= criba[n])
		factores.push_back(criba[n]);
	return factores;
}
```

# Para calcular el mayor divisor propio

Otra idea que aparece en algunos problemas es la del mayor divisor propio (un
divisor que no es el numero mismo). Resulta que esto es muy fácil de calcular.

La idea es que cualquier divisor de x se puede obtener tomando x y dividiendolo
por algun otro divisor. En particular, si queremos el máximo divisor propio,
vamos a querer dividir por el menor divisor posible (distinto a 1). Pero ya
vimos en la anterior seccion que ese divisor es primo y se puede obtener
fácilmente a partir de la criba.

Entonces, si definimos `criba[x]` igual que en la sección anterior, tenemos que:

```c++
int mayor_divisor_propio(int n) {
	return n / criba[n];
}
```
