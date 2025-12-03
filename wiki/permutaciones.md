# Permutaciones

Una permutación en N elementos es una función biyectiva del conjunto finito {0, 1, 2, ..., N-1} a sí mismo.

## Representación

Una permutación en N elementos se puede representar como un arreglo de N elementos, donde el i-ésimo elemento es el elemento que se mapea a i.

O sea, dada `f` una permutación en N elementos, la representamos mediante un arreglo `F` tal que `F[i] = f(i)` para todo `i` en {0, 1, 2, ..., N-1}.

Por ejemplo, si tenemos f permutacion en 3 elementos, tal que f(0) = 1, f(1) = 2, f(2) = 0, podemos representarla como el arreglo [1, 2, 0].

```c++
using perm = vector<int>;
perm f = {1, 2, 0};
```

## Temas interesantes para programación competitiva

- composición
- neutra
- inversas
- grupos de permutaciones
- representación como grafo
- ciclos
- transposiciones
- inversiones
- paridad
- generación
- ranking/unranking

## Composición

Dadas dos permutaciones `f` y `g`, la composición `f∘g` es la permutación que se obtiene aplicando `f` después de `g`.

O sea, `(f∘g)(i) = f(g(i))` para todo `i` en {0, 1, 2, ..., N-1}.

Implementación:

```c++
perm compose(perm const& f, perm const& g) {
  perm h(sz(f));
  forn(i, sz(f)) h[i] = f[g[i]];
  return h;
}
```

## Permutación neutra

La permutación neutra es la permutación que deja todos los elementos en su posición original.

O sea, `(Id)(i) = i` para todo `i` en {0, 1, 2, ..., N-1}.

La llamamos así porque es el elemento neutro de la composición.

Implementación:

```c++
perm id(int n) {
  perm id(n);
  forn(i, n) id[i] = i;
  return id;
}
```

## Inversa

Dada una permutación `f`, la inversa `f^-1` es la permutación tal que `f∘f^-1 = Id` y `f^-1∘f = Id`.

O sea, `(f^-1)(i) = j` si y solo si `f(j) = i` para todo `i` en {0, 1, 2, ..., N-1}.

Implementación:

```c++
perm inverse(perm const& f) {
  perm inv(sz(f));
  forn(i, sz(f)) inv[f[i]] = i;
  return inv;
}
```

## Representación como grafo

Una permutación se puede representar como un grafo dirigido, donde cada nodo es
un elemento de {0, 1, 2, ..., N-1} y cada arista va desde el nodo `i` al nodo
`f(i)`.

Por ejemplo, la permutacion `f = {1, 2, 0}` se puede representar como el grafo:

```
0 -> 1
1 -> 2
2 -> 0
```

Este grafo es un ciclo de longitud 3.

En general, cualquier grafo permutacion esta compuesto por ciclos.

Por que?

- Porque cada nodo tiene grado de salida 1 (por definicion que dimos recién)
- Por que cada nodo tiene grado de entrada 1 (porque f es inyectiva, o sea no hay dos nodos distintos u, v, con f(u) = f(v))

Aplicación curiosa: el problema de los prisioneros.

Hay 100 prisioneros numerados del 1 al 100, y 100 cajas con números del 1 al 100, una al lado de la otra.

Los numeros se colocan en las cajas de manera aleatoria.

Cada prisionero puede abrir 50 cajas a su elección.

Si el prisionero abre la caja con su número, es libre.

Si el prisionero no encuentra su número en las 50 cajas, es condenado.

Los prisioneros pueden comunicarse entre sí antes de empezar el acto, pero no pueden comunicarse una vez que empieza el acto.

Cual es la estrategia que maximiza la probabilidad de que todos los prisioneros sean libres?

> Primero, una no-solucion:
>
> Cada prisionero abre 50 cajas aleatorias.
>
> La probabilidad de que encuentre su número es 1/2.
>
> La probabilidad de que todos los prisioneros sean libres es (1/2)^100 = 1/2^100.
>
> Esto es muy pequeño.

> Segunda no-solucion:
>
> Cada prisionero abre las 50 cajas en orden decreciente de números.
>
> Exactamente la mitad de los prisioneros van a encontrar su número.
>
> La probabilidad de que todos salgan libres es 0.

> Solucion: Cada prisionero abre la caja que está en la posición con su número.
>
> Si en encuentra un número x que no es su número, entonces abre la caja que está en la posición x.
>
> Repite esto hasta que encuentre su número o hasta que haya abierto 50 cajas.
>
> La probabilidad de que todos salgan libres es la probabilidad de que todo ciclo de una permutacion tenga longitud menor o igual a 50.
>
> Para 100 elementos, esto resulta ser aproximadamente 31.2%.

# Representación de otras cosas como permutaciones

Imaginate el cubo de Rubik.

Nos interesa hacer un programa que resuelva el cubo de Rubik.

Cada cara del cubo de Rubik tiene 9 cuadrados. Hay 6 caras, por lo que hay `6*9 = 54` cuadrados.

En realidad, los cuadrados centrales no se mueven, por lo que podemos pensar en `6*8 = 48` cuadrados.

- Representamos un cubo de Rubik como un array de `48` elementos, donde el i-esimo elemento es el color del i-esimo cuadrado.

  El cubo resuelto tiene los primeros `8` elementos iguales a 1, los siguientes `8` iguales a 2, etc.

- Representamos cada uno de los 12 movimientos basicos del cubo de Rubik como una permutacion.

  Por ejemplo rotar la cara superior 90 grados en sentido horario, como la permutación que intercambia los 8 cuadrados de la cara superior de manera circular, y los 12 cuadrados que la rodean, tambien de manera circular.

Para resolver el cubo, hacemos un BFS sobre el grafo implicito que se construye aplicando las 12 operaciones basicas del cubo de Rubik a un estado inicial. Esto desafortunadamente es muy lento, ya que el grafo tiene `4,3 * 10^19` estados.

Una busqueda BFS bidireccional/meet-in-the-middle visita a unos `3,8 * 10^7` estados, que es aceptable.

## Transposiciones, inversiones y paridad

Una transposicion es una permutacion que intercambia dos elementos y deja los otros elementos en su lugar.

Por ejemplo, la permutacion `{1, 0, 2}` es una transposicion porque intercambia el 1 y el 0, y deja el 2 en su lugar.

Una inversion es una pareja de indices `(i, j)` tal que `i < j` y `A[i] > A[j]`.

- **Definicion:** La paridad de una permutacion es igual a la paridad de la cantidad de inversiones.

- **Proposicion:** Una transposicion de elementos consecutivos tiene exactamente una inversion.

- **Proposicion:** Cualquier transposicion es impar.

- **Proposicion:** La paridad de una composicion de permutaciones se comporta como la paridad de una suma de numeros.

  - `  par ∘   par = par`
  - `  par ∘ impar = impar`
  - `impar ∘   par = impar`
  - `impar ∘ impar = par`

- **Proposicion:** Una permutacion es par si y solo si se puede escribir como producto de un numero par de transposiciones.

Demostracion de todas estas cosas: 

- cualquier permutacion se puede escribir como composicion de transposiciones.

- cualquier transposicion se puede escribir como composicion de una cantidad impar de transposiciones de elementos consecutivos.

- la paridad de una composicion se comporta como la suma cuando uno de las dos permutaciones es una transposicion de elementos consecutivos pq aumenta o decrece por 1 la cantidad de inversiones. (ver los casitos)


## Grupos de permutaciones

Un par de propiedades:

- La composición de permutaciones es asociativa.
- La permutación neutra es el elemento neutro de la composición.
- Cada permutación tiene una inversa.

Por lo tanto, el conjunto de todas las permutaciones en N elementos con la composición forma un grupo.

Esto significa que podemos aprovechar resultados de la teoría de grupos para estudiar permutaciones.


### Potencias de permutaciones

Para cualquier permutacion `f` y cualquier entero `k`, `f^k` es la permutacion que se obtiene aplicando `f` `k` veces.

O sea, `(f^k)(i) = f(f(...f(i)...))` para todo `i` en {0, 1, 2, ..., N-1}.

Implementación:

```c++
// O(N * k)
perm power(perm const& f, int k) {
  perm res = id(sz(f));
  forn(i, k) res = compose(res, f);
  return res;
}
```

Se puede implementar usando exponenciacion binaria.

```c++
// O(N * log k)
perm power(perm const& f, int k) {
  if (k == 0) return id(sz(f));
  if (k == 1) return f;
  if (k%2 == 0) return power(compose(f, f), k/2);
  return compose(f, power(f, k-1));
}
```

### Orden de una permutacion

De la teoria de grupos sabemos que toda permutacion tiene un orden, que es el menor entero positivo `k` tal que `f^k = Id`.

O sea, para cualquier permutacion `f`, existe un entero `k` tal que `f^k = Id` y `f^(k-1) = f^-1`.

Esta es una manera poco practica de calcular la inversa de una permutacion, pero es interesante saber que existe. Aparte nos lo pueden preguntar en algun problema.

Analizando los ciclos de una permutacion, podemos ver que el orden de una permutacion es el MCM de las longitudes de los ciclos.

O sea, el orden de un ciclo de longitud `L` es `L`, y aparte cualquier multiplo de `L` tambien es una potencia que da la identidad.

Si una permutacion tiene ciclos de longitudes `L1, L2, ..., Lk`, entonces el orden de la permutacion es un numero que es multiplo de todos los `Li` y es el menor numero que cumple esto. O sea, el MCM de los `Li`.


### Renombrar elementos

Dada una permutación `f`, y un renombramiento `g`, podemos construir una
permutación renombrada `h` tal que `h(g(i)) = g(f(i))` para todo `i` en
`{0, 1, 2, ..., N-1}`.

un renombramiento es otra permutación, no es una función arbitraria.

La idea es que el elemento que antes se llamaba `i`, ahora se llama `g(i)`.

O sea, si en el "mundo original" teniamos `f(i) = j`, ahora en el "mundo
renombrado" deberiamos tener `h(g(i)) = g(j)`.

Algebraicamente, trabajamos

      h(g(i)) = g(f(i))
    { sea j = g(i), entonces i = g^-1(j) }
      h(j) = g(f(g^-1(j)))
    { generalizacion }
      h = g ∘ f ∘ g^-1

Implementación:

```c++
perm rename(perm const& f, perm const& g) {
    return compose(g, compose(f, inverse(g)));
}

// Si expandimos la definicion de composicion, es mas eficiente
perm rename(perm const& f, perm const& g) {
    perm h(sz(f));
    forn(i, sz(f)) h[g[i]] = g[f[i]];
    return h;
}
```

> Esto es un ejemplo del concepto de "conjugacion" en teoría de grupos.
>
> La conjugacion es una relacion de equivalencia.
>
> Dos elementos `a` y `b` (de un grupo) son conjugados si existe un elemento `g` tal que `g∘a∘g^-1 = b`.
>
> O sea, `a` y `b` son "equivalentes" o "conjugados" si se pueden obtener uno del otro aplicando una conjugacion.
>
> Dos elementos conjugados suelen compartir propiedades interesantes.
>
> Por ejemplo, si `a` y `b` son conjugados, entonces `a` y `b` tienen el mismo
> orden.
>
> En el caso de permutaciones, dos elementos conjugados tienen la misma cantidad de ciclos de cada longitud.
>
> Aparte, dos permutaciones conjugadas tienen la misma paridad. (caso particular de lo anterior)

## `next_permutation`

Esta es una funcion que se encuentra en la libreria `algorithm` de C++.

Dada una permutacion `p`, esta funcion la modifica para que pase a la siguiente permutacion en orden lexicografico.

Por ejemplo, si `p = {1, 2, 3}`, entonces `next_permutation(p.begin(), p.end())` modifica `p` para que sea `{1, 3, 2}`.

Si `p` es la ultima permutacion en orden lexicografico, entonces `next_permutation` la modifica para que sea la primera permutacion en orden lexicografico.

Uso para iterar por todas las permutaciones:

```c++
int n; cin >> n;
vector<int> p(n);
forn(i, n) cin >> p[i];
sort(begin(p), end(p));
do {
    for (int x : p) cout << x << " ";
    cout << "\n";
} while (next_permutation(begin(p), end(p)));
```

Esto imprime todas las permutaciones del input en orden lexicografico.

# Generacion de permutaciones (ranking/unranking)

Hay problemas en los que nos piden la k-esima permutacion en orden lexicografico
, o la permutacion que ocupa la k-esima posicion en orden lexicografico. (muchas
veces con restricciones adicionales)

Esto se llama "ranking/unranking".

## Ranking

Dada una permutacion `p`, calcular su posicion en orden lexicografico.

## Unranking

Dada una posicion `k`, calcular la k-esima permutacion en orden lexicografico.

Implementación:

```c++
int rank(perm const& p) {
    // TODO:
    // Implementar
    // la idea es contar la cantidad de permutaciones que son menores que p
    // en orden lexicografico.
    // Para esto, contamos la cantidad que comienzan con algo <p[0]
    // luego la cantidad que comienzan con p[0] y el segundo elemento <p[1]
    // etc.
    // tipicamente nos van a pedir la respuesta en modulo
}
```

Implementación:

```c++
perm unrank(int k) {
    // TODO:
    // Implementar
}
```