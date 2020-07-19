from random import choice

def pass_generator(long_password):

    alphabet_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    characters = ['!', '@', '#', '$', '%', '&', '*', '_', '-', '=', '/', '+', '?', '(', ')']
    everything = alphabet_min + alphabet_let + characters + num
    chosen_one = []
    generated = []

    for i in range(long_password):
        chosen_one = choice(everything)
        generated.append(chosen_one)
    # str una clase str() invoca el constructor de esa clase y devuelve una instancia de esa clase.
    password = str().join([str(i) for i in generated])

    return password

if __name__ == '__main__':

    print('Este Es Un Generador De Contraseñas Seguras')
    print('\nLo recomendable es que una contraseña tenga mas de 11 caracteres de longitud, pero puedes eligir la longitud que mas te guste.')
    long_password = int(input('\nIngresa la logitud de tu contraseña: '))

    password = pass_generator(long_password)
    print('Tu contraseña es:\n',password)