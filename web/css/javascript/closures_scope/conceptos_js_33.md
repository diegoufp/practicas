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