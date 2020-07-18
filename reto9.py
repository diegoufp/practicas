import random

def ruleta(numero):

    numero_aleatorio = random.randint(1 , 100)
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
    numero = int(input('Ingresa un numero(entero) entre 1 y 100: '))
    
    if numero <= 0:
        print('Solo se admiten numero entre 1 y 100')
    elif numero >= 11:
        print('Solo se admiten numeros entre 1 y 100')
    else:
        ruleta(numero)

    