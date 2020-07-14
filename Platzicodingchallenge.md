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

### Resolviendo reto 6

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