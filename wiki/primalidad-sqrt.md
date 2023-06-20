Para saber si un numero `X` es primo, contamos cuantos divisores tiene. Si tiene exactamente 2, es primo. Para hacer esto, podemos iterar por todos los enteros desde `1` hasta `X`, y guardar en un contador cuantos de ellos dividen a `X`.

Se puede mejorar bastante con dos ideas:

 - cortando apenas se encuentra un divisor mayor a `1` y menor a `X`.
 - cortando la iteración al llegar a `raiz(X)`.

Entonces, tendríamos esta implementación:

```c++
bool es_primo(int X) {
    if (X == 1) return false;

    for (int k = 2; k*k <= X; ++k)
        if (X % k == 0) return false;

    return true;
}
```

# Explicacion larga

Para saber si un numero es primo, cuento cuántos divisores tiene. Si tiene exactamente 2, es primo.

Para hacer esto, podemos iterar por todos los enteros desde `1` hasta `X`, y guardar en un contador cuantos de ellos son divisores de `X`.

```c++
bool es_primo(int X) {
    int divisores = 0;
    for (int k = 1; k <= X; ++k)
        if (X % k == 0) divisores++;
    return divisores == 2;
}
```

Pero bueno, esta no es una forma muy eficiente de lograrlo. Si conocés de complejidad asintótica, podríamos decir que este algoritmo tiene complejidad `O(X)`. Veamos dos ideas que agilizan este proceso un montón.

## Idea 1: Cortar al encontrar un divisor entre dos y `X-1`

Estos son los primeros numeros naturales. Debajo de cada uno, dice "NO" si ese número no es primo.

```
        X:  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
es primo?: NO       NO    NO    NO NO NO    NO    NO NO NO    NO    NO
```

Mirando la lista se nota que, exceptuando al dos, los numeros pares no son primos.

No solo eso sino que, exceptuando al tres mismo, los multiplos de tres tampoco son primos.

### ¿Qué está pasando acá?

Capaz habrás oído que todo numero es divisible por uno y por si mismo. Esto significa que todos los números tienen *al menos* dos divisores: uno y si mismos (excepto el uno, que es su propio y único divisor).

Aparte, si un número es par (y mayor a dos), también va a tener al dos como divisor, por lo que tendrá *al menos* tres divisores, lo cual lo descalifica inmediatamente de ser número primo (acordate que los primos son los números que tienen **exactamente** dos divisores).

Lo mismo pasa con los multiplos de tres: tienen al uno, al tres, y a si mismos como divisores, lo cual los descalifica de ser primos.

### ¿Esto será algo propio del dos y el tres?

Seguro que te estás preguntando si pasa lo mismo con numeros más grandes: ¿Será cierto que si un numero es multiplo de otro (distinto de uno), entonces el primero no es primo?

Y tal cual, incluso podemos aplicar la misma lógica que antes: Si tenemos un numero `X`, y otro numero `k`, donde `1 < k < X`, y aparte `X` es multiplo de `k`, entonces `X` tiene *al menos* tres divisores: uno, `k`, y si mismo, `X`. Por lo tanto, `X` no es primo.

Esto nos lleva a una optimización muy importante: apenas encontramos un divisor mayor a uno y menor a `X` podemos terminar la ejecución, respondiendo que `X` no es primo. Por el otro lado, si no existe un ejemplo de un `k` con esas características, entonces `X` es primo.

```c++
bool es_primo(int X) {
    if (X == 1) return false;
    for (int k = 2; k < X; ++k)
        if (X % k == 0) return false;
    return true;
}
```

Esto concluye la primera optimización. En la práctica, la función es unas 10 veces más rápida que antes.

Si conocés el tema de complejidad asintótica, podemos decir que la complejidad en el peor caso es `O(X)`, pero la complejidad promedio pasa a ser `O(X/ln(X))`.

El peor caso ocurre cuando `X` es primo: en estos casos el bucle recorre desde dos hasta `X-1` sin encontrar ningún divisor, realizando `X-2` iteraciones en total.

## Idea 2: Solo considerar divisores hasta la raiz cuadrada de `X`

Supongamos que hay dos números P y Q, que cumplen que `P * Q = X`. Resulta que
es matemáticamente imposible que ambos sean mayores a la raíz cuadrada de X.

### Por que?

Sabemos que `raiz(X) * raiz(X) = X`. Si tanto `P` como `Q` fueran mayores a
`raiz(X)`, entonces su producto sería aún mayor. En ese caso, podríamos concluir
que `P * Q > X`. Pero esto es imposible porque, como dijimos antes, `P * Q = X`.

### De qué sirve esto?

Sirve muchisimo! Significa que si un numero tiene divisores, entonces alguno de
ellos es menor o igual a `raiz(X)`. Osea, si estoy buscando divisores y no
encuentro ninguno menor o igual a `raiz(X)`, ¡es porque el numero no tiene divisores!

Esta idea permite cortar la búsqueda mucho antes: en vez de llegar hasta
`X-1`, solo hace falta buscar hasta `raiz(X)`.

```c++
bool es_primo(int X) {
    if (X == 1) return false;
    for (int k = 2; k <= sqrt(X); ++k)
        if (X % k == 0) return false;
    return true;
}
```

Para que ande un poco más rápido, es recomendable usar la expresión `k*k <= X`
en vez de `k<=sqrt(X)`.


```c++
bool es_primo(int X) {
    if (X == 1) return false;
    for (int k = 2; k*k <= X; ++k)
        if (X % k == 0) return false;
    return true;
}
```
