Vamos a ver un poquito sobre la línea de comandos. Shell, terminal, consola, ... - técnicamente todas esas palabras son cosas disintas pero no nos vamos a meter en los detalles. Por ahora solo nos interesa afianzarnos con usar la línea de comandos.

La línea de comandos es una interfaz basada en texto. Nos permite interactuar con la computadora escribiendo comandos y obteniendo una respuesta. Algunos comandos importantes:

+ `pwd`: (print working directory): muestra el directorio en el cual estamos parados
+ `cd DIR`: (change directory) nos hace movernos hacia el directorio `DIR`
+ `ls`: (list) muestra los archivos y directorios que están en el directorio actual
+ `cat FILENAME`: (concatenate) muestra el contenido de un archivo
+ `cp FROM TO`: (copy) crea una copia del archivo `FROM` llamada `TO`
+ `mv FROM TO`: (move) mueve el archivo `FROM` a la ubicación `TO` (se puede usar para renombrar archivos también)
+ `g++ programa.cpp -o programa`: compila el archivo `programa.cpp`, produciendo un ejecutable llamado `programa`

Otras cosas importantes:
+ `Ctrl+L` típicamente limpia la pantalla
+ Usar las flechas de arriba y abajo típicamente muestra los últimos comandos ejecutados
+ `./programa` ejecuta el archivo ejecutable `programa`
+ `Ctrl+C` típicamente detiene el programa/comando que actualmente está corriendo (útil si nuestro programa entra en un bucle infinito)

Además podemos crear "scripts" - archivos conteniendo una secuencia de comandos para correr. Por ejemplo, se creamos un archivo `compilar.sh` con el siguiente contenido:
```
g++ programa.cpp -o programa
./programa
```
y en la consola escribimos
```bash
chmod +x compilar.sh # para hacerlo ejecutable
./compilar.sh 
```
se va a compilar y correr el programa `programa.cpp`.

La mejor forma de aprender a usar la consola es jugando y googleando los errores con los que nos encontramos (vale para muchas cosas en la vida). Algunas cosas más para investigar:
+ `chmod`
+ `clear`
+ pasarle "banderas" a comandos - e.g.: `cp -r DIR1 DIR2` hace que `cp` copie todo el contenido de la carpeta `DIR1` a una nueva carpeta `DIR2`
+ el programa `make` - e.g.: `make programa.cpp`