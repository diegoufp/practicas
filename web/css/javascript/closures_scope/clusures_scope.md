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

Si la variable global esta declarada con `let` o con `const` en vez de `var` esta no se agrega como propiedad del objeto `window`