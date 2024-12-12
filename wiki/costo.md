<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script src="mathjax-config.js"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Analisis de costo

El analisis asintotico de costo es una forma de medir a grandes rasgos la
eficiencia de un programa.

Al hablar del costo de un programa nos referimos a su tiempo de ejecucion o, en
otras palabras, la cantidad de operaciones que hace.

Estas son las ideas importantes:

- Podemos clasificar los programas segun su costo, y hay un orden fijo entre
  las clases
- Un programa de una clase menor corre más rápido que un programa de una clase
  mayor cuando el input es grande.
- Si sabemos la clase de costo de un programa, podemos estimar el tiempo de
  ejecución que tendrá al enviarlo al juez.

Usando estas herramientas podemos darnos una idea de antemano, de qué costo
tiene que tener la solución a un problema, y así descartamos muchas posibles
ideas, sin tener que pensar en todos los detalles.

Concretamente, expresamos el costo en función de algún parámetro de la entrada.
Por lo general el parametro es el tamaño de la entrada, y lo llamamos N.

Para indicar costo escribimos la letra "O", seguido de la ley de la función
entre paréntesis.

Por ejemplo: O(N) significa que el programa hace aproximadamente N operaciones
al recibir una entrada de tamaño N.

Algo importante sobre el analisis de costo es que es aproximado:

- No nos importan los factores constantes. Si un programa hace N o 5N
  operaciones, se considera \\( O(N) \\) en ambos casos (formalmente
  \\(O(5N) = O(N)\\)).

  Lo mismo pasa si el programa hace N operaciones rápidas (como sumar enteros) o
  N operaciones lentas (como calcular raices cuadradas), en ambos casos es O(N).

  No se considera lo mismo cuando se llega a una clase de costo superior:
  \\(O(N^{2})\\) no es lo mismo que \\(O(N)\\).

- Muchas veces encontrar el costo exacto es muy dificil y nos conformamos con
  una cota superior (pesimista, mayor al verdadero costo).

  ¿Por qué? Es facil. Si somos pesimistas e incluso así resulta que el programa
  es suficientemente rápido, entonces podemos enviarlo sin tener dudas.

  En cambio, si somos demasiado optimistas terminamos pensando que algo va a ser
  suficientemente rapido cuando realmente no lo es.

Ejemplos:

La función de abajo tiene costo \\(O(k)\\), porque el bucle realiza
\\(\frac{k}{2}\\) iteraciones.

```c++
int suma_pares(int datos[], int k) {
    int resultado = 0;
    for (int i = 0; i < k / 2; ++i)
        resultado += datos[i * 2];
    return resultado;
}
```

La función de abajo tiene costo \\(O(k^{2})\\), porque el bucle interno realiza
\\(k\\) iteraciones, y se repite \\(k\\) veces, haciendo un total de
\\(k\cdot k = k^{2}\\) iteraciones.

```c++
int inversiones(int datos[], int k) {
    int resultado = 0;
    for (int i = 0; i < k; ++i)
        for (int j = 0; j < k; ++j)
            if (i < j && datos[i] > datos[j])
                resultado += 1;
    return resultado;
}
```

## Desglosando programas

Muchas veces es dificil analizar el costo de un programa todo junto. Por suerte
hay algunas reglitas que nos sirven para analizar por partes.

### Secuenciacion

Si un programa tiene dos partes, el costo asintotico del programa entero es el
maximo de las dos partes.

Por ejemplo, este programa tiene costo \\(O(k^{2})\\)

```c++
int pepe(int datos[], int k) {
    int x1 = suma_pares(datos, k);    // costo O(k)
    int x2 = inversiones(datos, k);   // costo O(k*k)
    return x1 + x2;
}
```

Lo mismo pasa con programas que usan condicionales, como `if` y `switch`.

### Iteración

El costo de un bucle es, a lo sumo, la cantidad de iteraciones multiplicada por
el máximo costo de una sola iteración.

Por ejemplo, este programa tiene costo menor o igual a \\(O(k^{2})\\).

```c++
int papa(int datos[], int k) {
    int x = 0;
    for (int i = 0; i < k; ++i) {     // k iteraciones
        x += suma_pares(datos, i);    // maximo costo O(k)
    }
    return x;
}
```

Decimos 'a lo sumo' porque hay algoritmos que tienen muchas iteraciones que
son muy rapidas y unas pocas iteraciones lentas. En esos casos, el costo puede
ser menor al producto entre el maximo costo y la cantidad de iteraciones.

> Esto se llama costo amortizado y se explica en detalle mas adelante.

## Ejercicios

Calcular el costo de estas funciones.

```c++
int f0(int n) {
  int res = 0;
  for (int i = 0; i < n; ++i)
      res = res + i;
  return res;
}

int f1(int n) {
  int res = 0;
  for (int i = 0; i < n; ++i)
      res = res + sqrt(i);
  return res;
}

int f2(int n) {
  int res = 0;
  for (int i = n-1; i >= 0; --i)
      res = res + 50;
  return res;
}

int f3(int n) {
  int res = 0;
  for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
          res = res + 1;
  return res;
}

int f4(int n) {
  int res = 0;
  for (int i = 0; i < n; ++i)
      for (int j = i; j < n; ++j)
          res = res + 1;
  return res;
}

int f5(int n) {
  int res = 0;
  for (int i = 0; i < n; ++i)
      for (int j = 0; j < i; ++j)
          res = res + 1;
  return res;
}

// (*)
int f6(int n) {
    int res = 0;
    for (int i = 0; i * i < n; ++i) {
        res = res + 1;
    }
    return res;
}

// (*)
int f7(int n) {
    int res = 0;
    for (int i = 0; i * i < n; ++i) {
        res = res + 1;
    }
    return res;
}

// (*)
int f8(int n) {
  int res = 0;
  for (int i = 1; i < n; i = i * 2)
      res = res + 1;
  return res;
}

// (*)
int f9(int n) {
  int res = 0;
  for (int i = n; i > 0; i = i / 2)
      res = res + 1;
  return res;
}

// (*)
int f10(int n) {
    int res = 0;
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < n; j += i) {
            res = res + 1;
        }
    }
    return res;
}
```

## Complejidad computacional

Hablando en criollo muchas veces le decimos complejidad al costo de un programa.
Esto es incorrecto. La complejidad computacional de un _problema_ (y no de un
_programa_) es el minimo costo asintotico posible que tiene un _programa_ que
resuelve ese _problema_.

Por ejemplo, se conocen algoritmos que ordenan arreglos con costo
\\(O(N \log (N))\\) y está demostrado matemáticamente que no existen algoritmos
de ordenamiento más rapidos que esto. Entonces, el problema de ordenar un
arreglo tiene complejidad \\(O(N \log (N))\\).

Si te interesa hacer un desvio por este tema teorico (que no es tan importante,
pero es bastante interesante), visitá el [articulo completo]( complejidad ).

## Costo amortizado

Muchas veces las reglas que vimos antes son demasiado pesimistas asique hace
falta hacer un analisis mas detallado.

Por ejemplo, siguiendo las reglas concluimos que el codigo de abajo tiene costo
menor o igual a \\(O(\texttt{tam\_a} \cdot \texttt{tam\_b})\\). Esto es verdad,
pero siendo mas preciso podemos ver que tiene costo
\\(O(\texttt{tam\_a} + \texttt{tam\_b})\\).

```c++
// a y b son arreglos con valores crecientes
// por ejemplo si tenemos
// a = [1, 5, 8, 13]
// b = [1, 2, 3, 6, 8, 9, 13]
// el resultado es 3 porque comparten el 1, el 8 y el 13
int contar_iguales(int a[], int tam_a, int b[], int tam_b) {
    int res = 0;
    int j = 0;
    for (int i = 0; i < tam_a; ++i) { // tam_a iteraciones
                                      // costo maximo O(tam_b)
        while (j < tam_b && b[j] < a[i]) j++;
        if (b[j] == a[i]) res++;

    }
    return res;
}
```

> TO-DO: explicar

**Ejercicio**: revisar la función número 10 del ejercicio anterior.

## Funciones recursivas

Para encontrar el costo de una funcion recursiva tenemos que resolver una
recurrencia. Esto es dificil en general pero hay tecnicas para casos
especificos.

> TO-DO: explicar como armar recurrencias

### Probar y chequear (con induccion)

Después de analizar varias funciones uno gana bastante intuición sobre el costo,
y termina siendo capaz de "adivinar" con muy alto procentaje de acierto.

Si acertamos despues se puede demostrar que es correcto usando inducción
matemática.

> TO-DO: ejemplos

### Teorema maestro

Para funciones que tienen varias ramas recursivas con tamaños proporcionales al
problema original hay una reglita mas o menos simple.

<https://es.wikipedia.org/wiki/Teorema_maestro>

<https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)>

> TO-DO: explicar

#### Teorema Akra-Bazzi

Es una versión mas potente pero más dificil de aplicar del teorema maestro. No
suele ser útil pero está bueno saber que existe.

<https://en.wikipedia.org/wiki/Akra%E2%80%93Bazzi_method>

> TO-DO: explicar
