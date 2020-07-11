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
