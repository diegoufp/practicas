# Closures Scope


## Scope
Cuando hacemos referencia a una variable, javascript va a empezar a buscar su definicion en el entorno mas cercano e ira buscando en entornos cada vez mas lejanos hasta que encuentre el entorno donde la variable este declarada, cada uno de estos entornos recibe el nombre de `scrope` en javascript.

El **Scope** es lo que le da significado a las variables y ademas determina el conjunto de variables que podemos accerder desde una linea de codigo.

El **scope** de cada variable depende de **como** y **donde** la declaremos y eso solo es algo que debemos decidir nosotros cuando escribimos el codigo de nuestro programa.

Con **como** me refiero a si la declaramos con `var`, `let` o `const`.
Y por **donde** me refiero a que si la declaramos de forma libre y fuera de toda funcion o si la declaramos dentros de una funcion o dentro de un bloque de codigo como un `if` por ejemplo.

Decimos que javascript tiene un **SCOPE LEXICO** `(lexical scoping)`, ya que el scope que va a tener cada variable se determina leyendo el codigo del programa sin tener que ejecutarlo. Es por eso que tambien a este modelo se le conoce como **SCOPE ESTATICO** `(static scoping)`

### Definicion de scope
El contexto actual de ejecucion. El contexto en el que los valores y las expresiones son "visibles" o pueden ser referenciados. Si una variable u otra expresion no esta "en el Scope-alcance actual", entonces no esta disponible para su uso. Los Scope tambien se pueden superponer en una jerarquia, de modo que los Scope secuendarios tengan acceso a los ambitos primarios, pero no al reves.

Las palabras **CONTEXTO** y **CONTEXTO DE EJECUCION** se parecen mucho pero son dos cosas distintas.

El **CONTEXTO** en javascript tiene que ver con el valor que tiene la variable `this` en algun momento de la ejecucion.
Cual es el objeto que se esta ejecutanto una funcion.

Lo que tiene que quedar claro es que cuando hablamos de **SCOPE** estamos hablando de **CONTEXTO DE EJECUCION** o mejor aun de **ENTORNO**, de lo que le da sugnificado a las variables. 

Con eso en claro hablemos de los distintos tipos de **SCOPE** que puede tener nuestras variables.

Como desarrolladores, de acuerdo a como escribamos nuestro codigo podemos decidir si una variable va a vivir en un `scope global` o en un `scope local`.

Como te imaginaras, las `variables globales` pueden ser accedidas desde cualquier lugar de nuestro programa. 

Las `variables globales` son las que declaramos fuera de toda funcion o bloque de codigo. Sin importar si las declaramos con `var`, `let` o `const`.

Las `varaibles grobales` estaran en memoria durante toda la ejecucion del programa.

Las `variables locales` solo se pueden acceder desde una aprte de nuestro programa.

Si dentro de la funcion declaramos otra variable, esa variable solo se va a poder acceder desde esa funcion, si intentamos accederla desde afuera vamos a tener un error de referencia cuando se quiera ejecutar esa linea de codigo:
```js
var fruta = 'manzana';

funcion comer(){
    var otraFruta = 'banana';
    console.log('Comiendo' + otraFruta);
}

console.log(otraFruta)// aqui es donde arrojaria un error de referencia
```

Lo mismo ocurre con los parametros que recibe una funcion, si bien no estan declarados con `var` o `const` esos parametros solo se van a poder acceder dentro de esa funcion.

Y por mas que estemos dentro de un bloque de un `if` como la variable esta declarada con `var`, esta se va a poder acceder sin problemas dentro de todo el cuerpo de la funcion donde esta su declaracion, si quisieramos podriamos acceder a ella desde afuera de donde fue declarada.
```js
var fruta = 'manzana';

funcion comer(){
    var otraFruta = 'banana';
    if (true){
        var unaFrutaMas = 'pera';
    }
    console.log('Comiendo' + otraFruta);
    console.log('comiendo' + unaFrutaMas);// esto es correcto
}

console.log(otraFruta)// aqui es donde arrojaria un error de referencia
```

Hay dos tipos de **SCOPE LOCAL**:
- **SCOPE DE FUNCION**: 
    - Las variables que tiene un scope de funcion se puede acceder dentro de todo el cuerpo de la funcion pero no fuera de ellas.
    - Las variables declaradas con var, siempre van a tener un scope de funcion sin importar en que parte de la funcion las declaremos. 

- **SCOPE DE BLOQUE**

    - Accesibles dentro de todo el bloque, pero no fuera del mismo.
    - Las variables declaradas con `let` o `const` van a tener un scope de bloque

- Las variables locales estaran en memoria durante la ejecucion de la funcion o bloque.
Un bloque en javascript es una porcion de codigo que esta encerrada entre llaves `{}`, puede ser el bloque de un `if`, `else`, `while`, `for`, el cuerpo de una funcion tambien es un bloque de codigo en si, la cosa es que si dentro de un bloque de codigo declaramos una variable con `let` o con `const, entonces fuera de ese bloque no vamos a poder accederla:
```js
var fruta = 'manzana';

funcion comer(){
    var otraFruta = 'banana';
    if (true){
        let unaFrutaMas = 'pera';
    }
    console.log('Comiendo' + otraFruta);
    console.log('comiendo' + unaFrutaMas);// aqui es donde arrojaria un error de referencia
}

console.log(otraFruta)// aqui es donde arrojaria un error de referencia
```
### Cual es mejor
Cual deberiamos usar?, el scope global o el scope local?

Si cada funcion tiene que tener variables globales y deacuerdo a los valores que tengan la funcion va a devolver una cosa u otra, entonces, la ejecucion de una funcion dependera de que en que estado este nuestro programa en ese momento. Las funciones se vuelven mas impredecibles por que dependen de cosas externas, haciendo que nuestro codigo se vuelva mas dificil de entender y mas facil de introducir variables.

Como buena practica de programacion debemos declarar nuestras variables dentro del scope mas reducido posible. Ademas las variables globales van a estar en memoria durante toda la ejecucion del programa, mientras que las variables locales van a estar en memoria durante la ejecuccion de la funcion o bloque.

## SCOPE CHAIN(cadena de scopes)

EN javaScript es bastante comun que dentro de una funcion tengamos otra funcion. 

```js
var fruta = 'manzana';

function comer() {
    var otraFruta = 'banana';

    function lavar(){
        console.log('Lavando' + fruta);
    }

    lavar();
    console.log('Comiendo' + otraFruta);
}
```
Si quisieramos, desde esta funcion podriamos acceder a la variable `fruta`, para accederla javascript primero va a buscando en el scope donde se encuentra esa linea de codigo, en este caso: `function lavar(){console.log('Lavando' + fruta);}`, al no encontarla va a buscarla en el scope padre y como no la encuentra la busqueda va a llevar hasta el scope global donde finalmente va a encontrar la variable.

ESte mecanismo se llama `cadena de scopes` y es lo que permite que las variables globales se puedan acceder desde cualquier lugar del programa.

Y si po equivocacion escribimos mal una variables, esa busqueda igual se va hacer siguiendo la cadena de scopes, llegando hasta el scope global y como ahi tampoco se encuentra la variable veremos le tipico error de referencia de que la variable no esta definida por que en este caso se escribio de manera incorrecta.  

Ahora una diferencia de lo que hace aca javaScript, si en ves de leer una variable que no existia, hubiesemos querido escribir un valor sobre ella, la busqueda igual se hubiese hecho hasta llegar al scope global y al no encontarla javascript crearia esa variable global por nosotros.

```js
var fruta = 'manzana';

function comer() {
    var otraFruta = 'banana';

    function lavar(){
        console.log('Lavando' + fruta);
    }

    furta = 'pera'; //
    lavar();
    console.log('Comiendo' + otraFruta);
}
```

Esto no esta muy bueno, pero se soluciona de manera muy sensilla , podemos evitar este comportamiento colocando una instruccion `'use strict'` para que el interprete de javaScript tenga esto en cuenta y no nos cree la variable global, en ves de eso nos mostrara un error.

```js
'use strict';
var fruta = 'manzana';

function comer() {
    var otraFruta = 'banana';

    function lavar(){
        console.log('Lavando' + fruta);
    }

    furta = 'pera'; //
    lavar();
    console.log('Comiendo' + otraFruta);
}
```

### Ocultamiento de variables

El **OCULTAMIENTO DE VARIABLES** (variable shadowing) se produce cuando una variable que esta en un scope mas reducido tiene el mismo nombre que otra que esta en un scope superior siguiendo su cadena de scopes.

```js
'use strict';
var fruta = 'manzana'; // esta es la variable oculta

function comer() {
    var fruta = 'banana';

    function lavar(){
        console.log('Lavando' + fruta);
        // podemos acceder a la variable ocula con :
        //  console.log('Lavando' + window.fruta);
    }

    lavar();
    console.log('Comiendo' + otraFruta);
}
```

Si, si queremos acceder a una variable global que esta oculta debemos hacerlo de alguna manera alternativa.

Si la variable global esta declarada con `let` o con `const` en vez de `var` esta no se agrega como propiedad del objeto `window`.

## CLOSURES
Las Clasusuras o closere son estas funciones anidadas que recuerdan el conjunto de variables a las que podian acceder, por mas que se las invoque desde otro lugar, desde otro scope.
Para crear una clausura o closure en javascript necesitamos 3 ingredientes:

- Primero una funcion que se encuentre escrita adentro de otra funcion lo que conocemos como una funcion anidada.
```js
function crearContador() {
    function incrementar(){    
    };
}
```

- Alguna variable que se encuentre en el scope de la funcion mas grande y que la funcion de adentro la utilice de alguna manera en este caso para incrementar su valor y devolver su valor incrementado.
```js
function crearContador() {
    let contador = 0;

    function incrementar(){
        contador = contador + 1;
        return contador;
    };
}
```

- Tercero, invocar a la funcion interna pero no desde el scope donde esta escrita si no que desde otros scope.

```js
function crearContador() {
    let contador = 0;

    return function incrementar(){
        contador = contador + 1;
        return contador;
    };
}

const contador1 = crearContador();
```
si bien desde el scope global no podemos acceder a la variable `contador` por que es una variable local de la funcion `crearContador`. Como retornamos la funcion interna y la pasamos a una nueva varibale llamada `contador1` cuando la invoquemos esta va a serguir vinculada a la variable local y va a poder accederla normalmente.

La funcion y la varible del ejemplo anterior estan unidos por un viculo ya que no solo se esta retornando la funcion si no que se esta retornando todo ese vinculo.

Cuando decimos `vinculo` nos referimos  aun vinculo vivo no es que se genere una foto de la variable cuando se crea la funcion.
```js
function crearContador() {
    let contador = 0;

    return function incrementar(){
        contador = contador + 1;
        return contador;
    };
}

const contador1 = crearContador();
```
Cuando se ejecuta la funcion esta accede al valor que tiene la varible en ese momento.

Imaginate que dentro del scope local ponemos un timer con una funcion que modifica el contador poniendolo en 100 dentro de 5 segundos:
```js
function crearContador() {
    let contador = 0;

    setTimeout(funcion() {
        contador = 100;
    }, 5000);

    return function incrementar(){
        contador = contador + 1;
        return contador;
    };
}

const contador1 = crearContador();
```

Cuando ejecutemos este programa nuestra funcion comenzara en 0 y a medida que lo ejecutemos se van incrementando de a 1 como antes, pero al cabo de 5 segundos su valor se actualiza y la proxima vez que llamemos a la funcion veremos que su valos ahora es 101.

### Entorno lexico 

El **entorno lexico** es un objeto que tiene los contextos de ejecucion donde se almancenan los nombres de las variables que existen dentro de una funcion y los valores actuales que tienen. Son como un diccionario.

En nuestro programa original, que crees que pasaria si despues de invocar a nuestro contador 3 veces volvemos a llamar a la funcion `crearContador` para crearnos otro contador, cuando lo invoquemos que valor va a tener ese nuevo contador?, y al viejo que le va a pasar?.
```js
function crearContador() {
    let contador = 0;

    return function incrementar(){
        contador = contador + 1;
        return contador;
    };
}

const contador1 = crearContador();
contador1();
contador1();
contador1();
contador1();
const contador2 = crearContador();
contador2();
```

Las clausuras no solo tiene que ver son los scope y las variables sino que tambien con los distintos contextos de ejecucion que se van creando cada vez que ejecuta una funcion.

Y para entender bien de que se trata esto tenemos que ver mas en detalle lo que pasa dentro de la pila de ejecucion, especialmente con algo que se llama `En torno Lexico` o `lexical environment`.

Cuando javascrip empieza a ejecutar nuestro programa lo primero que hace es crear el contexto de ejecuacion inicial para eso crea el primer registro de la pila de ejecucion, un registro asociado a la funcion que engloba a todo el programa.

Y todo contexto de ejecucion pasa por dos fases:
- fase de creacion: Donde se carga en memoria todo lo necesario para ejecutar esa funcion, en esta etapa se incializa el registro con cierta informacion como el archivo al que pertenece la funcion, se coloca el puntero de la proxima linea a ejecutar, para el primer registro se crear el registro global (que en los navegadores es window), se pone el valor que va a tener `this` dentro de la funcion(que en este caso como no estamos en modo estricto va a apuntar al objeto window), tambien se asocia el contexto de ejecucion que se esta creando con el codigo que se va a ejecutar(en este caso todo nuestro script), se crea un **entorno lexico** son como un diccionario, tienen clave y valor, donde las claves son los nombres de las variables declaradas dentro de la funcion recibidas como parametros y lo valores son los valores actuales que tienen las variables y cuando le asignamos un nuevo valor a una variable esa actualizacion se hace aca en el entorno lexico donde se encuentre esa variable, los objetos, las funciones y los arraiz en verdad se guardan como referencias o punteros a las posiciones de memoria donde realmente se encuentran esos objetos.

naturalmente dentro del mismo entorno lexico las claves son unicas, por que no podemos tener dos variables con el mismo nombre dentro de la misma funcion, si alguna vez lo googleas, esta parte de entorno lexico se llama `registro de entorno` o `environment record`.

Cada entorno lexico tiene un puntero a su entorno lexico exterior, el entorno en el que este fue creado.

Muchas veces cuando decimos que al ejecutarse una funcion se crea un nuevo scope para sus variables en verdad nos referiamos a este objeto el `entorno lexico`, el lugar donde se van a almacenar las variables y parametros que utiliza esa funcion.

En nuestro caso para la funcion global javascript ya sabe que existen 3 identificadores de variables, el nombre de la funcion que es un identificador mas y como es una funcion que es declarada, se carga por completo en memoria directamente cuando se esta creando este contexto de ejecucion y cada vez que javascript crea una nueva funcion en memoria la vincula al entorno donde la creo, asi esta funcion queda vinculada al entorno lexico global.

Veamoslo de otra forma, cada objeto que contiene una funcion tiene una propieda oculta llamada `crearContador.[[Entono]]` la cual apunta al entorno lexico donde se creo esa funcion, ademas en el entorno lexico global, estan estan nuestras dos variables `contador1` y `contador2`. Como ambas estan declaradas con `const` su valor inicial es no inicializada , su ubiesen estado declaradas con `var` su valor seria undefined, recordemos que esto es lo que se conoce como hosting en javascript darle valores iniciales a las variables y cargar las funciones en memoria junto antes de comenzar la ejecucion de las funciones, y por ultimo cada entorno lexico guarda un puntero de entorno lexico exterior pero en el caso de la funcion global este puntero va a estar vacio ya que es el primer entorno que se esta creando.

Ahora si se apila esta registro en la pila de ejecicion y comienza la fase de ejecucion javascript va ejecutando sentencia por sentencia, las declaraciones de funciones o de variables le sirvieron a javascript en la fase anterior para crear el entorno lexico con sus valores iniciales pero aun tiene que ejecutarlas, asi que pasa directamente al `contar1` donde se encuentra con una asignacion, estamos asignando el resultado de ejecutar una funcion. 

crea un nuevo contexto de ejecucion para esta funcion, carga la informacion necesaria que vimos antes, el nombre del archivo al que pertenece la funcion, cual es la proxima instruccion a ejecutar , le da un valor inicial a `this:window` (como no estamos en modo extricto y es una funcion suelta esta variable va apuntar al objeto global) y en este caso no se crea un objeto global por que no estamos en la funcion global y este ya fue creado, pero si se crea `arguments: {...}` (un objeto similar a los arrays que contienen todos los argumentos que recibe la funcion cuando se le invoco) y como antes se crea un entorno lexico con las variable declaradas en la funcion o recibidas como parametros y a que conceta este entorno lexico con su entorno lexico exterior, ahora si, terminada la fase de creacion de este nuevo contexto de ejecucion se apila y se comienza a ejecturar. 

Al estar retornando una funcion como su fuera cualquier otro valor javascript en otro momento crea una nueva instancia de esta funcion en memoria, es como sic reara un nuevo objeto, pero al tratarse de una funcion va a conectarla al entorno donde esta siendo creada.

Esta es la `clausura` una funcion que pasamos de aca para alla como si fuera una variable mas pero que sigue conectada al entorno lexico en el que fue creada.

Aqui es donde se viene lo interesante.

`const contador2 = crearContador();`
Se vuelve a invocar a la funcion grande, para ejecutarla el motor de java script crea un nuevo contexto de ejecucion para ejecutar esta funcion y es uno nuevo, no reutiliza el contexto de ejecucion que habia creado para la primera ejecucion.

**CADA VEZ QUE SE EJECUTA UNA FUNCION EN JAVASCRIPT, SE CREA UN NUEVO CONTEXTO DE EJECICION CON UN NUEVO ENTORNO LEXICO**