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