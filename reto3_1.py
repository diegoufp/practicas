
if __name__ == '__main__':
    print(f'Este programa puede ayudarte a convertir las horas y minutos a segundos.\n')
    horas = int(input(f'Cuantas "horas" quieres convertir a segundos?: '))
    minutos = int(input(f'Cuantos "minutos" quieres convertir a segundos? '))

    h_segundos = horas * 3600
    m_segundos = minutos * 60
    segundos = h_segundos + m_segundos

    print(f'\nLas horas y minutos que ingresaste dan un total de "{segundos}" segundos.')