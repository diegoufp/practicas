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

## Practica de carrito de compras

Creamos archivos `.json`, `.js` y `html` para nuestro proyecto.

Para poder acceder o leer esos elementos de la `api.js` nosotros usamos lo que es el fetch.
```js
//codigo de javascript

const items = document.getElementById("items");
const templateCard = document.getElementById('template-card').content;// con esto estariamos accediendo a los elementos
// podemos hacer el fragment directamente aca, recuerden que el fragment es como una memoria volatil por lo cual se puede ocupar para todas las cosas que queramos pintar mientras se quiera una estrucutra igual
const fragment = document.createDocumentFragment();

// tenemos un addEventListener que va a esperar que se lea todo nuestro html y luego ejecute alguna funcion 
// el 'DOMContentLoaded' se dispara cuando el documento HTML ha sido completamente cargado y parseado, sin esperar hojas de estilos, images y subframes para finalizar la carga.
document.addEventListener('DOMContentLoaded', () => {
    fetchData() // con esto se estaria haciando la tarea principal de solamente capturar los datos
});

items.addEventListener('click', e => {
    // con esto escuchariamos el click del boton
    addCarrito(e)
})

// para usar el fech nosotros tenemos que usar una funcion de flecha
const fetchData = async() => {
    try {
        // en el try nosotros hacemos la peticion
        const res = await fetch('api.json');
        const data = await res.json();
        pintarCards(data);

    } catch (error) {
        console.log(error);
    }
};

//ahora tendriamos que pintar la informacion.
const pintarCards = data => {
    // en este caso usaremos forEach por que la api esta en json, no vamos a hacer lo mismo cuando tengamos la correccion de los carritos por que va a ser una coleccion de objetos
    data.forEach(producto => {
        // como nosotroa ya tenemos el template y ya tenemos el fragment, ahora tenemos que acceder efectivamente a este esqueleto.
        // en este caso vamos a modificar el h5
        templateCard.querySelector('h5').textContent = producto.title;
        templateCard.querySelector('p').textContent = producto.precio;
        // setAttribute establece el valor de un atributo en el elemento indicado. Si el atributo ya existe, el valor es actualizado, en caso contrario, el atributo es a;adido con el nombre y valor indicado.
        templateCard.querySelector('img').setAttribute("src", producto.thumbnailUrl);
        templateCard.querySelector('.btn-dark').dataset.id = producto.id; // con esto estariamos vincualando el boton con su respectivo data-id, es una informacion primordial.

        // ahora que tenemos el tempalete tenemos que hacer la clonacion
        const clone = templateCard.cloneNode(true);
        fragment.appendChild(clone)
    })
    items.appendChild(fragment);
};
```
```html
<!-- Codigo html-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    <title>Carrito de compras</title>
</head>
<body>
    <div class="container">
        <h1>Carrito</h1>
        <hr>
        <div class="row" id="items"></div>
    </div>
    <!-- Cuando tengamos que recorrer elemento y pintarlos en el sitio web, es recomentable utilizar <template> con los fragment para evitar el reflow, si es solo un elemento podemos crearlo con inerhtml-->
    <template id="template-card">
        <div class="col-12 mb-2 col-md-4">
            <div class="card">
                <img src="" alt="" class="card-img-top">
                <div class="card-body">
                    <h5>Titulo</h5>
                    <p>precio</p>
                    <button class="btn btn-dark">Comprar</button>
                </div>
            </div>
        </div>
    </template>

    <script src="/code.js"></script>
</body>
</html>
```

### Agregar producto al carrito
```js
//codigo de js
const items = document.getElementById('items');
const templateCard = document.getElementById('template-card').content;
const fragment = document.createDocumentFragment();
let carrito = {}; // creamos este objeto carrito para agregar las cosas al carrito

document.addEventListener('DOMContentLoaded', () => {
    fetchData()
});

items.addEventListener('click', e => {
    addCarrito(e);
})


const fetchData = async () => {
    try {
        
        const res = await fetch('api.json');
        const data = await res.json();
        pintarCards(data);

    } catch (error) {
        console.log(error);
    }
};

const pintarCards = data => {
    data.forEach(producto => {
        templateCard.querySelector('h5').textContent = producto.title;
        templateCard.querySelector('p').textContent = producto.precio;
        templateCard.querySelector('img').setAttribute("src", producto.thumbnailUrl);
        templateCard.querySelector('.btn-dark').dataset.id = producto.id; 
        const clone = templateCard.cloneNode(true);
        fragment.appendChild(clone)
    });
    items.appendChild(fragment);
};

const addCarrito = e => {
    //console.log(e.target);
    //console.log(e.target.classList.contains('btn-dark')); // aqui estamos detectando el boton
    if(e.target.classList.contains('btn-dark')){
        setCarrito(e.target.parentElement);
    };
    e.stopPropagation();// nos servia para deterner algun otro evento que se pueda generar en nuestro 'items'
};

const setCarrito = objeto => {
    // el 'objeto' sera todo lo que nosotros hemos seleccionado
    // el setCarrito lo que va hacer es capturar todos esos elementos
    const producto = {
        //estamos accediendo a esa infomarcion
        id: objeto.querySelector('.btn-dark').dataset.id,
        title: objeto.querySelector('h5').textContent,
        precio: objeto.querySelector('p').textContent,
        cantidad: 1
    };

    // vamos a acceder al elemento que se esta repitiendo
    if(carrito.hasOwnProperty(producto.id)){
        //si esto existe significa que el producto se esta duplicando por lo tanto se tiene que aumentar la cantidad
        producto.cantidad = carrito[producto.id].cantidad + 1;
    }
    // ahora tenemos que empujarlo al carrito
    // los trespuntos '...' se hace llama spriteoperator, con los tres puntos solamente estamos adquiriendo la informacion que esta en producto, es decir que estamos haciendo una copia.
    carrito[producto.id] = {...producto};

    console.log(producto)
};
```
```html
<!-- codigo html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    <title>Carrito de compras</title>
</head>
<body>
    <div class="container">
        <h1>Carrito</h1>
        <hr>
        <div class="row" id="cards"></div>
    </div>

    <template id="template-card">
        <div class="col-12 mb-2 col-md-4">
            <div class="card">
                <img src="" alt="" class="card-img-top">
                <div class="card-body">
                    <h5>Titulo</h5>
                    <p>precio</p>
                    <button class="btn btn-dark">Comprar</button>
                </div>
            </div>
        </div>
    </template>

    <script src="/code.js"></script>
</body>
</html>
```

### Template del carrito de compras
```html
<!--codigo de html-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    <title>Carrito de compras</title>
</head>
<body>
    <div class="container">
        <h1>Carrito</h1>
        <hr>
        <table class="table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Item</th>
                <th scope="col">Cantidad</th>
                <th scope="col">Acción</th>
                <th scope="col">Total</th>
              </tr>
            </thead>
            <tbody id="items"></tbody>
            <tfoot>
              <tr id="footer">
                <th scope="row" colspan="5">Carrito vacío - comience a comprar!</th>
              </tr>
            </tfoot>
          </table>
        <div class="row" id="cards"></div>
    </div>

    <template id="template-card">
        <div class="col-12 mb-2 col-md-4">
            <div class="card">
                <img src="" alt="" class="card-img-top">
                <div class="card-body">
                    <h5>Titulo</h5>
                    <p>precio</p>
                    <button class="btn btn-dark">Comprar</button>
                </div>
            </div>
        </div>
    </template>

    <template id="template-footer">
        <th scope="row" colspan="2">Total productos</th>
        <td>10</td>
        <td>
            <button class="btn btn-danger btn-sm" id="vaciar-carrito">
                vaciar todo
            </button>
        </td>
        <td class="font-weight-bold">$ <span>5000</span></td>
    </template>
    
    <template id="template-carrito">
      <tr>
        <th scope="row">id</th>
        <td>Café</td>
        <td>1</td>
        <td>
            <button class="btn btn-info btn-sm">
                +
            </button>
            <button class="btn btn-danger btn-sm">
                -
            </button>
        </td>
        <td>$ <span>500</span></td>
      </tr>
    </template>

    <script src="/code.js"></script>
</body>
</html>
```
```js
// codigo de js
const cards = document.getElementById('cards');
const items = document.getElementById('items'); // se seleccionan los nuevos elementos d ela tabla
const footer = document.getElementById('footer'); // se seleccionan los nuevos elementos d ela tabla
const templateCard = document.getElementById('template-card').content;
const templateFooter = document.getElementById('template-footer').content;// se seleccionan los nuevos templates
const templateCarrito = document.getElementById('template-carrito').content;// se seleccionan los nuevos templates
const fragment = document.createDocumentFragment();
let carrito = {};

document.addEventListener('DOMContentLoaded', () => {
    fetchData()
});

cards.addEventListener('click', e => {
    addCarrito(e);
})


const fetchData = async () => {
    try {
        
        const res = await fetch('api.json');
        const data = await res.json();
        pintarCards(data);

    } catch (error) {
        console.log(error);
    }
};

const pintarCards = data => {
    data.forEach(producto => {
        templateCard.querySelector('h5').textContent = producto.title;
        templateCard.querySelector('p').textContent = producto.precio;
        templateCard.querySelector('img').setAttribute("src", producto.thumbnailUrl);
        templateCard.querySelector('.btn-dark').dataset.id = producto.id; 
        const clone = templateCard.cloneNode(true);
        fragment.appendChild(clone)
    });
    cards.appendChild(fragment);
};

const addCarrito = e => {
    if(e.target.classList.contains('btn-dark')){
        setCarrito(e.target.parentElement);
    };
    e.stopPropagation();
};

const setCarrito = objeto => {
    
    const producto = {
        
        id: objeto.querySelector('.btn-dark').dataset.id,
        title: objeto.querySelector('h5').textContent,
        precio: objeto.querySelector('p').textContent,
        cantidad: 1
    };

    
    if(carrito.hasOwnProperty(producto.id)){
        producto.cantidad = carrito[producto.id].cantidad + 1;
    }
    
    carrito[producto.id] = { ...producto };
    pintarCarrito();
};

// ahora pintaremos lo del carrito en el dom
const pintarCarrito = () => {
    
    // para que no ocurra un error en el carrito que se dibujen duplicados vamos a partir de un innerHTM vacio
    items.innerHTML = ''

    // podemos hacer un forEach pero antes tenemos que usar un Object.values por que estamos trabajando con un objeto y no se pueden usar las funciones de los array
    Object.values(carrito).forEach(producto => {
        //este producto tenemos que pintarlo
        templateCarrito.querySelector('th').textContent = producto.id;
        templateCarrito.querySelectorAll('td')[0].textContent = producto.title;
        templateCarrito.querySelectorAll('td')[1].textContent = producto.cantidad;
        templateCarrito.querySelector('.btn-info').dataset.id = producto.id;
        templateCarrito.querySelector('.btn-danger').dataset.id = producto.id;
        templateCarrito.querySelector('span').textContent = producto.cantidad * producto.precio;

        const clone =  templateCarrito.cloneNode(true);
        fragment.appendChild(clone);
    })

    // ahora si lo estariamos pintando
    items.appendChild(fragment);
};
```