# CSS

Para referenciar el archivo de estilos de css tenemos que escribir en html `<link rel="stylesheet" href="">` donde `href` es la ruta hacia el archivo de estilo de css.

## Selectores

- `*` :  **Selector universal**. ejemplo:
```css
* {
    color: #ab32de;
}
```

- `h1` : **Selector de tipo(elementos)**, es decir que se refiere a la etiqueta misma. Ejemplo:
```css
h1 {
    color: red;
}
```

- `.titulo` :  **Selector por clase**, se le agrega un atributo llamado `class` en el codigo de html y en el archivo de css se hace la referencia poniendo el mismo nombre de la clase con un punto`.` al principio. Ejemplo:
```html
<!-- > Este el es el codigo de html <-->
<h2 class="titulo">Este es un titulo</h2> 
```
```css
/* Este es el codigo de css */
.titulo {
    color:red;
}
```

- `#elemento` : **Selector por id**, es algo similar al selector por clase, solamente que en lugar de una `class` es un `id` (esto en el archivo de html), en el archivo de css en lugar de iniciarlo con un punto es con el signo `#`, pero en esta ocacion los `id` tienen que ser unicos.Ejemplo:
```html
<!-- > Este el es el codigo de html <-->
<h2 id="elemento">Este es un titulo</h2> 
```
```css
/* Este es el codigo de css */
#elemento {
    color:red;
}
```

- `[rancio="si"]` : **Selector por atributo**. En este caso se crea un atributo en html (puede ser cualquier atributo) y lo copiamos tal cual en el archivo de css solo que dentro de conchetes.Ejemplo:
```html
<!-- > Este el es el codigo de html <-->
<h2 rancio="si">Este es un titulo</h2> 
```
```css
/* Este es el codigo de css */
[rancio="si"] {
    color:red;
}
```

- `h2 p` : **Selector por descentiente**. Si queremos modificar una etiquete que se encuantre dentro de otra sin modificar las demas del mismo tipo entonces podemos usar el selector por descendiente, en este ejemplo se muestra como se cambiara de color solo a las etiquetas `p` que se encuentren dentro de un `h2`. Tambien se puede hacer con clases:
```html
<!-- > Este el es el codigo de html <-->
<h2><p>Este es un titulo</p></h2> 
<p>hola</p>
<h2 class="clase-de-b"><b>jshabfjhbfus</b></h2>
```
```css
/* Este es el codigo de css */
h2 p {
    color:red;
}

.clase-de-b b {
    color: blue;
}
```

- `p:hover` : **Selector por pseudo-clase**. Cuando pasemos el mouse sobre el elemento `p` se va  aponer de color rojo.Tambien podemos hacerlo de manera descendiente.Ejemplo:
```html
<!-- > Este el es el codigo de html <-->
<h2><p>Este es un titulo</p></h2> 
<p>hola</p>
<h2 class="clase-de-b"><b>jshabfjhbfus</b></h2>
```
```css
/* Este es el codigo de css */
p:hover {
    color:red;
}

.clase-de-b b:hover {
    color: blue;
}
```
```
# lista de pseudi-clases
:active
:checked
:default
:dir()
:disabled
:empty
:enabled
:first
:first-child
:first-of-type
:fullscreen
:focus
:hover
:indeterminate
:in-range
:invalid
:lang()
:last-child
:last-of-type
:left
:link
:not()
:nth-child()
:nth-last-child()
:nth-last-of-type()
:nth-of-type()
:only-child
:only-of-type
:optional
:out-of-range
:read-only
:read-write
:required
:right
:root
:scope
:target
:valid
:visited

```

- `selector::pseudo-elemento { propiedad: valor; }` : **Pseudoelementos** nos permiten agregar elementos a la etiqueta, permiten añadir estilos a una parte concreta del elemento seleccionado. (Se activa con "::" despues de la etiqueta)). Lista de Pseudoelementos:
```
::after
::before
::first-letter
::first-line
::selection
::backdrop
::placeholder
::marker
::spelling-error
::grammar-error
```

## Especificidad

jerarquía | Selector | ejemplo
------|----------
1 | `important` | `c {color:red !important}`
2 | `estilos en linea(en el codigo de html` | `<h1 style="color:red">`
3 | `identificadores` | `#id {}` 
4 | `clases` | `.clase {}`
4 | `pseudo-clases` | `.clase p:hover {}`
4 | `atributos` | `[rancio="si"] {}`
5 | `elementos` | `a {}`
5 | `pseudo-elementos` | `selector::pseudo-elemento { propiedad: valor; }`

Cuando usamos selectores de la misma jerarquia entonces el que esta mas abajo es el que se queda. Ejemplo:
```css
a {
    color: red
}

a {
    color: blue
}
/* En este caso el color que se quedaria es el azul por que es el que esta abajo */
```
Sin embargo si usamos selectores de jerarquias diferentes entonces gana el que tenga la jerarquia mas alto.

## Metodologia BEM
La Metodologia Bem es una metodologia que consiste en evitar seleccionar muchas clases y evitar generar conflctos entre estas. queriendo conocer que elementos estamos seleccionando de manera mas rapida apartir de las clases.

Lo que haremos en la metodologia Bem es nombrar de manera eficiente las clases. En esta ocacion la clase de un div se llama `form` y dento de este existen dos input a los cuales sus clases los nombraremos con el mismo `from` del div pero agregandole dos guiones bajos y despues el nombre del elemento. ESto se hace pos secciones.Ejemplo:
```html
<div class="form">
    <input type="text" class="form__input">
    <input type="password" class="form__input">
</div>
```
En dado caso de que tengamos demaciados elementos iguales para diferenciarlos agregaremos dos guiones medios y una frace, en este caso usaremos la palabra `active`, con esto lograremos diferenciar un elemento del resto de manera mas eficiente.Ejemplo:
<div class="form">
    <input type="text" class="form__input--active">
    <input type="text" class="form__input">
    <input type="text" class="form__input">
    <input type="text" class="form__input">
    <input type="text" class="form__input">
    <input type="password" class="form__input">
</div>
```
Si contamos con mas aelmento adentro de una seccion siempemente tenemos que agregar un guion medio y el nombre del elemeto.Ejemplo:
<div class="form">
    <p class="form__p">
        <input type="text" class="form__p-input">
    </p>
</div>
```

## Teoria de las medidas
En css se tiene dos unidades de medida las **relativas** y las **definidas**.

Para sacar el valor por defecto que tiene el navegador usaremos:
```css
* {
    padding: 0px;
    margin: 0px;
}
```

### Medidas relativas
Adiferencia de las meidas definidas estas medidas relativas pueden adaptarse al tama;o de la caja, si se hace ams grande o mas peque;a.
- rem
- em
- vw (-) 
- vh (|)

**100vw** es el ancho de toda la pantalla entera. 
**100vh** es es el largo de toda la pantalla. 
Ejemplo:
```css
.form {
    background-color: #000;
    width: 50vw;
    height: 50vh;
}
```

Por defecto **1em** es igual a 16px(lo decide el navegador).
Pero este valor se puede cambiar dependiendo del valor de la caja contenedora ya que se hereda. Ejemplo:
```css
.form {
    font-size: 25px
}
.form__h2 {
    font-size: 5em;
    /* Ahora que su caja contenedora vale 25px entonces `1em` vale 25px y como estamos usando `5em` entonces la letra medira 125px  */
}
```

### Medidas definidas
Si defines un tipo de letras con medidas definidas cuando trate de adaptar el sitio a dispositivos moviles el tama;o de la letra seguira igual de grande y puede resultar molesto para el consumidor.
- px
- cm 
- mm 
- pt

## Propiedasdes de texto

- `font-size` : es la propiedad en css que nos permite cambiar el tama;o de la letra.

- `font-family`: Es la tipografia(tipo de letra)

- `line-height`: El line height nace del centro de la letra(el tama;o del contenedor). 1 Line height = 1/2 del tama;o de la letra hacia arriba + 1/2 del tama;o de la letra hacia abajo.

- `font-weight`:  el grosor de la letra va de 100 a 900.

- `text-aling`: si tiene la propiedad `center` entrara el texto al largo de la caja.
### Explortar tipografias
Para ello visitaremos [Google fonts](https://fonts.google.com/ "Google fonts")

## Nomalize css
El navegador te pone todas las propiedades por defecto de cada uno de los elementos, pero aveces tenemos cuestiones en los cuales los navegadores no son tanbuenos por ejemplo el padding

De manera mas rapida podemos buscar un [normalize .css](https://necolas.github.io/normalize.css/ "normalize .css") en google y descargarlo.

## Box

Has dos tipos de cajas. 

- Cajas que son el linea.
El tama;o depende del contendio que contiene.
A los elementos en linea no se les pueda dar `height` ni `width`.

- Cajas que son en bloque.
Siempre se ajustan al ancho de su contenedor.
A los elemenos en bloque si se les pueda dar `height` y `width`.

### box model


### propiedades de cajas

- `display` : nos permite cambia el comportamiento de las cajas. nos permite hacer que las cajas en bloque se comporten como cajas en linea. Ejemplo:
```css
h2 {
    display: inline;
}
```
- `padding` : ES la distancia que existe entre el texto y los bordes de la caja.
```
padding-top: arriba
padding-bottom: abajo
padding-left: izquierda
padding-rigth: derecha
padding: si ponemos solamente un valor entonces aplicara a los 4 lados por igual.
pading: top-bottom righ-left;
pading: top righ-left bottom;
padding: top rigth bottom left; 
```
 
- `height`: alto

- `width`: ancho

- `box-sizing`: si tiene la propiedad `content-box` el height y el width se le sumaran al padding. Si tiene la propiedad `` haremos que el ancho y el largo total de la caja sean los valores del height y el width.

- `margin`: es la distancia que existe entre dos cajas.
```
margin-top: arriba
margin-bottom: abajo
margin-left: izquierda
pmargin-rigth: derecha
margin: si ponemos solamente un valor entonces aplicara a los 4 lados por igual.
margin: top-bottom righ-left;
margin: top righ-left bottom;
margin: top rigth bottom left; 
```

- `border-radius`: redonderar los bordes

- `border`: en border le podemos poner 3 propiedades.Ejemplo:
```css
*{
    border: 4px solid blue;
/*  border: tama;o estilo color */
}
```

- `line-height`: es lo que se tiene en el texto, que viene siendo el `content`.

- `box-shadow`: nos permite ponerle sobra a la caja.ejemplo:
```css
* {
    box-shadow: 2px 4px 15px 0 #000;
/*  box-shadow: ejex ejey tama;o_del_desenfoque borde color */
}
/* Para duplicar el efecto podemos separarlo por comas para que se mas intenso */
* {
    text-shadow: 2px 4px 15px #000, 2px 4px 15px 0 #000, 2px 4px 15px 0 #000;
/*  box-shadow: ejex ejey tama;o_del_desenfoque color */
}
```

- `text-shadow`: nos permite ponerle sobra a las letras.Ejemplo:
```css
* {
    text-shadow: 2px 4px 15px #000;
/*  box-shadow: ejex ejey tama;o_del_desenfoque color */
}
/* Para duplicar el efecto podemos separarlo por comas para que se mas intenso */
* {
    text-shadow: 2px 4px 15px #000, 2px 4px 15px #000, 2px 4px 15px #000
/*  box-shadow: ejex ejey tama;o_del_desenfoque color */
}
```

- `transform`: si le agregamos la propiedad `rotate` podemos rotar.Ejemplo:
```css
* {
    transform: rotate(90deg);
/*  transform: rotate(grados de rotacion); */
}
```

1:53