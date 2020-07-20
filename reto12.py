from datetime import datetime, timedelta

def birthday(dayi, monthi, yeari):

    dt = datetime.now()
    birth = dt.replace(year= yeari, month= monthi, day= dayi)
    year_current = dt.year
    current_dirthday = birth.replace(year=year_current) 
    next_year = dt.year + 1

    days_for_birthday = 0
    if dt < current_dirthday: #Este año es su cumpleaños
        days_for_birthday = current_dirthday - dt
    elif dt > current_dirthday: #El siguiente año es su cumpleaños
        current_dirthday = birth.replace(year= next_year) 
        days_for_birthday = current_dirthday - dt
    else:
        print('error')

    return days_for_birthday


if __name__ == "__main__":
    print('Con este programa podras calcular cuanto falta para tu proximo cumpleaños\n')

    day_input = int(input('Ingresa el dia en el que naciste: '))
    month_input = int(input('Ingresa el mes en el que naciste: '))
    year_input = int(input('Ingresa el año en el que naciste: '))

    days_for_birthday = birthday(day_input, month_input, year_input)
    print(f'Faltar {days_for_birthday} dias para tu cumpleaños')