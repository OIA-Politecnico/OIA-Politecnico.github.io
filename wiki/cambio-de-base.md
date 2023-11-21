# Cambio de base

En la escuela todos aprendimos a representar números grandes usando secuencias de dígitos (números chiquitos, menores a diez). A cada digito se le asigna un valor absoluto distinto dependiendo de su posición, que se corresponde con multiplicar el dígito con una potencia de diez. Así, los primeros dígitos representan valores más grandes y decimos que son "más significativos".

La idea fundamental detrás de este sistema es que es posible separar cualquier número en una parte que es múltiplo de 10 y otra parte que no, y que es menor a diez. En términos algebráicos, podemos decir que cualquier número natural `n` se puede expresar de esta forma:

```
n = 10 * c + r
```

Donde `c` y `r` son numeros naturales y, mas especificamente, `r` es un digito (el ultimo dígito de `n`). Por ejemplo:

- `  9 = 10 *  0 + 9`
- ` 45 = 10 *  4 + 5`
- ` 70 = 10 *  7 + 0`
- `246 = 10 * 24 + 6`

A partir de la formulita de arriba se puede ver que `c` es el cociente de `n` con `10` y `r` es el resto. O sea, si dado un numero `n` quisieramos descomponerlo en sus dos partes `c` y `r`, haríamos una cosa así:

```c++
int main() {
  int n;
  cin >> n;

  int c = n / 10;
  int r = n % 10;

  cout << n << " = 10 * " << c << " + " << r << "\n";
}
```

Para encontrar todos los digitos `n`, podemos volver a descomponer `c` en dos partes hasta que no se pueda mas.

```c++
int main() {
  int n;
  cin >> n;

  // mientras haya mas de un digito
  while (n >= 10) {

    // descompongo en partes
    int c = n / 10;
    int r = n % 10;

    cout << r << " ";

    // sigo descomponiendo c
    n = c;
  }

  // ahora queda un solo digito
  cout << n << "\n";
}
```

De esta forma podemos separar `n` en dígitos.

En la escuela muchos vimos tambien el sistema binario (en mi época lo tomaban en el examen de ingreso del poli. ¿Ahora lo siguen tomando?). En ese momento aprendimos que el procedimiento para convertir un numero a binario es muy parecido a lo que vimos recien: dividimos el numero por dos y encontramos cociente y resto. El resto es el ultimo digito binario. Al cociente lo volvemos a dividir por dos hasta que no se pueda mas, y así vamos consiguiendo todos los digitos.

En código, también podemos escribir esto de forma casi identica a la anterior.

```c++
int main() {
  int n;
  cin >> n;
  while (n >= 2) {
    int c = n / 2;
    int r = n % 2;
    cout << r << " ";
    n = c;
  }
  cout << n << "\n";
}
```

Si comparamos los dos programas, vemos lo unico que cambia es el numero que usamos para dividir (en cada lugar que usamos `10` antes, ahora usamos `2`). Entonces, nos podríamos preguntar si esta idea tiene sentido para cualquier numero que elijamos. ¡Y resulta que sí!

El mismo razonamiento que hicimos para separar un numero en un multiplo de diez y un digito (menor a diez) es válido para cualquier numero, el cual llamamos base. O sea, siempre podemos expresar cualquier numero `n` de la siguiente forma:

```
n = BASE * c + r
```

Por ejemplo

- ` 26 = 8 * 3 + 2                                = 32 en base 8`
- ` 49 = 7 *   7 + 0 = 7 * (7 * 1 + 0) + 0        = 100 en base 7`
- ` 26 = 5 * 5 + 1 = 5 * (5 * 1 + 0) + 1          = 101 en base 5`
- `256 = 2 * 128 + 0 = 2 * (2 * 64 + 0) + 0 = ... = 100000000 en base 2`
- `256 = 16 * 16 + 0 = 16 * (16 * 1 + 0) + 0      = 100 en base 16`

> Aunque normalmente usamos numeros naturales, se puede tomar como base a **cualquier numero real excepto 0 y 1**.
> 
> Para pensar: ¿por qué estos dos números no funcionan?

Con esta idea, estamos listos para definir el algoritmo de cambio de base.

Hay que tener un poco de cuidado porque este metodo nos da los digitos en orden de menos a más significativo, que puede ser el orden incorrecto para, por ejemplo, imprimir el numero. Para resolver esto los podemos guardar en una lista y darlos vuelta al final:

```c++
vector<int> cambio_de_base(int n, int base) {
  vector<int> digitos;
  while (n >= base) {
    int c = n / base;
    int r = n % base;
    digitos.push_back(r);
    n = c;
  }
  digitos.push_back(n);
  reverse(digitos.begin(), digitos.end());
  return digitos;
}

int main() {
  int n, base;
  cin >> n >> base;
  vector<int> digitos = cambio_de_base(n, base);
  for (int x : digitos) {
    cout << x << " ";
  }
  cout << "\n";
}
```