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
Se pueden solicitar datos al usuario.Cuando le damos de datos numeros, ese dato sera en str, pero se puede convertir a entero con `parseInt()`. Ejemplo:
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

## Arreglos o array
Los array son un tipo de contenedor de diferentes tipos de elementos de diferentes tipos de datos.

Los arrays ya no son un dato primitivo, los arrays ya vienen a ser objetos.
```js
let arrays = [];
```
Las posiciones en un arrayn se cuentan desde el 0
```js
document.write(frutas[0])
```

## Arrays Asociativos
Los arrays asociativos se parecen mas al formato `.json` que trabaja con el cambio de informacion.

un array asociativo es como un array que tiene un array asociado. Son como los diccionarios en python.

```js
let pc1 = {
    nombre: "Dalato",
    procesador: "Intel Core I7"
    ram: "16GB",
    espacio: "1TB"
}

/* si tratamos de buscar un dato en el array asociativo "pc1" entonces tendremos que llamar a 'nombre' y no al '0', o nos saldra un error.*/
document.write(pc1["nombre"])

/* Con esto podriamos hacer algo como esto. */

let nombre = pc1["nombre"];
let procesador = pc1["procesador"];
let ram = pc1["ram"];
let espacio = pc1["espacio"];

frase = `el nombre de mi PC es: <b>${nombre}</b> <br> el procesador es: <b>${procesador}</b> <br> la memoria ram es: <b>${ram}</b> <br> el espacio en disco es de <b>${espacio}<b>`;

document.write(frase);
```

## Bucles e Iteracion

- `if` : se ejecuta una vez si la condicion se cumple.Ejemplo: `if (numero < 10) {numero++}`.

- `while` : Se ejecuta constantemente hasta que su condicional ya no sea `true`.Ejemplo: `while  (numero < 10) {numero++}`

- `do while:` : con el do while es distinto, primero indico las instrucciones y despues pregunto la condicion. Ejemplo:
```js
do {
    numero++;
    document.write(numero + "<br>")
}

while (numero <= 6);
```

- `break` : el break termina la sentencia .Ejemplo:
```js
while(numero < 1000){
    numero++;
    document.write(numero);
    if (numero == 10) {
        break;
    }
}
```

- `for` : la primera diferencia es que en el `for` podemos declarar variables.Ejemplo:
```js
let i = 20;

for (let i = 0; i < 6; i++){}
/* aqui estamos declarando dos veces 'i',no tira un error por que dentro de 'for' se pueden declarar variables, en este caso 'i' valdra 0 dentro del bloque del codigo del 'for'.
las partes de un bucle:
1. declaracion e inicializacion
2. condicion
3. iteracion(aumento o decremento)*/

/* tambien existe una forma de declarar una variable por fuera del for e inicializarla dentro del fot*/
let i;
for (i = 6; i >= 0; i--){}

/* tambien existe una forma de declarar e inicializar una variable por fuera del for*/
let i = 6;
for (i; i >= 0; i--){}
```

- `continue` :
podemos saltarnos un numero poniendo un if dentro del for.Ejemplo:
```js
for (let i=0; i < 20; i++){
    if(i == 12) {
        continue;
    }
    document.write(i + "<br>")
}
```

- `for in` : nos manda el indice(posicion) en la que estan los elementos.ejemplo:
```js
let animales = ["gato", "perro", "tiranosaurio rex"];
animales.edad = 20;

for (animal in animales){
    document.write(animal + "<br>");
}
/*  0
    1
    2
    edad
*/ 
for (animal in animales){
    document.write(animales[animal] + "<br>");
}
/*  gato
    perro
    tiranosaurio rex
*/ 
```

- `for of` : nos muestra directamente el valor de los elementos.Ejemplo:
```js
for (animal of animales){
    document.write(animal + "<br>");
}
/*  gato
    perro
    tiranosaurio rex
*/ 
```

- `label` : label es una sentencia que nos permite asociar un bucle a un nombre.Ejemplo:
```js
array1 = ["maria", "josefa", "roberta"];
array2 = ["pedro", "marcelo", array1, "josefina"];

forRnacio:
for (let array in array2){
    if (array == 2){
        for (let array of array1){
           if (array == "maria"){
            continue forRancio;
            } 
            document.write(array + "<br>");
        }
    }
    else {
        document.write(array2[array]+ "<br>");
    }
}
```

## funciones
Una funcion es una porcion de codigo que se puede guardar para reutilizarlo, asi ahorramos codigo.Ejemplo:
```js
function saludar(){}
```