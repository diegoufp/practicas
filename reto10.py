from itertools import islice

def traductor(mucho_texto):

    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    primera_letra = mucho_texto[0]

    i = 0
    vocal = vocales[i]
    while i < 10:

        if primera_letra == vocal:
            traduccion = mucho_texto[:] + 'way'
            print(i)
            return traduccion
        else:
            i += 1

    if i == 10:
        traduccion = mucho_texto[1:] + mucho_texto[0] + 'ay'
        return traduccion
    else:
        traduccion = 'Ocurrio un error'

    return 0

if __name__ == "__main__":
    print('Traductor a Pig Latin ')
    mucho_texto = input('Ingresa la palabra que quieres traducir a Pig Latin: ')

    texto_traducido = traductor(mucho_texto)

    print(texto_traducido)