
# Puntaje

La OIA es una competencia de programación donde cada problema puede otorgar un
máximo de 100pts.

Para obtener este puntaje, el participante debe enviar el código fuente de un
programa que solucione los casos de prueba (que son secretos) de forma correcta
y con un rendimiento adecuado. (o sea, tiene que andar "rápido" y usar "poca"
memoria)

Si la solución de un participante no cumple con los requisitos del problema
puede recibir puntaje parcial o no recibir ningún punto. En estos casos el
sistema corrector (le decimos "el juez") da un veredicto que indica por qué no
se otorgaron más puntos:

- CE/error de compilación: el código enviado no compila
- WA/respuesta incorrecta: el programa enviado no resuelve correctamente algunos
  casos
- RTE/error de ejecución: el programa enviado experimenta un error al ejecutar
  (suele ser el famoso segfault)
- TLE/límite de tiempo excedido: el programa enviado tarda demasiado tiempo en
  ejecutar
- MLE/límite de memoria excedido: el programa enviado usa demasiada memoria

Cada problema define condiciones especificas que determinan cómo se asigna el
puntaje parcial, pero algunas cosas son siempre iguales:

- El problema se divide en subtareas, que son versiones especializadas y más
  faciles del problema, donde cada una aporta una cantidad de puntos menor a
  100
- Si se envia una solución que obtiene puntos en una subtarea, esos puntos se
  mantienen permanentemente
- Los 100 puntos se obtienen resolviendo todas las subtareas

Por ejemplo: Primero se envia una solución que obtiene 15pts en la subtarea 1, y
0 en todas las demás. Después se envía una solucion que obtiene 15pts en la
subtarea 2, y 0 en todas las demás. En este caso se obtiene un total de 30pts.

# Estrategia

Mas allá del conocimiento de teoría, hay varias cosas que está bueno saber a la
hora de participar en OIA para divertirse más, sacar más puntos y sufrir menos
los nervios. Acá se explican algunas de esas cosas.

## Aprovechar las subtareas

Normalmente es mucho más fácil sacar 15 puntos en la subtarea más fácil de un
problema que sacar los ultimos 15 puntos en un problema en el que ya sacamos 85,
**incluso si ya descubrimos la idea para sacar esos puntos**.

Aparte, si nos tomamos 10 minutos para meter 15 puntos fáciles después podemos 
olver e intentar sacar los puntos más dificiles. En cambio, la implementación de
100 puntos para un problema puede tener partes complejas, que cometamos errores,
y al final nos quedemos sin tiempo incluso para meter los 15 puntos puntos
fáciles de otro problema.

En conclusión: aunque puede ser muy dificil, hay que aguantar la tentación y
siempre **robar puntos**.

## Hacer dibujos

Una de las herramientas mas potentes del cerebro humano es la capacidad de
reconocer patrones y relaciones visualmente. Para aprovechar esto, está bueno
hacer muchos dibujos y diagramas. Algunas ideas:

- Dados dos arrays de longitud N, interpretar los elementos de uno como
  coordenadas-x, y los del otro como coordenadas-y en el plano cartesiano
- Dado un [grafo]( grafos ), dibujarlo
- Dado un arbol, dibujarlo como un camino largo (un diámetro), y varias ramas
  chicas que le cuelgan
- Dado un arbol dibujar los nodos ordenados de izquierda a derecha en pre-orden
- Dibujar los estados de una [DP]( dp ) y sus transiciones como un grafo

> Arriba se mencionan temas de teoría, asi que está bueno releer esta sección
> después de aprender un tema nuevo.

## Frenar los nervios

En una prueba muchas veces nos podemos poner nerviosos, cansarnos o simplemente
tener un mal estado de ánimo. Algunas ideas para combatir estos efectos:

- Tomar agua durante la competencia (la deshidratación en una prueba de 4 o 5
  horas es muy real)
- Ir al baño durante la competencia (alejarse un rato ayuda a bajar los nervios,
  aparte hace falta si se toma mucha agua)
- Hacer competencias en internet para acostumbrarse