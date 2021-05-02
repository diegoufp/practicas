# Dom - curso JavaScript

## Que es DOM?
EL DOM da una representacion del documento como un grupo de nodos y objetos estructurados que tienene propiedades y metodos. Esencialmente, conecta las paginas web a scripts o legunajes de programacion.

EN pocas palabras, el DOM es la forma en que javascript puede acceder a nuestro documento html. Cuando nostros tenemos un html tenemos diferentes partes como etiquetas y contenido, javascript lo lleva a un documento en grupo de nodos y objetos.

## Document
Representa cualquier pagina web cargada en el navegador. Si quisieramos seleccionar el `h1` dentro del archivo de html por medio de javascript siemplemente escribimos:
```js
document.querySelector('h1')
```

y si quisieramos modificar el contenido de digo `h1` por meido de js simplemente tendriamos que escribir:
```js
document.querySelector('h1').textContent = 'Texto desde JS'
```

## Acceder al DOM
```html
<body>
    <h1>Hola al DOM</h1>
    <p>Text estatico</p>
    <h3>Titulo h3</h3>
    <h3>Titulo dos h3</h3>
    <script src="app.js"></script>
</body>
```
```js
document.querySelector('h3')
console.log(document.querySelector('h3'))
// querySelector selecciona el primero selector que coincida con lo que estamos buscando, en este caso h3.
```
Si quisieramos acceder al segundo `h3` existen varias alternativas:
```html
<body>
    <h1>Hola al DOM</h1>
    <p id="parrafo">Text estatico</p>
    <h3>Titulo h3</h3>
    <h3 class="h3-danger">Titulo dos h3</h3>
    <script src="app.js"></script>
</body>
```
```js
document.querySelector('h3')
console.log(document.querySelector('.h3-danger'))
console.log(document.querySelector('#parrafo'))
// pero para los id hay una mejor opcion para buscar, el cual seria:
console.log(document.getElementById('parrafo')) // esta es la forma mas rapida para buscar por medio de un id
```

Si quisieramos acceder a varios elementos con la msima clase podemos usar:
```html
<body>
    <h1>Hola al DOM</h1>
    <p id="parrafo">Text estatico</p>
    <h3 class="h3-danger">Titulo h3</h3>
    <h3 class="h3-danger">Titulo dos h3</h3>
    <script src="app.js"></script>
</body>
```
```js
console.log(document.querySelectorAll('.h3-danger'))
console.log(document.querySelectorAll('h3'))
```

## Element

Una vez tenemos el elemento podemos modificarlo.

1. Accedemos al elemento
2. Modificamos el elemento

Generalmente nostros vamos a guardar nuestros elementos en una `const`, aun que tambien se podria guardar en un `var` o un `let`.
```html
<body>
    <h1>Hola al DOM</h1>
    <p id="parrafo">Text estatico</p>
    <h3 class="h3-danger">Titulo h3</h3>
    <h3 class="h3-danger">Titulo dos h3</h3>
    <script src="app.js"></script>
</body>
```
```js
const parrafo = document.querySelector('#parrafo') ;// tambien tenemos la opcion de usar: 'getElementById'
// textContent lo que hace es modificar su contenido
parrafo.textContent = 'text Content JS' ;// si agregamos etiquetas con 'textContent' entonces se veran tal cual en el html
parrafo.innerHTML = 'text con innerHTML' ;
// aun que los dos parecen similares. Con 'innerHTML' podriamos por ejemplo colocar etiquetas
parrafo.innerHTML = '<b>text con innerHTML</b>' ;// en este caso la palabra aparecio en negritas en el html 

// tambien podriamos agregar una clase desde javascript
// 'classList' permite agregar clases especificas
parrafo.classList.add('h3-danger')
// si queremos agregar mas de una clase entonces las separamos por comas
parrafo.classList.add('h3-danger', 'my-2')
```

## createElement()

`createElement()` nos permitira crear elementos.

```html
<!-- codigo html -->
<body>
    <h1>Hola al DOM</h1>
    <ul id="lista">
        <!-- Nosotros a traves de javascript insetaremos los 'li' -->
    <ul>
</body>
```
```js
// Codigo js
const lista = document.getElementById('lista');
console.log(lista);

// para crear la etiqueta 'li' tenemos una funcionalidad en js llamada 'createElement'
const li = createElement('li'); // con esto hemos creado una etiqueta 'li'
// pero aun no le hemos dicho donde se va a posicionar y tambien falta agregarle el texto que contendra
li.textContent = 'primer elemento'; // con esto escrebiremos el texto que contendra
// para indicarle la direccion en donde se posicionara el 'li' usamos:
lista.appendChild(li); // con esto le estamos diciendo que lista incorpora en el nodo hijo el elemento 'li'
```


Para crear multiples lista para posicionar dentro de un `ul` entonces podemos hacer:
```html
<!-- codigo html -->
<body>
    <h1>Hola al DOM</h1>
    <ul id="lista">
        <!-- Nosotros a traves de javascript insetaremos los 'li' -->
    <ul>
</body>
```
```js
// Codigo js
const lista = document.getElementById('lista');
console.log(lista);

const li = createElement('li');
const arrayElement = ['primer elemento', 'segundo', 'tercero'];

arrayElement.forEach(item => {
    console.log(item);
    const li = createElement('li');
    li.textContent = item;

    lista.appendChild(li);
});

// Una segunda opcion para resolver este problema seria:
arrayElement.forEach(item => {
    // si usamos template string( las comilla ``) que nos permitiran ingresar mas facilmente las etiquetas junto con un objeto dianmico
    lista.innerHTML += `<li>${item}</li>`
})
// sin embargo esta opcion puede generar problemas en nuestra pagina web por algo llamado 'Reflow'
// el Reflow ocurre cuando un navegador debe procesar y dibujar parte o la totalidad de una apgina web nuevamente , como despues de una actualizacion en un sitio interactivo.
// en pocas palabras nosotros estamos actualizando nuestro sitio web cada vez que se agrega un elemento nuevo en nuestro 'ul'


// este es un problema que se genera con los dos opciones
```

## Fragment
fragment vino a solucionar algo que conocemos como reflow. Fragment es una version ligera del Document que almacena un segmento de una estructura de document compuesta de nodos como un documento estandar. 
Por ende en un fragment vamos a guardar todo un template o nodos HTML que luego pintaremos en nuestro DOM, asi evitamos en mayor parte el Reflow.
```html
<!-- codigo html -->
<body>
    <h1>Hola al DOM</h1>
    <ul id="lista">
        <!-- Nosotros a traves de javascript insetaremos los 'li' -->
    <ul>
</body>
```
```js
// Codigo js
const lista = document.getElementById('lista');
console.log(lista);

const li = createElement('li');
const arrayElement = ['primer elemento', 'segundo', 'tercero'];

const fragment = document.createDocumentFragment(); //este fragmento nos permitira guardar la estrucutra antes de ser incorporada a nuestro html
// otra opcion valida seria:
// const fragment = new DocumentFragment()
arrayItem.forEach(item => {
    const li = document.createElement('li');
    li.textContent = item;
    fragment.appendChild(li); 
});
//con esto el fragment a sido creado, ahora solo falta empujarlo
// esto es lo importante ya que una vez que finalice nuestro ciclo forEach nostros hacemos un appendCHild del fragment
lista.appendChild(fragment);
```
para insertar la lista al revez:
```js
const lista = document.getElementById('lista');
console.log(lista);

const li = createElement('li');
const arrayElement = ['primer elemento', 'segundo', 'tercero'];

const fragment = document.createDocumentFragment(); 
arrayItem.forEach(item => {
    const li = document.createElement('li');
    li.textContent = item;
    const childNode = fragment.firstChild;
    console.log(item, childNode);

    fragment.insertBefore(li, childNode);
});
lista.appendCHild(fragment);
```

## Templete HTML
Supongamos que necesitamos incorporar de forma dinamica este elemento:
```html
<ul id="lista">
    <!--<li class="list">
        <b>Nombre: </b> <span class="text-danger">descripcion...</span>
    </li> -->
</ul>
```
```js
const lista = document.querySelector('#lista');

const arrayLista = ['item 1', 'item 2', 'item 3'];

const fragment = document.createDocumentFragment();
arrayLista.forEach(item => {
    const li = document.createElement('li');
    li.classList.add('li');
    const b = document.createElement('b');
    b.textContent = 'Nombre: ';
    li.appendChild(b);
    const span = document.createELement('span');
    span.classList.add('text-danger');
    span.textContent = item;
    li.appendChild(b);
    li.appendChild(span);
    fragment.appendChild(li)
});
lista.appendChild(fragment);
```
si tratamos de resolver este problema con `createElement` entonces tendremos un condigo muy extenso, para ello existe una solucion.

- Podria ser tentador utilizar `innerHTML` pero el innerHTML no acepta el `fragment` por lo tanto no podrimaos utilizarlo.

```html
<ul id="lista">
    <!--<li class="list">
        <b>Nombre: </b> <span class="text-danger">descripcion...</span>
    </li> -->
</ul>
```
```js
const lista = document.querySelector('#lista');

const arrayLista = ['item 1', 'item 2', 'item 3'];

// este fragment creado con let ira almacenando nuestra cadena 
let fragment = ''
arrayLista.forEach(item => {
    // en este fragment iremos incorporando por cada vuelta la estructura
    fragemnt += `
    <li class="list">
        <b>Nombre: </b> <span class="text-danger">${item}</span>
    </li>
    `// haciando esto evitariamos el reflow, sin embargo sigue teniendo un menor rentimiento que el createElement
});
lista.innetHTML = fragment;
```
- Entonces cual es la mejor solucion?
El elemento HTML <template> es un mecanismo para manetener el contenido HTML del lado del cliente que no se renderiza cuando se carga una pagina, pero que posteriormente puede ser instanciado durante el tiempo de ejecucion empleando JavaScript.

La mejor solucion seria utilizar tamplate y fragment.
Los template sirven para hacer una estrucutra que podremos replicar en el ul.
Se recomiend que los template los dejen abajo de todo el codigo html. por que es una guia que nosotros vamos a utilizar con js para usar lo.
```html
<body>
    <ul id="lista">
        <!--<li class="list">
            <b>Nombre: </b> <span class="text-danger">descripcion...</span>
        </li> -->
    </ul>
    <!-- paso 1: creamos nuestro template en nuestro html>
    <template id="template-li">
        <li class="list">
            <b>Nombre: </b> <span class="text-danger">descripcion...</span>
        </li>
    </template>
</body>
```
```js
const lista = document.querySelector('#lista');

const arrayLista = ['item 1', 'item 2', 'item 3'];

const template = document.querySelector('#template-li').content //por que nos interesa el fragmento de la etiqueta entonces agregaremos un .content
const fragment = document.createDocumentFragment()

arrayLista.forEach(item => {
    template.querySelector('.text-danger').textContent = item; // hay que ser mas especificos en dise;os de paginas ma conplejas
    // posteriormente vamos a hacer un clon de nuestro template
    const clone = template.cloneNode(true);
    //luego empujamos el clon
    fragment.appendCHild(clone);
});

lista.appendChild(fragment)
```

## addEventListener(click), event delegation y stopPropagation
`addEventListener` es para detectar eventos por ejemplo cuando le hacemos click a un boton. Tiene muchas funcionalidades nosotros podemos detectar incluso cuando el mouse este sobre un elemento.

primero vamos a agregar [Bootstrap](https://getbootstrap.com/ "Bootstrap") al html para hacer los estilos  a la velocidad de la luz.
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
```
```html
<body>
    <div class="container py-5 bg-warning text-center">
        <h1>Contador</h1>
        <button class="btn btn-info">
            Aumentar
        </button>
        <button class="btn btn-danger">
            Disminuir
        </button>
        <h4 class="my-5">Contador: <span id="span">0</span></h4>
    </div>
<body>
```
```js
const container = document.querySelector('.container');
const btnDisminuir = document.querySelector('btn-danger');
const span = document.getElementById('span');
let contador = 0;

container.addEventListener('click', (e) => {
    //console.log(e.target) //esto nos mostrara las etiquetas que estamos clickeando
    if(e.target.classList.contains('btn-info')){
        contador ++;
        span.textContent = contador;
    };

    if(e.target.classList.contains('btn-danger')){
        contador --;
        span.textContent = contador;
    };
});
```

- `stopPropagation` : indicarle que cuando hagamos click en un evento dentro del contenerdo solamente ese evento se ejecute y no se haga una propagacion, esto en el caso de que hayamos creamos un `addEventListener` en el body o quermaos evitar que se propage al contenedor padre.

```js
const container = document.querySelector('.container');
const btnDisminuir = document.querySelector('btn-danger');
const span = document.getElementById('span');
let contador = 0;

container.addEventListener('click', (e) => {
    //console.log(e.target) //esto nos mostrara las etiquetas que estamos clickeando
    if(e.target.classList.contains('btn-info')){
        contador ++;
        span.textContent = contador;
    };

    if(e.target.classList.contains('btn-danger')){
        contador --;
        span.textContent = contador;
    };
    e.stopPropagation()
});

document.body.addEventListener('click', () => {
    console.log('diste click')
});
```
`stopPropagation` no se debe confundir con `preventDefault`.
`preventDefault` : cuando nosotro tenemos un formulario y le damos al boton de submit por defecto se hace una solucitud en `get`, por lo tanto con este `preventDefault` podemos evitar ese comportamiento.