# Javascript
Javascript es lenguaje de programacion, e sun lenguaje orientado a objetos, e sun lenguaje Imeprativo, eso quiere decir que primero se ejecuta una linea despues otra y despues otra.Es un lenguaje dinamico, esto quiere decir que la variable no se ajusta al dato, el dato se ajusta a la variable 

### plugings de vsc
- `live server` : permite recargar de manera automatica la pagina cuando ocurra un cambio en el codigo.

## Para que lo usamos?
- Dinamismo de sitios web(todos los sitios web para que sean dinamicos necesitamos ponerle javascript)(dinamicos del lado del cliente)
- Servidor en NodeJS
- Tecnologias Frontend como Angular, React o Vue.JS

Otros usos no tan comunes:
- INteligenci artificial
- Placas electronicas (Jhonny Five)
- Mobile Apps
- Desktop
- Etc..

## Formas de Enlazar Javascript
La mejor forma es como contenido en un formato .js
Ejemplo:
```html
<!-- Codigo HTML -->
<body>
    <script src="codigo.js"></script>
</body>
```

## Variables
Una variable es un espacio que guardamos en memoria.
La variable se puede **definir**, **inicializar**, **se puede modificar a lo largo del tiempo**
Ejemplo:
```js
recipiente = "papel"
```
**Tipos de datos**
```js
string = "cadena de texto"
number = 19
booleano = true or false
```
Son datos primitivos ya que ya vienen con el lenguaje de js.

**Casos especiales de datos**
se tiene que tener en cuenta que son 3 tipos de datos que nos habla de que la variable no esta definida o hay un error. 
- `Undefined` : indicador de que la variable no esta definida
- `Null` : es una variable que es nula o vacia.
- `Nan` : cuando tratan de hacer una operacion con algo que no es un numero.

**Declarar una variable**
Hay 3 formas de declararla, cada una de estas tiene sus caracteristicas
- `var` : (tiene alcanze global)
- `let` : (let nos limita el alcanze de la variable a el bloque en que la ejecutamos). Ejemplo: para declarar: `let recipiente;` , para inicializarla: `recipiente = 15;`. Tambien se puede declarar e inicializar en la misma linea.
- `const` : Es una variable constante(las variables constantes no pueden cambiar su valor). Se tiene que inicializar cuando se declara.Ejemplo: `const recipiente = 15;`

**Multiples variables**
Podemos declarar una o mas variables a la vez.Ejemplo:
`let numero, numero2, numero3;`

**Hoisting**
Este es un concepto un tanto distinto pero habla basicamente de como funcionan las fases de creacion y de ejecucion. 

**Pruebas con Prompt**
Se pueden solicitar datos al usuario.Ejemplo:
`let nombre = prompt("dime tu nombre");`

## Operandores

- Operadores de asignacion: Un operador de asignacion asigna un valor al operando de la izquierda basado en el valor del operando de la derecha.Ejemplo`x = y`

- Operadores Aritmeticos: Toman valores numericos ( ya sean literales o variables) como sus operandos y retornan un valor numerico unico.Ejemplo:
```js
numero1 = 10;
numero1++; //se pone solo primero por que normalmente se ejecuta despues de que la variable es guardada//
numero = numero1;

alert(numero) //el resultado sera 9 //
```

**operadores**

- `addition(+)`
- `increment(++)`
- `decrememnt(--)`
- `subtraction(-)`
- `division(/)`
- `exponentation(**)`
- `multiplication(*)`
- `remainder(%)`
- `resto(&)`

## Concatenacion

La concatenacion en pocas palabras es unir strings, para concatenar unimos dos lineas de texto.Ejemplo:
```js
saludo = "hola pedro.";
pregunta = "Como estas?";

frase = saludo + pregunta; 
```

hay una problema al tratar de concatenar numero en lugar de sumarlos.Se resulve asi: 
```js
numero1 = 5;
numero2 = 8;

frase = "" + numero 1 + numero2;

// el resultado sera: 58//
// esto es por que cuando la cadena detecta texto combierte todo en una cadena de texto//
```

Otra forma de concatenar seria con el metodo `concat`.Ejemplo:
```js
numero = "53"; //concat es para los string, necesitas obligatoriamente almenos un string para que funcione//
numero2 = 8;

frase = numero.concat(numero2);
```

Otra forma de concatenar seria con backtiks y la variable entre `${}`.Ejemplo:
```js
nombre = "lucas dalto";

frase = `soy ${nombre} y estoy caminando`;
//soy lucas dalto y estoy caminando //
```

## Operadores (Intermedio)
**Operadores de comparacion**
Los operadores de comparacion comparan dos expresiones y devuelven un valor boolean que representa la relacion de sus valores.

- `Equality(a==b)` : no diferencia de los tipos de datos:
```js
let numero = 23;
let text = "23";
text == numero
//True//
```
- `Inequality(a != b)`
- `Identity(a === b)` : hace la comparacion de manera estricta, si diferencia los tipos de dato.
- `Non-identity(a !== b)`
- `Greater than(a > b)`
- `Greater than or equal(a >= b)`
- `Less than(a < b)`
- `Less than or equal(a <= b)`

**Operadores logicos**
Los operadores logicos nos devuelve un resultado a partir de que se cumpla (o no) una condicion, su resultado es booleano, y sus operandos son valores logicos o asimilables a ellos. 

- `&&` : si las dos condiciones son `true` va a ser `true`.
- `||` : si hay una verdadera, todo es verdadero, si las dos son falsas devuelve falso. 
- `!` : devuelve los contrario: `!false` entonces devolvera `true`.

## Camel Case
La primera letra de todas va en minuscula y despues cada nueva palabra su primera letra va en mayuscula.Ejemplo:`palabra1Palabra2Palabra3`

Esta es la forma en la que deberiamos trabajar con js.

## Condicionales
Una concidiconal es una centencia, que nos permite es validar algo.
- `if () {}` : condicional principal especifica

- `else if (){}`: podemos poner un numero de infinito de conficionales intermedias.

- `else {}`: si nunguna de las anteriores condiciones se cumple se ejecutara else.