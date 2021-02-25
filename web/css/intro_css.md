# CSS

Para referenciar el archivo de estilos de css tenemos que escribir en html `<link rel="stylesheet" href="">` donde `href` es la ruta hacia el archivo de estilo de css.

En css le podermos dar atributos a uno o mas selectores al mismo tiempo.Ejemplo:
```css
/* un solo selector */
.caja {}

/* dos selectores */
.caja1, .caja2 {}
```

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
# lista de pseudi-clases mas comunes:
Hay pseudo-clases que no funcionan en div pero `:hover` si funciona en block e inline.

:hover   : lo que hace es escuchar el elemento cuando ponemos el mouse encima.
:link    : cambia de color cuando visitamos un link.(su nivel de gerarquia esta arriba de las clases y por debajo de un id)
:visited : es para cambiar de color los links visitamos cuando usamos la pseudo-clase `link`.(su nivel de gerarquia esta arriba de las clases y por debajo de un id)
:active  : Cuando demos click ocurre el efecto indicado(para cambiar de color se usa el `background`)
:focus   : lo mismo que `active` pero con input.
:lang   : es una funcion de reconocimiento de lenguaje.Ejemplo: .caja b:lang(en){background: red;}

sin embargo tambien tiene que tener la propiedad en html para que funcione.Ejemplo:
<div class="caja">
    <b lang="en">
        hellow how are you
    </b>
<div>
```


- `selector::pseudo-elemento { propiedad: valor; }` : **Pseudoelementos** son elementos que no son elmentos. Unos permiten agregar elementos a la etiqueta, permiten añadir estilos a una parte concreta del elemento seleccionado. (Se activa con "::" despues de la etiqueta)). Lista de Pseudoelementos:
```
:: first-line     |  block (no funcionan en inline)
:: first-letter   |  block (no funcionan en inline)
:: placeholder    
:: after          |  hijos - content (necesario) - inline
:: before         |  hijos - content (necesario) - inline
:: selection
```
- `:: first-line` : modifica la primera linea de un texto.Ejemplo:
```css
.texto::first-line {
    color: blue;
    font-size: 2em;
}
```
- `::first-letter` : modifica la primer letra.

- `::placeholder` : lo entontramos en el `input type="text"` del html y nos permite agregar estilo a un texto dentro del input.Ejemplo:
```html
<body>
    <input type="text" placeholder="aquiva un texto cualquiera">
<body>
```
```css
input::placeholder {
    color: red;
}
```
- `::selection`: cuando seleccionamos un texto con el mouse y el texto se subraya con azul y las letras se vuelven blancas, eso es el selection.Se comporta como un elemento inline.

- `::before`: cuando aplicamos un seudo-elemnto before lo que estamos haciando es creando un hijo del elemento al que le estamos aplicando el seudo-elemento.Lo que se puede hacer con el before es poder escribir un texto el cual ocupara un espacio (en este caso antes de la letra 'a' que se escribio en el html).Ejemplo:
```html
<body>
    <b>
        a
    </b>
</body>
```
```css
    b::before {
        content: "me suscribi"
    }
```
Una particularidad es que en la pagina no se puede subrayar el seudo-elemento.

- `::after` : es lo mismo que el `before` solo que en lugar de escribirlo antes de la letras 'a' se escribira despues.Ejemplo:
```html
<body>
    <b>
        a
    </b>
</body>
```
```css
b::before {
        content: "me suscribi";
        color: #fff;
}

b::after {
    content: "un canal de youtube";
    color: red;psps
}

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

- `box-sizing`: si tiene la propiedad `content-box` el height y el width se le sumaran al padding. Si tiene la propiedad `border-box` haremos que el ancho y el largo total de la caja sean los valores del height y el width. 

- `margin`: es la distancia que existe entre dos cajas.
`margin: auto` nos permite centar los elementos cuando trabamos con bloques y que no estan posicionados( esto quiere decir que  arriba y abajo no tendran modificacion y en los costados se daran medidas igual para que se centre la caja)

```
margin-top: arriba
margin-bottom: abajo
margin-left: izquierda
margin-rigth: derecha
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

- `outline` : A diferencia del border, el outline no ocupa un espacio real y tampoco afecta a las demas cajas.Tambien se usa para remarcar cajas.Ejemplo:
```css
*{
    outline: 4px solid blue;
/*  outline: tama;o estilo color */
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

- `opacity`: Es la transparencia y sus valores van del 0 al 1.

## z index
z index es orden en que se muestran las cosas (en cuanto a profundidad se refiere), cuando tenemos dos cajas en el mismo espacio, la caja que tenga un `z inde` mas alto es la que se ordenara primero, eso quiere decir que esa caja se mostrara al frende y las demas cajas que tengas un `zindex` mas caja se ordenaran detras de esta.
El `z index` solamente funciona cuando las cajas estan posicionadas, si las cajas no estan posicionadas el `z index` no funciona.
Ejemolo:
```html
<!-- > Codigo de html para ejemplo <-->
<body>
    <div class="caja1">caja1</div>
    <div class="caja2">caja2</div>
    <div class="caja3">caja3</div>
    <div class="caja4">caja4</div>
</body>
```
```css
/* Condigo de css para ejemplo */
div{
    width: 120px;
    height: 120px;
    display: block;
}

.caja1 {
    background-color: red;
}

.caja2 {
    background-color: green;
    position: relative;
    top: 60px;
    left: 20px;
    z-index: 1; /*este atributo permite que la caja2 se ponga sobre la caja3, si lo quitamos entonces la caja2 quedara abajo de la caja3 */
}

.caja3 {
    background-color: blue;
    position: relative;
}

.caja4 {
    background-color: yellow;
}

```
La recomendaciones que exista una diferenecia de 100 entre las cajas que tengan `z-index` esto por si queremos poner mas cajas en el medio no existan promblemas.

### Conflicto de z-index
En contenedor padre siempre estara por atras del contenedor hijo. La unica forma que existe de que el contenedro padre este por ensima del contedor hijo es:
```html
<!-- > Codigo de html para ejemplo <-->
<body>
    <div class="contenedor">
        <div class="hijo"></div>
    </div>
</body>
```
```css
/* Condigo de css para ejemplo */

.contenedor {
    width: 300px;
    height: 300px;
    background: blue;
    margin: 40px;
    position: relative;
    /* para que el contendor padre puede estan sobre el contenedor hijo es necesario de que no este definido un z-index */
}

.hijo {
    background-color: orange;
    width: 120px;
    height: 120px;
    position: relative;
    top: -20px;
    left: -20px;
    z-index: -1;
}
```
## Position
`position` lo que hace  es posicionar los elementos, estar posicionado significa que adquirira nuevas propiedades, las propiedades que arquiere nos permite hacer varias cosas.

Las propiedades `top` y `left` son las mas importantes, el sistema prestara mas atencion a las medidas de `top` y `left` y se aparte de estas dos tambien se encuentran las medidas de `bottom` y `rigth` entonces a estas ultimas dos las ignorara.
```html
<!-- > Codigo de html para ejemplo <-->
<body>
    <div class="caja1">caja1</div>
    <div class="caja2">caja2</div>
    <div class="caja3">caja3</div>
    <div class="caja4">caja4 </div>
</body>
```
```css
/* Condigo de css para ejemplo */
div{
    width: 120px;
    height: 120px;
    display: block;
}

.caja1 {
    background-color: red;
}

.caja2 {
    background-color: green;
}

.caja3 {
    background-color: blue;
}

.caja4 {
    background-color: yellow;
}

```
Existenn 5 posibilidades en `position`:

- `static`: que es el valor por defecto, cuando se utiliza este valor se considera como que no esta posicionado, por lo tanto no adquisira las propiedades al estar posicionado.

- `relative`: Cuando utilizamos el valor `relative` el espacio que guarda la caja lo conserva. Cuando trabajamos con html cada caja tiene un espacio reservado, si movemos la caja en espacio tambien se movera con la imagen de la caja, pero si usamos `relative` la imagen de la caja se movera pero el espacio se conservara en el espacio original.Ejemplo:
```css
/* Condigo de css para ejemplo */
div{
    width: 120px;
    height: 120px;
    display: block;
}

.caja1 {
    background-color: red;
}

.caja2 {
    background-color: green;
    position: relative;
    top: 300px;
}

.caja3 {
    background-color: blue;
}

.caja4 {
    background-color: yellow;
}

```

- `absolute`: el position absolute es similar al position relavita, pero existen 3 diferencias. En position absolute el espacio ya no esta reservado. Se toma de refetencia el viewport para mover las cajas(puede tomar como punto de referencia al contenedor si esta posicionado). el tama;o de la caja se ajusta al contenido aun que sea un bloque.


```html
<!-- > Codigo de html para ejemplo <-->
<body>
    <div class="contenedor">
        <div class="caja1">caja1</div>
        <div class="caja2">caja2</div>           
        <div class="caja3">caja3</div>
        <div class="caja4">caja4</div>
        <div class="caja5">caja5</div>
    </div>
</body>
```

```css
/* Condigo de css para ejemplo */
div{
    display; block;
    background: green;
    position: absolute;
}

div div {
    height: 100px;
    width: 100px;
    background: yellow;
}

.contenedor {
    position: static;/* si lo cambiamos por `relative` entonces tomara al contenedor como referencia en lugar del viwport */
    border: 4px solid red;
    margin: 50px auto;
    height: 450px;
    width: 450px;
}

.caja1 {
   
}
.caja2 {
    right: 0;
}

.caja3 {
    right: 0;
    bottom: 0;
}

.caja4 {
    bottom: 0;
}

.caja5 {
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    margin: auto;
    /* con este truco se pueden centrar las cajas sin saber las medidas del contenedor */
}
```

- `fixed`: fixed es exactamente igual que absolute solamente que queda fijado. Este efecto por lo general se le da a la publicidad, todo el contenido se puede mover menos la publicidad, esta se queda estatica.Ejemplo:
```html
<body>
    <div class="caja-fixed">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quia, quae asperiores ducimus ipsum nesciunt corporis quam est cumque in omnis aut voluptate! Corporis pariatur facere tempore, repellat at deleniti ipsa.
    </div>
    <div class="texto">
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aliquid itaque quia quos at beatae dignissimos voluptatibus nobis, alias tempora eveniet eum, hic repellendus praesentium expedita. Ex sit quaerat tempore facere!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia ipsam quibusdam a maiores pariatur ratione ad similique. Quos ut ullam unde assumenda aliquam delectus mollitia, sit quas dignissimos error suscipit!
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dicta dolor sint deserunt dolores hic quia laboriosam rem numquam delectus. Tenetur voluptatibus autem non aperiam vero neque eius consectetur voluptatum voluptates.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas necessitatibus nisi ratione quidem eaque cumque, sapiente minima optio, est eius praesentium et culpa tempora laborum ut, repellat qui eos maiores?
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Unde dignissimos est explicabo placeat ad aut excepturi distinctio rerum molestiae ipsum? Praesentium modi ducimus dolor illum! Incidunt consectetur repellat et cum.
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
    </div>
</body>
```
```css
.caja-fixed {
    background: red;
    position: fixed;
    top: 20px
}
```

- `sticky`: es como un fixed y a la vez un relative. Lo que podemos hacer con esto es definir en que momento de la pagina va a estar fijo. Ejemplo:
```html
<body>
        <div class="texto">
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aliquid itaque quia quos at beatae dignissimos voluptatibus nobis, alias tempora eveniet eum, hic repellendus praesentium expedita. Ex sit quaerat tempore facere!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia ipsam quibusdam a maiores pariatur ratione ad similique. Quos ut ullam unde assumenda aliquam delectus mollitia, sit quas dignissimos error suscipit!
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dicta dolor sint deserunt dolores hic quia laboriosam rem numquam delectus. Tenetur voluptatibus autem non aperiam vero neque eius consectetur voluptatum voluptates.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas necessitatibus nisi ratione quidem eaque cumque, sapiente minima optio, est eius praesentium et culpa tempora laborum ut, repellat qui eos maiores?
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Unde dignissimos est explicabo placeat ad aut excepturi distinctio rerum molestiae ipsum? Praesentium modi ducimus dolor illum! Incidunt consectetur repellat et cum.
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
    </div>
    <div class="caja-sticky">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quia, quae asperiores ducimus ipsum nesciunt corporis quam est cumque in omnis aut voluptate! Corporis pariatur facere tempore, repellat at deleniti ipsa.
    </div>
    <div class="texto">
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aliquid itaque quia quos at beatae dignissimos voluptatibus nobis, alias tempora eveniet eum, hic repellendus praesentium expedita. Ex sit quaerat tempore facere!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia ipsam quibusdam a maiores pariatur ratione ad similique. Quos ut ullam unde assumenda aliquam delectus mollitia, sit quas dignissimos error suscipit!
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dicta dolor sint deserunt dolores hic quia laboriosam rem numquam delectus. Tenetur voluptatibus autem non aperiam vero neque eius consectetur voluptatum voluptates.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas necessitatibus nisi ratione quidem eaque cumque, sapiente minima optio, est eius praesentium et culpa tempora laborum ut, repellat qui eos maiores?
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Unde dignissimos est explicabo placeat ad aut excepturi distinctio rerum molestiae ipsum? Praesentium modi ducimus dolor illum! Incidunt consectetur repellat et cum.
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
    </div>
</body>
```
```css
.caja-sticky {
    background: red;
    position: sticky;
    top: 0;
}
```
## Display
La propiedad display lo que hace es modificar el comportamiento de las cajas, no modifica tanto el comportamiento entre las cajas, sino modifica el comportamiento en si de una caja en particular.

La propiedad display tiene muchos valores, esto son algunos de esos valores que son los que mas se usan:
```
- block
- inline

- inline-block

- grid
- flex

- inline-flex
- inline-grid
```
- `inline`: en tama;o de la caja de adapta al contenido, generalmente se utiliz apaa texto

- `inline-block`:  a los inline-block les podemos dar un ancho y un alto(podemos modificar las dimenciones de la caja). tambien nos permite poner un bloque al lado del otro.En pocas palabras se comportara como un bloque pero su tama;o predefinido se adaptar aal contenido.

## overflow
En pocas palabras es el escroll que se tiene en el sitio, cuando existe mucho contenido en el sitio existira contendio que sobresalga de lo que podemos ver.
```
Existen 3 tipos:
- overflow
- overflow-y
- overflow-x
```

Tenemos varios valores para esta propiedad:
```
- auto
- hidden
- scroll
```

- `auto`: la propiedad auto lo que hace es que detecta de que encaso de que el contendo sobrepase la caja entonces pone la posiblidad de que podamos scrollear dentro de la caja.Ejemplo:
```html
<body>
    <div class="texto">
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aliquid itaque quia quos at beatae dignissimos voluptatibus nobis, alias tempora eveniet eum, hic repellendus praesentium expedita. Ex sit quaerat tempore facere!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia ipsam quibusdam a maiores pariatur ratione ad similique. Quos ut ullam unde assumenda aliquam delectus mollitia, sit quas dignissimos error suscipit!
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dicta dolor sint deserunt dolores hic quia laboriosam rem numquam delectus. Tenetur voluptatibus autem non aperiam vero neque eius consectetur voluptatum voluptates.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas necessitatibus nisi ratione quidem eaque cumque, sapiente minima optio, est eius praesentium et culpa tempora laborum ut, repellat qui eos maiores?
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Unde dignissimos est explicabo placeat ad aut excepturi distinctio rerum molestiae ipsum? Praesentium modi ducimus dolor illum! Incidunt consectetur repellat et cum.
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quibusdam similique ut. Magni, perspiciatis? Totam quia ex tempora, eaque perspiciatis doloribus odit at sapiente accusamus nulla eos excepturi quis repellat!
    </div>
</body>
```
```css
.texto {
    margin: auto;
    margin-top: 50px;
    width: 320px;
    height: 350px;
    border: 4px solid red;
    background: grey;
    overflow: auto;
}
```

- `scroll`: pone obligatoriamente la barra del scroll, por mas que no sea obligatorio scrollear.

- `hidden`: oculta el scroll

## float
Con floar se puede hacer un efecto de que un texto envualva la imagen.Ejemplo:
```html
<!-- Es necesario de que el texto no se encuntre dentro de otra caja para que funcione el efecto de envolver a la iamgen con el texto  -->
<body>
    <div class="cont">
        <img src="direccion de la iamgen">
        mucho texto
    <div>
</body>
```
```css
.cont {
    margin: auto;
    margin-top: 50px;
    border: 4px solid red;
    background: grey;
    width: 50%;
    padding: 20px;
}

.cont img {
    float: right;
    width: 300px;
    margin-right: 18px;
}
```
3:43