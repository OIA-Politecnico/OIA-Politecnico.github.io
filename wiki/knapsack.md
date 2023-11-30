
# 🚧 Página en construcción 🚧
# Optimización de DP

## El Problema

El problema de la mochila (mejor conocido como "knapsack problem") es uno de los más estudiados de la computación.

En este problema nos dan un conjunto de objetos, cada uno con un peso y un valor. El objetivo es elegir algunos de esos objetos, maximizando el valor obtenido, sin que la suma de sus pesos supere un tope predeterminado (también parte de la entrada del problema).

Formalmente, nos dan una lista de pesos de longitud N, una lista de valores de longitud N y un tope de peso, T, y queremos responder con el mayor valor que se puede obtener sin superar el tope de peso.

Hay muchas variantes y las más conocidas están dadas por las respuestas a las siguientes preguntas:

- Se puede tomar el mismo objeto más de una vez?
- Se pueden tomar objetos parcialmente?

Veamos el caso en el que no se puede tomar el mismo objeto más de una vez, ni se pueden tomar objetos parcialmente. Aparte, tomemos cotas de N<=1000 y T<=100000.

## Primer intento: DP recursiva

Un enfoque que podemos tomar para este problema es DP recursiva. Por ejemplo, lo podríamos implementar como muestra abajo.

```c++
const int MAXN = 1000;
const int MAXT = 100000;

int N, T;
int peso[MAXN];
int valor[MAXN];

int dp[MAXT+1][MAXN+1];
// Devuelve el mayor valor que se puede obtener usando objetos
// desde el i-esimo en adelante, y con suma de peso a lo sumo t.
int mochila(int t, int i) {
  if (i == n) return 0;
  if (t == 0) return 0;
  if (dp[t][i] != -1) return dp[t][i];

  // siempre puedo no tomar el objeto
  int r = mochila(t, i+1);

  // si me queda suficiente espacio, pruebo agarrar el objeto
  if (t >= peso[i])
    r = max(r, mochila(t-peso[i], i+1) + valor[i]));

  return r;
}

int run_mochila() {
  return mochila(T, 0);
}
```

Aunque esto funciona y tiene una complejidad aceptable, es probable que si enviamos esta solución a un juez online recibamos TLE (límite de tiempo excedido).

## Segundo intento: DP iterativa

Un parche que solemos aplicar cuando una DP recursiva es demasiado lenta, es convertirla a forma iterativa.

Esto nos ahorra el costo de la recursión y podemos aprovechar para eliminar algunos ifs (aunque en este caso no lo vamos a hacer, para mayor claridad).

```c++
int run_mochila() {
  dforn(i, n+1) {
    forn(t, T+1) {
      if (i == n) { dp[t][i] = 0; continue; }
      if (t == 0) { dp[t][i] = 0; continue; }
      int r = dp[t][i+1];
      if (t >= peso[i])
        r = max(r, dp[t-peso[i]][i+1] + valor[i]));
      dp[t][i] = r;
    }
  }
  return dp[T][0];
}
```

Aunque este código es más repido que el anterior, puede no ser suficiente para obtener "aceptado" como veredicto. Ahora, la lentitud viene de recorrer por columnas en vez de por filas. No voy a ahondar demasiado (porque no se tanto del tema) pero hay dos cosas para saber:

Primero, las matrices en C se organizan por filas. Que quiero decir? En C (y C++), un array bidimensional es una tira larga de memoria, donde primero viene toda la primer fila, después toda la segunda fila, etc. Por ejemplo, si tenemos este código:

```c++
int pepe[2][5];
forn(i,2) {
  forn(j,5) {
    pepe[i][j] = i;
  }
}
```

En memoria, pepe es la lista `[0 0 0 0 0  1 1 1 1 1]`

Entonces, las posiciones pepe[1][0] y pepe[1][1] están pegadas en memoria, pero las posiciones pepe[0][1] y pepe[1][1] están bastante léjos (a 5 ints de distancia en este caso, pero es más si las filas son más grandes).

Segundo, las computadoras modernas están más optimizadas para acceder a memoria que está cerca entre sí que a memoria que está lejos entre sí. Esto se debe a dos componentes que tienen los microprocesadores modernos:

- La caché, que guarda los valores de memoria a los que se accedieron recientemente, para acceso más rápido.
- El prefetcher, que intenta predecir direcciones de memoria que se leeran en el futuro, y las guarda en la caché antes de tiempo.


## Solución 1: Transponer la matriz

Si el problema es que cada acceso a memoria es muy lejano al anterior, lo que podemos hacer es acercarlos. Una forma de hacer esto es transponer la matriz (intercambiamos los indices). Con ese cambio, cada salto de `t` a `t+1` nos llevará a la siguiente posicion de la misma fila, y no a la misma posición de la siguiente fila.

Debido al orden en memoria de las matrices en C++, esto resulta ser una gran mejora.

```c++
int dp[MAXN+1][MAXT+1]; // no olvidemos intercambiar las cotas de la matríz
int run_mochila() {
  dforn(i, n+1) {
    forn(t, T+1) {
      if (i == n) { dp[i][t] = 0; continue; }
      if (t == 0) { dp[i][t] = 0; continue; }
      int r = dp[i+1][t];
      if (t >= peso[i])
        r = max(r, dp[i+1][t-peso[i]] + valor[i]));
      dp[i][t] = r;
    }
  }
  return dp[0][T];
}
```

Con este cambio bastante pavo (ordenar los datos para poder recorrer por filas), logramos hacer mejor uso de la cache y el prefetcher, y podemos obtener mejoras del 10x.

Suele ser muy fácil cambiar un programa que procesa por columnas a uno que procesa por filas, asique está bueno tener esto en cuenta.

## Solución 2: Usar dos filas

Otra solución distinta viene de observar tres cosas:

- Si las filas fueran cortas, incluso acceder a la siguiente fila sería amigable con la caché.
- En cada iteración del loop externo solo leemos de la columna `i+1` y escribimos en la columna `i`.
- En módulo 2, `i` siempre es distinto a `i+1`. (En particular `i%2 != (i+1)%2`)

Esto nos permite guardar solo 2 columnas: una de la cual leemos y otra en la cual escribimos. Para implementar esto sin lógica adicional, usamos `i%2` y `(i+1)%2` para alternar el rol de las columnas.

```c++
int dp[MAXT+1][2];  // las filas ahora tienen dos elementos
int run_mochila() {
  dforn(i, n+1) {
    forn(t, T+1) {
      if (i == n) { dp[t][i%2] = 0; continue; }
      if (t == 0) { dp[t][i%2] = 0; continue; }
      int r = dp[t][(i+1)%2];
      if (t >= peso[i])
        r = max(r, dp[t-peso[i]][(i+1)%2] + valor[i]));
      dp[t][i%2] = r;
    }
  }
  return dp[T][0%2];
}
```

Notar que acá volvimos al orden de fila-columna que no era amigable con la caché. Sin embargo ahora las filas son muy chicas, e incluso pasar de una fila a la siguiente es un salto muy corto en memoria. Así, terminamos esquivando el problema de la caché completamente.

Aparte de ser más amigable con la caché, esto reduce el uso de memoria de O(N*T) a O(T), que no es poca cosa.

Evidentemente, este truco es más potente que el anterior (transponer la matriz), pero menos aplicable (solo sirve en problemas donde necesitamos pocas columnas).

## Solución 3: Push DP

> 🚧 Seccion en construcción 🚧

En las soluciones con DP iterativa, recorremos la matriz juntando los valores necesarios para computar la posición actual. En cambio, podemos dar vuelta todas las relaciones, y por cada posición de la matriz "empujar" información hacia las posiciones que referenciarian la posición actual.

Eso es, en vez de preguntar "¿que estados necesito para construir la solucion al actual?", preguntamos "¿para cuáles otros estados puedo construir soluciones a partir del actual?".

El primer tipo de DP se denomina "pull DP", y el segundo "push DP".

Veremos que la solución que venimos trabajando puede convertirse a estilo push, pero esto no es cierto en general. De la misma manera, hay DPs estilo push que no se pueden convertir a estilo pull. Desafortunadamente, encontrar esas push DP necesita una forma de pensar completamente distinta a la que venimos trabajando.

Algo notable de las soluciones basadas en push DP que suelen ser más cortas que la pull DP correspondiente.

```c++
int dp[MAXT+1][MAXN+1];
int run_mochila() {
  dforr(i, 1, n+1) {
    forn(t, T+1) {
      dp[t][i-1] = max(dp[t][i-1], dp[t][i]);
      if (t+peso[i] <= T)
        dp[t+peso[i]][i-1] = max(dp[t+peso[i]][i-1], dp[t][i] + valor[i]));
    }
  }
  return dp[T][0];
}
```

> TODO: explicación

```c++
int dp[MAXT+1];
int run_mochila() {
  forn(i, n) dforn(t, T+1) if (t+peso[i] <= T)
    dp[t+peso[i]] = max(dp[t+peso[i]], dp[t] + valor[i]));
  return dp[T];
}
```