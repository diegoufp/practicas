# 33 CONCEPTOS DE JAVASCRIPT

## 1. La PILA DE EJECUCION(Call Stack)
Es la base para entender por que en javascript se puede hacer solo una cosa a la vez y como es que se ejecutan nuestros programas.

- **Que es el CALL STACK?**
Basicamente es como un mapa que usan los motores de JavaScript a la hora de ejecutar nuestros programas y le sirve para saber en que funcion estan parados durante la ejecucion del programa y por que funciones fueron pasando previamente hasta llegar ahi y de esta manera cuando el motor termine de ejecutar la funcion actual puede continuar ejecutando la funcion previa desde el lugar exacto que se habia realizado la llamada a la funcion actual y asi si esta funcion llama a otra el motor va a saber donde tiene que volver cuando termine de ejecutar la otra funcion.

- **Comportamiento de las pilas**
Cuando queremos agregar un elemento a una pila debemos apilarlo arriba del todo y de la misma manera si queremos sacar un elemento, debemos sacar el elemento que tiene arriba del todo de la pila.

A las pilas tambien se les conoce como **LIFO** por sus siglas en ingles Last In First Out(El ultimo en entrar es el primero en salir), lo que significa que cuando queremos sacar un elemento de la pila tenemos que sacar el que esta arriba del todo, que fue el ultimo que pusimos.

La pila de ejecucion que tienen los motores de javascrpt es como la pila de platos pero en vez de platos vamos a tener otra cosa.

- **Como funciona la pila de ejecucion?**
El motor de javascript va ir leyendo el codigo de nuestro programa y cada vez que se encuentre con el llamado de una funcion va a crear un registro o **frame** con informacion asociada a esta funcion y lo va agregar a la pila, este registro va a contener toda la informacion necesaria para que el motor pueda ejecutar esta funcion y ante una nueva llamada  a una funcion, el motor crea un nuevo registro para poder ejecutar esta funcion y lo agrega a la pila, de esta manera el registro que queda arriba del todo de la pila coincide con la funcion que el motor esta ejecutando.

**EL MOTO DE JS PUEDE EJECUTAR UNA SOLA COSA A LA VEZ**

No puede ejecutar dos cosas al mismo tiempo por que solo cuenta con una sola pila de ejecucion, cuando termine de ejecutar la funcion con la que estaba trabajando, ya sea por que llego al final o se encontro con una instruccion de return, el motor va a sacar el registro que tiene hasta arriba del todo de la pila y va a continuar trabajando con el registro que quedo debajo y la funcion que este registro tiene asociada.

- **(anonymous)**
Cuando ejecutamos un programa en javascript la primer funcion que se agrega a la pila es una funcion anonima que engloba a todo el programa, es como si fuera el hilo principal del programa y cuando esta funcion salga de la pila, significa que se termino la ejecucion del programa principal.

- **STACKTRACE**
La secuencia de llamadas que se fueron dando durante la ejecucion de un programa hasta que sucedio una excepción o un error inesperado.

- **SCOPE**
El contexto actual de ejecuacion. El contexto en que los valores y las expresiones son 'visibles' o pueden ser referenciados. Si una variable u otra expresion no esta 'en el scope-alcance actual', entonces no esta disponible para su uso. Los Scope tambien se pueden superponer en una jerarquia, de modo que los Scope secundarios tengamos acceso a los ambietos primarios, pero no al reves.

- **CONTEXTO DE EJECUCION (SCOPE)**
Variables y funciones que se pueden acceder cuando se esta ejecutando una funcion.

El conjunto de variables que tiene acceso a la funcion, con el contexto (htis), arguments u objeto global (window o global)

- **THIS**
`This` es una variable muy especial que tiene las funciones de javascript hace referencia al objeto que seria como el 'due;o' de la funcion y el valor que tiene `this` determina lo que se llama como el contexto de la funcion.

- **ARGUMENTS**
No es un array, pero es un objeto muy similar a las arrays que tienen las funciones en su scope local, bueno no todas las funciones, las 'funciones flechas' no lo tienen disponible. Los `arguments` contiene todo parametros que recibe la funcion cuando fue invocada.

En la funcion anonima que engloba todo nuestro programa no tenemos `argumets` por que todavia no se llamo a ningun funcion, pero si tenemos otra cosa, una referencia al objeto global, que en el caso de los navegadores este objeto se llama `window` y en el caso de notejs este objeto se llama `global` y este objeto global tiene un monton de propiedades, metodos y otros objetos que son muy utiles y que podemos acceder desde cualquier funcion de nuestro programa, como por ejemplo la consola, cuando escribimos `console.log()` estamos haciando referencia al objeto global pero este esta implicito, no hace falta que escribamos `window.console.log()` o `global.console.log()`, todo esto esta dentro del scope o contexto de ejecucion de una funcion.


- **call stack**
Cada vez que seleccionamos una funcion del `call stack` podemos ver cual es su contexto de ejecucion, eso es por que cada vez que se llama a una funcion se crea un nuevo scope o contexto de ejecucion, para esa funcion, y tambien se lo guarda en el registro asociado al llamado de esa funcion en la pila de ejecucion.

En la pila de ejecucion no solo se guarda el nombre de la funcion, el archivo al que petenece y el numero de la proxima linea a ejecutar si no que tambien se guarda su contexto de ejecucion.

Y vas a ver que muchas veces decimos `pila de ejecicion`, `call stack` o `pila de contextos de ejecucion` para referirnos a lo mismo, esta pila de registros o frames que guarda informacion relacionada a los llamados de las funciones que se fueron haciando durante la ejecucion de un programa.

Y en los navegadores podemos acceder a esta informacion, en la seccion de `call stack` podemos ver en que orden se fueron llamando a las funciones hasta llegar a la funcion que se esta ejecutando actualmente, es decir, como se fueron apilando los registros en la pila. Mientras que en la seccion de `scope` podemos ver el cotexto de ejcucion de la funcion que esta seleccionada en el `call stack`.

Cada vez que se invoca una funcion, se crea un contexto de ejecucion para esa funcion y se lo agrega a la pila y por mas que se trate de la mis a funcion con el mismo nombre son dos elementos distintos en la pila de ejecucion cada uno con su propio contexto de ejecucion.

Las funciones dejan la pila una ves que se terminan de ejecutar y cuadno las funciones no terminaron no pueden salir de la pila todavia.

- **Volar la pila de ejecucion**
Cada motor define un limite para la cantidad de entradas que puede almacenar la pila de ejecucion y por suerte los motores de javascript tienen este limite por que si no nuestra computadora seguria ejecutando nuestro programa infinitamente, esto en el caso de alguna funcionr recursiva.

## 2. TIPOS DE DATOS PRIMITIVOS 
En javascript el tipado es `Dinamico`, lo que significa, que las variables **no tienen un tipo de dato particular** asociado. Podemos asignarle y re-asignarle **cualquier valor** a **cualquier variable**.

En javascript el **tipado es debil**, lo que significa que, podemos realizar operaciones entre variables de distintos tipos. Como por ejemplo sumar un numero y un string:
```js
2 + '3'
// el resultado es:
'23'
```
En este caso cuando el motor de javascript ejecute esta linea de codigo hara su mejor esfuerzo para lograrlo, infiriendo automaticamnete que nosotros queriamos concatenarlo como si fueran ambos de tipo string, esto recibe el nombre de **coercion de tipos**, la conversion impricita de tipo que realiza el motor de JavaScript para poder concretar una operacion y tiene un efecto muy grande sobre como se ejecutan nuestros programas.

El **Tipo de una variable** se determina cuando **se ejecute la linea de codigo** que contiene a esa vaiable. **Depende de la operacion** que se este realizando con ella. Si hubiesemos realizado una resta en vez de una suma, el motor de javascript habria convertido automaticamente de string a numero y el resultado que obtendriamos seria `-1`:
```js
2 - '3'
// el resultado seria:
-1
```

Por sus caracteristicas particulares, en javascript existen dos grandes grupos de tipos de datos, los tipos de datos `primitivos` y los `objetos`, y entender las principales caracteristicas de cada grupo y en que se diferencian es muy importante.

- **Que es tipo de dato primitivo?**
Cuando decimos `primitivo` queremos decir 'basico', un tipo de dato basico, como el texto `hola` o el numero 2.

Los tipo de datos primitivos tienen dos caracteristicas muy importantes, la primera de ellas es que no poseen **ni metodos ni propiedades**.

Si creamo una variable llamada `numero` y le asignamos el numero `2`, veremos que si le agregamos el atributo `nombre` despues, cuando queramos obteenerlo la asignacion no tuvo ningun efecto:
```js
var numero = 2;
numero.nombre = 'numero dos';
numero.nombre
// undefined
```

Entonces como puedo obtener la longitud de un texto o convertirlo a mayusculas con el metodo `.toUpperCase()`?:
```js
'sacha'.toUpperCase()
// "SACHA"
```

La otra caracteristica muy importante que tienen los datos primitivos es que estos son `inmutables`

Si tenemos una variable con el valor `cocina` y queremos que ahora diga `bocina` no podemos cambiarle el primer caracter nadamas, hacer eso no tiene ningun efecto, la unica manera de modificar la variable es asignandole un nuevo valor:
```js
var texto = "cocina";
texto[0] = "B";
texto
//cocina
texto = "bocina"
texto
//bocina
```

Los **tipos de datos primitivos** son valores basicos, inmutables y que no poseen metodos ni propiedades.

Para obtener el tipo de dato que contiene una variable podemos usar `typeof`:
```js
var nombre = "sancha"
typeof nombre
// "string"
typeof 29
// "number"
// tambien es valido usalo con parentesis:
typeof(true)
// "boolean"
```

- **Que tipos de datos existen en javascript?**
Existen 6 tipos de datos primitivos:
- `string`
- `number`
- `booolean`
- `null`
- `undefined`
- `symbol`

EN javascript todo valor que no se de alguno de estos tipos es un `objeto`, asi es, los arrays son objetos, las funciones son objetos, las fechas, las expresiones regulares y cualquier objeto literal tambien.

- **string(cadenas de texto)**
Los string sirven para represntar texto en nuestro programas.
la comilla invertida nos permite interpolar entre una variable o una expresion dentro del string:
```js
var edad = 29;
var nombre = 'sancha';
var apellido = 'Lifszyc';

var saludo = `Hola, me llamo ${nombre} ${apellido} y tengo ${edad} a;os de edad`;
// basicamnete temer algo de codigo dentro del string para que el resultado forme parte del mismo.
```
Para representar los strings, javascript utiliza una codificacion que se llama `UTF-16`, lo que nos permite representar caracteres de un monton de alfabetos, incluso emojis.

Y si queremos saber cuantos caracteres tiene un string podemos acceder a su propiedad `.lenght`:
```js
'sancha'.length
//6
```

Hay un string que no tiene logitud,el string vacio `''` y sirve mucho para darle un valor inicial a una variable:
```js
''.length
// 0
```

Para obtener un string apartir de una variable podemos llamar al metodo `.toString()` o tambien concatenarla con el string vacio:
```js
var edad = 29;
edad.toString();
// "29"
edad + '';
// "29"
```
Pero si utilizamos el metodo `toString()` tenemos que asegurarnos que la varaible no contenga `null` ni `undefined` o se lo contrario obtenderemos un error:
```js
var edad = null;
edad.toString();
// error
```

- **number**
En javascript no existe tanta variedad, solo existe un tipo de dato para los numeros, `number`, y sirve para representar tanto los numeros enteros como los decimales y los negativos tambien. Existe el `0` y el `-0` pero si los comparamos tienen el mismo valor:
```js
0 === -0
/// true
```

Vamos a ver que a la hora de representar numeros decimales javascript no es muy preciso:
```js
0.1 + 0.2
// El resultado de esta operacion es:
// 0.300000000004
// y en realidad si vemos mas decimales este numero es mas largo todavia:
(0.1 + 0.2).toFixed(100)
// 0.3000000000000000440809204580548556000000000000000000000000000 
```
Esto tiene que ver con como estan dise;ados los numero dentros de un lenguaje, en estos lenguajes para representar un numero se utiliza un formato que se llama `IEEE 754` y en este formato cada numero ocupa 64 bits en la memoria de la computadora, es decir, 8 byts.

Y asi como tenemos errores de aproximasion al usar una calculadora esto es algo muy similar, cuando trabajamos con numero decimales en javascript es muy importante que usemos la funcion `.toFixed()` para poder truncar un numero por la cantidad de digitos despues de la coma que queremos usar:
```js
var numero = (0.1 + 0.2).toFixed(2);
numero
// "0.30"
// pero esta funcion nos devuelve un string 
// si lo que quermos es un numero podemos agregar el simbolo '+' para convertirlo a tipo numerico:
var numero = +(0.1 + 0.2).toFixed(2);
numero
// 0.3
```
El rango de numero que podemos usar con este formato va desde `numeroMinimo = -(2 ** 53) + 1` hasta `numeroMaximo = (2 ** 53) - 1`. Y que pasa despues de estos limites?, podemos seguir representando numeros con 64 bits mas aya de estos limites pero estos numero van a ser aproximaciones y si realizamos calculos con estos numeros vamos a tener resultados que no esperamos:
```js
// como por ejemplo si al numero maximo le sumamos uno va a resultaro lo mismo que sumarle 2
numeroMaximo + 1
// 9007199254740992
numeroMaximo + 2
// 9007199254740992
```
Por eso es que a estos numero limites tambien se les puede acceder con `numeroMinimo === Number.MIN_SAFE_INTEGER` y `numeroMaximo === Number.MAX_SAFE_INTEFER`, marcan el rango de numeros donde es seguro realizar operaciones numericas. 

Para verificar que un numero se encuentra dentro de los limites podemos usar:
```js
Number.isSafeInteger(54564458455)
```
y cuanto mas nos alejemos de los limites mayor sera la aproximacion.

`Number.MAX_VALUE` y `Number.MIN_VALUE` son el numero mas grande y el mas peque;o que vamos a poder ver representado con estos 64bits, pero recuerda que no es seguro operar con ellos, son solo una aproximacion de esos valores. Pero hay dos valores de tipo `number` que van mas alla de estos numeros y es el infinito positivo y negativo:
```js
Infinity

-Infinity
```
Ningun numero es mas grande que el infinito ni mas peque;o que el infinito negativo y para verificar que un numero no sea infinito podemos usar la funcion:
```js
isFinite(300)
//true
isFinite(Infinity)

// infinito o infinito negativo es el resulado de dividir un numero por 0 o por -0
3 / 0
// Infinity
3 / -0
// -Infinity
```
Si dividimos 0 enter 0, vamos a obtener el ultimo valor que existe de tipo `number`:
```js
0 / 0
// NaN
```

- **NaN(Not a Number)**

Este valor se llama `NaN(Not a Number)` y aun que su nombre diga lo contrario es de tipo `number` y es el resultado que obtendremos de computos invalidos como por ejemplo dividir un string por un numero:
```js
r = "hola" / 3
r
// NaN
r + 3
//NaN
```
`NaN` se va a propagar por cualquier otro calculo que querramos hacer con el.

`NaN` es un valor muy especial en javascript, no es igual a nada ni siquiera es igual a `NaN`:
```js
Nan === NaN
// false
```

Pero por suerte contamos con una funcion llamada `isNaN()` que nos permite verificar si el parametros que le pasamos es `Nan`:
```js
isNaN(30)
// false
isNaN(NaN)
// true
```

- **Boolean**