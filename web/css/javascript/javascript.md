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

saludar() /* de esta forma se llama la funcion */
```

La segunda forma de crear una funcion es:
```js
saludar = function () {

}

saludar()
```

- `return` : nos sirve para que nos devuelva un valor.Ejemplo:
```js
function saludar(){
    alert("hola");
    return "la funcion se ejecuto correctamente"
}

let saludo = saludar();

document.write(saludo)
```

- `parametros` : las funciones no son funciones sin parametros. Ejemplo:
```js
function suma(num1, num2){
    let res = num1 + num2;
    document.write(res);
    document.write("<br>")
} 

suma(12,32)
suma(22,55 )
```

- `funciones flecha` : el `function` se cambia por una fecha.Ejemplo:
```js
// asi seria una funcion normal
const saludar = function(nombre){
    lat frase = `Hola! ${nombre}! Como estas?`;
    document.write(frase)
}

// asi seria la funcion flecha
const saludar = (nombre)=>{
    lat frase = `Hola! ${nombre}! Como estas?`;
    document.write(frase)
}

// la funcion flecha tambien se puede reducir a:
const saludar = nombre => document.write(frase);
// ocurre el return automanticamente

```

## Programacion orientada a objetos (POO)
cuando trabajamos con programacion orientada a objetos trabajamos con una especie de ideologia, es decir tenemos el mismo paradigma como referencia, todos son objetos. 

Para empezar debemos recordar que los objetos tiene dos conceptos que los definen:
1- `PROPIEDADES` : EL primer concepto son las cualidades de un objeto, que son las caracteristicas o cualidades, por ejemplo, tiene altura, tiene color, tienen  marca, tiene puertas, tiene velocidad minima o maxima.
 
2- `METODOS` : Luego estan las funcionalidades, todo lo que hace que nuestro objeto tenga funciones particulares, por ejemplo, un auto se puede apagar, puede encender, puede arrancar, etc. 

La programacion orientada a objetos es un paradigma de la programacion que lo que hace es intentar actualizando la forma en la que programamos mejorandola y haciaendo que podamos programar objetos como si lo hicieramos en la vida real.


## Conceptos basicos de POO 
- `clase` : lo que hacen sor crear objetos
- `objetos` : son la creacion de las clases
- `atributo` : los las propiedades, las particulaidades, las caracteristicas que tiene el objeto
- `metodo` : las cosas que puede hacer nuestro objeto.
- `constructor` : es una particularidad que tienen las clases que son obligatorias. Cuando creamos una clase tenemos que crear un constructor que nos va a construir las propiedades el objeto.
- `instanciada` : cuando finalizamos todo se podria decri que la clase esta instanciada

Vamos a intentar crear una clase que sea `animal`:
```js
class animal {
    // lo que haremos en el contructor sera pasar los parametros que contendra nuestra clase
    constructor(especie,edad,color){
        // 'this' es el objeto que queremos crear
        // 'this.especie' es diferente al parametros 'especie' por si solo
        // cuando ponemos 'this.especie', le estamos diciendo que el objeto va a tener cierta caracteristica, una propiedad, un atributo 
        this.especie = especie;
        this.edad = edad;
        this.color = color;
        this.info = `Soy ${this.especie}, tengo ${this.edad} y soy de color ${this.color}`;
    }
}
// Instanciar la clase
// el 'new' lo que hace es instanciar un objeto pero va a ser un objeto de la clase (en este caso 'animal').
// los objetos se tiene que definir con 'const'. 
// Tengase en cuenta que si la definen con let, en caso de que sin queres mas adelante modifiquen el valor de esa variable, no les va a saltar ningun error y por ende, estaria fallando su programa.
const perro = new animal("perro", 5, "rojo");
document.write(perro.info)
```

**Metodos**
Los metodos son las acciones que podemos hacer. Los metodo son una funcion dentro de una clase.Ejemplo:
```js
class animal{
    constructor(especie,edad,color){
        this.especie = especie;
        this.edad = edad;
        this.color = color;
        this.info = `Soy ${this.especie}, tengo ${this.edad} y soy de color ${this.color}`;
    }

    // esta seria una funcion creada dentro de una clase por lo que se le llama 'Metodo'.
    // Las funciones fecha no pueden ser usadar dentro de las clases para crear metodos
    verInfo(){
        document.write(this.info)
    }
}

const perro = new animal("perro", 5, "marron")
perro.verInfo()
```

## Caracteristicas de la POO

- `Abstraccion` : Cuando hablamos de abstraccion nos referimos a intentar reducir lo que mas podamos el objeto, hacemos que sea lo menos complejo que podamos. en pocas palabras es simplificar el objeto.
- `Modularidad` : Es la capacidad de resolver un problema grande separandolo por partes.
- `Encapsulamiento` : Hacer que todo los datos sean privados, que los usuarios no puedan acceder a ellos facilmente.
- `Polimorfismo` : Ver como un objeto se comporta de manera distinta ante el mismo metodo solamente por que sus propiedades son dsitintas. Es la capacidad que tiene un objeto para comportance distinto por sus propiedades.

```js
//Ejemplo de polimorfismo
class animal{
    constructor(especie,edad,color){
        this.especie = especie;
        this.edad = edad;
        this.color = color;
        this.info = `Soy ${this.especie}, tengo ${this.edad} y soy de color ${this.color}`;
    }
    verInfo(){
        document.write(this.info + "<br>")
    }
    ladrar(){
        if (this.especie == "perro") {
            document.write("Waw! <br>");
        } else {
            document.write("No puede ladrar, ya que es un " + this.especie + "<br>")
        }
    }
}

const perro = new animal("perro", 5, "marron")
const gato = new animal("gato", 2 , "negro")
const pajaro = new animal("pajaro", 1, "verde")

// Esto es el polimorfismo ya que no todos van a ladrar aun que tengan el mismo metodo, esto es po ruq elos objetos tiene propiedades distintas
perro.ladrar();
gato.ladrar();
pajaro.ladrar();
```

## Otros conceptos de POO
Estos conceptos ya vendrian siendo lo que va a tener cambios visuales en el codigo.

- `Herencia` : Crear una clase que va a tomar todo lo que hace la otra clase pero agregandole cosas nuevas.Ejemplo:
```js
class Animal{
    constructor(especie,edad,color){
        this.especie = especie;
        this.edad = edad;
        this.color = color;
        this.info = `Soy ${this.especie}, tengo ${this.edad} y soy de color ${this.color}`;
    }
    verInfo(){
        document.write(this.info + "<br>")
    }
}
// Esto es la herencia
/* con 'class perro extends animal' lo que le estamos diciendo es, la clase 'perro' va a contener todo lo que tiene la clase 'animal' pero se le van a agregar algunas cosas en especifico */
class Perro extends Animal {
    constructor(especie,edad,color,raza){
        // lo que esta en 'super' es lo que va a heredar de la clase animal.
        super(especie,edad,color);
        this.raza = raza;
    }
    ladrar(){
        alert("WAW!");
    }
}

// no podemos tener un objeto con el mismo nombre que una clase.
const perro = new Perro("perro", 5, "marron", "doberman")
const gato = new Animal("gato", 2 , "negro")
const pajaro = new Animal("pajaro", 1, "verde")

perro.verInfo();
gato.verInfo();
pajaro.verInfo();
```


- `Metodos esteticos` : Es un metodo que no necesita que la clase se defina para poder ser creado.Ejemplo:
```js
class Animal{
    constructor(especie,edad,color){
        this.especie = especie;
        this.edad = edad;
        this.color = color;
        this.info = `Soy ${this.especie}, tengo ${this.edad} y soy de color ${this.color}`;
    }
    verInfo(){
        document.write(this.info + "<br>")
    }
}

class Perro extends Animal {
    contructor(especie,edad,color,raza){
        super(especie,edad,color);
        this.raza = raza;
    }
    // Esto tranquilamente podria ser un metodo estatico, no estoy usando las propiedades y como no estoy usando las propiedades no es necesario crear el objeto.
    // para crear metodos estaticos hacemos uso de 'static'
    static ladrar(){
        alert("WAW!");
    }
}

const perro = new Perro("perro", 5, "marron", "doberman")
const gato = new Animal("gato", 2 , "negro")
const pajaro = new Animal("pajaro", 1, "verde")

perro.verInfo();
gato.verInfo();
pajaro.verInfo();
```


- `Metodos Accesores (Getters, Setters)` : los metodos `Getters` son para obtener un valor, los `Setters` para modificarlo o definirlo.Ejemplo:

```js
class Animal{
    contructor(especie,edad,color){
        this.especie = especie;
        this.edad = edad;
        this.color = color;
        this.info = `Soy ${this.especie}, tengo ${this.edad} y soy de color ${this.color}`;
    }
    verInfo(){
        document.write(this.info + "<br>")
    }
}

class Perro extends Animal {
    constructor(especie,edad,color,raza){
        super(especie,edad,color);
        this.raza = null;
    }
    // el setter es para para modificarlo o definirlo.
    // este es un metodo que se convierte a propiedad:
    set setRaza(newName){
        this.raza = newName;
    }
    // El getter es para obtener informacion.
    get getRaza(){
        return this.raza;
    }
}

const perro = new Perro("perro", 5, "marron", "doberman")
const gato = new Animal("gato", 2 , "negro")
const pajaro = new Animal("pajaro", 1, "verde")
// Raramente los Getters y Setters funcionan como propiedades. Entonces esta seria la forma erronea de hacerlo:
// perro.modificarRaza("pedro");
// la forma correcta seria:
perro.setRaza = "Pedro";
document.write(perro.getRaza)
```

## Metodos de Cadena


- `concat()` : junta dos o mas cadenas y retona una nueva
```js
let cadena = "cadena de prueba";
// lo que ocurre de forma automatica es: let cadena = new String("cadena de prueba");
resultado = cadena.concat("hola");
document.write(resultad;o)
```

- `startsWith()` : Si una cadena comienza con los caracteres de otra cadena, devuelve `true`, sino devuelve `false`. Es estricta y toma en cuenta los espacios.
- `endsWith()` : Si una cadena termina conm los caracteres de otra cadena, devuelve `true`, sino devuelve `false`.
- `includes()` : Si una cadena puede encontrarse dentro de otra cadena, devuelve `true`, sino devuelve `false`. Busca las cadenas no importa si estan al inicio o al final.
- `indexOf()` : Devuelve el indice del primer caracter de la cadena, si no existe, devuelve -1. busca las cadenas no importa la posicion pero en vez de arrojar un `true o false` devuelve la pocision donde inicia la primera letra de la cadena que estamos buscando.
- `lastIndexOf()` : Devuelve el ultimo indice del primer caracter de la cadena, si no existe, devuelve -1. los mismo que `indexOf()` solo que en vez de devolver la posicion de el primer caracter este devuelve la posicion del primer caracter de la ultima palabra buscada.
```js
let cadena = "pedro es un tarado tarado tarado tarado tarado tarado";
resultado = cadena.lastIndexOf("tarado");
document.write(resultado);//arroja la posicion 40
```
- `padStart()` `[propuesta estandar]`: Rellenar cadena al principio con los caracteres deseados.
```js
let cadena = "abc";
resultado = cadena.padStart(10,"1");
document.write(resultado); // lo que arrojara sera: 1111111abc
```
- `padEnd()` `[propuesta de ECMA]` : Rellenar cadena al final de los caracteres deseados.
- `repeat()` : Devuelve la misma cadena pero repetida la cantidad
```js
let cadena = "abc";
resultado = cadena.repeat(10);
document.write(resultado);
```

- `split()` : Divide la cadena como le pidamos. lo devuelve en un array.
```js
let cadena = "Hola,como,estas";
resultado = cadena.split(",");
document.write(resultado[0]); //arroja: Hola
```
- `substring()` : Nos retona un pedazo de la cena que seleccionamos. lo que hace es crear un nuevo string.
```js
let cadena = "ABCDEFG";
resultado = cadena.substring(0,2);
documnet.write(resultado); //Arroja: AB
```
- `toLowerCase()` : Convierte una cadena a minuscula
- `toUpperCase()` : Convierte una cadena a mayuscula
- `toString()` : Metodo devuelve una cadena que representa al objeto especificado. Devuelve una cadena convertida a string.
```js
let cadena = ["pedro", "matias"];
let resultado = cadena.toString();
document.write(resultado[0]); // arroja: p
```
- `trim()` : Elimina los espacios en blanco al principio y al final de una cadena.
```js
let cadena = "   pedro   ";
let resultado = cadena.trim();
document.write(resultado.length);
```
- `trimEnd()` : Elimina los espacios en blanco al final de una cadena.
- `trimStart()` : Elimina los espacios en blanco al comienzo de una cadena.
- `valueOf()` : Retorna el valor primitivo de un objeto string.

- `.length` : es una apropiedad de las cadenas de texto el cual te dice cuantas caracteres tiene lo que se esta buscando.
```js
let cadena = "   pedro   ";
let resultado = cadena;
document.write(resultado.length); //arroja: 11
```

## Metodos de Arrays

**___TRANSFORMADORES___** : los transformadores modifican al array directamente.
- `pop()` : elimina el ultimo elemento de un array y lo devuelve.
```js
let nombres = ["pedro", "maria" , "jorge"];
let resultado = nombres.pop();
document.write(resultado);
```
- `shift()` : elimina el primer elemento de un array y lo devuelve.
- `push()` : agrega un elemento al array al final de la lista.
```js
let nombres = ["pedro", "maria" , "jorge"];
let resultado = nombres.push("juancito", "robet");
document.write(resultado);
```
- `reverse()` : invierte el orden de los elementos de un array.
- `unshift()` : agrega uno o mas elemneto al inicio del array, y devuelve la nueva longitud del array.
- `sort()` : ordena los elementos de un arreglo (array) localmente y devuelve el arreglo ordenado.
- `splice()` : cambia el contenido de un array eliminando elementos existentes y/o agregando nuevos elementos.
```js
numero.splice(1,3) // lo primero que ponemos es la posicion(1) y despues indicamos cuantos elementos queremos eliminar(3)
// y si quisieramos agregar nuevos elementos ponemos:
numero.splice(1,3,"roberto", "gustavo", "maximo")
```

**___ACCESORES___** : lo que hace es crear un nuevo array, el original no se modifica.
- `join()` : une todos los elementos de un matriz (u objeto similar) en una cadena y la devuelve.
```js
let numero = ["abecedario", "manzana", "pedro", "dedo", "bobo"]
documet.write(numero + "<br>")
let resultado = numeros.join("<br>elemento: ") // es diferente al toString() ya que en este podemos utilizar el separado que querramos
document.write("elemento: " + resultado);
```
- `slice()` : devuelve una parte del array dentro de un nuevo array empezando por inicio hasta fin (fin no incluido).
```js
let numero = ["abecedario", "manzana", "pedro", "dedo", "bobo"]
documet.write(numero + "<br>")
let resultado = numeros.slice(0,2) // es parecido al substring
document.write(resultado);
```
- Metodos ya vistos en cadenas: `toString()`, `indexOf()` , `lastINdexOf()`, `includes()`.

**___DE REPETICION___**
- `filter()` : crea un nuevo array con todos los elementos que cumplan la condicion.funciona aprecido a un bucle.
```js
let numero = ["abecedario", "manzana", "pedro", "dedo", "bobo"];
numero.filter(numero => document.write(numero + "<br>")) // iniciara un bucle imprimiendo los elmentos de la cadena uno por uno hasta que se terminen y finalizara le bucle,es como un for en python.
// tambien funcionaria con :
numero.filter(function(numero){
    document.write(numero + "<br>")
})
// y la forma mas simple seria:
numero.filter(numero)
// en filter tenemos una cualidad que el forEach no tiene
// podemos devolver los elementos de una cadena que cumplan con una condicion.
resultado = numeros.filter(numero => numero.length > 5)
```
- `forEach()` : ejecuta la funcion indicada una vez por cada elemento del array. es similar a `filter()`.
- `map()`

## Objetos Math - Basico