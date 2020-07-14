from random import choice

def partida(jugada, user_name):
    if jugada >= 6:
        return 'nadie'
    mano = ['Tijeras', 'Papel', 'Piedra', 'Rata', 'Spock']
    jugador = mano[jugada - 1]
    computadora = choice(mano)

    print(f'La computadora saco {computadora}')

    if (jugador == mano[0]  and computadora == mano[1]) or (jugador == mano[1]  and computadora == mano[2]) or (jugador == mano[2]  and computadora == mano[3]) or (jugador == mano[3]  and computadora == mano[4]) or (jugador == mano[4]  and computadora == mano[0]):
        return user_name
    elif (jugador == mano[0]  and computadora == mano[3]) or (jugador == mano[1]  and computadora == mano[4]) or (jugador == mano[2]  and computadora == mano[0]) or (jugador == mano[3]  and computadora == mano[1]) or (jugador == mano[4]  and computadora == mano[2]):
        return user_name
    elif jugador == computadora:
        return 'nadie'
    else:
        return 'computadora'

if __name__ == "__main__":
    user_name = input('Ingresa tu user name: ')
    computadora = 0
    jugador = 0
    i = 0
    while i < 3:
        print('-' * 20)
        print(f'Ronda {i + 1} de 3')
        print('Tijeras = 1\nPapel = 2\nPiedra = 3 \nRata = 4\nSpock = 5')
        jugada = int(input('Ingrega el numero de la jugada que quieres hacer: '))

        ganador = partida(jugada, user_name)
        if ganador == 'computadora':
            computadora += 1
        else:
            jugador += 1
        print(f'La ronda numero {i + 1} la gana {ganador}')
        i += 1

    if computadora > jugador:
        print('El ganador definitivo es la computadora')
    elif computadora < jugador:
        print(f'El gandor definitivo eres tu {user_name}')
    elif computadora == jugador:
        print('Fue un empate')
    else:
        print('error')
