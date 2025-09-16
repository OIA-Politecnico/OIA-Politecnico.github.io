
# Treap / Arbol cartesiano

Queremos una estructura de datos para representar secuencias, que soporte las
siguientes operaciones de forma eficiente:

- `split(s, k)`: divide la secuencia s en dos, la primera tiene los k primeros
  elementos y la segunda el resto.
- `merge(s, t)`: concatena s y t.

La idea principal es usar una estructura de arbol, donde el recorrido en inorden
nos da la secuencia.

En otras palabras, si tenemos un arbol t

       x
     /  \
    L    R

La secuencia representada por el arbol es

    inorden(t) = inorden(L) + [x] + inorden(R).

```cpp

struct node {
	int val;
	int tam;

	node* l;
	node* r;
};

// crea una secuencia con un solo elemento
node* make(int val) {
	return new node { val, 1, nullptr, nullptr };
}

// longitud de la secuencia
int tam(node* n) { return n ? n->tam : 0; }

void recalc(node* n) {
	n->tam = tam(n->l) + 1 + tam(n->r);
}

```

## Split

Recordemos que conceptualizamos el arbol como una secuencia.

Donde, 

    inorden(t) = inorden(L) + [x] + inorden(R).

Entonces, si queremos cortar la secuencia en dos, tenemos dos casos:

- si el corte es antes del elemento x, entonces tendriamos que cortar la
  secuencia L.
- si el corte es despues del elemento x, entonces tendriamos que cortar la
  secuencia R.

Por ejemplo, si

    inorden(t) = [1, 2, 3] + [5] + [7, 8, 9]
	              0  1  2     3     4  5  6

Entonces si queremos cortar la secuencia entre los indices 1 y 2, entonces vamos
a tener que cortar la secuencia L en [1, 2] y [3] (usando recursión), y devolver
dos partes:

- la parte antes del corte: [1, 2]
- la parte despues del corte: [3] + [5] + [7, 8, 9]

En cambio, si queremos cortar la secuencia entre los indices 4 y 5, entonces
vamos a tener que cortar la secuencia R en [7] y [8, 9] (usando recursión), y
devolver dos partes:

- la parte antes del corte: [1, 2, 3] + [5] + [7]
- la parte despues del corte: [8, 9]

En este segundo caso hay que tener cuidado con los indices:

    inorden(t) = [1, 2, 3] + [5] + [7, 8, 9]
	indices en t: 0  1  2     3     4  5  6
	indices en L: 0  1  2
	indices en R:                   0  1  2

Como vemos, el indice 4 en t, corresponde al indice 0 en R. Esto viene de que
hay 3 elementos en L, y 1 elemento raiz en t, 4 en total.

O sea, si queremos cortar la secuencia en el indice k, y este cae en la parte
de la derecha, entonces el indice en R es k - tam(L) - 1.

El algoritmo está implementado a continuación, y tiene complejidad O(altura del
arbol).

Observacion: split se puede generalizar para que particione la secuencia segun
un predicado binario.

```cpp

pair<node*, node*> split(node* s, int k) {
	if (s == nullptr) return {nullptr, nullptr};
	if (tam(s->l) < k) {
		auto [l, r] = split(s->r, k-tam(s->l)-1);
		s->r = l;
		recalc(s);
		return {s, r};
	} else {
		auto [l, r] = split(s->l, k);
		s->l = r;
		recalc(s);
		return {l, s};
	}
}

```

## Merge

La siguiente operación es la inversa de la anterior, merge.

Dadas dos secuencias s y t, merge devuelve una secuencia que resulta de concatenar
s y t.

Supongamos que tenemos dos arboles s y t:

       x          x'
     /  \        /  \
    L    R      L'   R'

Que representan las secuencias:

    inorden(s) = inorden(L) + [x] + inorden(R)
    inorden(t) = inorden(L') + [x'] + inorden(R')

El objetivo es combinarlos en un solo arbol, que represente la secuencia:

	  inorden(s)                    + inorden(t)
    = inorden(L) + [x] + inorden(R) + inorden(L') + [x'] + inorden(R')

Para combinarlos en un solo arbol, tenemos que elegir un nodo como raiz.

Por ejemplo, tomemos x como raiz. En ese caso, lo unico que puede ir a la
izquierda de la raiz es L.

       x
     /  \
    L    ?

Pero ¿qué puede ir a la derecha de x?

En la secuencia resultante, R y t (que esta compuesto por L', x' y R') deben ir a
la derecha de x, en ese orden.

Por lo tanto, podemos poner la concatenacion de R y t a la derecha de x.

       x
     /  \
    L    merge(R, t)

Siguiendo esta idea, la implementación es la siguiente:

```cpp

node* merge(node* s, node* t) {
	if (s == nullptr) return t;
	if (t == nullptr) return s;
	s->r = merge(s->r, t);
	recalc(s);
	return s;
}

```

Es fácil ver que la operación merge tiene complejidad O(altura del arbol).

Sin embargo, no hay nada que nos asegure que el arbol va a estar balanceado.

## Balanceo con prioridades

Una mejora seria elegir el nodo raiz de manera aleatoria.

```cpp

node* merge(node* s, node* t) {
	if (s == nullptr) return t;
	if (t == nullptr) return s;
	if (rand()%2 == 0) {
		s->r = merge(s->r, t);
		recalc(s);
		return s;
	} else {
		t->l = merge(s, t->l);
		recalc(t);
		return t;
	}
}

```

Una idea un poco mejor seria agregar un prioridad a cada nodo, y elegir el nodo
de mayor prioridad como raiz.

Resulta que, si la prioridad de cada nodo es aleatoria, entonces el arbol va a
estar balanceado con alta probabilidad.

```cpp

struct node {
	int val;

	int prio;

	int tam;
	node* l;
	node* r;
};

// crea una secuencia con un solo elemento
node* make(int val) {
	return new node { val, rand(), 1, nullptr, nullptr };
}

node* merge(node* s, node* t) {
	if (s == nullptr) return t;
	if (t == nullptr) return s;
	if (s->prio > t->prio) {
		s->r = merge(s->r, t);
		recalc(s);
		return s;
	} else {
		t->l = merge(s, t->l);
		recalc(t);
		return t;
	}
}

```

# Sumas en rango

Otra mejora que podemos agregar es mantener la suma de los valores de la
secuencia (o cualquier operacion asociativa).

Para esto, basta con agregar un campo en el nodo que guarde la suma de los
valores de la secuencia y modificar la funcion de recalculo.

```cpp

struct node {
	int val;
	int sum;

	int prio;
	int tam;

	node* l;
	node* r;
};

// crea una secuencia con un solo elemento
node* make(int val) {
	return new node { val, val, rand(), 1, nullptr, nullptr };
}

void recalc(node* n) {
	n->tam = tam(n->l) + 1 + tam(n->r);
	n->sum = n->val + sum(n->l) + sum(n->r);
}

```

Ahora podemos hacer consultas de suma de la secuencia completa.

```cpp

int sum(node* n) {
	return n ? n->sum : 0;
}

```

Para calcular la suma de un subarreglo, basta con hacer usar split para obtener
la parte que nos interesa, y luego tomar la suma.

Como el arbol se modifica, despues hay que volver a unirlo.

```cpp

int range_sum(node* n, int i, int j) {
	auto [n_, r] = split(n, j);
	auto [l, md] = split(n_, i);
	int res = sum(md);
	merge(merge(l, md), r);
	return res;
}

```

## Lazy propagation

Otra mejor es agregar lazy propagation.

Aparte de todas las mismas operaciones que soporta un segment tree, tambien
podemos soportar algunas permutaciones de la secuencia.

Por ejemplo, podemos hacer actualizaciones que reviertan el orden de los elementos
de un subarreglo.

> TODO: mostrar como se hace

```cpp

```

## Secuencias ordenadas

Aparte de secuencias arbitrarias, tambien podemos representar secuencias
ordenadas.

Para lograr una insercion en O(log n), podemos usar una version modificada de
split que nos permite particionar la secuencia entre los elementos menores a x
y los mayores o iguales a x.

La lógica es casi la misma, pero en vez de usar un indice k, usamos el valor x.

```cpp

pair<node*, node*> split_key(node* s, int x) {
	if (s == nullptr) return {nullptr, nullptr};
	if (s->val < x) {
		auto [l, r] = split_key(s->r, x);
		s->r = l;
		recalc(s);
		return {s, r};
	} else {
		auto [l, r] = split_key(s->l, x);
		s->l = r;
		recalc(s);
		return {l, s};
	}
}

node* insert(node* s, int x) {
	auto [l, r] = split_key(s, x);
	return merge(merge(l, make(x)), r);
}

bool contains(node* s, int x) {
	auto [l, r] = split_key(s, x);
	auto [m, r_] = split(r, 1);
	bool res = m != nullptr && m->val == x;
	merge(l, merge(m, r_));
	return res;
}

```

Observacion: Si la secuencia esta ordenada, entonces el arbol se convierte en un
arbol binario de busqueda.

contains se puede optimizar aprovechando este hecho.

insert tambien se puede optimizar, pero la implementacion de arriba es mas
sencilla y bastante mas corta.

```cpp

bool contains(node* s, int x) {
	if (s == nullptr) return false;
	if (s->val < x) return contains(s->r, x);
	if (s->val > x) return contains(s->l, x);
	return true;
}

```
