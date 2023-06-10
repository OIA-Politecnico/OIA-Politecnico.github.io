
## Puntaje

En la OIA, cada problema puede otorgar un máximo de 100pts.

Para obtener este puntaje, el participante debe enviar una solución que solucione los
casos de prueba (que son secretos) de forma correcta y con un rendimiento adecuado.

Si la solución de un participante no cumple con los requisitos del problema, puede
recibir puntaje parcial, o no recibir ningún punto. En estos casos el juez da un veredicto
que indica por qué no se otorgaron más puntos:

- WA/respuesta incorrecta: el código enviado no resuelve correctamente algunos casos.
- RTE/error de ejecución: el código enviado experimenta un error al ejecutar (suele ser el famoso segfault).
- CE/error de compilación: el código enviado experimenta un error al compilar.
- TLE/límite de tiempo excedido: el código enviado tarda demasiado tiempo en ejecutar.
- MLE/liḿite de memoria excedido: el código enviado usa demasiada memoria

Para determinar el puntaje parcial, cada problema define condiciones distintas pero se
siguen un par de reglas.

Primero, el problema se divide en subtareas, que son versiones
especializadas y más faciles del problema, donde cada una aporta una cantidad de puntos
menor a 100.

Segundo, si se envia una solución que obtiene puntos en una subtarea, esos
puntos se mantienen permanentemente.

Tercero, los 100 puntos se obtienen resolviendo todas las subtareas.

Por ejemplo: Primero se envia una solución que obtiene 15pts en la subtarea 1, y 0 en
todas las demás. Después se envía una solucion que obtiene 15pts en la subtarea 2, y 0
en todas las demás. En este caso se obtiene un total de 30pts.

# Estrategia

Mas allá del conocimiento específico, competir requiere de una serie de habilidades
transversales. Esta sección apunta a armar a un participante con las herramientas
necesarias para afrontar una competencia sin volverse loco, y poder divertirse.

## Subtareas

En general es mala idea apuntar a sacar 100pts en un problema cuando hay
10pts o 15pts que salen fácil en ese u otro problema. Como reglita, solo tendríamos
que ponernos a pensar en el caso general de un problema una vez que tenemos mas de
0pts en todos los problemas.

Matemáticamente, la cuenta es muy fácil. Si esta relacion vale (y ojo que casi siempre vale)

    (probabilidad de sacar 15pts o más) x 15 > (probabilidad de sacar 100pts) x 100

entonces la conclusión es simple: **Hay que robar puntos**.

## Resolución de Problemas

Una de las herramientas mas potentes del cerebro humano es la capacidad de
reconocer patrones y relaciones visualmente. Para aprovechar esto, está bueno
hacer muchos dibujos. Algunas ideas:

- Dado un grafo, dibujarlo.
- Dados dos arrays de longitud N, interpretar los elementos de uno como coordenadas-x, y los del otro como coordenadas-y en el plano cartesiano.
- Dado un arbol, dibujarlo como un camino largo (un diámetro), y varias ramas chicas que le cuelgan.

**nota:** Estas ideas particulares dependen de conocimientos especificos, asique
está bueno releer esta sección después de aprender una técnica nueva.

## Estado Físico y Mental

En una competencia lo que más afecta nuestro rendimiento son los nervios, el cansancio
y el estado de ánimo. Algunas ideas para combatir estos efectos:

- tomar agua durante la competencia (la deshidratación en una competencia de 5 horas es muy real)
- ir al baño durante la competencia (alejarse de la competencia un rato ayuda a bajar los nervios)
- hacer competencias en internet para acostumbrarse