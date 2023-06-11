# Programación dinámica

Si la fuerza bruta es para sacar un par de puntos en cualquier problema, la
programación dinámica sirve para sacar "bastantes" puntos en "bastantes" problemas.

La idea general es separar cada problema en subproblemas del mismo tipo que se
solapan. Cada uno de esos subproblemas también se resolverá separando en
sub-subproblemas, y así sucesivamente.

Entonces, si guardamos las soluciones a todos los subproblemas de tamaño 1 en una
tabla, podemos aprovecharlas para construir las soluciones a los de tamaño 2.
Esas para los de tamaño 3, y así sucesivamente hasta construir la solución al
problema total.

Generalmente se usa para problemas sobre:

- Tableros
- Arreglos
- Grafos Aciclicos

Un problema se puede resolver con programación dinámica cuando tiene
"subestructura óptima", que significa mas o menos que la solución se puede
construir combinando soluciones a subproblemas. (No es tan importante, pero se
puede googlear)

## Numeros de fibonacci

La secuencia de fibonacci comienza con los valores cero y uno. Cada elemento de
ahi en adelante es igual a la suma de los dos anteriores. En notacion matemática
tendríamos esto:

```
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)    (si n >= 2)
```

La forma más directa de traducir esto a código es usando una función recursiva:

```c++
int f(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (n >= 2) return f(n-1) + f(n-2);
}
```

El problema con esto es que es extremadamente lento (probá llamar esta función
con distintos valores de n menores a 100 y medir cuanto tiempo toma).

Se vuelve lento porque calcula los mismos valores de f muchas veces. Por
ejemplo, para calcular `f(100)`, ¡tiene que calcular `f(95)` 8 veces!

## Calculo con tabla

Como dice en la introducción, podemos usar una tabla para acelerar el calculo:

```c++
int f(int n) {
  vector<int> tabla(n+1);

  tabla[0] = 0;
  tabla[1] = 1;
  for (int i = 2; i <= n; ++i)
    tabla[i] = tabla[i-1] + tabla[i-1];

  return tabla[n];
}
```

De esta forma, cada valor de la tabla se calcula una sola vez, y tenemos un
programa mucho más eficiente.

En este fue fácil usar una tabla, pero muchas veces se complica.

## Memorización

En cambio podemos aplicar un truco muy sencillo: agregarle una tabla a la
función recursiva. Si el valor ya fue calculado, que devuelva el valor de la
tabla. Si no, que lo calcule y lo guarde en la tabla.

```c++
bool fue_calculado[1000];
int tabla[1000];
int f(int n) {
    if (fue_calculado[n]) return tabla[n];

    int resultado;

    if (n == 0) resultado = 0;
    if (n == 1) resultado = 1;
    if (n >= 2) resultado = f(n-1) + f(n-2);

    tabla[n] = resultado;
    fue_calculado[n] = true;

    return resultado;
}
```

Esto tiene el mismo efecto que el calculo directo con tabla (cada posición se
calcula una sola vez), pero la traducción dada la forma recursiva es mucho más
directa.

Como mantener dos tablas resulta engorroso, podemos trabajar con un valor
especial. Ponemos un "-1" en todas las posiciones de la tabla que no fueron
calculadas, y luego verificar si un valor fue calculado es tan simple como
verificar que sea distinto a `-1`.

```c++
int tabla[1000];
void iniciar_tabla() {
    memset(tabla, -1, sizeof(tabla)); // truquito para llenar de -1
}
int f(int n) {
    if (tabla[n] != -1) return tabla[n];
    if (n == 0) return tabla[n] = 0;
    if (n == 1) return tabla[n] = 1;
    if (n >= 2) return tabla[n] = f(n-1) + f(n-2);
}
```