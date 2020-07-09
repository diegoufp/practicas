# Platzicodingchallenge 100 dias

## Dia 1 - Hello, world!

Hello, world!
Hello, world! es el programa más básico que puede existir en cualquier lenguaje de programación. Todos recordamos la primera vez que escribimos un Hello, world! y lo satisfactorio que fue.
El reto del día de hoy es escribir Hello, world! en todos los lenguajes de programación que puedas. 

### Resolviendo reto 1

- **Python**

```
print ('Hello world')
```

- **C**

```
printf("Hello world");
```

## Dia 2 - Área de un triángulo

¿Recuerdas tus clases de Geometría?

Es momento de poner ese conocimiento a la práctica. El área de un triángulo se describe de la siguiente manera: A = (b * h) / 2 .

El reto del día de hoy es escribir un programa que tome la base y la altura como parámetros y calcule el área del triángulo. Bonus: El programa debe determinar si el triángulo es isósceles, equilátero o escaleno.

### Resolviendo reto 2

Pra poder resolver este reto necesitas conocer la fórmula de Herón.

```python

def triangulo (a, b, c):
    altura = 0
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