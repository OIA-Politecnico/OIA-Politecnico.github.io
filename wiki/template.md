# Plantilla de programación competitiva

Al resolver varios problemas durante una competencia, hay pedazos de codigo
(macros, constantes, funciones) que vamos a usar en todos (o casi todos) los
problemas.

Para no andar copiando y pegando cada cosa a medida que nos damos cuenta que va
a hacer falta, está bueno armar un archivo plantilla al principio de la prueba,
el cual podemos duplicar al empezar a codear la solución de un problema.

Como hay que saberla de memoria, no está bueno que la plantilla sea larga.
Tampoco queremos que sea tan corta que terminamos perdiendo más tiempo
re-escribiendo las mismas definiciones todo el tiempo o buscandolas entre los
otros archivos que creamos.

Esta es una plantilla razonable para OIA:

```c++
#include <bits/stdc++.h>
using namespace std;
#define forr(i,a,b) for(int i=int(a);i<int(b);++i)
#define forn(i,n) forr(i,0,n)
using ll = long long;

int const MAXN = -1;
```
