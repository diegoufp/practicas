import random

def ruleta(numero):

    numero_aleatorio = random.random(range(1,100))

    print(numero_aleatorio)

    return 0

if __name__ == "__main__":
    print('Trata de adivinar el numero')
    numero = int(input('Ingresa un numero(entero) entre 1 y 100: '))
    
    if numero <= 0:
        print('Solo se admiten numero entre 1 y 100')
    elif numero >= 101:
        print('Solo se admiten numeros entre 1 y 100')
    else:
        ruleta(numero)

    