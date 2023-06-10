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

Para saber si un numero es primo, cuento cuantos divisores tiene. Si tiene exactamente 2, es primo.

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

Estos son los primeros numeros naturales. Debajo de cada uno, tenemos `OO` si es primo y `--` si no lo es.

```
        X:  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
es primo?: -- OO OO -- OO -- OO -- -- -- OO -- OO -- -- -- OO -- OO --
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

## Idea 2: Solo cosiderar divisores hasta la raiz cuadrada de `X`

> ⚠️ Esta sección es muy pesada y necesita re-edición ⚠️

### Observación: No hace falta verificar numeros mayores a X/2

Algo interesante para observar es lo siguiente:

Si `p` fuera un divisor de `X` que es mayor a `X/2` y menor a `X` (osea `X/2 < p < X`), tendriamos que `X/p` es un divisor de `X`, menor a `2` y mayor a `1` (osea `1 < X/p < 2`).

Pero si `X/p` fuera menor a `2` y menor a `1`, no sería un numero entero, por lo que `p` no sería un divisor de `X`.

De ahí, concluimos que no puede existir un divisor mayor a `X/2` y menor a `X`, por lo que nuestra iteración puede frenar al llegar a `X/2`.


### Observación: No hace falta verificar numeros mayores a X/3

Con un razonamiento similar al anterior, podemos concluir que no hay divisores de `X` mayores a `X/3` y menores a `X/2`. Aparte, si se verifica primero que `2` no es divisor de `X`, `X/2` tampoco sera divisor de `X`.

Entonces, si como primer paso verificamos que `X` no tenga a `2` como divisor, nuestra iteracion puede frenar al llegar a `X/3`.

```c++
bool es_primo(int X) {
    if (X == 1) return false;
    if (X % 2 == 0) return false;  // ***

    for (int k = 3; k <= X/3; ++k) // ***
        if (X % k == 0) return false;

    return true;
}
```

### Observación: No hace falta verificar numeros mayores a X/4

Nuevamente, podemos hacer el mismo razonamiento: siempre que verifiquemos que `X` no es multiplo de `2` ni de `3`, podemos detener nuestra iteracion al llegar a `X/4`.

```c++
bool es_primo(int X) {
    if (X == 1) return false;
    if (X % 2 == 0) return false;
    if (X % 3 == 0) return false;  // ***

    for (int k = 4; k <= X/4; ++k) // ***
        if (X % k == 0) return false;

    return true;
}
```

### Bastante repetitivo... ¿Se podrá generalizar?

Este razonamiento se puede extender arbitrariamente, y llegamos a lo siguiente: Si `X` no es multiplo de ningun entero `2, 3, ..., p-1, p`, entonces la iteracion puede detenerse en el paso `X/p`.

Para implementar esta idea, le podemos agregar otro parametro a la funcion `es_primo`, y hacer dos bucles.

El primer bucle verifica la condicion "`X` no es multiplo de ningun entero `2, 3, ..., p`" y el segundo verifica el resto de los posibles divisores.

```c++
bool es_primo(int X, int p) {         // ***
    if (X == 1) return false;

    for (int k = 2; k <= p; ++p)      // ***
        if (X % k == 0) return false; // ***

    for (int k = p+1; k <= X/p; ++k)  // ***
        if (X % k == 0) return false;

    return true;
}
```

Resulta ser optimo elegir `p = X/p`. Resolviendo, encontramos que `p = X/p = raiz(X)`.

En este caso, tenemos `X/p < p+1`, por lo que el segundo bucle no hace ninguna iteracion, y podemos eliminarlo.

Aparte, calcular raices cuadradas puede ser lento asique, como optimización, podemos usar la condición `k*k<=X`.

Entonces, llegamos a esta implementación:

```c++
bool es_primo(int X) {
    if (X == 1) return false;

    for (int k = 2; k*k <= X; ++k)
        if (X % k == 0) return false;

    return true;
}
```

### Demostracion matemática

Lxs lectorxs amantes de la matemática pueden revisar este esbozo de demostración:

Hipotesis: `X` es un numero natural, y no tiene divisores menores o iguales a `raiz(X)`.

Tesis: `X` no tiene divisores mayores a `raiz(X)`.

Demostración:

Utilizamos reduccion al absurdo: (osea, supongamos lo contrario de lo que queremos demostrar, y veamos que eso lleva a una contradicción lógica).

Supongamos que `p` es un divisor de `X`, mayor a `raiz(X)`.

Entonces, `q := X/p` es un natural y es divisor de `X`.

Como `p` es mayor a `raiz(X)`, entonces `q` debe ser menor a `raiz(X)`.

`q` es divisor de `X` y es menor a `raiz(X)`. Por lo tanto `X` tiene un divisor menor a raiz(X)

Pero esto contradice la hipotesis, asique no puede existir un `p` divisor de `X`, mayor a `raiz(X)`.

Concluimos que `X` no tiene divisores mayores a `raiz(X)`.