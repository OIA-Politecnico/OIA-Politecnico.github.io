
# Archivos base en OIA

## Introducción

En las competencias oficiales de OIA, el código que se entrega no debe realizar
E/S. En cambio, se debe enviar un archivo que contiene una función que recibe
los datos ya cargados en memoria, y los devuelve de la misma manera.

Será el jurado quien se encargue de generar código que lea los datos y los pase a
nuestro programa. Para garantizar la compatibilidad, el prototipo de la función
debe cumplir exactamente con la descripción dada en el enunciado.

Aunque en una competencia oficial el jurado ofrece una plantilla con el
prototipo adecuado para cada problema, esto no siempre está disponible al
resolver un problema en el juez OIA.

## Ejemplo - Auto electrico

El enunciado del problema "Auto electrico", especifica el prototipo al decir:

> Se debe implementar una función
>
> electromovil(E : ENTERO; ubicacion, autonomia : ARREGLO[E] de ENTEROS)
>
> Que devuelva un ARREGLO de ENTEROS, ...

El prototipo correspondiente en C++ es este:

```c++
vector<int> electromovil(int E, vector<int> ubicacion, vector<int> autonomia) {
}
```

> TO-DO: agregar una explicación del proceso de traducir de la especificacion
> que dan en OIA a C++

> TO-DO: agregar guias paso a paso de problemas especificos (e.g.
> "Auto eléctrico", "Señalizando un camino...") 

## Referencia

Al convertir los tipos a C++, se debe seguir esta tabla: [tipos](img/Tabla%20de%20tipos.pdf)
