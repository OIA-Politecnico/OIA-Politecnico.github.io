
# Archivos base en OIA

## Introducción

En las competencias oficiales de OIA, el código que se entrega no debe realizar
E/S. En cambio, se debe enviar un archivo que contiene una función que recibe
los datos ya cargados en memoria, y los devuelve de la misma manera.

Será el jurado quien se encargue de generar código que lea los datos y los pase a
nuestro programa. Para garantizar la compatibilidad, el prototipo de la función
debe cumplir exactamente con la descripción dada en el enunciado.

En una competencia oficial el jurado ofrece una plantilla con el prototipo
adecuado para cada problema. Como competidores solo tenemos que rellenar la
parte de adentro de la función.

> **Es de vital importancia que nuestro programa NO realice entrada y salida.**
>
> Si nuestro programa usa cin/cout/scanf/printf el juez va a **rechazar nuestra
> solución**.

Sin embargo los archivos base no siempre están disponible al resolver un
problema en el juez OIA. Una parte de este articulo está dedicado a cómo armar
los archivos por nuestra cuenta.

## Uso del evaluador

Al bajar los archivos base del sistema, nos encontramos con dos cosas
`electromovil.cpp` y `evaluadorElectromovil.cpp`.

El primero contiene la función que tenemos que completar. Sus argumentos y su
resultado están explicados en el enunciado de cada problema. Tiene esta pinta:

```c++
#include <vector>
using namespace std;
vector<int> electromovil(int E, vector<int> ubicacion, vector<int> autonomia) {
  // ¡agregar código de la solución acá!
  return {};
}
```

El segundo contiene todo el código que realiza entrada y salida, que podemos
usar para testear nuestro programa. Tiene esta pinta:

```c++
#include "electromovil.cpp"
#include <iostream>
using namespace std;
int main() {
  int N, E;
  cin >> N >> E;
  vector<int> ubicacion(N);
  for (int i = 0; i < N; ++i) cin >> ubicacion[i];

  // ... etc ...

  vector<int> resultado = electromovil(E, ubicacion, autonomia);

  for (int i = 0; i < resultado.size(); ++i) cout << resultado[i] << " ";
  cout << "\n";
}
```

Para compilar el programa tenemos que ejecutar este comando en la terminal:

```sh
g++ evaluadorElectromovil.cpp -o electromovil
```

Para ejecutarlo despues solo hace falta:

```sh
./electromovil
```

## Como armar archivos base

### Ejemplo - Auto electrico

El enunciado del problema "Auto electrico", especifica el prototipo al decir:

> Se debe implementar una función
>
> electromovil(E : ENTERO; ubicacion, autonomia : ARREGLO[E] de ENTEROS)
>
> Que devuelva un ARREGLO de ENTEROS, ...

El prototipo correspondiente en C++ es este:

```c++
vector<int> electromovil(int E, vector<int> ubicacion, vector<int> autonomia);
```

> TO-DO: agregar una explicación del proceso de traducir de la especificacion
> que dan en OIA a C++

> TO-DO: agregar guias paso a paso de problemas especificos (e.g.
> "Auto eléctrico", "Señalizando un camino...") 

### Referencia

Al convertir los tipos a C++, se debe seguir esta tabla: [tipos](img/Tabla%20de%20tipos.pdf)

