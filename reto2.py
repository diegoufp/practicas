import math


def triangulo (a, b, c):
    altura = 0
    area = 0
    
    grados_senoA = ((math.asin(a / c)) * (180 / 3.141592653589793))
    grados_senoB = ((math.asin(b / c)) * (180 / 3.141592653589793))
    grados_senoC = ((math.asin(c / b)) * (180 / 3.141592653589793))

    if grados_senoA == grados_senoB == grados_senoC:
        tipo_de_triangulo = 'equilatero'
        print('area de', tipo_de_triangulo)
        altura = ((3 ** 0.5) * a) / 2
        area = ((3 ** 0.5) / 4) * (a ** 2)
    elif grados_senoA == grados_senoB or grados_senoB == grados_senoC or grados_senoC == grados_senoA:
        tipo_de_triangulo = 'isoceles'
        print('area de', tipo_de_triangulo)
        if grados_senoA == grados_senoB:
            altura = ((a ** 2) -((b ** 2) / 4)) ** 0.5
            area = (c * altura ) / 2
        elif grados_senoB == grados_senoC:
            altura = ((b ** 2) -((c ** 2) / 4)) ** 0.5
            area = (a * altura ) / 2
        else: 
            altura = ((c ** 2) -((a ** 2) / 4)) ** 0.5
            area = (b * altura ) / 2
    else: 
        tipo_de_triangulo = 'escaleno'
        print('area de', tipo_de_triangulo)
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c))
    
    print('Este triangulo es',tipo_de_triangulo)
    
    return area


if __name__ == "__main__":
    a_input = int(input('Cual es el primer lado del triangulo?: '))
    b_input = int(input('Cual es el segundo lado del triangulo?: '))
    c_input = int(input('Cual es el tercer lado del triangulo?: '))

    resultado = triangulo(a_input , b_input, c_input)
    print(f'El area de este triangulo es {resultado}')
