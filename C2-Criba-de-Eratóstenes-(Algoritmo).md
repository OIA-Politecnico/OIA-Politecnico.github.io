La [criba de Eratóstenes (Wikipedia)](https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes) es un algoritmo eficiente para encontrar los divisores de todos los números hasta una cota.

El algoritmo se basa en que es más fácil encontrar los múltiplos de un número que sus divisores.

Si iteramos por los multiplos "x" de un numero "p", entonces sabemos que "p" es divisor de "x" y lo podemos insertar en la lista de divisores de "x".

Luego de completar este proceso para todos los valores posibles de "p", cada numero tendrá todos sus divisores.

```c++
// criba[x] va a contener todos los divisores de x
// por ejemplo criba[12] = {1,2,3,4,6,12}
vector<int> criba[MAXN];

void init_criba() {

  for (int p = 1; p < MAXN; ++p) {

    // itero por los multiplos de p
    for (int x = 0; x < MAXN; x += p) {

      // x es multiplo de p
      // por lo tanto p es divisor de x
      // asique lo agrego a la lista de divisores
      criba[x].push_back(p);
    }
  }
}
```

Analicemos la complejidad.

El for de adentro itera desde `0` hasta `n`, haciendo saltos de longitud `p`. Entonces, hace a lo sumo `n/p` iteraciones. Tomando en cuenta que `p` toma los valores `1,2,3,...,n`, la cantidad total de iteraciones es a lo sumo `n/1 + n/2 + n/3 + ... + n/n`.

Haciendo factor común `n` tenemos `n*(1/1 + 1/2 + 1/3 + ... + 1/n)`. Resulta que `1/1 + 1/2 + 1/3 + ... + 1/n` es aproximadamente `ln(n)` (ver [Número armónico (Wikipedia)](https://es.wikipedia.org/wiki/N%C3%BAmero_arm%C3%B3nico) para más información).

Asique la cantidad total de iteraciones es aproximadamente `n*ln(n)`. Osea, la criba tiene complejidad `O(n*log(n))`

# Para buscar primos

Una aplicación común de la criba es buscar números primos. (Esto es lo que explica el articulo de Wikipedia, asique si no está clara esta sección, puede servir revisarlo)

**Observacion:** un número es primo si tiene exactamente 2 divisores.

Entonces, dada la criba que vimos arriba, podemos definir la función `es_primo` fácilmente:

```c++
bool es_primo(int x) {
  return sz(criba[x]) == 2;
}
```

Esto es bastante bueno. Podemos responder si un numero menor a `MAXN` es primo o no en `O(1)`, a cambio de un precomputo (construir la criba) de tiempo `O(N*log(N))`.

Pero bueno, se puede tunear la criba para tener un precomputo más barato.

**Definicion:** Para todo numero "x", sus **divisores triviales** son 1 y "x".

**Observacion:** Para cualquier numero "x" mayor a 1, este es compuesto si tiene un divisor no trivial.

Con esa idea podemos tunear el algoritmo de la criba para solo guardar un arreglo de booleanos.

En este caso, el for de adentro va a marcar todos los multiplos "no triviales" de "p"

```c++
// criba[x] es true si x es mayor a 1 y tiene un divisor no trivial
bool criba[MAXN];

void init_criba() {

  // arrancamos en 2 para no marcar los multiplos de 1 (divisor trivial)
  for (int p = 2; p < MAXN; ++p) {

    // marcamos los multiplos no triviales de p como compuestos
    // arrancamos en 2*p para no marcar a p mismo (divisor trivial)
    for (int x = 2*p; x < MAXN; x += p) {
      criba[x] = true;
    }
  }
}

bool es_primo(int x) {
  return x > 1 && !criba[x];
}
```

Este algoritmo tiene la misma complejidad que el anterior pero es bastante más rápido en la práctica. Con una observación más podemos obtener una versión con mejor complejidad (y aún más rápida en la práctica).

**Observacion:** Si x es multiplo de un numero compuesto, entonces también es multiplo de un número primo. (Porque todo compuesto es multiplo de un primo y la relación es transitiva).

De ahi concluimos que nunca hace falta marcar los multiplos de un numero compuesto, pues ya van a estar marcados por ser multiplos de un primo. Esto nos permite una optimización:

```c++
void init_criba() {

  for (int p = 2; p < MAXN; ++p) {

    // solo marco los multiplos de p si p es primo
    if (!criba[p]) {

      for (int x = 2*p; x < MAXN; x += p) {
        criba[x] = true;
      }
    }
  }
}
```

Agregar ese if baja la complejidad a `O(n*log(log(n)))`, pero no es fácil de demostrar.

# Para calcular el menor divisor no trivial

Otro uso común de la criba es para buscar el menor divisor no trivial.

Mientras que podemos simplemente acceder al segundo divisor que nos genera la criba básica (el primero es siempre 1), también es posible aplicar una optimización similar a la sección anterior.

**Observación:** El menor divisor no trivial de un numero siempre es primo.

**Observación:** La criba descubre los divisores en orden de menor a mayor.

Con estas dos ideas tenemos que

 - igual que antes, no hace falta mirar los multiplos de numeros compuestos (esto nos baja la complejidad a` O(n*log(log(n)))`).
 - la primera vez que se marca un numero, es a causa de su menor divisor no trivial.

Y surge esta implementación

```c++
// si tiene, criba[x] es el menor divisor no trivial de x
// si no tiene, (porque x es primo o ≤1), entonces criba[x] es 0
int criba[MAXN];

void init_criba() {
  for (int p = 2; p < MAXN; ++p) {

    // solo necesito marcar los multiplos de primos
    if (criba[p] == 0) {
      for (int x = 2*p; x < MAXN; x += p) {

        // Si x ya está marcado entonces ya tiene su menor
        // divisor no trivial, así que no lo vuelvo a marcar.
        if (criba[x] == 0) {
          criba[x] = p;
        }
      }
    }
  }
}

int menor_divisor_no_trivial(int x) {

  if (criba[x] == 0) {
    // en este caso, x no tiene divisores no triviales
    // delvolveremos lo que necesitemos en el problema particular.
  }

  return criba[x];
}
```

# Para calcular el mayor divisor no trivial

**Observacion:** Si p es el mayor divisor no trivial de x y q es el menor, entonces p*q=x

Osea, podemos usar las funciones de la sección anterior.

```c++
int mayor_divisor_no_trivial(int x) {
  return x / menor_divisor_no_trivial(x);
}
```