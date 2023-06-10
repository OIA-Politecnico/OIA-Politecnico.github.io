En las olimpíadas se asume acceso a un entorno basado un linux para programar. Con lo cual estaría bueno si se instalan una ditribución de linux (como Ubuntu, por ejemplo) en una computadora para familiarizarse. No obstante, siguiendo los pasos detallados abajo van a poder practicar en windows

###  Instalar programas para compilar C++
+  Instalar MYSYS2 corriendo el instalador disponible acá: https://www.msys2.org/
+  Se crea una aplicación llamada "MYSYS2 UCRT64". Se puede encontrar escribiendo "UCRT64" en el menu de inicio
![1.png](https://user-images.githubusercontent.com/44166492/235012378-d57a5366-22d6-4ad9-b6f3-801e321c2785.png)
+  Abrir el programa. Se abre una terminal/consola
+  Correr `pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain`. Cuando pregunta si desea continuar, escribir "y" y Enter para confirmar
![2.png](https://user-images.githubusercontent.com/44166492/235012841-61fa4f9f-ed02-4e6d-a960-b7d57f8165d9.PNG)
+  Validar que se hayan instalado los programas corriendo `g++ --version`, `gdb --version` y `make --version`
![2.png](https://user-images.githubusercontent.com/44166492/235025817-b22e6a67-41fa-44ff-9999-f09b46abbbb5.PNG)

### Instalar y configurar VSCode
+  Instalar Visual Studio Code corriendo el instalador disponible acá: https://code.visualstudio.com/
+  Instalar la extensión de C/C++ de Microsoft (Ctrl-Shift+X abre el buscador de extensiones)
![4.png](https://user-images.githubusercontent.com/44166492/235027034-0f87d558-3c57-4016-bc86-ec148b7c0ef5.PNG)
+  Hacer Ctrl-Shift+P y escribir "settings.json" para abrir el archivo de configuración de VSCode
+  Agregar el siguiente bloque de código dentro de las llaves que encierran todo (y agregar una coma al final de la línea anterior):
```
    "terminal.integrated.profiles.windows": {
      "MSYS2 UCRT": {
        "path": "cmd.exe",
        "args": [
          "/c",
          "C:\\msys64\\msys2_shell.cmd -defterm -here -no-start -ucrt64"
        ]
      }
    }
```
+  Su settings.json debería verse algo así (Ctrl+S para guardar el archivo):
```
{
    "workbench.startupEditor": "none",
    "editor.minimap.enabled": false,
    "editor.detectIndentation": false,
    "security.workspace.trust.untrustedFiles": "open",
    "explorer.confirmDragAndDrop": false,
    "editor.fontSize": 16,
    "editor.accessibilityPageSize": 12,
    "editor.tabSize": 2,
    "git.mergeEditor": false,
    "workbench.iconTheme": "material-icon-theme",
    "terminal.integrated.profiles.windows": {
      "MSYS2 UCRT": {
          "path": "cmd.exe",
          "args": [
              "/c",
              "C:\\msys64\\msys2_shell.cmd -defterm -here -no-start -ucrt64"
          ]
      }
    }
}
```
+  Abrir una terminal
![5.png](https://user-images.githubusercontent.com/44166492/235029595-96d4edb2-7b8b-4dad-a41f-f4f0e7c05ad2.png)
+  Debería aparecer la opción "MYSYS2 UCRT"
![6.png](https://user-images.githubusercontent.com/44166492/235028863-e51a3a43-d12b-4cf0-8de6-06637356bf8c.png)
+  Voilá, deberían poder correr `g++ miprograma.cpp -o miprograma` y `./miprograma` para compilar y correr
![7.png](https://user-images.githubusercontent.com/44166492/235032601-9735b46f-cc15-4ba3-9696-1ff852dda4a9.PNG)

Ejemplo de un setup para codear:
+  Makefile: define compilador y banderas de compilación (flags) a usar
```
CPPFLAGS = -std=c++17 -Wall -g
CC = g++
```
+  comp.sh: script que compila y devuelve las primeras N lineas de error, e.g.: `./comp.sh main 10`
```
rm -f $1
clear
make $1 2>&1 | head -$2
```
+  run.sh: script que compila y corre el programa, usando un archivo como input, e.g.: `./run.sh main input.txt`
```
rm -f $1
clear
make $1 && ./$1 < $2
```