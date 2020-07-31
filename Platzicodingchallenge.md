# Platzicodingchallenge 100 dias

## Dia 1 - Hello, world!

Hello, world!
Hello, world! es el programa más básico que puede existir en cualquier lenguaje de programación. Todos recordamos la primera vez que escribimos un Hello, world! y lo satisfactorio que fue.
El reto del día de hoy es escribir Hello, world! en todos los lenguajes de programación que puedas. 

### Resolviendo reto 1

- **Python**

```python
print('Hello world')
```

- **C**

```c
printf("Hello world");
```

## Dia 2 - Área de un triángulo

¿Recuerdas tus clases de Geometría?

Es momento de poner ese conocimiento a la práctica. El área de un triángulo se describe de la siguiente manera: A = (b * h) / 2 .

El reto del día de hoy es escribir un programa que tome la base y la altura como parámetros y calcule el área del triángulo. Bonus: El programa debe determinar si el triángulo es isósceles, equilátero o escaleno.

### Resolviendo reto 2

Para poder resolver este reto necesitas conocer la fórmula de Herón.

```python

def triangulo (a, b, c):
    area = 0

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    if a == b == c:
        tipo_de_triangulo = 'equilatero'
        print('El tipo de triangulo es', tipo_de_triangulo)
       
    elif a == b or b == c or c == a:
        tipo_de_triangulo = 'isoceles'
        print('El tipo de triangulo es', tipo_de_triangulo)
       
    else: 
        tipo_de_triangulo = 'escaleno'
        print('El tipo de triangulo es', tipo_de_triangulo)
    
    return area


if __name__ == "__main__":
    a_input = float(input('Cual es el primer lado del triangulo?: '))
    b_input = float(input('Cual es el segundo lado del triangulo?: '))
    c_input = float(input('Cual es el tercer lado del triangulo?: '))

    resultado = triangulo(a_input , b_input, c_input)
    print(f'El area de este triangulo es {resultado}')
```

## Dia 3 - Reloj

¿Sabes cuántos segundos hay en 32 horas y 20 minutos? No te preocupes, yo tampoco. Para eso tenemos a las computadoras.
El reto del día de hoy es escribir un programa que tome como parámetros las horas y los minutos y que nos calcule los segundos. 

### Resolviendo reto 3

```python
def segundero(horas, minutos):

    horas_segundos = horas * 3600
    minutos_segundos = minutos *60

    return horas_segundos + minutos_segundos

if __name__ == "__main__":

    horas_input = int(input('Cuantas horas quieres convertir a segundos?: '))
    minutos_input = int(input('Cuantos minutos quieres convertir a segundos?: '))

    segundos = segundero(horas_input, minutos_input)

    print(f'{horas_input} horas y {minutos_input} minutos equivalen a {segundos} segundos.')
```

## Dia 4 - Repite la palabra

¿Sabías que para repetir las mismas instrucciones dentro de un programa podemos utilizar for loops o while loops? ¿Sabías que todo lo que puedes hacer con esas loops lo puedes hacer con recursión?

El reto del día de hoy es crear un programa que recibe como parámetro un string y la cantidad de veces que queremos repetir ese string y devuelve una cadena con las repeteciones. ¿El twist? Sólo puedes usar una función recursiva (pro tip: no olvides tu caso base).

### Resolviendo reto 4

Las funciones recursivas son funciones que se llaman a sí mismas durante su propia ejecución. Ellas funcionan de forma similar a las iteraciones, pero debe encargarse de planificar el momento en que dejan de llamarse a sí mismas o tendrá una función recursiva infinita.

```python
def repetidor_fraces(frace, veces, multiplo):

    if veces == 0:
        print(f'El resultado es ninguno, por que {frace}\nmultiplicado por 0 es igual a los amigos que tienes.')
    elif veces <= 1:
        print(multiplo)
        return 0
    else:
        multiplo = (multiplo + ' ' + frace)
        repetidor_fraces(frace, veces - 1, multiplo)
    
if __name__ == "__main__":
    frase_input = input('Ingresa la frace que quieres repetir: ')
    veces_input = int(input('Ingresa el numero de veces que quieres repetir la frace: '))

    repetidor_fraces(frase_input, veces_input, frase_input) 
```

## Dia 5 - ¿Necesitamos vocales?

¿Sabías que existen idiomas, como el Hebreo, en donde no existen letras para las vocáles? Lo bueno es que podemos ignorarlas y aún entender lo que está escrito con puras consonantes.
El reto del día de hoy es eliminar las vocales de este párrafo y tratar de leerlo.

En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lantejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda. El resto della concluían sayo de velarte, calzas de velludo para las fiestas, con sus pantuflos de lo mesmo, y los días de entresemana se honraba con su vellorí de lo más fino. Tenía en su casa una ama que pasaba de los cuarenta y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza que así ensillaba el rocín como tomaba la podadera. Frisaba la edad de nuestro hidalgo con los cincuenta años. Era de complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo de la caza. Quieren decir que tenía el sobrenombre de «Quijada», o «Quesada», que en esto hay alguna diferencia en los autores que deste caso escriben, aunque por conjeturas verisímiles se deja entender que se llamaba «Quijana». Pero esto importa poco a nuestro cuento: basta que en la narración dél no se salga un punto de la verdad.

### Resolviendo reto 5

```python
def main():
    string = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lantejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda. El resto della concluían sayo de velarte, calzas de velludo para las fiestas, con sus pantuflos de lo mesmo, y los días de entresemana se honraba con su vellorí de lo más fino. Tenía en su casa una ama que pasaba de los cuarenta y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza que así ensillaba el rocín como tomaba la podadera. Frisaba la edad de nuestro hidalgo con los cincuenta años. Era de complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo de la caza. Quieren decir que tenía el sobrenombre de «Quijada», o «Quesada», que en esto hay alguna diferencia en los autores que deste caso escriben, aunque por conjeturas verisímiles se deja entender que se llamaba «Quijana». Pero esto importa poco a nuestro cuento: basta que en la narración dél no se salga un punto de la verdad."
    vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    for i in vocales:
        string = string.replace(i, ' ')
    print(string)

if __name__ == "__main__":

    main()
```

## Dia 6 - Calculadora

¿Necesitamos nuestra Casio cuando tenemos Python? Yo la verdad todavía amo a mi calculadora de bolsillo, pero también amo hacer programas.El reto del día de hoy es crear una calculadora básica que reemplace a nuestra Casio. Crea un programa que tome un número, un operador, y otro número y realice el cálculo correcto.Ejemplo:```
calculadora(2, “+”, 2) -> 4
calculadora(4, “/”, 2) -> 2

### Resolviendo reto 6

El método eval () analiza la expresión pasada a este método y ejecuta la expresión (código) de Python dentro del programa.

En términos simples, la eval()función ejecuta el código de Python (que se pasa como argumento) dentro del programa.

```python
def calculadora(num_1, num_2, operador):

    operation = num_1 + operador + num_2
    try:
        operation = eval(operation)
    except (NameError, SyntaxError)  as e:
        print(f'\n{e}')
        print('No introdujiste un valor numérico o de operación. Intenta de nuevo.')
    else:
        return operation

if __name__ == "__main__":
    numero_1 = input('Ingresa un numero: ')
    simbolo = input('Ingresa el símbolo de la operación: ')
    numero_2 = input('Ingresa un segundo numero: ')

    resultado = calculadora(numero_1, numero_2, simbolo)
    if resultado:
        print(f'\n{numero_1} {simbolo} {numero_2} = {resultado}')
```

## Dia 7 - Piedra, papel o tijera

Este es un juego en el que nunca fui bueno, pero eso no significa que hacer un programa sea difícil.El reto del día de hoy es escribir un programa que reciba como parámetro “piedra”, “papel”, o “tijera” y determine si ganó el jugador 1 o el jugador 2. Bonus: ¿puedes hacer modificar tu programa para que el ganador sea el que gané 2 de 3 partidas?Ejemplo:```
ppt(“piedra”, “papel”) ➞ “El ganador es el jugador 2”

### Resolviendo reto 7

La biblioteca random contiene una serie de funciones relacionadas con los valores aleatorios. El listado completo de funciones de esta biblioteca se describe en el manual de Python.
La función choice(secuencia) elige un valor al azar en un conjunto de elementos. Cualquier tipo de datos enumerable (tupla, lista, cadena, range) puede utilizarse como conjunto de elementos.

```python
from random import choice

def partida(jugada, user_name):
    if jugada >= 6:
        return 'nadie'
    mano = ['Tijeras', 'Papel', 'Piedra', 'Rata', 'Spock']
    jugador = mano[jugada - 1]
    computadora = choice(mano)

    print(f'La computadora saco {computadora}')

    if (jugador == mano[0]  and computadora == mano[1]) or (jugador == mano[1]  and computadora == mano[2]) or (jugador == mano[2]  and computadora == mano[3]) or (jugador == mano[3]  and computadora == mano[4]) or (jugador == mano[4]  and computadora == mano[0]):
        return user_name
    elif (jugador == mano[0]  and computadora == mano[3]) or (jugador == mano[1]  and computadora == mano[4]) or (jugador == mano[2]  and computadora == mano[0]) or (jugador == mano[3]  and computadora == mano[1]) or (jugador == mano[4]  and computadora == mano[2]):
        return user_name
    elif jugador == computadora:
        return 'nadie'
    else:
        return 'computadora'

if __name__ == "__main__":
    user_name = input('Ingresa tu user name: ')
    computadora = 0
    jugador = 0
    i = 0
    while i < 3:
        print('-' * 20)
        print(f'Ronda {i + 1} de 3')
        print(""" Elije tu mano:
        [1] Tijeras
        [2] Papel
        [3] Piedra
        [4] Rata
        [5] Spock
        """)
        jugada = int(input('Ingrega el numero de la jugada que quieres hacer: '))

        ganador = partida(jugada, user_name)
        if ganador == 'computadora':
            computadora += 1
        else:
            jugador += 1
        print(f'La ronda numero {i + 1} la gana {ganador}')
        i += 1

    if computadora > jugador:
        print('El ganador definitivo es la computadora')
    elif computadora < jugador:
        print(f'El gandor definitivo eres tu {user_name}')
    elif computadora == jugador:
        print('Fue un empate')
    else:
        print('error')
```

## Dia 8 - Volumen de un cilindro 

Las matemáticas son base fundamental de la lógica y programación, por eso es importante practicarlas constantemente. Un cilindro es un cuerpo geométrico que requiere de varias fórmulas, aplícalas en un programa que reciba datos como su altura y radio de las bases para mostrar el resultado acotado a un decimal.

### Resolviendo reto 8

```python
import math

def area(altura, radio):
    pi = math.pi

    a = 2 * pi * radio * (radio + altura)

    return a

def volumen(altura, radio):
    pi = math.pi

    v = (pi) * (radio ** 2) * (altura)

    return v

if __name__ == "__main__":
    print('Con este programa podras calcular el area y el volumen de un cilindro.')
    altura = float(input('Ingresa la altura del cilindro: '))
    radio = float(input('Ingresa el radio del cilindro: '))

    volumen_resultado = volumen(altura, radio)
    area_resultado = area(altura, radio)
    print(f'Tu cilindro tiene un volumen de {volumen_resultado} y su area es de {area_resultado}.')
```


## Dia 9 - Número secreto

Este es un juego sencillo que trata de adivinar un número aleatorio, el truco está en que no sabes cuál es ese número pero en cada ingresarás un número y sabrás si este es mayor o menor al número secreto. Así que toma en cuenta estas restricciones para intentar adivinar el número y no olvides contar el número de intentos para mostrarlo una vez aciertes.

### Resolviendo reto 9

```python
import random

def ruleta(numero):

    numero_aleatorio = random.randint(1 , 10)
    i = 0
    while numero_aleatorio != numero:
        if numero > numero_aleatorio:
            print(f'{numero} es mayor al numero secreto')
        else:
            print(f'{numero} es menor al numero secreto')
        i += 1
        numero = int(input('Intentalo de nuevo, ingresa un nuevo numero: '))
    
    if numero == numero_aleatorio:
        print(f'Adivinaste! En el intento numero {i} descubriste que el numero secreto es {numero_aleatorio}.')
        return 0


if __name__ == "__main__":
    print('Trata de adivinar el numero')
    numero = int(input('Ingresa un numero(entero) entre 1 y 10: '))
    
    if numero <= 0:
        print('Solo se admiten numero entre 1 y 10')
    elif numero >= 11:
        print('Solo se admiten numeros entre 1 y 10')
    else:
        ruleta(numero)
```


## Dia 10 - Traductor de _Pig Latin_

El Pig Latin es una lengua lúdica que consiste en modificar las palabras con base en las siguientes condiciones:

1. Si una palabra comienza con sonido de consonante, se pasan todas las consonantes antes de la primer vocal y se agrega la sílaba “ay” al final (comida = omidacay).

2. Si la palabra inicia con vocal, entonces agrega la sílaba “way” al final (onomatopeya = onomatopeyaway).

Tu objetivo es crear un programa que reciba un texto y lo traduzca a esta lengua ¿qué resultados obtuviste?


### Resolviendo el reto 10

El método **split** devuelve una lista de cadenas después de dividir la cadena dada por el separador especificado.
La función **join** convierte una lista en una cadena formada por los elementos de la lista separados por comas.


```python
def traductor_de_palabras(mucho_texto):

    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    activador = 0
    primera_letra = mucho_texto[0]
    palabra_corregida = None

    for i in vocales:

        if i == primera_letra:
            palabra_corregida = mucho_texto + 'way'
            return palabra_corregida
        else:
            activador += 1

    if activador == 10:
        palabra_corregida = mucho_texto[1:] + mucho_texto[0] + 'ay'

        return palabra_corregida
    else:
        return 'ocurrio un error'

def separador_de_palabras(mucho_texto):

    particion = mucho_texto.split()
    j = 0
    for i in particion:
        palabra_corregida = traductor_de_palabras(i)
        particion[j] = palabra_corregida
        j += 1
    
    reconstruccion = ' '.join(particion)

    return reconstruccion

if __name__ == "__main__":
    print('Traductor a Pig Latin ')
    mucho_texto = input('Ingresa el texto que quieres traducir a Pig Latin: ')

    texto_traducido = separador_de_palabras(mucho_texto)

    print('Texto traducido:\n',texto_traducido)
```



## Dia 11 - Generador de contraseñas

Un ejercicio que siempre resulta útil para aplicar aleatoriedad es la generación de contraseñas. Básicamente debes crear un string de caracteres al azar tomando en cuenta las siguientes condiciones que el usuario debe poder elegir:

- Longitud de la contraseña.
- Si incluirá minúsculas, mayúsculas, números y caracteres especiales (incluyendo espacios).

### Resolviendo el reto 11

```python
from random import choice

def pass_generator(long_password):

    alphabet_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    characters = ['!', '@', '#', '$', '%', '&', '*', '_', '-', '=', '/', '+', '?', '(', ')']
    everything = alphabet_min + alphabet_let + characters + num
    chosen_one = []
    generated = []

    for i in range(long_password):
        chosen_one = choice(everything)
        generated.append(chosen_one)
    # str una clase str() invoca el constructor de esa clase y devuelve una instancia de esa clase.
    password = str().join([str(i) for i in generated])

    return password

if __name__ == '__main__':

    print('Este Es Un Generador De Contraseñas Seguras')
    print('\nLo recomendable es que una contraseña tenga mas de 11 caracteres de longitud, pero puedes eligir la longitud que mas te guste.')
    long_password = int(input('\nIngresa la logitud de tu contraseña: '))

    password = pass_generator(long_password)
    print('Tu contraseña es:\n',password)
```

## Dia 12 - Próximo cumpleaños

Muchos lenguajes de programación cuentan con un módulo para manejar tiempo y fechas. Haz uso de este módulo para crear un programa al que le ingreses tu fecha de nacimiento y te diga cuantos días faltan para tu próximo cumpleaños.


### Resolviendo el reto 12

```python
from datetime import datetime, timedelta

def birthday(dayi, monthi, yeari):

    dt = datetime.now()
    birth = dt.replace(year= yeari, month= monthi, day= dayi)
    year_current = dt.year
    next_year = dt.year + 1
    current_dirthday = birth.replace(year=year_current) 

    days_for_birthday = 0
    if dt < current_dirthday: #Este año es su cumpleaños
        days_for_birthday = current_dirthday - dt
    elif dt > current_dirthday: #El siguiente año es su cumpleaños
        current_dirthday = birth.replace(year= next_year) 
        days_for_birthday = current_dirthday - dt
    else:
        print('error')

    return days_for_birthday


if __name__ == "__main__":
    print('Con este programa podras calcular cuanto falta para tu proximo cumpleaños\n')

    day_input = int(input('Ingresa el dia en el que naciste: '))
    month_input = int(input('Ingresa el mes en el que naciste: '))
    year_input = int(input('Ingresa el año en el que naciste: '))

    days_for_birthday = birthday(day_input, month_input, year_input)
    print(f'Faltar {days_for_birthday} dias para tu cumpleaños')
```



## Dia 13 - Calculadora de propina

Imagina que pediste comida a domicilio (porque debemos quedarnos en casa), así que crearás un programa al cual ingresarás el valor de los platillos ordenados, obtendrás la suma total de la comida y calcularás un porcentaje de propina. Recuerda que puedes ingresar una cantidad indeterminada de platillos, indica a tu programa cuando calcular el resultado final.

### Resolviendo el reto 13
```python
def food_saucer(order):

    if order == 1:
        return 60
    elif order == 2:
        return 80
    elif order == 3:
        return 30
    elif order == 4:
        return 20
    elif order == 5:
        return 30
    elif order == 7:
        return 40
    elif order == 8:
        return 20
    else:
        print('No esta dentro de las opciones')
        return 0

def tip(saurcer):

    yes_or_not = int(input("""
    Quieres dejar propina? (Elige el numero de la opcion)
                            
                        [1] Yes
                        [2] No
    """))

    if (yes_or_not == 2) or (yes_or_not == 'No') or (yes_or_not == 'no'):
        return saurcer
    elif (yes_or_not == 1) or (yes_or_not == 'Yes') or (yes_or_not == 'yes'):
        percentage = int(input('Que porcejate quiere dejar de propina?: '))
        percentag = percentage / 100
        perc = saurcer * percentag

        return perc

if __name__ == "__main__":

    print('welcome to the restaurant of another world\n')
    print('Que desea ordenar?: ')
    order = int(input("""
    (Elige el numero de la opcion)
    Menú:
            [1] Especial del dia: 
                   - Chuleta empanizada.
                   - Agua de limon.
                   - Un flan.
            
            [2] Langostinos fritos:
                    - Camarones empanizados
                    - Pan
                    - Salsa tartara
                    - Un plato de sopa
                    
            [3] Espagueti con salsa boloñesa
            
            [4] Café
            
            [5] Parfait de chocolate
            
            [6] Omurice

            [7] Filete de tofu

            [8] Arroz 
    """ ))

    saurcer = food_saucer(order)
    percentage = tip(saurcer)
    account = saurcer + percentage
    print(f'Cuenta:\nTotal consumido: {saurcer}\nPorcentaje de propina: {percentage}\nTotal a pagar: {account}')
```


## Dia 14 - Números primos

Escribe un programa al que le indiques un número cómo límite y determinará todos los números primos desde el 1 hasta el número límite ingresado.
Recuerda que los números primos tienen las siguientes características:

- Es un número natural entero mayor a 1.
- Tiene únicamente 2 divisores: el mismo número y el 1.

### Resolviendo el reto 14

```python
def primos(limit):

    for x in range(2,limit + 1):
        if x == 2:
            print(x)
        elif x == 3:
            print(x)
        elif x == 5:
            print(x)
        elif x == 7:
            print(x)
        else:
            if x%2 != 0 and x%3 != 0 and x%5 != 0 and x%7 != 0 and x%x == 0:
                print(x)
            else:
                continue

if __name__ == "__main__":
    limit = int(input('Ingresa un numero limite para calcular los numero primos: '))

    primos(limit)
```

## Dia 15 - Calculadora de volúmenes, el usuario debe elegir entre Cilindro, Cubo y Esfera

Las matemáticas son base fundamental de la lógica y programación, por eso es importante practicarlas constantemente. Un cilindro es un cuerpo geométrico que requiere de varias fórmulas, aplícalas en un programa que reciba datos como su altura y radio de las bases para mostrar el resultado acotado a un decimal.

### Resolviendo el reto 15


## Dia 16 - Calculadora v2

Te diste cuenta de que muchas veces hacemos cálculos que son con más de dos valores, quiero que crees el algoritmo para programar una calculadora a la que le puedas agregar tantos números como tú requieras, deberá servir para adiciones y multiplicaciones

### Resolviendo el reto 16
```python
def calculadora(operation):

    try:
        result = eval(operation)
    except (NameError, TypeError, SyntaxError) as e:
        print(f'{e}\n')
        print(f'No introdujiste un valor numérico, de operación o la la operacion esta mal escrita. Intenta de nuevo.')
        return 0
    else:
        if type(result) == int or type(result) == float or type(result) == complex:
            return result
        else:
            return 0

if __name__ == '__main__':
    operation = input('Ingresa la operacion que quieres resolver: ')

    result = calculadora(operation)

    print(result)
```


## Dia 17 - Ordenar una lista de números de mayor a menor

El próximo reto será que ordenes una lista de 10 números aleatorios de mayor a menor y viceversa.

### Resolviendo el reto 17

## Dia 18 - Memory (parte 1)

Crea un código que te muestre 4 caracteres entre los siguientes de forma aleatoria: "#$%()/&

### Resolviendo el reto 18

## Dia 19 - Memory (part2)

Lleva un registro del Orden en el que aparecieron los caracteres

### Resolviendo el reto 19

## Dia 20 - Memory (part3)

Dale al usuario un menú para que elija en el orden correcto los caracteres

### Resolviendo el reto 20

## Dia 20 - Memory (part4)

Crea el código para evaluar si el orden del usuario fue el mismo mostrado por el programa y decirle si ganó o en caso contrario si perdió

### Resolviendo el reto 20

## Dia 21 - ¿Cuánto vas a ahorrar?

"El interés compuesto te sirve para generar más dinero gracias a los intereses que generas, es decir, hace que el valor que se paga por intereses se vaya aumentando mes a mes, por que el dinero sobre el cuál se hace el cálculo del interés se incrementa cada vez que se liquidan los respectivos intereses que ganaste el mes previo.
Crea una calculadora que te diga cuánto vas a tener en 6 meses, 1 año y 2 años al ahorrar 100 dólares con una tasa de interés a tu favor del 4%

### Resolviendo el reto 21
