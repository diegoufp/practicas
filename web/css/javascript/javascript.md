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