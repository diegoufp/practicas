def loop(palabra, veces, cadena=[]):

    sep = ','
    if veces <= 0 :
        cad = sep.join(cadena)
        print(cad)
        return str(cad)
    else:
        cadena.append(palabra)
        print(cadena)
        loop(palabra, veces - 1)


if __name__ == '__main__':
    print(f'Este programa sirve para repetir una palabra el numero de veces que gustes\n')
    palabra = input(f'Cual es la palabras que quieres repetir?: ')
    veces = int(input('Cual es el numero de veces que quieres repetir la palabra?: '))

    cadena = loop(palabra, veces)

    print(loop(palabra, veces))
