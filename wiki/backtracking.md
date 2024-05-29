
# Backtracking

- [CSES - Chessboard and Queens](https://cses.fi/problemset/task/1624)
- [Codeforces - Help Caretaker](https://codeforces.com/contest/142/problem/C)
- [OIA - Consigamos un solo color](https://juez.oia.unsam.edu.ar/task/112) (\*)

En un monton de problemas, la solución más directa es probar todas las posibilidades y quedarse con la mejor. La cantidad de posibilidades suele ser exponencial en el tamaño del problema asique esto no entra, pero con algunas optimizaciones puede entrar para N chico (incluso hasta N=100, dependiendo del problema)

Hay algunas diferencias entre problemas de busqueda (donde queremos construir algo que cumple una propiedad) y problemas de optimizacion (donde aparte queremos maximizar una funcion de puntaje), asique veamos uno y uno.

# Problema de búsqueda: N Reinas

Enunciado: Colocar N reinas de ajedrez en un tablero de NxN sin que se amenacen.

> En el ajedrez, una reina amenaza a todas las piezas que estan en la misma fila, columna o diagonal.

## Solucion

La solucion mas directa para un tamaño de tablero N constante, es poner N fors anidados que prueban las posiciones de las reinas.

    void reinas() {
    	int const N = 5;
    	forn(i1, N*N) forn(i2, N*N) forn(i3, N*N) forn(i4, N*N) forn(i5, N*N) {
    		if (!se_amenazan(i1, i2, i3, i4, i5)) {
    			imprimir_tablero(i1, i2, i3, i4, i5);
    			return;
    		}
    	}
    }
    // Implementar se_amenazan() e imprimir_tablero() queda de ejercicio :)

Esto no anda si la cantidad de reinas depende del input, pero se puede hacer lo mismo con recursion para manejar una cantidad variable de reinas.

    int N; // tamaño del tablero
	vector<int> posiciones;
    
    // n es la cantidad de reinas que falta poner
	// la funcion devuelve si lo pudo hacer o no
    bool colocar(int n) {
    	if (n == 0) {
    		if (se_amenazan(posiciones)) return false;
			imprimir_tablero(posiciones);
			return true;
    	}

    	forn(i, N*N) {
    		posiciones[n-1] = i;
    		if (colocar(n-1)) return true;
    	}
    	return false;
    }

	void reinas(int tamano) {
		N = tamano;
		posiciones.resize(tamano);
		colocar(tamano);
	}



La idea es asignar la posicion de una reina, recursivamente poner el resto de las reinas y si no se pudo seguimos iterando probando nuevas posiciones.

Esto anda, pero para N=7 ya es super lento.

Por suerte tiene un par de cosas que son obviamente lentas:

- Para una misma configuracio de reinas, prueba todas las permutaciones
- Pone reinas en posiciones ya amenazadas

Resolver el primer punto es facil. Si forzamos algun orden entre las reinas, no vamos a probar todas las permutaciones. Por ejemplo, podemos decidir que cada reina que colocamos va en una posicion mayor a todas las anteriores.

Implementativamente, es facil de adaptar el programa: agregamos un parametro que indica la minima posicion a probar. Al recursionar, siempre pasamos la posicion elegida más uno.

    bool colocar(int n, int i0) {
		// ...

    	forr(i, i0, N*N) {
    		posiciones[n-1] = i;
    		if (colocar(n-1, i+1)) return true;
    	}

		// ...
    }

Al no probar permutaciones, dividimos la complejidad por `factorial(N)`. Con esto va rapido hasta N=15.

Ahora resolvemos el segundo punto.

La idea es verificar si la configuracion elegida es válida en cada paso de la busqueda en vez de solo al final.

Si modificamos `se_amenazan()` tal que tome el indice de la primera reina colocada, lo podemos codear fácil asi:

    bool colocar(int n, int i0) {
		if (se_amenazan(posiciones, n)) return false;

		// ...
    }

En general no es facil analizar cuanto va a acelerar el programa este tipo de cosas, pero en este programa en particular, la optimizaciones nos permite acotar el programa a `O(factorial(N))`. (porque, al poner una pieza por fila y columna, el array de posiciones es una permutacion).

Bueno, en realidad es menor que N factorial, pero se re complica el analisis :(.

## Optimizaciones especificas al problema

Estas dos optimizaciones tal cual se ven arriba se pueden aplicar a cualquier problema, pero es muy comun tunearlas para el problema particular.

Por ejemplo, podemos combinar el orden de las reinas con la idea de que cada reina va en una fila distinta y forzar a que `colocar(n)` siempre coloque una reina en la fila `N-n`:

Como esto codifica el orden en el parametro `n`, no hace falta pasar otro parametro `i0`.

    bool colocar(int n) {
		// ...

		int fila = N-n;
    	forn(columna, N) {
			int i = fila * N + columna;
    		posiciones[n-1] = i;
    		if (colocar(n-1)) return true;
    	}

		// ...
    }

El chequeo de validez tambien se puede optimizar para este problema.

Si mantenemos un conjunto de columnas y diagonales amenazadas, podemos solo colocar reinas en posiciones que no estan amenazadas.

Como siempre nunca ponemos reinas que se amenazan, no hace falta verificarlo al principio de la funcion ni en el caso base.

    bool col[MAXN];
    bool diag1[MAXN];
    bool diag2[MAXN];
    bool colocar(int n) {
    	if (n == 0) {
    		// El tablero es valido por construccion :D
    		imprimir_tablero();
    		return true;
    	}
    
    	int fila = N-n;
    	forn(columna, N) {
    		int i = fila * N + columna;
    
    		int d1 = fila + columna;
    		int d2 = fila - columna + (N-1);
    
    		if (col[columna] || diag1[d1] || diag2[d2]) continue;
    
    		// marco como ocupadas
    		col[columna] = diag1[d1] = diag2[d2] = true;
    
    		posiciones[n-1] = i;
    		if (colocar(n-1)) return true;
    
    		// marco como libres
    		col[columna] = diag1[d1] = diag2[d2] = false;
    	}
    
    	return false;
    }

Un ultimo truco seria guardar los arreglos de booleanos con mascaras de bits y pasarlos como argumento de la recursion en vez de que sean globales, pero se pone bastante el feo el codigo.

# Problema de optimizacion: tractores

Enunciado: Colocar la mayor cantidad de tractores posibles en un tablero de NxM, sin que se solapen. Un tractor se puede rotar multiplos de 90 grados, y puede tener una de las siguientes formas:

    ###    #       #       #
     #     ###     #     ###
     #     #      ###      #

> Vamos a ver cómo calcular la máxima cantidad sin devolver la configuración que la logra, pero sería fácil cambiar el código para que también la devuelva.

## Solucion

De nuevo, la idea es hacer una función recursiva que va poniendo y sacando tractores. En los problemas de optimizacion aplican las mismas optimizaciones que a los problemas de busqueda:

- En vez de poner tractores en cualquier lugar, y verificar que sea una configuración válida (sin tractores solapados) al final, podemos evitar construir configuraciones invalidas

- Para no probar permutaciones de la misma configuración, podemos forzar un orden entre los elementos (que la esquina superior izquierda de cada tractor esté en una posición mayor a la de todos los anteriores)

Para que no sea completamente repetitivo, vamos a arrancar con esas optimizaciones ya implementadas.

La principal diferencia entre un problema de optimizacion y uno de busqueda es que no podemos cortar la busqueda después de encontrar una configuración válida cualquiera, sino que tenemos que seguir explorando porque puede haber configuraciones mejores.

Esto hace que los problemas de optimización sean, a grandes rasgos, más difíciles de optimizar que los de búsqueda.

    int N, M;
    bool tablero[MAXN][MAXN];
    
    int tractores(int cantidad, int i0) {
    
    	int mejor_calidad = cantidad;
    	forr(i, i0, N*M) {
    		forn(rotacion, 4) {
    			if (!tractor_dentro_del_tablero(i, rotacion)) continue;
    			if (tractor_solapa_tablero(i, rotacion)) continue;
    
    			poner_tractor(i, rotacion);
    
    			int calidad = tractores(cantidad+1, i+1);
    			if (calidad > mejor_calidad) mejor_calidad = calidad;
    
    			sacar_tractor(i, rotacion);
    		}
    	}
    
    	return mejor_calidad;
    }
    // todas las funciones para manipular el tablero son ejercicios :shrug:

Esto anda, pero toma 36 segundos en resolver el problema de 8x8.

La principal optimización se llama "branch and bound". La idea es calcular una cota superior a la calidad que se puede obtener en una rama de la busqueda. Si no es mayor a la mejor calidad ya encontrada (globalmente), no hace falta seguir explorando esa rama.

Por ejemplo, en este problema sabemos que un tractor ocupa 5 posiciones y la cantidad de posiciones libres desde `i0` en adelante es a lo sumo `N*M-i0`. Por lo tanto, siendo super optimistas, la máxima cantidad de tractores que podriamos llegar a colocar es `(N*M-i0)/5`.

La implementación es así:

	int mejor_calidad_global = 0;
    int tractores(int cantidad, int i0) {

    	int mejor_calidad = cantidad;

		int calidad_optimista = cantidad + (N*M-i0)/5;
		if (calidad_optimista <= mejor_calidad_global)
			return mejor_calidad;
    
    	forr(i, i0, N*M) {
			// ...
    	}
		
		// ...
    
    }

Esto baja el tiempo de 36 segundos a 6 segundos (Para N=8, M=8).

Esta optimización es muy sensible a la cota que logramos calcular. O sea, si calculamos una cota más ajustada, puede andar mucho más rápido.

Por ejemplo, intentemos solo contar casillas realmente libres mirando el tablero.


    int tractores(int cantidad, int i0) {
		// ...

    	int libres = 0;
    	forr(i, i0, N*M) {
    		int fila = i / M, columna = i % M;
    		if (!tablero[fila][columna]) libres++;
    	}
    	int calidad_optimista = cantidad + libres/5;

    	// ...
    }

Con este cambio pasamos de 6 segundos a 0,3 segundos (N=8, M=8)

Podemos hacer algunas cosas más, como no contar posiciones libres con sus 4 vecinos ocupados, pero el codigo se vuelve medio feo.

----------

# Articulo viejo

> A continuacion esta la version vieja del articulo. Es bastante confusa y verborragica... disculpas :^(.

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

