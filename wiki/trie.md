# Trie

Trie es una estructura para almacenar strings de forma eficiente.

Un Trie es un arbol donde cada subarbol contiene las strings que arrancan con
cada caracter. O sea, en un subarbol están todas las strings que empiezan con
'a', otro tiene las que empiezan con 'b', otro con 'c', etc.

En el segundo nivel del arbol las strings se separan por su segundo caracter, en el tercero por el tercer caracter y así sucesivamente.

Esta estructura nos permite insertar, eliminar y buscar strings en O(N).

El trie sirve para resolver problemas que piden calcular cosas relacionadas a strings que tienen prefijos en común.

## Problemas

- [Oia selectivo 2009 - Formando equipo](https://juez.oia.unsam.edu.ar/task/51)

## Implementación básica

La forma del árbol es suficiente para representar las strings, asi que no hace falta guardarlas explícitamente.

```c++
struct trie {
    map<char, trie> hijos;
    bool es_final = false;

    void insertar(string s) {
        insertar(&s[0]);
    }
    void insertar(char* s) {
        if (*s == '\0') {
            es_final = true;
        } else {
            hijos[*s].insertar(s+1);
        }
    }

    bool contiene(string s) {
        return contiene(&s[0]);
    };
    bool contiene(char* s) {
        if (*s == '\0') {
            return es_final;
        } else {
            return hijos[*s].contiene(s+1);
        }
    }
};
```

# Greedy sobre un trie -- Maximum xor

Trie no sirve solo para hacer la busqueda común, tambien podemos implementar
busquedas mas complejas aprovechando la estructura.

Por ejemplo, dada un numero en binario podemos usar un trie para encontrar el
numero de un conjunto que tiene el maximo xor posible con ese numero.

Para hacer esto representamos los numeros con strings de 0s y 1s y hacemos un
greedy.

```c++
struct trie {
    // ...
    
    void maximizar_impl(char* s, string& salida) {
        char nxt = hijos.count('0') ? '0' : '1';
        if (*s == '0' and hijos.count('1')) nxt = '1';
        salida.push_back(nxt);
        hijos[nxt].maximizar_impl(s+1, salida);
    }
    
    string maximizar(char* s) {
        string salida;
        maximizar_impl(s, salida);
        return salida;
    }
};
```

## DP sobre un trie -- **COMPLETAR**
