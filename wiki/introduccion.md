# ¿Qué es OIA?

OIA es la Olimpíada Informática Argentina, la rama Argentina de la International Olympiad in Informatics (IOI).

OIA tiene 4 etapas, culminando en la final mundial de IOI. Para clasificar a cada etapa se toma en cuenta la posición obtenida en la etapa anterior.

- Certamen Jurisdiccional (participa toda la Provincia de Santa Fe, separado por edad)
- Certamen Nacional (participa toda Argentina, separado por edad)
- Certamen de Selección (participa toda Argentina, sin separar por edad)
- Certamen Mundial (participa todo el mundo, sin separar por edad)

## Competencia

En OIA es una competencia de programación donde cada problema puede otorgar un
máximo de 100pts.

Para obtener este puntaje, el participante debe enviar el código fuente de un
programa que solucione los casos de prueba (que son secretos) de forma correcta
y con un rendimiento adecuado. (o sea, hay que codear un programa que ande
"bien", "rápido" y use "poca" memoria)

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

