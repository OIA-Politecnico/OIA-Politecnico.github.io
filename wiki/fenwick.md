
#Fenwick Tree

## Introduccion

Motivacion (problema, complejidad), queries en rango.

## Tutorial

El codigo, que hace cada funcion, algunos ejemplos.

## Guia

Paso a paso de un problema

## Referencia

```c++
int const MAXN = 10000000;
int ft[MAXN+1];

// realiza la actualización A[i] += x;
// se debe cumplir que i >= 1
void update(int i, int x) {
  for (; i < MAXN+1; i += i&-i) ft[i] += x;
}

// devuelve la suma de A[1..i]
int query(int i) {
  int x = 0;
  for (; i > 0; i -= i&-i) x += ft[i];
  return x;
}
```

## Explicacion

Vimos que el [*segment tree*](segment-tree) es una estructura que mantiene la
suma de algunos rangos predeterminados para poder responder consultas de suma en
rango y aplicar actualizaciones en tiempo logarítmico.

```
[                      16                      ]
[           8          ][           8          ]
[     4    ][     4    ][     4    ][     4    ]
[  2 ][  2 ][  2 ][  2 ][  2 ][  2 ][  2 ][  2 ]
[1][1][1][1][1][1][1][1][1][1][1][1][1][1][1][1]
```

<br>

El *Fenwick tree* es una estructura similar. Aunque guarda solo la mitad de los
rangos del *segment tree*, puede responder consultas de suma **en prefijo** y
aplicar actualizaciones en tiempo logarítmico.

```
[                      16                      ]
[           8          ]                        
[     4    ]            [     4    ]            
[  2 ]      [  2 ]      [  2 ]      [  2 ]      
[1]   [1]   [1]   [1]   [1]   [1]   [1]   [1]   
```

<br>

Usar especificamente estos rangos tiene algunas ventajas extra:

- cada rango tiene su extremo derecho en una posición distinta del arreglo y,
- dado el extremo derecho, es posible calcular el extremo izquierdo
  eficientemente usando truquitos de bits.
- dado un indice es posible encontrar todos los rangos que la cubren
  eficientemente usando truquitos de bits.

> Normalmente es recomendable (por ejemplo en la implementación de segment tree)
> trabajar con rangos `[l,r)` (cerrado-abierto), y con indices basados en cero.
>
> Sin embargo, los detalles internos del fenwick tree hacen que sea más cómodo
> trabajar con rangos `(l, r]` (abierto-cerrado), y con indices basados en uno.
>
> De acá en adelante usamos esa convención.

La primera observacion nos permite una representación muy sencilla de la
estructura: Almacenamos el valor del rango `(l, r]` en la posicion `r` de un
arreglo. En otras palabras, declarar un Fenwick tree se hace así:

```c++
// MAXN es el máximo N que pide el problema.
int ft[MAXN+1];
```

La segunda observación nos siguiere un algoritmo muy sencillo para responder
consultas:

1. Queremos calcular la suma del rango (0, r]
1. Ponemos un indice i en la posicion r
1. Acumulamos el rango que termina en i y movemos i al inicio de ese rango
1. Ahora solo falta calcular (0, i]. si `i == 0` ya terminamos
1. Si no, volvemos al paso 3

En particular, dado el extremo derecho `r` (el índice del último elemento que
está incluido dn el rango), la longitud del rango es `r&-r`. Por lo tanto el
extremo izquierdo es `r-(r&-r)`.

> La expresión `r&-r` devuelve el *least significant bit* de `r`.
> Matemáticamente, ese valor es la máxima potencia de dos que es divisor de r.
>
> Este dato puede ayudar a entender el funcionamiento interno e inventar
> variaciones de la estructura pero, para nuestros fines, alcanza con pensar que
> justo justo, de casualidad, nos da la longitud del rango que termina en `r`.

Traduciendo el algoritmo a código tendriamos algo así:

```c++
int query(int r) {
  int acum = 0;
  int i = r;
  while (i != 0) {
    acum += ft[i];
    i -= i&-i;
  }
  return acum;
}
```

<br>

O, en su forma compacta más típica:

```c++
int query(int i) {
  int x = 0;
  for (; i > 0; i -= i&-i) x += ft[i];
  return x;
}
```

<br>

La tercera observación nos sugiere un algoritmo similar para realizar
actualizaciones: Si queremos sumar `x` en la posicion `i`, basta que sumar `x`
en todos los rangos que cubren la posicion `i`.

En particular, resulta que los rangos estan anidados de una forma especial: el
rango más chico que contiene al rango que termina en la posicion `r` es el rango
que termina en la posicion `r+(r&-r)`.

> De nuevo, no hace falta entender el por qué de esto ya que el *Fenwick tree*
> se usa como caja negra la mayoria del tiempo.

Pasando directo a la implementación, el código queda así:

```c++
void update(int i, int x) {
  for (; i < MAXN+1; i += i&-i) ft[i] += x;
}
```

### Suma en rango

Tenemos una estrctura que nos responde consultas de suma en prefijo rápidamente.
A qué suena? A [tabla aditiva](tabla-aditiva)!

Igual que la tabla aditiva, podemos usar fenwick tree para responder sumas en
rango.

```c++
// devuelve la suma de A[l..r]
int query(int l, int r) {
  return query(r) - query(l-1);
}
```

### Interpretacion "range add, point get"

> Notas del editor de la wiki -- Quizá se podría sacar esto a su propio artículo
> de difference-array y prefix-sum.

Hasta ahora, vimos que Fenwick tree es una estructura que tiene dos operaciones:

- Sumar un valor en un punto
- Obtener la suma de un prefijo o de un rango

Pero hay otra forma de interpretar el fenwick tree que nos deja pensar que las
operaciones son:

- Sumar un valor a todos los elementos de un sufijo o de un rango
- Obtener el valor en un punto

Lo sorprendente es que el código es idéntico, solo hace falta usar la imaginación.

Imaginemos que `MAXN = 10`. Inicialmente nuestro arreglo está lleno de ceros.
Supongamos que se hacen dos operaciones: `update(3, 7)` y `update(9, -7)`.
Ahora, si llamamos `query` en cada posicion, veríamos lo siguiente:

```
query(i) =  0  0  7  7  7  7  7  7  0  0
i        =  1  2  3  4  5  6  7  8  9 10
```

Aunque sabemos que en realidad hicímos dos actualizaciones en punto y después
varias consultas de suma en prefijo, podemos imaginarnos algo un poco distinto:

Primero sumamos +7 a todos los elementos del rango [3...8] y despues accedimos a
cada uno.

Ambas interpretaciones son consistentes en si mismas, pero nos permiten encarar
problemas totalmente distintos.

> Notas del editor de la wiki -- cosas que faltan
>
> Interpretaciones:
>
> - Bolsa de rangos :check:
> - Arbol infinito
> - least significant bit :check:
> - Array implicito

