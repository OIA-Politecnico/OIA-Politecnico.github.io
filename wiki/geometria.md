
# Geometria (alerta, muy incompleto)

Una de las nociones fundamentales en la geometria computacional es el giro a favor o en contra del reloj (clockwise, counterclockwise). Es decir, dados tres puntos O, A, y B queremos saber si si hubiera un reloj con centro en O, las manecillas rotarian en direccion de A hacia B o de B hacia A.

```
       A --__
      /      --
     /         \
    /           \   El giro de A hacia B es a favor del reloj
   /            |
                v
 O  ----------  B

TODO: poner una grafica de verdad (giro a favor del reloj)
```

Por ejemplo, puede servir para verificar si un punto pertenece a un triangulo. El punto P pertenece a un triangulo ABC si y solo si los tres siguientes giros son en contra del reloj: 

- El giro de B hacia P, con centro en A
- El giro de C hacia P, con centro en B
- El giro de A hacia P, con centro en C

```
                                      B                                         
                                   .                                            
                                         .        P2                            
                              .                                                 
                                                                                
                         .              P1    .                                 
                      .                                                         
                    C  .                                                        
                               .                  .                             
                                         .                                      
                    P3                              . A                         

TODO: poner un grafica de verdad (punto en triangulo)
```

- El punto P1 respeta los tres giros
- El punto P2 no respeta el giro con centro en A
- El punto P3 no respeta el giro con centro en C

Aparte, la nocion de giro a favor/en contra del reloj es fundamental para implementar la mayoria de algoritmos de geometria computacional, como los diversos algoritmos que calculan la capsula convexa.

En C++ podemos declarar la funcion con este tipo de datos:

```
bool cw(pt o, pt a, pt b);  // responde si el giro de a hacia b con centro en o es a favor del reloj
bool ccw(pt o, pt a, pt b); // responde si el giro de a hacia b con centro en o es en contra del reloj
```

Esto nos puede despertar varias preguntas. Por ejemplo, que es el tipo de datos `pt`?

```
struct pt { int x, y; };
```

- suma de puntos

```
pt operator + (pt a, pt b) {
  return {a.x + b.x, a.y + b.y}:
}
```

- suma de vectores "graficamente" y "algebraicamente"

```
                flecha A
                  ____--->C
             B----       ^
            ^           /  flecha B
flecha B   /           /
          /   ____--->A
         x----           
            flecha A

TODO: poner una grafica de verdad (suma de vectores)
```

- diferencia de vectores "cuanto le falta a A para llegar a B", "distancia en linea recta"

```
pt operator - (pt a, pt b) {
  return {a.x - b.x, a.y - b.y}:
}
```

- Interesante porque podemos converir la pregunta `ccw(o,a,b)` (una pregunta sobre tres elementos) a una pregunta sobre `foo(o-a,o-b) (una pregunta sobre solo dos elementos)

- longitud (pitagores)

```
double len(pt p) {
  return sqrt(p.x*p.x + p.y*p.y);
}

// otra opcion que ofrece C++
double len(pt p) { return hypot(p.x, p.y); }
```

- producto escalar "que tan paralelos son dos vectores"

```
int dot(pt a, pt b) {
  return a.x * b.x + a.y * b.y;
}
```

- Positivo cuando el angulo es menor a 90
- Nulo cuando el angulo es exactamente 90
- Negativo cuando el angulo es mayor a 90

- Formula `dot(a,b) = len(a) * len(b) * coseno(angulo entre a y b)`

- rotacion de 90 grados

```
pt girar(pt a) {
  return {-a.y, a.x};
}
```

- "que tan perpendiculares son dos vectores, y para que lado es el giro"

```
pt det(pt a, pt b) {
  return dot(girar(a), b);
}
```

- determinante o producto vectorial

```
int det(pt a, pt b) {
  return a.x * b.y - a.y * b.x;
}
```
