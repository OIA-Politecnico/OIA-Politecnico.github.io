La complejidad asíntotica (o complejidad, a secas) es una forma de medir a grandes rasgos
la eficiencia de un programa.

Al usar complejidad para medir programas, los agrupamos en grupos, que llamamos "clases de
complejidad".

Estas son las ideas importantes de usar complejidad:

- Hay un orden fijo entre las clases de complejidad
- Si un programa está en una clase de complejidad menor que otro, casi seguro que el primero es más rápido.
- Si sabemos la clase de complejidad de un programa, podemos estimar el tiempo de ejecución que tendrá al enviarlo para evaluación.

Usando estas herramientas podemos darnos una idea de antemano, de qué complejidad
tiene que tener la solución a un problema, y así descartamos muchas posibles ideas,
sin tener que pensar en todos los detalles.

La complejidad está dada por una expresión que representa la cantidad de operaciones que realiza un programa.

Mas concretamente, expresamos la complejidad cómo una función de algún parámetro de la entrada. Por
lo general, el tamaño del conjunto de datos, al que solemos llamar n. Para indicar complejidad
escribimos la ley de la función entre paréntesis, siguiendo la letra 'O'. Por ejemplo: O(n)

Ejemplos:

La función de abajo tiene complejidad O(n), porque el bucle realiza n iteraciones.

```c++
int suma(int datos[], int n) {
    int resultado = 0;
    for (int i = 0; i < n; ++i)
        resultado += datos[i];
    return resultado;
}
```

La función de abajo tiene complejidad O(n\*n), porque el bucle interno realiza n
iteraciones, y se repite n veces, para un total de n\*n iteraciones.

```c++
int inversiones(int datos[], int n) {
    int resultado = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (i < j && datos[i] > datos[j])
                resultado += 1;
    return resultado;
}
```

Es importante notar que a los fines de la complejidad, si un programa realiza n,
2\*n, n+50, etc. operaciones, es todo lo mismo, y la complejidad es O(n).

Lo mismo pasa si el programa realiza n operaciones rápidas (como sumar enteros),
o n operaciones lentas (como calcular raices cuadradas): en ambos casos es O(n).

Aparte, si un programa hace dos cosas con distintas complejidades, la complejidad
del programa es la mas grande de esas dos

Ejemplo:

Este programa tiene complejidad O(n\*n)

```c++
int cosa_loca(int datos[], int n) {
    int x1 = suma(datos, n);          // complejidad O(n)
    int x2 = inversiones(datos, n);   // complejidad O(n*n)
    return x1 + x2;
}
```

Ejercicio: dar las complejidades de estas funciones

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
  for (int i = 1; i < n; i = i * 2)
      res = res + 1;
  return res;
}

// (*)
int f7(int n) {
  int res = 0;
  for (int i = n; i > 0; i = i / 2)
      res = res + 1;
  return res;
}
```