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
