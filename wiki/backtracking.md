
# Problemas de búsqueda

> TO-DO: reescribir esta sección basandose en problemas concretos

Encontrar valores (i,j,k,q) que cumplan alguna propiedad.

### Fuerza bruta

La técnica más confiable para sacar un par de puntos en este tipo de problema es la fuerza bruta. Esta consiste en probar todas las candidatas a solucion y quedarse con alguna que sea efectivamente una solucion al problema.

La forma más común de hacer esto es con varios for anidados. Osea, los algoritmos de fuerza bruta tienen esta pinta:

```c++
vector<int> resolver() {
  forn(i, n) {
    forn(j, n) {
      forn(k, n) {
        forn(q, n) {
          if (es_solucion_valida(i, j, k, q)) {
            return {i, j, k, q};
          }
        }
      }
    }
  }
}
```

La complejidad de este algoritmo es O(N ^ cantidad), que es extremadamente lento. Justamente por eso, atacar un problema con fuerza bruta rara vez nos va a dar un puntaje alto.

### Backtracking

Para mejorar esto usamos el backtracking, una estrategia donde descartamos muchas posibilidades de un tirón. Esto se implementa con varios ifs dentro de los bucles de la fuerza bruta.

```c++
vector<int> resolver() {
  forn(i, n) {

    // *** agregamos este if ***
    if (i_es_invalido(i)) continue;

    forn(j, n) {

      // *** agregamos este if ***
      if (j_es_invalido(i, j)) continue;

      forn(k, n) {
        forn(q, n) {
          if (es_solucion_valida(i, j, k, q)) {
              return {i, j, k, q};
          }
        }
      }
    }
  }
}
```

La mayoria de las veces un if en el bucle externo optimiza más que un if en un bucle interno, por lo que puede ser util cambiar el orden de los bucles. Ojo! Esto no siempre se puede. Por ejemplo, en el codigo de arriba, necesitamos un valor de "i" para saber si "j" es invalido, por lo que no sería posible cambiar el orden de los bucles.

Si encontramos buenas formas de optimizar el backtracking, a veces podemos robar un par de puntos más. Sin embargo, no suele ser suficiente para sacar “muchos” puntos en un problema. (Para eso existen las otras técnicas!)

Problema: ["ocho reinas" (Wikipedia)]( https://es.wikipedia.org/wiki/Problema_de_las_ocho_reinas )

Por otro lado, este código tiene un problema grande: hay un for por cada variable (i,j,k,q). Esto significa que no podemos resolver problemas donde la cantidad de variables es muy grande o depende de la entrada.

### Fuerza bruta recursiva

Esto se puede resolver con una función recursiva: definimos una función que como argumento toma un número que indica cuál variable debe asignar. Una vez asignado un valor, pasa a la siguiente variable, y así recursivamente.

Luego de asignar todas las variables, verifica si la solucion es correcta y, en caso de serlo, termina la busqueda.

```c++
vector<int> valores;
int cantidad;

bool busqueda(int var) {
  if (var == cantidad) {
    if (es_solucion_valida(valores)) {
      return true;
    } else {
      return false;
    }
  } else {
    forn(valor, n) {
      valores[var] = valor;
      bool exito = busqueda(var+1);
      if (exito) return true;
    }
    return false;
  }
}

vector<int> resolver() {
  valores.resize(cantidad);
  busqueda(0);
  return valores;
}
```

Esto tiene todos los mismo problemas de tiempo de ejecucion que vimos con la fuerza bruta

### Backtracking recursivo

Para resolver esto, volvemos a recurrir a la idea del backtracking. En vez de verificar si la solucion es valida al final, podemos revisar si con los valores ya asignados es imposible construir una solucion valida.

No hace falta que este chequeo sea infalible! Lo importante es dejar pasar **todas** las soluciones validas, y cortar la **mayor cantidad posible** de soluciones invalidas.

```c++
vector<int> valores;
int cantidad;

bool busqueda(int var) {
  if (var == cantidad) {
    if (es_solucion_valida(valores)) {
      return true;
    } else {
      return false;
    }
  } else {

    // *** agregamos este if ***
    if (ya_es_imposible(valores, var)) return false;

    forn(valor, n) {
      valores[var] = valor;
      bool exito = busqueda(var+1);
      if (exito) return true;
    }
    return false;
  }
}

vector<int> resolver() {
  valores.resize(cantidad);
  busqueda(0);
  return valores;
}
```

Problema: ["¡Consigamos un solo color!" Nacional Nivel 3 2012]( https://www.oia.unsam.edu.ar/_media/prob/c3a12n3p2.pdf )

## Problemas de optimizacion

Aparte de encontrar una solución válida, la fuerza bruta puede usarse para encontrar la mejor solución a un problema (la de menor costo, de menor tamaño, etc)

En estos casos, el codigo es muy parecido:

```c++
vector<int> resolver() {
  vector<int> valores = {0,0,0,0};
  vector<int> mejor_solucion = {0,0,0,0};

  forn(i,n) {
    valores[0] = i;
    forn(j,n) {
      valores[1] = j;
      forn(k,n) {
        valores[2] = k;
        forn(q,n) {
          valores[3] = q;
          if (costo(valores) < costo(mejor_solucion)) {
            mejor_solucion = valores;
          }
        }
      }
    }
  }

  return mejor_solucion;
}
```

Ahora, para optimizar es un poco distinto.

Nos preguntamos si, con las variables asignadas hasta ahora, es imposible obtener un costo menor al que se tiene actualmente. Para hacer esto podemos calcular un costo optimista, correspondiente a una solucion "ideal" que se puede formar de ahora en adelante.

Si esta solucion ideal no puede vencer a la que ya se encontró, entonces ninguna solución real podrá vencerla tampoco.

```c++
vector<int> resolver() {
  vector<int> valores = {0,0,0,0};
  vector<int> mejor_solucion = {0,0,0,0};

  forn(i,n) {
    valores[0] = i;
    forn(j,n) {
      valores[1] = j;

      // *** agregamos este if ***
      if (costo_optimista_ij(i, j) >= costo(mejor_solucion)) continue;

      forn(k,n) {
        valores[2] = k;
        forn(q,n) {
          valores[3] = q;
          if (costo(valores) < costo(mejor_solucion)) {
            mejor_solucion = valores;
          }
        }
      }
    }
  }
  return mejor_solucion;
}
```

Y de la misma manera que antes, podemos extender esto a problemas con cantidades arbitrarias de variables usando recursion.

```c++
vector<int> valores;
vector<int> mejor_solucion;
int cantidad;

void busqueda(int var) {
  if (var == cantidad) {
    if (costo(valores) < costo(mejor_solucion)) {
      mejor_solucion = valores;
    }
  } else {
    if (costo_optimista(valores, var) >= costo(mejor_solucion)) return;
    forn(valor, n) {
      valores[var] = valor;
      busqueda(var+1);
    }
  }
}

vector<int> resolver() {
  valores.resize(cantidad, 0);
  mejor_solucion.resize(cantidad, 0);
  busqueda(0);
  return mejor_solucion;
}
```

