
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script src="mathjax-config.js"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# MathJax

Se pueden embeber scripts en Github Pages. En particular, para embeber MathJax hay que poner esto en cualquier parte del markdown (yo lo pongo al principio)

    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script src="mathjax-config.js"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

Despues se puede usar para escribir bloques de formulas usando `$$ formula en LaTeX $$` o `\\[ formula en LaTeX \\]` (sí, doble backslash). Por ejemplo:

\\[ \frac{a}{b} \\]

El codigo se puede escribir de estas dos formas:

    \\[ \frac{a}{b} \\]

    $$ \frac{a}{b} $$

Tambien se puede usar para escribir formulas "inline" usando `\\( formula \\)`.

Ejemplo: \\(a \leq b\\).

Codigo: `\\(a \leq b\\)`.

## Formulas alineadas

Dentro de un bloque de formula `$$...$$` se puede usar `\begin{aligned} ... \end{aligned}` con el markador `&` para escribir formulas alineadas (anda mal en bloques `\\[...\\]`). Por ejemplo:

$$\begin{aligned}
a & = 3 - b \cdot 77 \\
a + b \cdot 77 & = 3
\end{aligned}$$

Codigo:

    $$\begin{aligned}
    a & = 3 - b \cdot 77 \\
    a + b \cdot 77 & = 3
    \end{aligned}$$
