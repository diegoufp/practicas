def area_triangulo(a, b, c):
    '''
    Se calcula el area del triangulo y se identifica el tipo de triangulo
    '''
    s = (a + b + c)/2
    area = (s*(s - a)*(s - b)*(s - c))**.5

    if a == b == c:
        triangulo = 'equilatero'
    elif (a == b) or (a == c) or (b == c):
        triangulo = 'isoceles'
    else:
        triangulo = 'escaleno'

    return triangulo, area

if __name__ == '__main__':
    print(f'Este programa calcula el area de un triangulo')
    primero = float(input(f'Cual es la longitud del primer lado?: '))
    segundo = float(input(f'Cual es la longitud del segundo lado?: '))
    tercero = float(input(f'Cual es la longitud del tercer lado?: '))

    triangulo, area = area_triangulo(primero, segundo, tercero)

    print(f'\nCon los datos que proporcionaste podemos inferir que:\nEs un triangulo {triangulo} y que su area es {area}')